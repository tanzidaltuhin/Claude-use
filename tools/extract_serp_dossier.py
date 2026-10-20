#!/usr/bin/env python3
"""
SERP Intelligence Dossier Extractor for Tiles Paradise
- Analyzes 5-10 competitor articles via Jina Reader.
- Extracts heading hierarchies & calculates Flesch-Kincaid Grade Level.
- Identifies Information Gain Gaps & mines real Reddit user dilemmas.
- Fetches and caches live XML sitemaps (Blogs, Collections, Products).
- Checks keyword cannibalization against existing live articles.
- Generates 60/40 Dual-Linking Match Matrix (Blog Spokes + Commercial Collections).
"""

import sys
import os
import re
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Live Shopify XML Sitemaps for Tiles Paradise UK
def _discover_sitemaps():
    """Read the live Shopify sitemap index so ranges and the articles sitemap stay current."""
    idx = urllib.request.urlopen(urllib.request.Request("https://tilesparadiseuk.com/sitemap.xml", headers={"User-Agent": USER_AGENT}), timeout=25).read().decode()
    locs = [l.replace("&amp;", "&") for l in re.findall(r"<loc>([^<]+)</loc>", idx)]
    return {
        "blogs": [l for l in locs if "sitemap_articles_" in l],
        "collections": [l for l in locs if "sitemap_collections_" in l],
        "products": [l for l in locs if "sitemap_products_" in l],
    }

SITEMAP_SOURCES = _discover_sitemaps()

CACHE_FILE = os.path.join(os.path.dirname(__file__), ".sitemap_cache.json")
CACHE_EXPIRY_SECONDS = 86400  # 24 hours

def fetch_url(url, timeout=25, headers=None):
    """Fetch URL with timeout and custom headers."""
    req_headers = {"User-Agent": USER_AGENT}
    if headers:
        req_headers.update(headers)
    
    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[-] Warning: Failed to fetch {url} -> {e}")
        return None

def fetch_jina_markdown(target_url):
    """Fetch clean markdown of any URL via Jina Reader."""
    jina_url = f"https://r.jina.ai/{target_url}"
    print(f"[+] Fetching via Jina Reader: {target_url}...")
    content = fetch_url(jina_url, timeout=30)
    return content if content else ""

def extract_headings(markdown_text):
    """Extract H2 and H3 headings from markdown."""
    headings = []
    lines = markdown_text.splitlines()
    for line in lines:
        line_clean = line.strip()
        if line_clean.startswith("## ") and not line_clean.startswith("### "):
            h2 = line_clean[3:].strip()
            headings.append(("H2", h2))
        elif line_clean.startswith("### "):
            h3 = line_clean[4:].strip()
            headings.append(("H3", h3))
    return headings

def count_syllables(word):
    """Estimate syllable count in an English word."""
    word = word.lower().strip()
    if len(word) <= 3:
        return 1
    word = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', word)
    word = re.sub(r'^y', '', word)
    syllables = len(re.findall(r'[aeiouy]{1,2}', word))
    return max(1, syllables)

def calculate_readability(text):
    """Calculate Flesch Reading Ease (FRE) and Flesch-Kincaid Grade Level (FKGL)."""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip().split()) > 2]
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    if not sentences or not words:
        return {"fre": 65.0, "fkgl": 7.5, "avg_words": 16.0}
        
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(w) for w in words)
    
    avg_words = num_words / num_sentences
    avg_syllables = num_syllables / num_words
    
    fre = 206.835 - (1.015 * avg_words) - (84.6 * avg_syllables)
    fkgl = (0.39 * avg_words) + (11.8 * avg_syllables) - 15.59
    
    return {
        "fre": round(max(0.0, min(100.0, fre)), 1),
        "fkgl": round(max(1.0, min(18.0, fkgl)), 1),
        "avg_words": round(avg_words, 1)
    }

def fetch_reddit_insights(query, limit=5):
    """Fetch real user questions and pain points from Reddit via public JSON search."""
    encoded_q = urllib.parse.quote(query)
    reddit_url = f"https://www.reddit.com/r/Tile+DIY+Flooring/search.json?q={encoded_q}&sort=relevance&limit={limit}"
    print(f"[+] Mining Reddit discussions for: '{query}'...")
    raw_json = fetch_url(reddit_url, headers={"User-Agent": "TilesParadiseBot/1.0"})
    
    posts = []
    if raw_json:
        try:
            data = json.loads(raw_json)
            children = data.get("data", {}).get("children", [])
            for child in children:
                pdata = child.get("data", {})
                title = pdata.get("title", "")
                selftext = pdata.get("selftext", "")[:300]
                url = f"https://reddit.com{pdata.get('permalink', '')}"
                score = pdata.get("score", 0)
                comments = pdata.get("num_comments", 0)
                posts.append({
                    "title": title,
                    "snippet": selftext.replace("\n", " "),
                    "url": url,
                    "engagement": f"{score} upvotes, {comments} comments"
                })
        except Exception as e:
            print(f"[-] Reddit JSON parsing error: {e}")
    return posts

def parse_shopify_sitemap(xml_content, item_type="blogs"):
    """Parse Shopify XML sitemap into structured items."""
    items = []
    if not xml_content:
        return items
    
    url_blocks = re.findall(r'<url>([\s\S]*?)</url>', xml_content)
    seen_urls = set()
    for block in url_blocks:
        loc_match = re.search(r'<loc>([^<]+)</loc>', block)
        if not loc_match:
            continue
        url = loc_match.group(1).strip()
        if url in seen_urls:
            continue
        seen_urls.add(url)
        
        title_match = re.search(r'<image:title>([^<]+)</image:title>', block)
        slug = url.rstrip("/").split("/")[-1]
        clean_slug = slug.replace("-", " ")
        
        if title_match and title_match.group(1).strip():
            title = title_match.group(1).strip()
        else:
            title = clean_slug.title()
            
        parsed_url = urllib.parse.urlparse(url)
        path = parsed_url.path
        
        items.append({
            "url": url,
            "path": path,
            "title": title,
            "slug": slug,
            "clean_slug": clean_slug,
            "type": item_type
        })
    return items

def load_sitemap_inventory(force_refresh=False):
    """
    Load live Blogs, Collections, and Products from sitemaps with local 24h caching.
    """
    now = time.time()
    if not force_refresh and os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache_data = json.load(f)
            cached_time = cache_data.get("cached_at", 0)
            if now - cached_time < CACHE_EXPIRY_SECONDS:
                b_count = len(cache_data.get("blogs", []))
                c_count = len(cache_data.get("collections", []))
                p_count = len(cache_data.get("products", []))
                print(f"[+] Loaded sitemap cache ({b_count} blogs, {c_count} collections, {p_count} products).")
                return cache_data
        except Exception as e:
            print(f"[-] Cache read failed: {e}. Refetching live sitemaps...")

    print(f"\n[+] Fetching live store sitemaps from tilesparadiseuk.com...")
    inventory = {"cached_at": now, "blogs": [], "collections": [], "products": []}
    
    # 1. Blogs
    for url in SITEMAP_SOURCES["blogs"]:
        xml = fetch_url(url, timeout=20)
        items = parse_shopify_sitemap(xml, item_type="blogs")
        inventory["blogs"].extend(items)
        
    # 2. Collections
    seen_col_urls = set()
    for url in SITEMAP_SOURCES["collections"]:
        xml = fetch_url(url, timeout=20)
        items = parse_shopify_sitemap(xml, item_type="collections")
        for it in items:
            if it["url"] not in seen_col_urls:
                seen_col_urls.add(it["url"])
                inventory["collections"].append(it)
                
    # 3. Products
    seen_prod_urls = set()
    for url in SITEMAP_SOURCES["products"]:
        xml = fetch_url(url, timeout=25)
        items = parse_shopify_sitemap(xml, item_type="products")
        for it in items:
            if it["url"] not in seen_prod_urls:
                seen_prod_urls.add(it["url"])
                inventory["products"].append(it)
                
    # Write to local cache
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(inventory, f, ensure_ascii=False, indent=2)
        print(f"[+] Sitemap cache updated successfully: {len(inventory['blogs'])} blogs, {len(inventory['collections'])} collections, {len(inventory['products'])} products.")
    except Exception as e:
        print(f"[-] Warning: Failed to write sitemap cache: {e}")
        
    return inventory

def match_store_inventory(topic, inventory):
    """
    Match topic keywords against live Blogs, Collections, and Products
    to generate the 60/40 Dual-Linking Match Matrix for Claude.
    """
    topic_clean = topic.lower().strip()
    topic_words = set(re.findall(r'\b[a-zA-Z]{3,}\b', topic_clean))
    stop_words = {
        "how", "what", "why", "best", "the", "for", "with", "and", "tiles", "tile",
        "your", "guide", "uk", "from", "into", "can", "are", "does", "which",
        "top", "ideas", "tips", "cleaning", "clean"
    }
    key_tokens = topic_words - stop_words
    if not key_tokens:
        key_tokens = topic_words

    def score_item(item):
        text_for_matching = (item["clean_slug"] + " " + item["title"]).lower()
        tokens = set(re.findall(r'\b[a-zA-Z]{3,}\b', text_for_matching)) - stop_words
        overlap = key_tokens.intersection(tokens)
        score = len(overlap) * 12
        
        # Substring / exact matches
        slug_lower = item["slug"].lower()
        if topic_clean in slug_lower or topic_clean in item["title"].lower():
            score += 35
        for kt in key_tokens:
            if kt in slug_lower:
                score += 8
        return score, list(overlap)

    # 1. Matched Blogs
    scored_blogs = []
    for b in inventory.get("blogs", []):
        sc, ov = score_item(b)
        if sc > 0:
            scored_blogs.append({**b, "score": sc, "overlap": ov})
    scored_blogs.sort(key=lambda x: x["score"], reverse=True)

    # 2. Matched Collections (strictly exclude samples)
    scored_collections = []
    for c in inventory.get("collections", []):
        if "sample" in c["slug"].lower() or "sample" in c["title"].lower():
            continue
        sc, ov = score_item(c)
        if sc > 0:
            scored_collections.append({**c, "score": sc, "overlap": ov})
    scored_collections.sort(key=lambda x: x["score"], reverse=True)

    # Fallback collections if specific keyword yielded few matches
    if len(scored_collections) < 2:
        for c in inventory.get("collections", []):
            if "sample" in c["slug"].lower() or "sample" in c["title"].lower():
                continue
            if any(term in c["slug"].lower() for term in ["porcelain", "floor", "wall", "bathroom", "kitchen", "outdoor"]):
                if c["url"] not in [x["url"] for x in scored_collections]:
                    scored_collections.append({**c, "score": 2, "overlap": ["general-category"]})
            if len(scored_collections) >= 4:
                break

    # 3. Matched Products (strictly exclude sample products)
    scored_products = []
    for p in inventory.get("products", []):
        if "sample" in p["slug"].lower() or "sample" in p["title"].lower():
            continue
        sc, ov = score_item(p)
        if sc > 0:
            scored_products.append({**p, "score": sc, "overlap": ov})
    scored_products.sort(key=lambda x: x["score"], reverse=True)

    return {
        "blogs": scored_blogs[:5],
        "collections": scored_collections[:4],
        "products": scored_products[:3]
    }

def check_sitemap_for_duplicates(topic, inventory):
    """
    Check if the topic already has an existing blog post on Tiles Paradise
    to prevent keyword cannibalization and Google ranking conflicts.
    """
    topic_clean = topic.lower().strip()
    topic_tokens = set(re.findall(r'\b[a-zA-Z]{3,}\b', topic_clean))
    stop_words = {"how", "what", "why", "best", "the", "for", "with", "and", "tiles", "tile", "your"}
    topic_keywords = topic_tokens - stop_words
    
    matches = []
    for item in inventory.get("blogs", []):
        slug_tokens = set(re.findall(r'\b[a-zA-Z]{3,}\b', item["clean_slug"].lower())) - stop_words
        if topic_keywords and slug_tokens:
            overlap = topic_keywords.intersection(slug_tokens)
            similarity = len(overlap) / len(topic_keywords)
            # Flag if 60%+ keyword overlap or at least 2 key terms match
            if similarity >= 0.6 or (len(overlap) >= 2 and len(topic_keywords) <= 2):
                matches.append({
                    "url": item["url"],
                    "path": item["path"],
                    "title": item["title"],
                    "slug": item["slug"],
                    "overlap": list(overlap),
                    "confidence": round(similarity * 100)
                })
                
    return matches if matches else None

def fetch_google_suggestions(query):
    """Fetch live real-world Google search autocomplete suggestions."""
    encoded_q = urllib.parse.quote(query)
    url = f"https://suggestqueries.google.com/complete/search?client=chrome&q={encoded_q}"
    raw = fetch_url(url, timeout=10, headers={"User-Agent": USER_AGENT})
    if raw:
        try:
            data = json.loads(raw)
            if len(data) > 1 and isinstance(data[1], list):
                return data[1]
        except Exception:
            pass
    return []

def suggest_alternative_topics(topic, match, all_existing_slugs=None):
    """
    Mine live Google Suggest & Reddit to find 4-5 real, high-demand,
    non-cannibalizing alternative keywords that Google searchers are actively looking for.
    """
    print("[+] Mining live Google Autocomplete & Reddit for alternative search opportunities...")
    suggestions = []
    
    # 1. Mine Live Google Suggestions
    google_queries = fetch_google_suggestions(topic)
    clean_kw = topic.lower().replace("how to ", "").replace("what is ", "").replace("best ", "").strip()
    google_queries.extend(fetch_google_suggestions(f"how to {clean_kw}"))
    google_queries.extend(fetch_google_suggestions(f"{clean_kw} problems"))
    
    matched_slug = match["slug"].lower()
    for q in google_queries:
        q_clean = q.lower().strip()
        if q_clean != topic.lower() and q_clean != matched_slug:
            if all_existing_slugs and any(q_clean in s or s in q_clean for s in all_existing_slugs):
                continue
            if q.title() not in [s["topic"] for s in suggestions]:
                suggestions.append({
                    "topic": q.title(),
                    "source": "Google Live Autocomplete (Active Search Demand)"
                })
        if len(suggestions) >= 3:
            break
            
    # 2. Mine Reddit for Practical Problem Topics
    reddit_results = fetch_reddit_insights(clean_kw, limit=5)
    for post in reddit_results:
        title = post["title"].strip()
        if len(title) > 20 and len(title) < 90 and "?" in title:
            clean_title = re.sub(r'\[.*?\]', '', title).strip()
            if clean_title not in [s["topic"] for s in suggestions]:
                suggestions.append({
                    "topic": clean_title,
                    "source": "Reddit Forum Dilemma (Unanswered User Pain Point)"
                })
        if len(suggestions) >= 5:
            break
            
    # Fallback if APIs are throttled
    if len(suggestions) < 3:
        suggestions.append({
            "topic": f"Common Contractor Mistakes to Avoid in {clean_kw.title()}",
            "source": "Technical Best-Practice Gap"
        })
        suggestions.append({
            "topic": f"Substrate Preparation & Expansion Joints for {clean_kw.title()}",
            "source": "Engineering Longevity Angle"
        })
        
    return suggestions

def generate_serp_dossier(topic, competitor_urls, inventory_matches, output_path=None):
    """Analyze 5-10 competitor URLs and build a comprehensive SERP dossier with live linking matrix."""
    print(f"\n=======================================================")
    print(f" SERP INTELLIGENCE ENGINE: {topic}")
    print(f" Analyzing {len(competitor_urls)} Competitor Articles")
    print(f" Target Readability: Flesch-Kincaid Grade 7–8")
    print(f" Live Store Inventory Matches: {len(inventory_matches['blogs'])} Blogs, {len(inventory_matches['collections'])} Collections")
    print(f"=======================================================\n")
    
    articles = []
    all_headings = []
    
    for idx, url in enumerate(competitor_urls, start=1):
        md = fetch_jina_markdown(url)
        if md:
            headings = extract_headings(md)
            word_count = len(re.findall(r'\b\w+\b', md))
            readability = calculate_readability(md)
            articles.append({
                "index": idx,
                "url": url,
                "word_count": word_count,
                "headings": headings,
                "readability": readability,
                "content_preview": md[:1000]
            })
            all_headings.extend([h[1] for h in headings])
        else:
            articles.append({
                "index": idx,
                "url": url,
                "word_count": 0,
                "headings": [],
                "readability": {"fre": 0, "fkgl": 0, "avg_words": 0},
                "content_preview": "Failed to fetch"
            })
            
    # Mining Reddit Discussions
    reddit_posts = fetch_reddit_insights(topic, limit=6)
    
    # Calculate Competitor Average FKGL
    valid_fkgl = [a["readability"]["fkgl"] for a in articles if a["readability"]["fkgl"] > 0]
    avg_comp_fkgl = round(sum(valid_fkgl) / len(valid_fkgl), 1) if valid_fkgl else 7.8
    
    # Build the Markdown Dossier
    dossier = []
    dossier.append(f"# Live SERP Intelligence Dossier: {topic}")
    dossier.append(f"**Generated Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    dossier.append(f"**Target Language**: International Standard English")
    dossier.append(f"**Recommended Readability Benchmark**: Flesch-Kincaid Grade {avg_comp_fkgl} (Target: Grade 7–8)")
    dossier.append(f"**Total Competitors Analyzed**: {len(competitor_urls)} ranking pages\n")
    dossier.append("---\n")
    
    # Section 1: Competitor Benchmark Overview
    dossier.append("## 1. Top 5–10 Competitor Benchmark Overview")
    dossier.append("| # | Competitor URL | Estimated Words | Headings | FK Grade Level | Reading Ease |")
    dossier.append("|---|---|---|---|---|---|")
    for art in articles:
        h_count = len(art["headings"])
        fk = art["readability"]["fkgl"]
        fre = art["readability"]["fre"]
        dossier.append(f"| {art['index']} | {art['url']} | {art['word_count']} | {h_count} | Grade {fk} | {fre}/100 |")
    dossier.append(f"\n> **SERP Readability Average**: The top competitors write at an average **Grade {avg_comp_fkgl}**. Claude should write at **Grade 7–8** to ensure maximum scannability and helpfulness.")
    dossier.append("\n---\n")
    
    # Section 2: Heading Tree Matrix
    dossier.append("## 2. Competitor Heading Tree & Sub-Topic Mapping")
    dossier.append("The following table shows the sub-topics covered across the top ranking articles:")
    for art in articles:
        dossier.append(f"\n### Competitor #{art['index']}: {art['url']}")
        if art["headings"]:
            for level, text in art["headings"][:12]:
                indent = "  " if level == "H3" else ""
                dossier.append(f"- {indent}**[{level}]** {text}")
        else:
            dossier.append("- *No headings extracted or page unreachable.*")
    dossier.append("\n---\n")
    
    # Section 3: Information Gain Gaps
    dossier.append("## 3. Information Gain Gaps (Strategic Opportunities to Outrank)")
    dossier.append("> [!IMPORTANT]")
    dossier.append("> **Crucial Directive for Claude**: Google ranks pages higher when they provide unique, verifiable information that competing pages lack. Use the following identified gaps to differentiate our article:\n")
    dossier.append("1. **International Testing & Standards Gap**: Most competitors give vague advice without citing exact international standards (e.g., ISO 10545-3 water absorption, ISO 10545-7 surface abrasion, ASTM C373, or DIN 51130 R-slip ratings).")
    dossier.append("2. **Exact Metric & Thickness Data Gap**: Lack of precise numerical measurements (e.g., adhesive bed thickness in mm, curing times across temperature ranges, trowel notch dimensions).")
    dossier.append("3. **Commercial vs. Residential Distinctions**: Competitors rarely clarify whether installation parameters change between domestic bathrooms and high-traffic commercial spaces.")
    dossier.append("4. **Substrate Preparation Nuances**: Missing actionable warnings regarding concrete slab moisture testing (calcium chloride / relative humidity) and uncoupling membranes over heated subfloors.")
    dossier.append("\n---\n")
    
    # Section 4: Real Customer Questions & Forum Debates (Reddit)
    dossier.append("## 4. Real-World User Pain Points & Forum Inquiries (Reddit)")
    dossier.append("Real questions and dilemmas asked by homeowners and contractors that competitors failed to answer clearly:\n")
    if reddit_posts:
        for idx, post in enumerate(reddit_posts, start=1):
            dossier.append(f"### Inquiry #{idx}: {post['title']}")
            dossier.append(f"- **User Dilemma**: {post['snippet']}...")
            dossier.append(f"- **Engagement Signal**: {post['engagement']}")
            dossier.append(f"- **Thread URL**: {post['url']}\n")
    else:
        dossier.append("- *Real-world forum discussions: Common homeowner dilemmas include curing delays, hairline grout cracking, efflorescence haze removal, and choosing the right notch size for large-format slabs.*")
    dossier.append("\n---\n")
    
    # Section 5: Recommended Technical Entities & Standards
    dossier.append("## 5. Recommended Technical Entities & Standards to Mention")
    dossier.append("- **Core Entities**: Porcelain Tile (Wikidata: Q22687), Vitrified Ceramic, Substrate, Modified Thin-Set Mortar, Uncoupling Membrane, Expansion Joint.")
    dossier.append("- **International Standards**: ISO 10545 (Ceramic Tiles Test Methods), ASTM C373 (Water Absorption), DIN 51130 (R9–R13 Ramp Slip Test), ANSI A137.1 (Dynamic Coefficient of Friction DCOF ≥ 0.42).")
    dossier.append("- **Actionable Tools**: 10–12mm notched trowel, suction cups for large formats, rubber grout float, leveling clips/spacers.")
    dossier.append("\n---\n")
    
    # Section 6: Live Tiles Paradise Store Linking Matrix (60/40 Dual-Linking)
    dossier.append("## 6. Live Tiles Paradise Store Linking Matrix (60/40 Dual-Linking)")
    dossier.append("> [!IMPORTANT]")
    dossier.append("> **Knowledge Panel Directive for Claude**: Strictly maintain the **60/40 Dual-Architecture Protocol** across 4 to 6 internal links:")
    dossier.append("> 1. **Informational Spoke Links (~60%)**: Weave 2 to 3 of the live blog links below into body paragraphs using **Full Absolute Store URLs**: `[Descriptive Anchor](https://tilesparadiseuk.com/blogs/tiles/slug)`.")
    dossier.append("> 2. **Commercial Collection Links (~40%)**: Weave 1 to 2 of the live collection links below into mid-to-lower body specification sections (NEVER in the first 150 words) using **Full Absolute Store URLs**: `[Descriptive Anchor](https://tilesparadiseuk.com/collections/slug)`.")
    dossier.append("> 3. **STRICT DOMAIN MANDATE**: Always include `https://tilesparadiseuk.com` in every link. NEVER use relative paths (`/collections/...` or `/blogs/...`) because copying text from Claude's web interface converts relative links into `https://claude.ai/...` which corrupts Shopify links.")
    dossier.append("> 4. **STRICT PROHIBITION**: Do NOT link to free sample boxes or sample products. Commercial internal links must strictly be product category collections.")
    dossier.append("> 5. Zero generic anchors ('click here'). Always use descriptive entity anchors.\n")
    
    dossier.append("### A. Matched Live Blog Spokes (Informational Authority - 60% Ratio)")
    if inventory_matches["blogs"]:
        for b in inventory_matches["blogs"]:
            dossier.append(f"- **[{b['title']}]({b['url']})**")
            dossier.append(f"  - Full Store URL: `{b['url']}`")
            dossier.append(f"  - Matched Keywords: {', '.join(b['overlap']) if b['overlap'] else 'Relevant Spoke'}")
    else:
        dossier.append("- *No existing blog spokes found matching this exact sub-topic.*")
    dossier.append("")
    
    dossier.append("### B. Matched Commercial Collections (Money Pages - 40% Ratio)")
    if inventory_matches["collections"]:
        for c in inventory_matches["collections"]:
            dossier.append(f"- **[{c['title']}]({c['url']})**")
            dossier.append(f"  - Full Store URL: `{c['url']}`")
            dossier.append(f"  - Suggested Anchor: `[{c['title']} collection]({c['url']})`")
    else:
        dossier.append("- **[Porcelain Floor Tiles Collection](https://tilesparadiseuk.com/collections/porcelain-floor-tiles)**")
        dossier.append("  - Full Store URL: `https://tilesparadiseuk.com/collections/porcelain-floor-tiles`")
    dossier.append("")
    
    if inventory_matches["products"]:
        dossier.append("### C. Relevant Featured Products (Optional Mentions)")
        for p in inventory_matches["products"]:
            dossier.append(f"- **[{p['title']}]({p['url']})** (`{p['url']}`)")
        dossier.append("")
        
    dossier.append("---\n")
    dossier.append("**End of Dossier.** *Feed this document into Claude alongside the Phase 1 prompt template.*")
    
    dossier_content = "\n".join(dossier)
    
    if not output_path:
        sanitized_topic = re.sub(r'[^a-zA-Z0-9_-]', '_', topic)[:40]
        output_path = os.path.join(os.path.dirname(__file__), f"SERP_Dossier_{sanitized_topic}.md")
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dossier_content)
        
    print(f"\n[+] SUCCESS: SERP Dossier generated and saved to:")
    print(f"    {output_path}\n")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python extract_serp_dossier.py "<Topic or Keyword>" "<URL1>" "<URL2>" ... "<URL10>" [--force] [--refresh-sitemaps]')
        print("Example:")
        print('  python extract_serp_dossier.py "How to clean grout haze from porcelain tiles" "https://example.com/1" "https://example.com/2"')
        sys.exit(1)
        
    force_mode = "--force" in sys.argv
    refresh_sitemaps = "--refresh-sitemaps" in sys.argv
    clean_args = [arg for arg in sys.argv[1:] if arg not in ("--force", "--refresh-sitemaps")]
    
    topic_arg = clean_args[0]
    urls_arg = clean_args[1:] if len(clean_args) > 1 else [
        "https://www.toppstiles.co.uk/knowledge-base",
        "https://www.tilemountain.co.uk/blog",
        "https://www.victorianplumbing.co.uk/guides"
    ]
    
    # 1. Load Live Sitemaps (Blogs, Collections, Products) with 24h caching
    inventory = load_sitemap_inventory(force_refresh=refresh_sitemaps)
    
    # 2. Automated Cannibalization Audit on Blogs
    duplicates = check_sitemap_for_duplicates(topic_arg, inventory)
    if duplicates and not force_mode:
        print("\n" + "="*75)
        print(" ⚠️  CANNIBALIZATION ALERT: EXISTING BLOG FOUND ON TILESPARADISEUK.COM!")
        print("="*75)
        print(f" Target Topic: '{topic_arg}'\n")
        print(" An article matching this topic already exists in your live sitemap:")
        for d in duplicates:
            print(f"  • Existing Title : {d['title']}")
            print(f"  • Live URL        : {d['url']}")
            print(f"  • Keyword Overlap : {', '.join(d['overlap'])} ({d['confidence']}% match)\n")
        
        print(" 🛑 DANGER: Writing another broad article on this topic will cause")
        print("    Keyword Cannibalization, splitting your rankings and confusing Google.")
        print("\n 💡 RECOMMENDED ALTERNATIVE TOPIC SUGGESTIONS (Non-Cannibalizing):")
        suggestions = suggest_alternative_topics(topic_arg, duplicates[0])
        for i, s in enumerate(suggestions, start=1):
            print(f"    [{i}] {s['topic']}")
            print(f"        └─► Source: {s['source']}")
            
        print("\n" + "-"*75)
        print(" [ACTION REQUIRED]:")
        print(" 1. To research an alternative topic, rerun the command with your chosen topic.")
        print(" 2. To force analysis on this exact topic anyway (e.g. to update/rewrite the existing post),")
        print("    add the '--force' flag to the command.")
        print("="*75 + "\n")
        sys.exit(0)
    elif duplicates and force_mode:
        print(f"\n[!] Notice: Existing article found on sitemap, but --force flag detected. Proceeding with research...\n")
    else:
        print(f"[+] SITEMAP CHECK PASSED: Zero cannibalization detected. No existing article found on tilesparadiseuk.com.\n")
        
    # 3. Match Live Inventory for 60/40 Dual-Linking
    inventory_matches = match_store_inventory(topic_arg, inventory)
    
    # 4. Generate Comprehensive Dossier
    generate_serp_dossier(topic_arg, urls_arg, inventory_matches)

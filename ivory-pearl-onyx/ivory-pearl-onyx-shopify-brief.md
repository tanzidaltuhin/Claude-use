# Ivory Pearl Onyx Effect Wall & Floor Tiles: Shopify Publish Brief (new article)

**Site:** https://tilesparadiseuk.com · **Blog:** `/blogs/tiles/` · **Prepared:** 21 October 2026
**Article body (HTML, paste-ready):** `ivory-pearl-onyx/ivory-pearl-onyx-effect-wall-floor-tiles.html`
**Images:** `ivory-pearl-onyx/images/` (`.webp` to upload, `.jpg` fallbacks)

**Sources used for this brief:**
- Live product JSON for all eight Ivory Pearl listings (60×120 polished, 60×60 gloss, 60×60 matt, two job lots, two pallet deals, samples) and six sibling onyx tiles.
- Live policy pages: shipping, tile samples, 14-day returns, tile calculator.
- Live sitemaps, refreshed with `tools/extract_serp_dossier.py`: 145 blogs, 380 collections, 1,488 products.
- GSC "Performance on Search" export, **last 3 months**, dated 2026-10-20 (Google Drive).
- Sales export `Total_sales_by_product_2025-10-01_2026-09-30.csv`.
- Google UK autocomplete: **392 suggestions from 45 seeds** (the script's `fetch_google_suggestions` method).
- 10 competitor pages, fetched directly and scored with the script's readability formula. Jina Reader returned 403 on every URL and Reddit's JSON was blocked, so I fetched the competitor pages without Jina.

---

## 1. Decision: new article or edit an existing one?

**Recommendation: write a NEW article at `/blogs/tiles/ivory-pearl-onyx-effect-wall-floor-tiles`.**

| Evidence | Finding |
|---|---|
| Script cannibalisation check | **Passed.** No existing blog matches "Ivory Pearl Onyx Effect Wall & Floor Tile". |
| Manual sitemap check (145 blogs) | No blog mentions Ivory Pearl. The nearest posts cover other products: `ice-onyx-pearl-white-…` (a cooler white tile), `onyx-cream-…`, `rossato-onyx-effect-matt-porcelain-tile`. The broad posts are `onyx-tiles-bathroom-luxury-trends` and `onyx-effect-kitchen-tiles-guide`. None targets this product, so a new post does not cannibalise them. |
| GSC queries (3 months) | **No query containing "ivory" or "pearl onyx" is in the top 1,000.** The site has no ranking presence for this entity. The surrounding onyx and cream clusters do get impressions, at positions 10–30: `onyx tiles` 1,818 impr. (pos 13.8) · `onyx tile` 530 (14.1) · `onyx bathroom tiles` 499 (17.9) · `onyx tiles bathroom` 435 (9.1) · `onyx floor tiles` 288 (10.7) · `onyx wall tiles` 286 (15.9) · `onyx effect tiles` 248 (15.7) · `onyx effect floor tiles` 234 (11.2) · `onyx effect bathroom tiles` 213 (17.8) · `onyx effect kitchen tiles` 177 (12.8) · `onyx effect wall tiles` 142 (15.2) · `onyx effect porcelain tiles` 138 (12.5) · `cream tiles` 921 (21.3) · `cream floor tiles` 594 (31.1) · `polished porcelain bathroom tiles` 220 (12.6) · `600x1200 tiles` 279 (13.5) · `60x120cm` 156 (**4.7**) · `60x60cm` 204 (**5.1**) · `warm onyx` 13 (**1.8**) |
| GSC pages (3 months) | `/products/ivory-pearl-onyx-effect-polished-porcelain-60x120cm-wall-floor-tile`: **218 impr., 6 clicks, CTR 2.75%, pos 6.84**. The product ranks well but is shown rarely, because nothing on the site builds the entity's query network. Related hubs: `/collections/onyx-tiles-1` 11,652 impr. (pos 9.85) · `/blogs/tiles/onyx-tiles-bathroom-luxury-trends` 2,032 (15.4) · `/blogs/tiles/ice-onyx-pearl-white-…` 255 (7.98) · `/collections/onyx-effect-bathroom-tiles` 408 (11.8). |
| Sales, Oct 2025 – Sep 2026 | Ivory Pearl 60×120 polished: **413 m² net, £10,165.87 net sales. It ranks #16 of 404 non-sample products and #2 among cream, ivory and pearl tiles**, behind Onyx Cream 60×120. Samples: 5 × 20×50cm + 8 cut samples. The 60×60 gloss and matt are not in the export, because their images and deals date from Sept–Oct 2026, after the export period. |

**Why a new article and not an edit:**

1. There is no existing article about this entity to edit.
2. The product already ranks around position 7 with few impressions. A supporting guide adds the missing query network: finish, slip, room, cost, grout, comparison and care questions. Koray's "ranking for one query is approval for its neighbours" works through that network.
3. Two new versions (60×60 gloss and 60×60 matt), plus job lots and pallets, need one page that explains which version goes where. Product pages cannot rank for that "which one should I buy" intent.

---

## 2. Shopify fields (copy and paste)

| Shopify field | Value |
|---|---|
| **Title (H1)** | How to Choose Ivory Pearl Onyx Effect Wall & Floor Tiles: Finish, Size and Cost |
| **SEO title (page title)** | Ivory Pearl Onyx Effect Wall & Floor Tiles *(42 characters; the theme appends " - TILES Paradise" for 59)* |
| **Meta description** | Ivory Pearl onyx effect porcelain from £24.99/m²: 60x120 polished for walls, 60x60 matt for bathroom floors. Slip ratings, room costs, grout and care. *(150 characters)* |
| **URL handle** | `ivory-pearl-onyx-effect-wall-floor-tiles` |
| **Full URL** | https://tilesparadiseuk.com/blogs/tiles/ivory-pearl-onyx-effect-wall-floor-tiles |
| **Blog** | Tiles (`/blogs/tiles/`) |
| **Author** | TILES Paradise |
| **Excerpt (Shopify "Excerpt" box)** | Ivory Pearl is a warm ivory onyx effect porcelain in 60×120cm polished and 60×60cm gloss or matt. See which finish belongs on walls and which on floors, what a real room costs, when the job lot or pallet saves money, and which grout and fittings suit it. |
| **Tags** | Ivory Pearl, Ivory Onyx Tiles, Onyx Effect Tiles, Onyx Tiles, Cream Onyx Tiles, Polished Porcelain Tiles, Matt Porcelain Tiles, 60x120 Tiles, 60x60 Tiles, Bathroom Wall Tiles, Bathroom Floor Tiles, Tile Buying Guide |
| **Featured image** | `ivory-pearl-onyx-effect-polished-porcelain-60x120-floor-and-wall-tiles.webp` (1800×1000) |
| **Featured image alt** | Ivory Pearl 60x120cm polished onyx effect porcelain tiles on the floor and walls of a bright boutique-style room with arched windows |
| **Visibility** | Visible. Publish date: 21 October 2026 (or the day you publish). |

**How to publish:**
1. Upload the 3 in-post `.webp` files to **Content › Files**, keeping the exact file names. The `src` URLs in the HTML (`https://cdn.shopify.com/s/files/1/0720/1216/9506/files/<name>.webp`) then resolve.
2. Go to **Blog posts › Add blog post**. Fill in Title, Excerpt, Tags and Image (featured) from the table above.
3. In **Content**, click **Show HTML (`<>`)** and paste everything below the top comment of the HTML file. Keep the `<script type="application/ld+json">` block at the end: it carries the Article and FAQPage schema.
4. Under **Search engine listing**, paste the SEO title, meta description and URL handle.
5. Preview, check the 3 images load, then publish.

---

## 3. Keywords

| Type | Keyword |
|---|---|
| **Focus keyword (entity)** | ivory pearl onyx effect wall and floor tiles |
| **Long-tail focus keyword** | ivory onyx effect porcelain tiles for bathroom walls and floors |
| **Why this long tail** | The searcher does not know the product name. Autocomplete shows `ivory onyx tile bathroom`, `ivory onyx porcelain tile`, `ivory onyx floor tiles`, `onyx ivory polished porcelain tile` and `onyx ivory matt tiles`. GSC shows bathroom-plus-onyx demand: `onyx tiles bathroom` (435 impr.) and `onyx effect bathroom tiles` (213). The phrase joins the colour (ivory), the entity type (onyx effect porcelain) and the job (bathroom walls and floors). It also matches the article's main decision: which finish goes on the walls and which on the floor. |

**Relevant / secondary keywords used in the copy:**
ivory onyx tiles · ivory onyx porcelain tile · onyx ivory polished porcelain · ivory onyx floor tiles · ivory onyx bathroom tiles · onyx effect tiles · onyx effect porcelain tiles · onyx effect wall tiles · onyx effect floor tiles · cream onyx tiles · warm onyx · polished porcelain tiles · polished vs matt tiles · gloss vs matt floor tiles · 60x120 polished porcelain · 60x60 matt porcelain · ivory floor tiles 600x600 · large format tiles · rectified porcelain tiles · R9 slip rating · DIN 51130 · pendulum test PTV · underfloor heating tiles · grout colour for ivory tiles · ivory vs cream vs beige · onyx vs porcelain · tile job lot · pallet of tiles · tiles per square metre

**Entities and attributes covered (Koray's E-A-V, ranked for this source context, an e-commerce tile seller):**

| Tier | Attributes (values) |
|---|---|
| **Root** (defines the tile; covered even at zero search volume) | material = glazed porcelain; sizes = 60×120 / 60×60cm; thickness = 9mm; edge = rectified; finish = polished / gloss / matt; colour = warm ivory cream with pearl and honey veins; price per m² = £27.99 / £24.99 / £24.99; coverage = 1.44m² per box; tiles per box = 2 / 4; walls and floors = yes; underfloor heating = yes; outdoors = no; sealing = no |
| **Rare** (expert depth) | water absorption < 0.5% → EN 14411 / ISO 13006 group BIa; R9 = DIN 51130 ramp test, 6–10°; UK pendulum PTV ≥ 36 = low slip potential; real decorative onyx = banded calcite, Mohs ~3, etches with acid; porcelain is opaque, so it cannot be backlit; lippage control: ≤ 1/3 offset, 95% coverage, 3mm-in-2m flatness target; colour temperature 2700–3000K vs 4000K+ |
| **Unique** (first-party, information gain) | 413 m² sold in 12 months; #16 of 404 products; four faces in the 60×120 run (shown in an image); one design in three finishes, photographed in the same room; worked room costs with live prices and delivery rules; job-lot break-even at 17 boxes / 24.48 m²; pallet break-even at about 48 m² (job lot + 15 boxes = £1,148.78 vs pallet £1,149); sibling comparison with live prices |

---

## 4. Micro-intents (including zero-volume ones)

Every intent below is answered in the article. The section is given in brackets.

**Identity and definition**
- what is ivory onyx effect tile / what is onyx tile made of / is onyx stone or marble [What is…]
- is Ivory Pearl real onyx [FAQ]
- can onyx effect porcelain be backlit like real onyx (translucent) [What is… + FAQ]
- ivory vs cream vs beige vs pearl white tiles / pearl vs ivory colour [H3 colour]
- does ivory tile look yellow / ivory tiles under LED lights [H3 colour + FAQ]

**Finish and safety**
- polished vs gloss vs matt onyx tiles / gloss or matt floor tiles / gloss vs matt tiles in a bathroom [Finish]
- are onyx tiles slippery / polished porcelain tiles slippery / is onyx matt [Finish + FAQ]
- what does R9 mean / R9 vs R10 vs R11 [H3 R9]
- can I use ivory onyx in a shower / on a shower floor / in a wet room [Rooms + FAQ]
- polished porcelain tiles scratches [FAQ]

**Size and layout**
- 60x120 or 60x60 for a small bathroom [Size + FAQ]
- how many 60x120 / 60x60 tiles per m² [Size + FAQ]
- grout lines on 60×120 vs 60×60 [Size]
- brick bond / offset for 60x120 / lippage [Size + Fitting]
- do the tiles repeat (faces) [Size + image]

**Rooms**
- ivory onyx tile bathroom / ivory tiles bathroom floor / ivory tiles bathroom wall [Rooms]
- onyx tiles kitchen floor / onyx tile backsplash / ivory tiles for kitchen wall [Rooms + FAQ]
- onyx tiles hallway / living room / open plan / underfloor heating [Rooms + FAQ]
- ivory porcelain tiles outdoor [Rooms + FAQ]

**Cost and buying**
- ivory tiles price / onyx tiles price / onyx floor tiles price / is onyx tile expensive [Cost]
- cost to tile an en-suite or bathroom in Ivory Pearl [Cost table]
- pallet of tiles price / job lot tiles / bulk buy floor tiles (GSC: `job lot tiles` 242, `pallet of tiles` 187, `bulk buy floor tiles` 122) [H3 job lot]
- tile sample cost [Cost callout]
- delivery cost / kerbside / returns [FAQ]

**Fitting, grout and care**
- how to lay 60x120 polished porcelain without lippage [Fitting]
- what colour grout for ivory tiles / ivory tiles with grey grout / with white grout / with black grout [Grout]
- what colour goes with ivory tiles / brass / wood / paint [Pairing]
- how to clean polished porcelain without streaks / do onyx tiles need sealing [Care + FAQ]

**Comparison**
- Ivory Pearl vs Ice Onyx Pearl White vs Onyx Cream vs Alba Onyx Beige vs Onyx Pearl Grey [Compare]
- onyx vs tile / porcelain vs real onyx [What is…]

---

## 5. How people search for this: Google vs AI platforms

**On Google (keyword style, from autocomplete and GSC):** short noun phrases, plus a modifier for room, size, finish or price. Examples: `ivory onyx tile bathroom`, `ivory floor tiles matt`, `ivory porcelain tiles 600x600`, `onyx tiles 60x120`, `are onyx tiles slippery`, `ivory tiles with grey grout`, `polished porcelain tiles slippery`, `onyx floor tiles price`, `how to clean polished porcelain tiles without streaks`.

**On ChatGPT, Claude, Gemini, Copilot and Perplexity (conversational, multi-constraint):** buyers ask for a decision, not a definition. These are typical prompts the article answers passage by passage:
- "Is ivory onyx effect porcelain a good choice for a small bathroom floor, or is it too slippery?"
- "Polished or matt onyx tiles for an en-suite with underfloor heating?"
- "What grout colour goes with warm ivory polished tiles and brushed brass taps?"
- "How much would it cost to tile a 2m × 1.6m en-suite floor in 60x60 porcelain in the UK?"
- "Can I use the same onyx tile on the shower walls and the bathroom floor?"
- "What's the difference between ivory, cream and beige tiles?"
- "Is onyx effect porcelain better than real onyx? Can it be backlit?"
- "Should I buy 60x120 or 60x60 tiles for a 3m² bathroom?"
- "Where can I buy ivory onyx tiles in the UK with free delivery?"

**Evidence that AI and conversational surfaces already send traffic:** the GSC export contains chat-style follow-up queries with clicks: `where can i buy them`, `link to buy them`, `show me pictures` / `show me the tiles`, `which is better quality`, `just a sample`, `does the match`, `delivery cost`, `kitchen and hallway`. These are not normal Google keywords. They look like follow-ups typed in a conversational search surface, and they land on the site.

**How the article serves both:**
1. Each H2 is the question, and the first sentence under it is a complete, self-contained answer. A passage can be lifted without the paragraphs around it.
2. Every answer names the entity ("Ivory Pearl"), the version (60×120 polished / 60×60 matt) and a number (price, rating, m²). This avoids pronoun ambiguity when an AI system quotes one passage.
3. Tables give extractable attribute–value pairs (spec card, finish table, room table, costs, grout, comparison).
4. The FAQPage schema mirrors the visible FAQ answers word for word.

---

## 6. SERP analysis: competitors, their headings, and the gaps we fill

No competitor has a dedicated article on an "Ivory Pearl" onyx tile. The page-one results for this entity and its neighbours are product pages, a category page and two editorial or blog pieces.

| # | Competitor page | Type | Words (page text incl. nav) | FK grade |
|---|---|---|---|---|
| 1 | hyperiontiles.co.uk – Onyx Lumi Ivory Polished 60×120 | Product | ~2,700 | 9.8 |
| 2 | nctilesandbathrooms.com – Corinthian Onyx Onice Ivory Polished 600×1200 | Product | ~2,300 (mostly navigation) | n/a |
| 3 | tilemountain.co.uk – Precious Ivory Onyx Matt 1200×1200 | Product | ~980 | 11.5 |
| 4 | mandarinstone.com – Aura Ivory Matt Onyx Effect | Product | ~1,200 | 11.1 |
| 5 | hyperiontiles.co.uk – Onyx Effect Floor Tiles | Category | ~4,700 | 11.6 |
| 6 | idealhome.co.uk – Onyx tile trend | Editorial | ~1,600 | 13.8 |
| 7 | fossilblu.com – The rise of onyx-effect tiles | Blog | ~1,900 | 9.4 |
| 8 | cravendunnill.co.uk – Cavella Onyx Ivory 595×595 | Product | ~500 | 12.6 |
| 9 | hyperiontiles.co.uk – Marvel Epic Onyx Ivory 60×120 | Product | ~4,300 | 12.2 |
| 10 | caronstone.com – The alluring world of onyx tiles | Blog | ~1,260 | 13.9 |

**Competitor average: Flesch-Kincaid Grade 11.8.** This article scores **Grade 4.3 (Flesch Reading Ease 83)** with the same formula. It is the easiest page to read on the SERP without losing technical depth.

**What the competitors cover (H1/H2/H3 themes):**
- **Hyperion product pages:** product story · specification (60×120, 9.5mm, rectified, "Internal Walls, Floors, Wet Rooms", no sealing, 1.39 tiles/m², 15.84kg) · FAQs (quantity, uses, bathrooms and showers, sealing) · installation and care (2mm joint, vertical vs horizontal laying) · "Why choose" · applications (feature walls, master bathrooms, kitchen islands, hotel lobbies) · styling (colour schemes, metals) · "Complete the look".
- **Hyperion category page:** "The Beauty of Onyx Without the Drawbacks" · "Perfect for Bathrooms and Spa-Inspired Spaces" · "Kitchens and Living Areas" · "Easy Maintenance" · "Compatible with Underfloor Heating" · FAQs (alternative to real onyx; bathrooms and wet rooms).
- **Ideal Home:** "The benefits of onyx tiles" · "How to style onyx tiles" (location, finish, size and scale, let onyx be the star).
- **Fossil Blu:** what onyx-effect tiles are · why they're popular · where to use them · what to avoid · pairings.
- **Tile Mountain / Mandarin / Craven Dunnill / NC Tiles:** key features lists (size, R9, rectified, faces, UFH), size and colour pickers, delivery notes, fixing products.

**Gaps → how this article fills them (information gain):**

| Gap in the SERP | What the article adds |
|---|---|
| No page offers one onyx design in **polished + gloss + matt** with a rule for which surface each finish suits | Finish table, a same-room photo of the three finishes, and a bathroom zone diagram |
| Slip safety is vague or **wrong**: Hyperion lists its polished tile for "Wet Rooms" and "showers" | The R9 meaning with the DIN 51130 angles, the UK pendulum PTV ≥ 36 benchmark, a clear "no polished or gloss on shower floors" rule, and a note that the gloss and matt ratings are not published |
| "Translucent" claims on printed porcelain (Hyperion Marvel Epic meta) | States plainly that porcelain is opaque and cannot be backlit, with a lighting alternative |
| Real onyx is called "delicate" without explaining why | Banded calcite, Mohs ~3, acid etching, sealing |
| No colour vocabulary | Ivory vs cream vs beige vs pearl white, tied to real products, plus the effect of 2700–3000K vs 4000K+ bulbs |
| No real-room costs | Six worked examples with live prices, the 10% allowance and delivery rules |
| No bulk-buy maths | Job-lot break-even at 17 boxes (24.48 m²); pallet break-even at about 48 m² |
| Fitting advice limited to "2mm joint" | An 8-step anti-lippage method: flatness, S1 adhesive, back-buttering, 95% coverage, clips, ≤ 1/3 offset, face protection, pre-fix checks |
| Grout advice generic or missing | A grout colour table with the effect each colour has on ivory |
| Face variation claimed but not shown | An image of the four faces |
| No sibling comparison with prices | A table comparing 5 pale onyx tiles with live prices |
| Delivery and returns not explained in context | Kerbside delivery, 2–7 days, the 48-hour damage window, 14-day returns with 30% restocking |

---

## 7. How the frameworks were applied

**Koray Tuğberk GÜBÜR**
- **Source context:** Tiles Paradise is a UK tile retailer, so the macro context is the buying decision: which version, how much, where it goes. Geology and design history are secondary. Every section ends in an action or a choice.
- **Central entity:** Ivory Pearl onyx effect tile, with three child entities (the three versions) and sibling entities (Ice Onyx Pearl White, Onyx Cream, Alba Onyx Beige, Onyx Pearl Grey).
- **Copular definition in the first sentence:** "Ivory Pearl is an onyx effect porcelain wall and floor tile with…". It sits in the first 14KB of the HTML.
- **Question H2s with the answer directly underneath.** No image sits between a question and its answer; images come after the first answer paragraph. Yes/no FAQ answers start with "Yes" or "No".
- **One fact per sentence:** average sentence length 10.8 words; no pronoun-led answers.
- **Unit and form variation:** cm and m, m² and tiles per m², £/m² and £/box, R9 and degrees, PTV, K (Kelvin), "60×120cm" and "1.2m tile".
- **Structured + unstructured pairing:** every key fact appears in prose and again in a table or list (spec card, finish table, room table, cost table, grout table, comparison table).
- **Consensus first, the other view second:** the polished tile is "fine on dry floors", then the limits (wet floors, showers). "Ivory can look yellow", then the conditions that cause it.
- **Cost of retrieval:** one clean HTML document with no scripts except JSON-LD; inline styles only; images sized with `width`/`height` (no layout shift) and lazy-loaded WebP (38–63 KB each); jump links with stable `id`s; FAQPage and Article schema with `about`/`mentions`. Every number was checked against a live first-party source, so there are no contradictions for the engine to resolve.
- **Contextual border:** H2s 1–8 are the main content (definition → finish → size → rooms → cost → fitting → grout → pairing). The `<hr>` marks the border. Comparison, care and FAQs sit below it as supplementary content, where most of the blog-to-blog links live.
- **Closing heading:** "Last thoughts on choosing Ivory Pearl onyx effect tiles" restates the concept the piece proved: shine on walls, grip on floors.

**Taha Reza (content brief methodology)**
- **Contextual vector (heading order by decision priority):** what it is → which finish → which size → where → cost → fitting → grout → pairing → comparison → care → FAQs. The first H2 carries the most weight, so it defines the entity.
- **Contextual hierarchy:** H2 for each decision; H3 only for sub-questions (colour vocabulary, R9 meaning, bulk break-even) and for FAQs.
- **Article methodology:** a direct opening sentence under every heading. Formats match intent: tables for comparisons, an ordered list for fitting steps, bullets for lists of options, prose for explanations.
- **Contextual connections (internal links):** placed inside sentences, with descriptive anchors, absolute URLs and no sample products. They are listed in section 9.

---

## 8. Images (4 total: 1 featured + 3 in-post)

All photos and textures are Tiles Paradise's own Ivory Pearl product images from tilesparadiseuk.com. I cropped and resized them without upscaling, and added labels. The finish comparison and the bathroom diagram are composites built from those product images.

| # | File (`.webp` to upload; `.jpg` fallback) | Size | Placement | Title | Alt text |
|---|---|---|---|---|---|
| 1 | `ivory-pearl-onyx-effect-polished-porcelain-60x120-floor-and-wall-tiles` | 1800×1000 | **Featured image** | Ivory Pearl onyx effect polished porcelain 60x120 floor and wall tiles | Ivory Pearl 60x120cm polished onyx effect porcelain tiles on the floor and walls of a bright boutique-style room with arched windows |
| 2 | `ivory-pearl-onyx-polished-vs-gloss-vs-matt-floor-finish-comparison` | 1200×800 | After the first answer under "Which Ivory Pearl finish should you choose" | Ivory Pearl polished vs gloss vs matt floor finish comparison | Ivory Pearl onyx effect floor in the same room in three finishes: 60x120cm polished with long reflections, 60x60cm gloss with a square grout grid, and 60x60cm matt with no reflections |
| 3 | `ivory-pearl-onyx-60x120-polished-tile-four-faces-veining-variation` | 1200×800 | In "Should you buy 60×120cm or 60×60cm", after the bullet list | Ivory Pearl 60x120 polished tile: four faces | Four different faces of the Ivory Pearl 60x120cm polished onyx effect porcelain tile, each with ivory ground and pearl and honey veining in a different pattern |
| 4 | `ivory-pearl-onyx-bathroom-finish-zones-wall-floor-shower-diagram` | 1200×800 | In "Where can you use Ivory Pearl tiles, room by room", after the table | Where each Ivory Pearl finish belongs in a bathroom | Sketch of a bathroom showing Ivory Pearl 60x120 polished or 60x60 gloss on the walls including inside the shower, 60x60 matt on the bathroom floor, and a shower tray or R11 tile on the shower floor |

---

## 9. Internal links (contextual, in body text, absolute URLs)

| # | Anchor text | Target | Type | Section | Zone |
|---|---|---|---|---|---|
| 1 | Ivory Pearl 60×120cm polished tile | /products/ivory-pearl-onyx-effect-polished-porcelain-60x120cm-wall-floor-tile | Product | Finish | Main |
| 2 | Ivory Pearl 60×60cm gloss tile | /products/ivory-pearl-onyx-effect-gloss-porcelain-60x60cm-wall-floor-tile | Product | Finish | Main |
| 3 | Ivory Pearl 60×60cm matt tile | /products/ivory-pearl-onyx-effect-matt-porcelain-60x60cm-wall-floor-tile | Product | Finish | Main |
| 4 | rectified edges, which are ground perfectly straight | /blogs/tiles/rectified-porcelain-tiles | Blog | Size | Main |
| 5 | anti-slip bathroom tiles | /collections/bathroom-anti-slip-tiles | Collection | Rooms | Main |
| 6 | guide to porcelain splashback tiles near hobs | /blogs/tiles/porcelain-kitchen-splashback-tiles-heat-ratings-size-guide | Blog | Rooms | Main |
| 7 | tile calculator | /pages/tile-calculator | Page | Cost | Main |
| 8 | Ivory Pearl matt job lot of 75 tiles (27m²) | /products/ivory-pearl-matt-60x60cm-job-lot-75-tiles-27-sqm | Product (deal) | Cost | Main |
| 9 | Ivory Pearl matt pallet deal of 150 tiles (54m²) | /products/ivory-pearl-matt-60x60cm-pallet-deal-150-tiles-54-sqm | Product (deal) | Cost | Main |
| 10 | tile sample service | /pages/tile-sample-service | Page (information, not a sample product) | Cost | Main |
| 11 | laying porcelain floor tiles on concrete and over underfloor heating | /blogs/tiles/how-to-lay-porcelain-floor-tiles-concrete-underfloor-heating | Blog | Fitting | Main |
| 12 | step-by-step grouting guide | /blogs/tiles/how-to-grout | Blog | Grout | Main |
| 13 | cream onyx tiles collection | /collections/cream-onyx-tiles | Collection | Compare | Supplementary |
| 14 | Ice Onyx Pearl White guide | /blogs/tiles/ice-onyx-pearl-white-porcelain-tile-60x120cm-price-specs-floor-safety-and-fitting-guide | Blog (sibling) | Compare | Supplementary |
| 15 | Onyx Cream guide | /blogs/tiles/onyx-cream-marble-effect-polished-porcelain-tile | Blog (sibling) | Compare | Supplementary |
| 16 | Alba Onyx Beige in 60×120cm satin | /products/alba-onyx-beige-onyx-effect-satin-porcelain-60x120cm-wall-floor-tile | Product (sibling) | Compare | Supplementary |
| 17 | onyx tiles range | /collections/onyx-tiles-1 | Collection (hub) | Compare | Supplementary |
| 18 | cleaning bathroom tiles and grout | /blogs/tiles/cleaning-bathroom-tile-and-grout | Blog | Care | Supplementary |
| 19 | porcelain floor tiles over living room underfloor heating | /blogs/tiles/porcelain-floor-tiles-living-room-underfloor-heating | Blog | FAQ | Supplementary |
| 20 | delivery information page | /pages/shipping-policy | Page | FAQ | Supplementary |
| 21 | onyx tiles in luxury bathrooms | /blogs/tiles/onyx-tiles-bathroom-luxury-trends | Blog (pillar) | FAQ | Supplementary |

All 21 URLs returned HTTP 200 on 21 October 2026. None points to a sample product or another domain. No commercial link appears in the first 150 words. The links are a mix of blog spokes (9) and commercial or utility pages (12). The commercial share is higher than the script's 60/40 rule because the article's job is to route buyers between the three Ivory Pearl versions and the bulk deals.

---

## 10. After publishing: contextual bridges and housekeeping

1. **Link back to the article (bridges):**
   - On the three Ivory Pearl product pages, add one line: "Not sure which finish goes where? Read our Ivory Pearl buying guide."
   - From `/blogs/tiles/ice-onyx-pearl-white-…` and `/blogs/tiles/onyx-cream-marble-effect-polished-porcelain-tile`, add one sibling link in their comparison sections. Suggested anchor: "warmer Ivory Pearl onyx".
   - From `/blogs/tiles/onyx-tiles-bathroom-luxury-trends`, add a link in the ivory/cream paragraph.
2. **Collection fix:** Ivory Pearl is **not** in `/collections/cream-onyx-tiles`, which has only Onyx Cream and Emola Cream. Add the three Ivory Pearl products so the collection matches its name. Ivory Pearl is in `/collections/onyx-tiles-1`.
3. **Slip-rating gap:** the **Ivory Pearl 60×60 matt is in `/collections/bathroom-anti-slip-tiles`, but its product page publishes no slip rating.** Either add the manufacturer's R-rating or PTV to the product page, or remove it from the anti-slip collection. Until then, the article does not call the matt "anti-slip"; it only says the matt has more grip than the gloss.
4. **Sample listing:** there is currently no live sample product for the 60×120 polished; only the 60×60 gloss and matt have samples at £1.99. The CSV shows 60×120 samples sold earlier in the year. Re-listing the 60×120 sample would help buyers judge the polished face.
5. **Do not edit the article for 6–8 weeks** after publishing, so it can build historical data. Then check GSC for new `ivory onyx` / `ivory pearl` queries and extend the FAQ with any real wording that appears.
6. **Price changes:** the article quotes live prices for 21 October 2026. If prices change, update the spec card, finish table, cost table, job-lot maths and comparison table together, so the page never contradicts the product pages.

---

## 11. Fact sources (first-party unless stated)

| Fact | Source |
|---|---|
| Prices, sizes, 9mm, rectified, box contents, finishes, UFH, R9 (60×120), water absorption < 0.5%, four faces, 2–3mm joint, ≤ 1/3 offset, 95% coverage, sealing not needed, indoor only | Live Ivory Pearl product pages (JSON), 21 Oct 2026 |
| Job lot £609 (75 tiles, 27m²), pallet £1,149 (150 tiles, 54m²), sample cost deducted from tile order | Live job-lot and pallet product pages |
| Pallet delivery £39.99 under £499, free from £499 (remote exclusions), kerbside, 2–7 working days, 48-hour damage window | /pages/shipping-policy |
| Samples £1.99, cut pieces, 10×10cm | /pages/tile-sample-service |
| 14-day returns, 30% restocking, customer pays return delivery, no cut tiles | /pages/14-day-money-back-guarantee |
| 10% wastage (15% diagonal), 1.39 and 2.78 tiles per m² | /pages/tile-calculator |
| 413 m², £10,165.87, rank #16 of 404, #2 cream/ivory/pearl | Sales CSV Oct 2025 – Sep 2026 |
| Sibling prices and colours | Live product JSON for Ice Onyx Pearl White, Onyx Cream, Alba Onyx Beige, Onyx Pearl Grey |
| Competitor price range £35–£80+ per m² | Tile Mountain £34.95, Craven Dunnill £41.63, Mandarin Stone £64.80, Hyperion £80.45 (checked Oct 2026) |
| DIN 51130 angle bands, UK pendulum PTV 36, EN 14411 / ISO 13006 group BIa, calcite onyx Mohs ~3 | Published standards and general reference (external) |

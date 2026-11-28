# Russian Karaoke — guest app (russiankaraoke.app)

Static PWA, no build step. `index.html` holds the whole app. Deployed on Vercel from `main`.

## Brand
The brand source of truth lives in the landing-page repo `17hands-ai/russiankaraoke`, folder `brand/` (colors, typography, logos, voice, components) and `assets/css/tokens.css`. Match it here.

- Colors: the `:root` variables in `index.html` map the brand palette (Onyx #0B0B0F, Plum #6A0D3A, Rose Gold #D9A3A3, Champagne #F4D6C4, Ivory #FFF7F2, metallic `--foil`). Variable names (`--night`, `--plum`, `--gold`…) are kept from v1 so the CSS below doesn't change.
- `--pink` (favorites) and `--mint` (sung) are functional state colors, not brand accents.
- Fonts: Cinzel + Forum (Cyrillic fallback) for display, Montserrat for body/UI, Great Vibes for script moments only.
- Logos: `rk-emblem.webp` (header + intro), `rk-wordmark.webp` (intro). Icons: `favicon-32.png`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png`.

## Rules
- Every UI string in English, Russian and Ukrainian.
- Don't rename the storage key `spoyka.v1` or move the app off `www.russiankaraoke.app` — guests' saved lists would vanish.
- Dark theme only.

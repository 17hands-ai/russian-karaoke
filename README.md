# Russian Karaoke — guest app

The customer-facing app for Russian Karaoke nights, brought to you by [17hands.ai](https://17hands.ai). Live at [russiankaraoke.app](https://russiankaraoke.app).

This repo is the app only. It is what guests open on their phones at an event. The landing page for russiankaraoke.com lives in a separate repo.

Guests search the catalog by song or singer (Russian, Ukrainian or Latin letters), keep a list for tonight, save favorites, and track what they have sung. The interface is in English, Russian and Ukrainian. No account: each guest's name and lists stay in their own browser, and they can add the app to their home screen.

## Files

- `index.html` — the whole app (no build step)
- `rk-emblem.webp`, `rk-wordmark.webp` — logo emblem and wordmark; `favicon-32.png`, `icon-*.png`, `apple-touch-icon.png` — icons
- Brand (colors, fonts, logos): see `CLAUDE.md` and the `brand/` folder in the landing-page repo
- `songs.json` — the catalog: one artist per line, `[artist, [[title, №, № with backing vocals], …]]`; `0` means that version does not exist. Guests see the backing-vocals № first, because that is the version the host plays by default. Russian and Ukrainian songs only for now
- `tools/build.py` — rebuilds `songs.json` from the Excel export (drops the trailing `+` some titles carry and merges plain and backing-vocals rows into one song)

## Address

Keep the app on `www.russiankaraoke.app`. Saved lists and home-screen icons are tied to that exact address, so moving it would make guests' lists look empty. The storage key `spoyka.v1` in `index.html` is an internal leftover from a working name; renaming it would also wipe saved lists.

## Deploy

Static site. On Vercel: import this repo, framework preset "Other", no build command, output directory left as the root.

## Update the catalog

```
pip install xlrd
python3 tools/build.py RussianKaraokeList.xls songs.json
```

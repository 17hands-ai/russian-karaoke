# russian-karaoke

Спой-ка: a mobile karaoke songbook for guests, by [17hands.ai](https://17hands.ai).

Guests search the catalog by song or singer (Russian, Ukrainian or Latin letters), keep a list for tonight, save favorites, and track what they have sung. No account: each guest's name and lists stay in their own browser.

## Files

- `index.html` — the whole app (no build step)
- `songs.json` — the catalog: one artist per line, `[artist, [[title, №, № with backing vocals], …]]`; `0` means that version does not exist
- `tools/build.py` — rebuilds `songs.json` from the Excel export

## Deploy

Static site. On Vercel: import this repo, framework preset "Other", no build command, output directory left as the root.

## Update the catalog

```
pip install xlrd
python3 tools/build.py RussianKaraokeList.xls songs.json
```

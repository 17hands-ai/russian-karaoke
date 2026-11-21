import xlrd,json,sys,unicodedata,collections
sh=xlrd.open_workbook(sys.argv[1]).sheet_by_index(0)
groups=collections.OrderedDict(); anomalies=0
for r in range(1,sh.nrows):
    no,title,artist,bek=[unicodedata.normalize('NFC',str(sh.cell_value(r,c)).strip()) for c in range(4)]
    g=groups.setdefault((artist,title),[0,0])
    i=1 if bek else 0
    if g[i]: anomalies+=1; continue
    g[i]=int(no)
by_artist=collections.OrderedDict()
for (artist,title),(plain,bek) in groups.items():
    by_artist.setdefault(artist,[]).append([title,plain,bek])
artists=sorted(by_artist.items(),key=lambda kv:kv[0].lower())
for a,l in artists: l.sort(key=lambda s:s[0].lower())
with open(sys.argv[2],'w',encoding='utf-8') as f:
    f.write('[\n'+',\n'.join(json.dumps([a,l],ensure_ascii=False,separators=(',',':')) for a,l in artists)+'\n]\n')
print('rows',sh.nrows-1,'songs',len(groups),'artists',len(artists),'both versions',sum(1 for g in groups.values() if g[0] and g[1]),'backing only',sum(1 for g in groups.values() if not g[0]),'anomalies',anomalies)

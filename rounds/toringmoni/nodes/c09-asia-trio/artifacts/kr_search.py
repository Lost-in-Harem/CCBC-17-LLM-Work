"""Korean-panel search: hanja words whose hangul reading matches the marker layouts."""
import sys, pickle, csv, re
sys.path.insert(0,'work'); sys.path.insert(0,'artifacts')
from wordsearch import WORDS
sys.path.insert(0,'artifacts')
from hangul_shape import parts, layout, CHO, JUNG, JONG

R=pickle.load(open('work/scores5.pkl','rb'))
T={k:dict(v) for k,v in R.items()}
HAN=re.compile(r'^[㐀-鿿豈-﫿]+$')

def load_kengdic():
    out=[]
    with open('work/dict/kengdic.tsv',encoding='utf-8') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            h=(r.get('hanja') or '').strip()
            s=(r.get('surface') or '').strip()
            if not HAN.match(h): continue
            if len(h)!=len(s): continue
            if not all(0xAC00<=ord(c)<0xD7A4 for c in s): continue
            out.append((h,s,(r.get('gloss') or '').strip()))
    return out

KD=load_kengdic()
print('kengdic hanja/hangul pairs:',len(KD), file=sys.stderr)

def ws(wk,w):
    cells=[f'{wk}#{i+1}' for i in range(WORDS[wk])]
    try: return [T[c][ch] for c,ch in zip(cells,w)]
    except KeyError: return None

def search(wk, need_layout, extra=None):
    res=[]
    seen=set()
    for h,s,g in KD:
        if len(h)!=WORDS[wk]: continue
        ok=True
        for pos,lay in need_layout.items():
            if layout(s[pos])!=lay: ok=False;break
        if not ok: continue
        if extra and not extra(s): continue
        v=ws(wk,h)
        if not v: continue
        key=(h,s)
        if key in seen: continue
        seen.add(key)
        res.append((min(v),sum(v)/len(v),h,s,g[:40]))
    res.sort(key=lambda r:-r[1])
    return res

if __name__=='__main__':
    which=sys.argv[1] if len(sys.argv)>1 else 'all'
    specs={
      'JP_+1_L': {0:'vert3'},
      'JP_+1_R': {2:'vert3', 3:'mixed2'},
      'JP_+5_L': {1:'3band', 2:'vert3'},
      'JP_+7_R': {0:'3band'},
      'JP_+5_R': {},
      'JP_+7_L': {},
    }
    for wk,need in specs.items():
        if which!='all' and which!=wk: continue
        r=search(wk,need)
        print(f'== {wk} layouts {need} : {len(r)} hits')
        for mn,av,h,s,g in r[:25]:
            print(f'   avg={av:.3f} min={mn:.3f}  {h} = {s}   {g}')

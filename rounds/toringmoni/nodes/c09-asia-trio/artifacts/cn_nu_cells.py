"""Rank 女-radical characters at CN_-6_L#2 / CN_+6_R#1 under the marker's pinyin
letter-shape.  The footer only records "vowel carrying a diacritic", so the TONE
is unrecoverable from the drawing - only the letter matters."""
import re, pickle, sys
sys.path.insert(0,'work'); sys.path.insert(0,'artifacts')
from pinyin_shape import load_cedict_pinyin, letter_shape
ids=pickle.load(open('work/dict/ids.pkl','rb'))
R=pickle.load(open('work/scores5.pkl','rb'))
E=load_cedict_pinyin()
PY1={}
for trad,simp,syls in E:
    for w in (trad,simp):
        if len(w)==1: PY1.setdefault(w,set()).add(syls[0].lower())
def nu(c): return any(s.startswith('⿰女') for s in ids.get(c,[]))
def rank(cell,pat,idx,n=15):
    print(f'== {cell}: 女-radical, pinyin letter-shape {pat}')
    k=0
    for i,(c,v) in enumerate(R[cell]):
        if not nu(c): continue
        for p in sorted(PY1.get(c,())):
            ls=letter_shape(p)
            if ls and tuple(ls[1])==pat:
                print(f'   #{i+1:<6} {c} {v:.3f}  {p}  -> footer letter "{ls[0][idx]}"')
                k+=1; break
        if k>=n: break
rank('CN_-6_L#2',(1,1,2),2)
print()
rank('CN_+6_R#1',(1,2),1)

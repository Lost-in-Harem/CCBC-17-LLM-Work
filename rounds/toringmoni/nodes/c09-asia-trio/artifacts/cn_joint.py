import sys, pickle, re
sys.path.insert(0,'work'); sys.path.insert(0,'artifacts')
from pinyin_shape import load_cedict_pinyin, letter_shape
from wordsearch import WORDS
R=pickle.load(open('work/scores5.pkl','rb'))
T={k:dict(v) for k,v in R.items()}
RK={k:{c:i+1 for i,(c,s) in enumerate(v)} for k,v in R.items()}
E=load_cedict_pinyin()
def run(wk,pos,pat,idx,allowed,maxrank):
    res=[];seen=set()
    for trad,simp,syls in E:
        for w in (simp,trad):
            if len(w)!=WORDS[wk] or w in seen: continue
            ls=letter_shape(syls[pos])
            if not ls: continue
            body,comps=ls
            if tuple(comps)!=pat: continue
            L=body[idx]
            if allowed and L not in allowed: continue
            cells=[f'{wk}#{i+1}' for i in range(WORDS[wk])]
            try:
                v=[T[c][ch] for c,ch in zip(cells,w)]; rk=[RK[c][ch] for c,ch in zip(cells,w)]
            except KeyError: continue
            if max(rk)>maxrank: continue
            seen.add(w)
            res.append((max(rk),sum(v)/len(v),w,' '.join(syls),L,rk))
    res.sort()
    print(f'== {wk}: both cells within top {maxrank} ({len(res)} hits)')
    for mr,av,w,s,L,rk in res[:25]:
        print(f'   worstrank={mr:<6} avg={av:.3f}  {w} [{s}] -> {L}   ranks={rk}')
run('CN_-6_L',1,(1,1,2),2,set('aou'),1500)
run('CN_+6_R',0,(1,2),1,set('aeiu'),1500)

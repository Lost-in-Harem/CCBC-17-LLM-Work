import sys, pickle, re
sys.path.insert(0,'work'); sys.path.insert(0,'artifacts')
from pinyin_shape import letter_shape
R=pickle.load(open('work/scores5.pkl','rb'))
# char -> set of pinyin (tone-numbered) from cedict single-char entries
CH={}
for line in open('work/dict/cedict.txt',encoding='utf-8'):
    if line.startswith('#'): continue
    m=re.match(r'^(\S+) (\S+) \[([^\]]*)\]', line)
    if not m: continue
    trad,simp,py=m.groups(); syls=py.split()
    if len(simp)==1 and len(syls)==1:
        CH.setdefault(simp,set()).add(syls[0]); CH.setdefault(trad,set()).add(syls[0])
cell=sys.argv[1]; pat=tuple(int(x) for x in sys.argv[2].split(','))
idx=int(sys.argv[3]); allowed=set(sys.argv[4]) if len(sys.argv)>4 else None
n=int(sys.argv[5]) if len(sys.argv)>5 else 25
out=[]
for rank,(ch,s) in enumerate(R[cell],1):
    for p in CH.get(ch,()):
        ls=letter_shape(p)
        if not ls: continue
        body,comps=ls
        if tuple(comps)!=pat: continue
        L=body[idx]
        if allowed and L not in allowed: continue
        out.append((s,rank,ch,p,L)); break
    if len(out)>=n: break
for s,rk,ch,p,L in out: print(f'{s:.3f} #{rk:<6} {ch} [{p}] -> {L}')

"""All 6-kana Japanese readings X X ち ゅ Y Z, scored against the marked cells."""
import sys, pickle, re
sys.path.insert(0,'work'); sys.path.insert(0,'artifacts')
from readings import load as load_read, to_hira
from jp_search import edict, char_readings
R=pickle.load(open('work/scores5.pkl','rb'))
T={k:dict(v) for k,v in R.items()}
RD=load_read()

def best_char(cell, pred):
    """best-scoring char at `cell` whose reading set satisfies pred -> (score, char, reading)"""
    for ch,s in R[cell]:
        rs=char_readings(ch)
        for r in rs:
            if pred(r): return (s,ch,r)
    return (0.0,'?','?')

ED=edict()
reads={}
for surf,r in ED:
    if len(r)==6 and r[2]=='ち' and r[3]=='ゅ':
        reads.setdefault(r,set()).add(surf)
print('candidate 6-kana readings with ちゅ at 3-4:',len(reads), file=sys.stderr)
out=[]
for r,surfs in reads.items():
    a=r[0:2]; k5=r[4]; k6=r[5]
    s1=best_char('KR_+4_L#1', lambda x,a=a: x==a)
    s5=best_char('KR_+8_L#1', lambda x,k5=k5: len(x)==3 and x[2]==k5)
    s6=best_char('KR_+8_L#2', lambda x,k6=k6: x==k6)
    sc=min(s1[0],s5[0],s6[0])
    out.append((sc,r,sorted(surfs)[:3],s1,s5,s6))
out.sort(reverse=True)
for sc,r,w,s1,s5,s6 in out[:30]:
    print(f'min={sc:.3f} {r} {w}')
    print(f'      +4L#1 {s1[1]}({s1[2]}) {s1[0]:.3f} | +8L#1 {s5[1]}({s5[2]}) {s5[0]:.3f} | +8L#2 {s6[1]}({s6[2]}) {s6[0]:.3f}')

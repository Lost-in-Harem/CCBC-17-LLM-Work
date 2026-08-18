"""Final scoring sweep: Source Han Sans weights + regional variants."""
import sys, os, numpy as np, pickle
sys.path.insert(0,'work')
from model3 import grid
import model as M
from search import charset
from observed import load

COMBOS = [('sansSC',0.0,0.88),('sansSC',0.03,0.88),('sansSC',0.01,0.89),
          ('shsLight',0.01,0.88),('shsDemi',0.0,0.88),('shsDemi',0.01,0.89),('shsDemi',0.03,0.88),
          ('shsMed',0.01,0.88),('shsBold',0.03,0.88),('shsBlack',0.05,0.88),
          ('sansJP',0.03,0.88),('sansKR',0.03,0.88),('sansTC',0.03,0.88),('serifSC',0.03,0.88)]

def db(fam,th,top):
    p=f'work/rv5_{fam}_{th}_{top}.npz'
    if os.path.exists(p):
        z=np.load(p,allow_pickle=True); return list(z['chars']), z['rv']
    chars=[];rv=[]
    for ch in charset('han'):
        g=grid(ch,fam,thresh=th,top=top)
        if g is None: continue
        chars.append(ch); rv.append(M.rooms(g).astype(np.int8))
    rv=np.stack(rv); np.savez_compressed(p,chars=np.array(chars),rv=rv)
    return chars,rv

def packed(rv):
    N=rv.shape[0]; out=np.empty((N,512),np.uint8); step=2000
    for a in range(0,N,step):
        b=rv[a:a+step]
        pm=(b[:,:,None]==b[:,None,:]).reshape(b.shape[0],4096)
        out[a:a+step]=np.packbits(pm,axis=1)
    return out

if __name__=='__main__':
    obs=load(); acc={k:{} for k in obs}
    for fam,th,top in COMBOS:
        chars,rv=db(fam,th,top); P=packed(rv)
        for k,g in obs.items():
            t=(g.reshape(64)[:,None]==g.reshape(64)[None,:]).reshape(1,4096)
            tp=np.packbits(t,axis=1)
            s=1-np.bitwise_count(np.bitwise_xor(P,tp)).sum(axis=1)/4096.0
            a=acc[k]
            for c,v in zip(chars,s):
                v=float(v)
                if v>a.get(c,0): a[c]=v
        print('done',fam,th,top, flush=True)
    res={k:sorted(v.items(),key=lambda kv:-kv[1]) for k,v in acc.items()}
    pickle.dump(res,open('work/scores5.pkl','wb'))
    for k in sorted(res):
        print(k, ' '.join(f'{c}:{v:.3f}' for c,v in res[k][:12]))

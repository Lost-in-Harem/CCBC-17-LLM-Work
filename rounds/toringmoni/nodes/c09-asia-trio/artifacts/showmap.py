"""Print the observed room map for a cell next to the model's map for given chars."""
import sys, numpy as np
sys.path.insert(0,'work')
from model3 import grid
import model as M
from observed import load
COMBOS=[('sansSC',0.0,0.88),('sansSC',0.03,0.88),('sansSC',0.01,0.89),
        ('shsLight',0.01,0.88),('shsDemi',0.0,0.88),('shsDemi',0.01,0.89),('shsDemi',0.03,0.88),
        ('shsMed',0.01,0.88),('shsBold',0.03,0.88),('shsBlack',0.05,0.88),
        ('sansJP',0.03,0.88),('sansKR',0.03,0.88),('sansTC',0.03,0.88),('serifSC',0.03,0.88)]
def canon(g):
    m={};o=[]
    for v in g.reshape(-1):
        if v not in m: m[v]=len(m)
        o.append(m[v])
    return np.array(o).reshape(8,8)
def agree(a,b):
    x=(a.reshape(64)[:,None]==a.reshape(64)[None,:]); y=(b.reshape(64)[:,None]==b.reshape(64)[None,:])
    return (x==y).mean()
obs=load()
cell=sys.argv[1]; chars=sys.argv[2]
O=canon(obs[cell])
best={}
for ch in chars:
    bs=-1;bg=None
    for fam,th,top in COMBOS:
        g=grid(ch,fam,thresh=th,top=top)
        if g is None: continue
        r=M.rooms(g); s=agree(O,r)
        if s>bs: bs,bg=s,canon(r)
    best[ch]=(bs,bg)
rows=[('OBS',O)]+[(f'{c} {best[c][0]:.3f}',best[c][1]) for c in chars if best[c][1] is not None]
hdr=''.join(f'{n:<12}' for n,_ in rows); print(hdr)
for i in range(8):
    print(''.join(''.join(str(x%10) for x in g[i])+'    ' for _,g in rows))

"""Rank characters for a cell, requiring an EXACT partition match on a chosen
subset of the 8x8 grid (a structural constraint read off the drawing) and
ranking the survivors by their full-grid agreement."""
import sys, os, numpy as np
sys.path.insert(0,'work')
from observed import load
COMBOS=[('sansSC',0.0,0.88),('sansSC',0.03,0.88),('sansSC',0.01,0.89),
        ('shsLight',0.01,0.88),('shsDemi',0.0,0.88),('shsDemi',0.01,0.89),('shsDemi',0.03,0.88),
        ('shsMed',0.01,0.88),('shsBold',0.03,0.88),('shsBlack',0.05,0.88),
        ('sansJP',0.03,0.88),('sansKR',0.03,0.88),('sansTC',0.03,0.88),('serifSC',0.03,0.88)]

def db(fam,th,top):
    p=f'work/rv5_{fam}_{th}_{top}.npz'
    z=np.load(p,allow_pickle=True); return list(z['chars']), z['rv']

def run(cell, rows, extra_cells=()):
    obs=load()[cell].reshape(64)
    S=[r*8+c for r in rows for c in range(8)]+list(extra_cells)
    S=np.array(sorted(set(S)))
    tgtS=(obs[S][:,None]==obs[S][None,:])
    tgtF=(obs[:,None]==obs[None,:])
    best={}
    for fam,th,top in COMBOS:
        try: chars,rv=db(fam,th,top)
        except FileNotFoundError: continue
        R=rv.reshape(len(chars),64)
        for i,c in enumerate(chars):
            r=R[i]
            if not np.array_equal((r[S][:,None]==r[S][None,:]), tgtS): continue
            f=((r[:,None]==r[None,:])==tgtF).mean()
            if f>best.get(c,0): best[c]=f
    return sorted(best.items(), key=lambda kv:-kv[1])

if __name__=='__main__':
    cell=sys.argv[1]; rows=[int(x) for x in sys.argv[2].split(',')]
    res=run(cell,rows)
    print(f'{cell}: exact partition match on rows {rows} -> {len(res)} characters')
    print('  '+' '.join(f'{c}:{v:.3f}' for c,v in res[:60]))

def cols(cell, cs):
    import numpy as np
    return run(cell, [], extra_cells=[r*8+c for r in range(8) for c in cs])

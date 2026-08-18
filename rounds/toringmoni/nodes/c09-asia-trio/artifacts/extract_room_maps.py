"""Observed 8x8 room maps for every character cell on the card."""
import json, numpy as np

def load():
    d = json.load(open('work/walls.json'))
    out = {}
    for k, v in d.items():
        if k == 'EXAMPLE': continue
        n = v['n']; V = v['V']; H = v['H']
        for c in range(n):
            g = np.full((8,8), -1, np.int32); r = 0
            for j in range(8):
                for i in range(8):
                    if g[j,i] >= 0: continue
                    st = [(j,i)]; g[j,i] = r
                    while st:
                        cj, ci = st.pop()
                        gi = c*8+ci
                        if ci+1 < 8 and not V[gi+1][cj] and g[cj,ci+1] < 0:
                            g[cj,ci+1] = r; st.append((cj,ci+1))
                        if ci-1 >= 0 and not V[gi][cj] and g[cj,ci-1] < 0:
                            g[cj,ci-1] = r; st.append((cj,ci-1))
                        if cj+1 < 8 and not H[cj+1][gi] and g[cj+1,ci] < 0:
                            g[cj+1,ci] = r; st.append((cj+1,ci))
                        if cj-1 >= 0 and not H[cj][gi] and g[cj-1,ci] < 0:
                            g[cj-1,ci] = r; st.append((cj-1,ci))
                    r += 1
            out[f'{k}#{c+1}'] = g
    return out

if __name__ == '__main__':
    o = load()
    for k in sorted(o):
        print('==', k, 'rooms=', len(set(o[k].reshape(64).tolist())))
        for j in range(8):
            print('   '+' '.join(f'{int(v):2d}' for v in o[k][j]))

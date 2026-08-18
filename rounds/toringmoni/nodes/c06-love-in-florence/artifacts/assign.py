# -*- coding: utf-8 -*-
"""M80 assignment DP: choose a set of disjoint carriers covering the stanza,
one per marker (any order), each carrier's loanword length = that marker's b.
Everything else must be common English."""
import sys, os
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import DICT, COMMON, LOAN, BIG
VOCAB = set(w for w in COMMON if len(w) >= 3) | set(
 'AN AT TO OF IN IS IT HE BE OR ON AS BY WE DO IF MY UP SO NO US AM ME GO A I S'.split())
VOCAB |= set(w for w in BIG if len(w) >= 6)
if os.environ.get('XV'): VOCAB |= set(os.environ['XV'].upper().split(','))
MAXW = max(len(w) for w in VOCAB)
PRE, SUF = defaultdict(list), defaultdict(list)
for W in DICT:
    if not (3 <= len(W) <= 14): continue
    for p in range(1, min(9, len(W))): PRE[W[:p]].append(W)
    for q in range(1, min(9, len(W))): SUF[W[len(W)-q:]].append(W)
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]
MINM = int(os.environ.get('MINM', '2'))

def carriers_at(s, pos, blen):
    n = len(s); res = []
    for p in range(0, min(9, blen)):
        A = s[pos:pos+p]
        if len(A) < p: break
        for ml in range(MINM, 14):
            m0, m1 = pos+p, pos+p+ml
            if m1 > n: break
            M = s[m0:m1]
            if M not in COMMON: continue
            for q in range(0, min(9, blen-p)):
                C = s[m1:m1+q]
                if len(C) < q: break
                if p + q < 1 or p + q >= blen: continue
                if p: cands = PRE.get(A, [])
                elif q: cands = SUF.get(C, [])
                else: continue
                for W in cands:
                    if len(W) != blen: continue
                    if W[:p] != A: continue
                    if q and W[blen-q:] != C: continue
                    X = W[p:blen-q] if q else W[p:]
                    if not X or X == M: continue
                    res.append((p+ml+q, W, A, M, C))
    return res

def solve(si, markers=None, topn=6):
    ms = markers if markers else STANZAS[si][1]
    s = STREAM[si]; n = len(s); K = len(ms)
    CACHE = {}
    def carr(pos, b):
        if (pos, b) not in CACHE: CACHE[(pos, b)] = carriers_at(s, pos, b)
        return CACHE[(pos, b)]
    FULL = (1 << K) - 1
    best = {(0, 0): (0.0, [])}
    frontier = defaultdict(set); frontier[0].add(0)
    for pos in range(n):
        for mask in list(frontier[pos]):
            st = (pos, mask)
            if st not in best: continue
            sc, trail = best[st]
            for L in range(2, min(MAXW, n-pos)+1):
                w = s[pos:pos+L]
                if w in VOCAB:
                    v = sc + L**1.25
                    st2 = (pos+L, mask)
                    if st2 not in best or best[st2][0] < v:
                        best[st2] = (v, trail + [('w', w)]); frontier[pos+L].add(mask)
            for k in range(K):
                if mask & (1 << k): continue
                for (cl, W, A, M, C) in carr(pos, ms[k][2]):
                    v = sc + 3.0 + (W in LOAN) * 25.0 + (len(A)+len(C))**1.3 + len(M)**1.1
                    st2 = (pos+cl, mask | (1 << k))
                    if st2 not in best or best[st2][0] < v:
                        best[st2] = (v, trail + [('c', (W, A, M, C, k))]); frontier[pos+cl].add(mask | (1 << k))
    res = best.get((n, FULL))
    tag = ' '.join(f'{p}({u or "-"}/{d})' for p,u,d in ms)
    print(f'===== stanza {si+1}  [{tag}]', flush=True)
    if not res:
        cands = [(p, m) for (p, m) in best]
        cands.sort(key=lambda x: (-x[0], -bin(x[1]).count('1')))
        print(f'  NO PARSE. stream({n}): {s}', flush=True)
        shown = 0
        for (p, m) in cands:
            if shown >= 4: break
            if p < n - 25: break
            sc2, tr = best[(p, m)]
            parts = []
            for kind, v in tr:
                if kind == 'w': parts.append(v.lower())
                else:
                    W, A, M, C, k = v
                    num = ms[k][1]
                    parts.append(f'<{A}[{M}]{C}={W}#{k+1}:{W[num-1] if num else "?"}>')
            print(f'   reach {p} mask {bin(m)} rest="{s[p:]}"', flush=True)
            print(f'     {" ".join(parts)}', flush=True)
            shown += 1
        return
    sc, trail = res
    parts, letters = [], [None]*K
    for kind, v in trail:
        if kind == 'w': parts.append(v.lower())
        else:
            W, A, M, C, k = v
            num = ms[k][1]
            L = W[num-1] if num else '?'
            letters[k] = L
            parts.append(f'<{A}[{M}]{C}={W}#{k+1}:{L}>')
    print('  ' + ' '.join(parts), flush=True)
    print(f'  ANSWER LETTERS (marker order): {"".join(x or "?" for x in letters)}   score {sc:.1f}', flush=True)

if __name__ == '__main__':
    for si in [int(x)-1 for x in sys.argv[1:]] or range(6):
        solve(si)

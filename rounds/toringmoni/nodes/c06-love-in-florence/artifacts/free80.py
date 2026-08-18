# -*- coding: utf-8 -*-
"""M80 free DP: minimise number of carriers; each carrier = A + M + C where
W = A+X+C is a dictionary word (any length 4..14), M a common English word."""
import sys, os
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import DICT, COMMON, LOAN, BIG
VOCAB = set(w for w in COMMON if len(w) >= 3) | set(
 'AN AT TO OF IN IS IT HE BE OR ON AS BY WE DO IF MY UP SO NO US AM ME GO A I S'.split())
VOCAB |= set(w for w in BIG if len(w) >= 7)
if os.environ.get('XV'): VOCAB |= set(os.environ['XV'].upper().split(','))
MAXW = max(len(w) for w in VOCAB)
PRE, SUF = defaultdict(list), defaultdict(list)
for W in DICT:
    if not (4 <= len(W) <= 14): continue
    for p in range(1, min(9, len(W))): PRE[W[:p]].append(W)
    for q in range(1, min(9, len(W))): SUF[W[len(W)-q:]].append(W)
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]

def carriers_at(s, pos):
    n = len(s); res = []
    for p in range(0, 9):
        A = s[pos:pos+p]
        if p and len(A) < p: break
        for ml in range(2, 13):
            m0, m1 = pos+p, pos+p+ml
            if m1 > n: break
            M = s[m0:m1]
            if M not in COMMON: continue
            for q in range(0, 9):
                C = s[m1:m1+q]
                if len(C) < q: break
                if p + q < 2: continue
                if p: cands = PRE.get(A, [])
                elif q: cands = SUF.get(C, [])
                else: continue
                for W in cands:
                    if len(W) <= p+q: continue
                    if p and q and not W.endswith(C): continue
                    if q and len(W) - q < p: continue
                    if W[:p] != A: continue
                    X = W[p:len(W)-q] if q else W[p:]
                    if not X or X == M: continue
                    res.append((p+ml+q, W, A, M, C))
    return res

def solve(si):
    s = STREAM[si]; n = len(s)
    INF = (10**9, 0)
    best = {0: ((0, 0), [])}
    for pos in range(n):
        if pos not in best: continue
        (nc, junk), trail = best[pos]
        for L in range(2, min(MAXW, n-pos)+1):
            w = s[pos:pos+L]
            if w in VOCAB:
                k = pos+L; v = (nc, junk)
                if k not in best or best[k][0] > v:
                    best[k] = (v, trail + [('w', w)])
        for (cl, W, A, M, C) in carriers_at(s, pos):
            k = pos+cl; v = (nc+1, junk)
            if k not in best or best[k][0] > v:
                best[k] = (v, trail + [('c', (W, A, M, C))])
    print(f'===== stanza {si+1}  markers: ' +
          ' '.join(f'{p}({u or "-"}/{d})' for p,u,d in STANZAS[si][1]), flush=True)
    if n not in best:
        print('  NO PARSE', flush=True); return
    (nc, junk), trail = best[n]
    print(f'  minimum carriers = {nc}', flush=True)
    print('  ' + ' '.join(v.lower() if k=='w' else f'<{v[1]}[{v[2]}]{v[3]}>' for k, v in trail), flush=True)
    # for each carrier slot, list dictionary options
    pos = 0
    for k, v in trail:
        if k == 'w': pos += len(v); continue
        W, A, M, C = v
        cl = len(A)+len(M)+len(C)
        opts = [(x[1] in LOAN, len(x[1]), x[1]) for x in carriers_at(s, pos)
                if x[0] == cl and x[2] == A and x[3] == M and x[4] == C]
        opts = sorted(set(opts), reverse=True)
        print(f'    carrier @{pos} "{A}[{M}]{C}" ({cl}): ' +
              ', '.join(f'{w}({l}){"*" if isl else ""}' for isl, l, w in opts[:14]), flush=True)
        pos += cl

for si in [int(x)-1 for x in sys.argv[1:]] or range(6):
    solve(si)

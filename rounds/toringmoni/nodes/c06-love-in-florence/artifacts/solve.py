# -*- coding: utf-8 -*-
"""Final extractor: for each marker (a/b, squares=n), the loanword W must have
len(W)=b and a Chinese rendering of exactly n characters; and W must appear in
the stanza as A+M+C where W=A+X+C and M is a common English word."""
import sys, os
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import COMMON
HERE = os.path.dirname(os.path.abspath(__file__))
Y = {}
for line in open(os.path.join(HERE, 'yayi.txt'), encoding='utf-8'):
    p = line.split()
    if len(p) >= 2: Y[p[0]] = p[1]
def nchar(z): return len([c for c in z if '一' <= c <= '鿿'])
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]
MINM = int(os.environ.get('MINM', '2'))
MINKEEP = int(os.environ.get('MINKEEP', '2'))

def find(W, s):
    """all (pos, A, M, C) with A+M+C in s, W = A+X+C, M common word"""
    out = []
    b = len(W); n = len(s)
    for p in range(0, b):
        A = W[:p]
        for q in range(0, b-p):
            C = W[b-q:] if q else ''
            if p + q < MINKEEP: continue
            X = W[p:b-q] if q else W[p:]
            if not X: continue
            start = 0
            while True:
                i = s.find(A, start) if A else start
                if A and i < 0: break
                j = i + p
                found = False
                for ml in range(MINM, 15):
                    if j+ml > n: break
                    M = s[j:j+ml]
                    if M not in COMMON or M == X: continue
                    if q and s[j+ml:j+ml+q] != C: continue
                    out.append((i, A, M, C))
                    found = True
                if A:
                    start = i + 1
                    if start > n: break
                else:
                    start = i + 1
                    if start > n - (p+q): break
    return out

for si, (_, ms) in enumerate(STANZAS):
    s = STREAM[si]
    print(f'===== stanza {si+1}', flush=True)
    for (pat, num, den) in ms:
        sq = len(pat)
        rows = []
        for W, z in Y.items():
            if len(W) != den or nchar(z) != sq: continue
            hits = find(W, s)
            if hits:
                best = max(hits, key=lambda h: len(h[1]) + len(h[3]))
                rows.append((len(best[1]) + len(best[3]), W, z, best))
        rows.sort(reverse=True)
        L = lambda W: W[num-1] if num else '?'
        print(f'  {pat}({num or "-"}/{den}) [{sq}字]: {len(rows)} candidates', flush=True)
        for keep, W, z, (i, A, M, C) in rows[:8]:
            print(f'      {W:12s} {z:10s} -> {L(W)}   text "{A}[{M}]{C}" @{i}', flush=True)

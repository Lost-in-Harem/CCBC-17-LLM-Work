# -*- coding: utf-8 -*-
"""For each marker, list every dictionary word of length b whose kept fragment
sits on a junk region. Ranked: common words first."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import COMMON, BIG, PLACES
from junk import isjunk, JUNK
DICT = BIG | PLACES
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]
MINKEEP = int(os.environ.get('MINKEEP', '3'))

def carriers(W, s, si):
    b = len(W); out = []
    for p in range(0, b):
        A = W[:p]
        for q in range(0, b-p):
            C = W[b-q:] if q else ''
            if p+q < MINKEEP: continue
            st = 0
            while True:
                i = s.find(A, st) if A else st
                if A and i < 0: break
                if not A and i > len(s)-q: break
                j = i+p
                for ml in range(2, 15):
                    if j+ml > len(s): break
                    M = s[j:j+ml]
                    if M not in COMMON: continue
                    if q and s[j+ml:j+ml+q] != C: continue
                    okA = p and isjunk(si, i, i+p)
                    okC = q and isjunk(si, j+ml, j+ml+q)
                    if okA or okC: out.append((p+q, A, M, C, i))
                st = i+1
                if st > len(s): break
    return out

for si in [int(x)-1 for x in sys.argv[1:]] or range(6):
    s = STREAM[si]
    print(f'===== stanza {si+1}  junk {[s[a:b] for a,b in JUNK[si]]}', flush=True)
    for (pat, num, den) in STANZAS[si][1]:
        rows = []
        for W in DICT:
            if len(W) != den: continue
            c = carriers(W, s, si)
            if c:
                best = max(c)
                rows.append((W in COMMON, best[0], W, best))
        rows.sort(key=lambda r: (-r[0], -r[1], r[2]))
        L = lambda W: W[num-1] if num else '?'
        letters = sorted({L(r[2]) for r in rows})
        print(f'  {pat}({num or "-"}/{den}) [{len(pat)}方框]: {len(rows)} words, letters {"".join(letters)}', flush=True)
        for isc, keep, W, (k, A, M, C, i) in rows[:14]:
            print(f'      {W:14s} -> {L(W)}  "{A}[{M}]{C}" @{i}', flush=True)

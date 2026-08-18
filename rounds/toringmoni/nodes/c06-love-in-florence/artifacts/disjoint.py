# -*- coding: utf-8 -*-
"""Rigorous: assign every marker a carrier such that the carriers occupy
PAIRWISE DISJOINT spans of the stanza text. Report all resulting answer words."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import COMMON
from junk import isjunk
HERE = os.path.dirname(os.path.abspath(__file__))
Y = {}
for line in open(os.path.join(HERE, 'yayi.txt'), encoding='utf-8'):
    p = line.split()
    if len(p) >= 2: Y[p[0]] = p[1]
def nchar(z): return len([c for c in z if '一' <= c <= '鿿'])
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]
MINKEEP = int(os.environ.get('MINKEEP', '2'))
BARE = os.environ.get('BARE', 'last')
WORDS = set(w.strip().upper() for w in open(os.path.join(HERE,'google10k.txt')) if len(w.strip())>=3)

def spans(W, s, si):
    """all (start, end, letter-index-word) placements of W as A+M+C"""
    out = []; b = len(W)
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
                    if okA or okC: out.append((i, j+ml+q))
                st = i+1
                if st > len(s): break
    return sorted(set(out))

for si, (_, ms) in enumerate(STANZAS):
    s = STREAM[si]
    opts = []
    for (pat, num, den) in ms:
        sq = len(pat); row = []
        for W, z in Y.items():
            if nchar(z) != sq: continue
            if num:
                if len(W) != den: continue
                idx = num
            else:
                if BARE == 'idx':
                    if len(W) < den: continue
                    idx = den
                else:
                    if len(W) != den: continue
                    idx = len(W)
            for (a, b) in spans(W, s, si):
                row.append((a, b, W, W[idx-1]))
        opts.append(row)
    # search for disjoint assignments
    res = set()
    n = len(ms)
    def rec(k, used, letters, chosen):
        if len(res) > 4000: return
        if k == n:
            res.add((''.join(letters), tuple(chosen))); return
        for (a, b, W, L) in opts[k]:
            if any(not (b <= x or a >= y) for (x, y) in used): continue
            rec(k+1, used+[(a, b)], letters+[L], chosen+[W])
    rec(0, [], [], [])
    answers = sorted({r[0] for r in res})
    good = [w for w in answers if w in WORDS]
    print(f'S{si+1}: {[len(o) for o in opts]} placements -> {len(res)} disjoint assignments', flush=True)
    print(f'   real words: {good[:30]}', flush=True)
    for w in good[:6]:
        ex = [r[1] for r in res if r[0] == w][0]
        print(f'      {w} <- {list(ex)}', flush=True)

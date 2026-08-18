# -*- coding: utf-8 -*-
"""Achievable letters per marker, then candidate answer words."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from puzzle import STANZAS
from lex import COMMON, BIG
from junk import isjunk
HERE = os.path.dirname(os.path.abspath(__file__))
Y = {}
for line in open(os.path.join(HERE, 'yayi.txt'), encoding='utf-8'):
    p = line.split()
    if len(p) >= 2: Y[p[0]] = p[1]
def nchar(z): return len([c for c in z if '一' <= c <= '鿿'])
STREAM = [''.join(c for c in s.upper() if c.isalpha()) for s, _ in STANZAS]
MINKEEP = int(os.environ.get('MINKEEP', '3'))

def has_carrier(W, s, si):
    b = len(W); best = None
    for p in range(0, b):
        A = W[:p]
        for q in range(0, b-p):
            C = W[b-q:] if q else ''
            if p + q < MINKEEP: continue
            st = 0
            while True:
                i = s.find(A, st) if A else st
                if A and i < 0: break
                if not A and i > len(s) - q: break
                j = i + p
                for ml in range(2, 15):
                    if j+ml > len(s): break
                    M = s[j:j+ml]
                    if M not in COMMON: continue
                    if q and s[j+ml:j+ml+q] != C: continue
                    okA = p and isjunk(si, i, i+p)
                    okC = q and isjunk(si, j+ml, j+ml+q)
                    if not (okA or okC): continue
                    if best is None or p+q > best[0]: best = (p+q, A, M, C, i)
                st = i + 1
                if st > len(s): break
    return best

WORDS = set(w.strip().upper() for w in open(os.path.join(HERE,'google10k.txt')) if len(w.strip())>=4)
WORDS |= set('''JADE COLD IRON PINE HORSE PULL MAPLE WHITE DEW DUST ASIA CAPE HOPE HORN GOOD
SAND LAND LAKE RAIN SOIL TAIL HAIR SAIL SHIP SKIN CHIN WEST EAST BEAR DEER HEAT MEAT PEAR
TASTE TOWER TIGER TRUTH TOOTH TOTAL TRACK TRAIN TREES THORN THUMB TRUNK TIDES TABLE
RICE LUCK ROCK DUCK NECK FACE RACE LACE PACE NICE MICE DICE LOCK SOCK DOCK BACK PACK SACK
GRASS CLOUD STONE RIVER PEARL IVORY CROWN SWEET BLACK LIGHT NIGHT WATER EAGLE SHEEP FIELD
MOUNT LOTUS JEWEL HOUSE GREEN AMBER CORAL SNOW MOON STAR GOLD SILK WOOD HILL BELL WOLF
OXEN FORD WELL DAWN SALT KING WAVE GATE CAVE PARK FARM PALM MAZE BANK HALL'''.split())

for si, (_, ms) in enumerate(STANZAS):
    s = STREAM[si]
    sets = []
    detail = []
    for (pat, num, den) in ms:
        sq = len(pat); D = {}
        BARE = os.environ.get('BARE', 'last')
        for W, z in Y.items():
            if nchar(z) != sq: continue
            if num:
                if len(W) != den: continue
                idx = num
            else:
                if BARE == 'idx':
                    if len(W) < den: continue
                    idx = den
                elif BARE == 'first':
                    if len(W) != den: continue
                    idx = 1
                else:
                    if len(W) != den: continue
                    idx = len(W)
            c = has_carrier(W, s, si)
            if c:
                L = W[idx-1]
                D.setdefault(L, []).append((c[0], W, z, c))
        sets.append(set(D) if D else set('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        detail.append(D)
    n = len(ms)
    cands = [w for w in WORDS if len(w) == n and all(w[i] in sets[i] for i in range(n))]
    print(f'S{si+1}: sets = ' + ' | '.join(''.join(sorted(x)) if len(x)<26 else '*' for x in sets), flush=True)
    print(f'   candidate answers: {sorted(cands)[:25]}', flush=True)
    for i, D in enumerate(detail):
        top = sorted(((max(v)[0], k, max(v)[1], max(v)[2]) for k, v in D.items()), reverse=True)[:6]
        print(f'   m{i+1} {ms[i][0]}({ms[i][1] or "-"}/{ms[i][2]}): ' +
              ', '.join(f'{k}<-{w}({z})' for _, k, w, z in top), flush=True)

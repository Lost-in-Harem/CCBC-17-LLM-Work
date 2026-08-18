"""Joint solver: assemble each footer string from the marker-constrained readings.

Run from the node directory.  Requires work/scores5.pkl (see score_cells.py),
work/dict/{cedict.txt,edict2.utf8,kengdic.tsv} and work/dict/unihan/.

Chinese  -> Korean panel footer : 3 groups of 2/3/2 pinyin letters
Korean   -> Japanese panel footer: 2 groups of 2/3 hangul syllables
Japanese -> Chinese panel footer : 1 group of 6 kana (box 4 is half-size = small kana)
"""
import sys, pickle
sys.path.insert(0, 'work')
from jp_search import edict, align, ws
from wordsearch import WORDS

SMALL = {'あ':'ぁ','い':'ぃ','う':'ぅ','え':'ぇ','お':'ぉ',
         'つ':'っ','や':'ゃ','ゆ':'ゅ','よ':'ょ','わ':'ゎ'}

def cands(wk, need):
    """Words for `wk` whose reading splits so that position p has `need[p]` kana."""
    out = {}
    for surf, read in edict():
        if len(surf) != WORDS[wk]: continue
        v = ws(wk, surf)
        if not v: continue
        a = align(surf, read)
        if not a: continue
        if all(len(a[p]) == c for p, c in need.items()):
            out.setdefault(surf, (min(v), sum(v)/len(v), a))
    return out

def kana_footer():
    """Every 6-kana Japanese reading reachable from the five marked cells."""
    c4  = cands('KR_+4_L', {0:2})      # boxes 1,2
    c8R = cands('KR_+8_R', {1:1})      # box 3
    c3  = cands('KR_-3_L', {2:2})      # box 4 (rendered small)
    c8L = cands('KR_+8_L', {0:3, 1:1}) # boxes 5,6
    def idx(c, f):
        d = {}
        for s, (mn, av, a) in c.items():
            k = f(a)
            if k is None: continue
            if k not in d or mn > d[k][0]: d[k] = (mn, s, '-'.join(a))
        return d
    i12 = idx(c4,  lambda a: a[0][0] + a[0][1])
    i3  = idx(c8R, lambda a: a[1])
    i4  = idx(c3,  lambda a: SMALL.get(a[2][0]))
    i56 = idx(c8L, lambda a: a[0][2] + a[1])
    reads = {}
    for s, r in edict():
        if len(r) == 6: reads.setdefault(r, []).append(s)
    out = []
    for r, words in reads.items():
        a, b, c, d = r[0:2], r[2], r[3], r[4:6]
        if a in i12 and b in i3 and c in i4 and d in i56:
            out.append((min(i12[a][0], i3[b][0], i4[c][0], i56[d][0]),
                        r, words[:3], i12[a], i3[b], i4[c], i56[d]))
    out.sort(reverse=True)
    return out

if __name__ == '__main__':
    res = kana_footer()
    print(f'{len(res)} assemblies whose 6-kana string is a real Japanese reading')
    for sc, r, w, *src in res[:20]:
        print(f'  min={sc:.3f} {r} {w}')
        print('        ' + '  '.join(f'{s[1]}({s[2]})' for s in src))

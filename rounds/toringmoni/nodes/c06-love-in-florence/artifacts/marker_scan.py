#!/usr/bin/env python3
"""One parameterised tester for the "square/fraction marker" hypothesis family.

Model under test
----------------
A marker  <squares>(a/b)  is read as:
  * b            = number of letters of a city name,
  * a            = 1-based index of the letter this marker contributes,
  * squares      = the *extra* letters of the carrier, one square each, read in
                   the order they occur in the carrier.
So a carrier is a stretch of the stanza with exactly  b + len(squares) letters
whose multiset is  city + extras.

Two readings of the squares are supported (both fit the FLORENCE anchor):
  --squares cv    black = consonant, white = vowel                  (default)
  --squares dup   black = letter absent from the city, white = present

Anchor that motivates the model:
  ceranflower (11) = FLORENCE (8) + A,W,R  ->  □■■(5/8)  ->  FLORENCE[5] = E

Usage examples (run from the Node directory):
  python3 artifacts/marker_scan.py scan    --dict work/cities15000.txt --minpop 150000
  python3 artifacts/marker_scan.py scan    --free --scope poem
  python3 artifacts/marker_scan.py letters --minpop 200000 --free --scope poem
  python3 artifacts/marker_scan.py csp     --dict work/cities15000.txt
Get the gazetteer with:
  curl -sLO https://download.geonames.org/export/dump/cities15000.zip
"""
import argparse, itertools, os, sys, unicodedata
from collections import Counter, defaultdict

# --------------------------------------------------------------- puzzle data
STANZAS = [
 ("A ushow's model should learn how to linchoearth tal or dress for phonegua shifting, "
  "such as adding a piece of outerni to highlight livelate.",
  [("101", 4, 9), ("101", 3, 4), ("110", 3, 6), ("111", 7, 11)]),
 ("Dear ckerman, I do p mean to offend you but it's ther haman's to songssant na tacroi "
  "filled e rotles!",
  [("11", 4, 9), ("1110", 1, 6), ("11", 4, 6), ("11", None, 5), ("11", None, 5)]),
 ("Being kstar of tiredness, this product is dac a ronher's choice to help you maup enter "
  "a iman's state of funthon at kea at any sheyinterval.",
  [("101", 5, 8), ("11", 5, 7), ("11", 1, 4), ("111", 6, 6), ("11", 4, 4)]),
 ("If Draco marfo meets sovie, ta is likely to be confused by the culture where soldiers "
  "da enemies with bullets gypt shells.",
  [("1110", 3, 8), ("11", 1, 5), ("11", 1, 4), ("110", 3, 7)]),
 ("If he ate a ceranflower instead of that fruit, he might be presumed innocent in stf, "
  "which is disappointing ty the reversepar toaing cinth.",
  [("111", 3, 6), ("11", 4, 5), ("011", 5, 8), ("11", 2, 5)]),
 ("I mingb that a tidot with hailus and a menfast's vibe is ordinary, but what if it's "
  "right in the middle of dymiddlehe?",
  [("110", 2, 9), ("11", 2, 5), ("101", 2, 6), ("11", None, 5)]),
]
# stanza 1 marker 2 is literally "(3/4 4)"; the three "(5)" markers carry no
# numerator in the source and are treated here as index 5 of a 5-letter name.
PSEUDO = {
 1: 'ushow linchoearth tal phonegua outerni livelate'.split(),
 2: 'ckerman p ther haman songssant na tacroi e rotles'.split(),
 3: 'kstar dac ronher maup iman funthon kea sheyinterval'.split(),
 4: 'marfo sovie ta da gypt'.split(),
 5: 'ceranflower stf ty reversepar toaing cinth'.split(),
 6: 'mingb tidot hailus menfast dymiddlehe'.split(),
}
VOWELS = set('AEIOU')

# ------------------------------------------------------------------ helpers
def words(sentence):
    out = []
    for tok in sentence.split():
        letters = ''.join(c for c in tok if c.isalpha()).upper()
        if letters:
            out.append((tok, letters))
    return out


def stream(si):
    """Letters of stanza si plus, per letter, the index of its printed word."""
    wl = words(STANZAS[si-1][0])
    s, owner = '', []
    for wi, (_, letters) in enumerate(wl):
        s += letters
        owner += [wi] * len(letters)
    return wl, s, owner


def pseudo_positions(si):
    wl, _, owner = stream(si)
    want = set()
    for wi, (tok, _) in enumerate(wl):
        base = ''.join(c for c in tok.lower() if c.isalpha())
        if base in PSEUDO[si] or base.rstrip('s') in PSEUDO[si]:
            want.update(i for i, o in enumerate(owner) if o == wi)
    return want


def spans(si, L, free):
    """Yield (start, end, letters, display) for every carrier of length L."""
    wl, s, owner = stream(si)
    if free:
        for a in range(len(s) - L + 1):
            disp = ' '.join(wl[w][0] for w in sorted(set(owner[a:a+L])))
            yield a, a + L, s[a:a+L], disp
    else:
        starts = {}
        pos = 0
        for wi, (_, letters) in enumerate(wl):
            starts[wi] = pos
            pos += len(letters)
        for i in range(len(wl)):
            seg = ''
            for j in range(i, len(wl)):
                seg += wl[j][1]
                if len(seg) > L:
                    break
                if len(seg) == L:
                    yield starts[i], starts[i] + L, seg, ' '.join(w[0] for w in wl[i:j+1])
                    break


def matcher(kind):
    if kind == 'cv':
        def sym(ch, city):
            return '0' if ch in VOWELS else '1'
    else:
        def sym(ch, city):
            return '0' if ch in city else '1'

    def match(span, city, pattern):
        k, need, cs = len(pattern), Counter(city), set(city)
        for pos in itertools.combinations(range(len(span)), k):
            if ''.join(sym(span[i], cs) for i in pos) != pattern:
                continue
            if Counter(span[i] for i in range(len(span)) if i not in pos) == need:
                return True
        return False
    return match


def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ''.join(c for c in s.upper() if c.isalpha())


def load_cities(path, minpop, alt):
    by_len = defaultdict(list)
    seen = set()
    with open(path, encoding='utf-8') as f:
        for line in f:
            p = line.rstrip('\n').split('\t')
            if len(p) < 15 or int(p[14] or 0) < minpop:
                continue
            names = [p[2] or p[1]]
            if alt and p[3]:
                names += [a for a in p[3].split(',') if a.isascii()]
            for n in names:
                k = norm(n)
                if 3 <= len(k) <= 14 and k not in seen:
                    seen.add(k)
                    by_len[len(k)].append(k)
    return by_len


def candidates(si, marker, by_len, match, free, scope):
    pat, num, den = marker
    L = den + len(pat)
    out = []
    for ti in ([si] if scope == 'stanza' else range(1, 7)):
        for a, b, seg, disp in spans(ti, L, free):
            for c in by_len.get(den, ()):
                if Counter(c) <= Counter(seg) and match(seg, c, pat):
                    out.append((ti, a, b, disp, c, c[num-1] if num else '?'))
    return out


# -------------------------------------------------------------------- modes
def mode_scan(args, by_len, match):
    for si, (_, ms) in enumerate(STANZAS, 1):
        for mi, m in enumerate(ms, 1):
            hits = candidates(si, m, by_len, match, args.free, args.scope)
            pat, num, den = m
            print(f'S{si}M{mi} {pat}({num or "-"}/{den}) len={den+len(pat)}: {len(hits)} hits')
            for h in hits[:args.show]:
                print(f'    S{h[0]} [{h[3]}] -> {h[4]} => {h[5]}')


def mode_letters(args, by_len, match):
    for si, (_, ms) in enumerate(STANZAS, 1):
        for mi, m in enumerate(ms, 1):
            hits = candidates(si, m, by_len, match, args.free, args.scope)
            letters = ''.join(sorted({h[5] for h in hits}))
            pat, num, den = m
            print(f'S{si}M{mi} {pat}({num or "-"}/{den}): {len(letters)} [{letters}]')


def mode_csp(args, by_len, match):
    """Disjoint carriers per stanza that also cover every pseudo-word letter."""
    for si, (_, ms) in enumerate(STANZAS, 1):
        rows = [candidates(si, m, by_len, match, args.free, 'stanza') for m in ms]
        need = pseudo_positions(si)
        print(f'S{si}: candidates {[len(r) for r in rows]} pseudo-letters {len(need)} '
              f'span-letters {sum(d+len(p) for p, _, d in ms)}')
        sols, order = [], sorted(range(len(rows)), key=lambda i: len(rows[i]))

        def rec(k, used, chosen):
            if len(sols) >= args.show:
                return
            if k == len(order):
                if need <= used:
                    sols.append(sorted(chosen))
                return
            for h in rows[order[k]]:
                r = set(range(h[1], h[2]))
                if r & used:
                    continue
                chosen.append((order[k], h))
                rec(k + 1, used | r, chosen)
                chosen.pop()
        rec(0, set(), [])
        print(f'   solutions: {len(sols)}')
        for sol in sols:
            print('   ', ''.join(h[5] for _, h in sol),
                  ' | ', ' ; '.join(f'{h[4]}<{h[3]}>' for _, h in sol))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['scan', 'letters', 'csp'])
    ap.add_argument('--dict', default='work/cities15000.txt', help='GeoNames dump')
    ap.add_argument('--minpop', type=int, default=0)
    ap.add_argument('--alt', action='store_true', help='also index alternate names')
    ap.add_argument('--free', action='store_true', help='ignore printed word boundaries')
    ap.add_argument('--scope', choices=['stanza', 'poem'], default='stanza')
    ap.add_argument('--squares', choices=['cv', 'dup'], default='cv')
    ap.add_argument('--show', type=int, default=8)
    args = ap.parse_args()
    if not os.path.exists(args.dict):
        sys.exit(f'gazetteer not found: {args.dict} (see the module docstring)')
    by_len = load_cities(args.dict, args.minpop, args.alt)
    print(f'# dict={args.dict} minpop={args.minpop} alt={args.alt} '
          f'spans={"free" if args.free else "word"} scope={args.scope} squares={args.squares}')
    {'scan': mode_scan, 'letters': mode_letters, 'csp': mode_csp}[args.mode](
        args, by_len, matcher(args.squares))


if __name__ == '__main__':
    main()

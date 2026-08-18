"""Pinyin letter shapes: how many ink components each letter of a syllable has.

A letter is drawn as one room unless it carries a dot or a diacritic:
  i / j            -> 2 (dot + stem)
  toned vowel      -> 2 (mark + body)
  ü                -> 3 (two dots + body)
"""
import re, pickle, os

VOWELS='aoeiuv'
def tone_index(syl):
    """Index of the letter that carries the tone mark (plain-letter syllable)."""
    s=syl
    if 'a' in s: return s.index('a')
    if 'o' in s: return s.index('o')
    if 'e' in s: return s.index('e')
    # iu -> u, ui -> i, otherwise last vowel
    for i in range(len(s)-1,-1,-1):
        if s[i] in 'iuv': return i
    return None

def letter_shape(syl_num):
    """'shu4' -> (letters, component counts per letter)."""
    m=re.match(r'^([a-zA-Zü:]+)([1-5])?$', syl_num)
    if not m: return None
    body=m.group(1).lower().replace('u:','v').replace('ü','v')
    tone=int(m.group(2) or 5)
    ti=tone_index(body) if tone in (1,2,3,4) else None
    comps=[]
    for i,ch in enumerate(body):
        n=1
        if ch in 'ij': n=2
        if ch=='v': n=3            # ü = two dots + body
        if ti is not None and i==ti:
            n = 2 if ch not in 'ijv' else n   # dot replaced by mark; ü keeps 3
        comps.append(n)
    return body, comps

def load_cedict_pinyin():
    p='work/dict/cedict_py.pkl'
    if os.path.exists(p): return pickle.load(open(p,'rb'))
    out=[]
    for line in open('work/dict/cedict.txt',encoding='utf-8'):
        if line.startswith('#'): continue
        m=re.match(r'^(\S+) (\S+) \[([^\]]*)\]', line)
        if not m: continue
        trad, simp, py = m.groups()
        syls=py.split()
        if len(syls)!=len(simp): continue
        out.append((trad, simp, syls))
    pickle.dump(out, open(p,'wb'))
    return out

if __name__=='__main__':
    for s in ['ku3','wu4','dan4','tou2','zhi1','ta1','nv3','liu2','shu4']:
        print(s, letter_shape(s))
    d=load_cedict_pinyin(); print('cedict entries with pinyin:', len(d))

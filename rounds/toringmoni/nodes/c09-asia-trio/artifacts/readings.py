"""Per-character readings from Unihan: Mandarin pinyin, Japanese kana, Korean hangul."""
import os, pickle, re

def load():
    p='work/dict/readings.pkl'
    if os.path.exists(p): return pickle.load(open(p,'rb'))
    d={}
    for line in open('work/dict/unihan/Unihan_Readings.txt',encoding='utf-8'):
        if line.startswith('#'): continue
        f=line.rstrip('\n').split('\t')
        if len(f)!=3: continue
        cp,key,val=f
        ch=chr(int(cp[2:],16))
        e=d.setdefault(ch,{})
        if key=='kJapanese':
            e['jp']=val.split()
        elif key=='kHangul':
            e['kr']=[v.split(':')[0] for v in val.split()]
        elif key=='kMandarin':
            e['py']=val.split()
    pickle.dump(d,open(p,'wb'))
    return d

KATA='ァィゥェォッャュョヮアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰヱヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴー'
HIRA='ぁぃぅぇぉっゃゅょゎあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゐゑをんがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽゔー'
K2H={k:h for k,h in zip(KATA,HIRA)}
def to_hira(s): return ''.join(K2H.get(c,c) for c in s)
SMALL='ぁぃぅぇぉっゃゅょゎ'
def morae(kana):
    """Split a kana string into glyph cells (a small kana is its own glyph here)."""
    return list(kana)

if __name__=='__main__':
    d=load(); print('chars',len(d))
    for c in '雪雷物線苦弹头锁物山地玲瓏':
        print(c, d.get(c))

"""Hangul syllable structure: how a syllable's jamo lay out in the square."""
CHO='ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
JUNG='ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
JONG=' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ'
VERT={0,1,2,3,4,5,6,7,20}          # ㅏㅐㅑㅒㅓㅔㅕㅖㅣ  -> vowel sits to the right
HORIZ={8,12,13,17,18}              # ㅗㅛㅜㅠㅡ          -> vowel sits below
def parts(s):
    o=ord(s)-0xAC00
    if not (0<=o<11172): return None
    c=o//588; v=(o%588)//28; j=o%28
    return CHO[c], JUNG[v], (JONG[j] if j else None), v

def layout(s):
    """'3band' | 'vert3' | '2col' | '2band' | 'mixed3' | 'mixed2'"""
    p=parts(s)
    if not p: return None
    c,v,j,vi=p
    if vi in HORIZ:  return '3band' if j else '2band'
    if vi in VERT:   return 'vert3' if j else '2col'
    return 'mixed3' if j else 'mixed2'

if __name__=='__main__':
    for s in '물선고포산각수라뇌설지':
        print(s, parts(s), layout(s))

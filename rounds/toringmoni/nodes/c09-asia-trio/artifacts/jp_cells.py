"""Rank Japanese-panel cells under the kana-count constraints read off the markers."""
import pickle, sys

SMALL = set('ャュョッァィゥェォヮゃゅょっぁぃぅぇぉゎヵヶ')
RD = pickle.load(open('work/dict/readings.pkl','rb'))
SC = pickle.load(open('work/scores5.pkl','rb'))

def hira(s):
    return ''.join(chr(ord(c)-0x60) if 0x30A1<=ord(c)<=0x30F6 else c for c in s)

def readings(ch, nkana, nosmall=True):
    """all readings of ch with exactly nkana kana (kun readings stripped of okurigana are NOT used)"""
    out=[]
    for r in RD.get(ch,{}).get('jp',[]):
        h=hira(r)
        if len(h)!=nkana: continue
        if nosmall and any(c in SMALL for c in h): continue
        out.append(h)
    return sorted(set(out))

def rank(cell, nkana, nosmall=True, top=40):
    res=[]
    for c,v in SC[cell]:
        rs=readings(c,nkana,nosmall)
        if rs: res.append((c,v,rs))
        if len(res)>=top: break
    return res

if __name__=='__main__':
    for cell,n,ns in [('KR_+4_L#1',2,True),('KR_+8_L#1',3,True),('KR_+8_L#2',1,True)]:
        print(f'=== {cell}  ({n} kana, no small) ===')
        for c,v,rs in rank(cell,n,ns,25):
            print(f'  {c} {v:.3f} {"/".join(rs)}')

"""Marker-consistent candidate filter.

The marker draws a character's part list: nested compositions in the same
direction are flattened (⿰A⿰BC -> three parts), and a part that itself
decomposes is drawn as a split box.
"""
import sys, pickle
sys.path.insert(0,'work')
from ids import IDS, parse, OPS

HORIZ = {'⿰':2,'⿲':3}
VERT  = {'⿱':2,'⿳':3}

def flatten(node):
    """Top-level part list with same-direction nesting flattened."""
    if isinstance(node,str): return [node]
    op,kids = node
    if op in HORIZ or op in VERT:
        fam = HORIZ if op in HORIZ else VERT
        out=[]
        for k in kids:
            if not isinstance(k,str) and k[0] in fam:
                out.extend(flatten(k))
            else:
                out.append(k)
        return out
    return list(kids)

def splits(part):
    if not isinstance(part,str): return True
    seqs=IDS.get(part)
    if not seqs: return False
    return any(s and s[0] in OPS for s in seqs)

ATOMIC = set('艹雨田牛月十口日一二三丨山川水火木土金人大小子女心手足目耳自口廿卅弓虫米糸言几冖宀广厂匚勹刀力又寸尸巾干幺廴彳彡纟讠钅饣扌氵忄犭阝辶亻亠冫凵匕卜厶囗夂夕宀寸小尢屮巛工己巾干幺广廴弋弓彐彡彳')

def sig(ch):
    seqs=IDS.get(ch)
    if not seqs: return {(1,(False,))}
    out=set()
    for s in seqs:
        try: node,_=parse(s,0)
        except Exception: continue
        parts=flatten(node)
        flags=tuple((False if (isinstance(p,str) and p in ATOMIC) else splits(p)) for p in parts)
        out.add((len(parts),flags))
    return out or {(1,(False,))}

MARK = {
 'CN_+2_L#1':(2,(0,1)), 'CN_-6_R#2':(2,(0,1)), 'CN_+6_R#1':(2,(0,1)),
 'CN_+7_L#2':(3,(0,1,0)), 'CN_+7_R#1':(3,(0,1,0)), 'CN_-6_L#2':(3,(0,0,1)),
 'JP_+5_L#2':(3,(0,0,0)), 'JP_+5_L#3':(2,(1,0)), 'JP_+1_L#1':(2,(1,0)),
 'JP_+1_R#3':(2,(1,0)), 'JP_+1_R#4':(2,(1,0)), 'JP_+7_R#1':(3,(0,0,0)),
 'KR_-3_L#3':(2,(0,0)), 'KR_+4_L#1':(2,(0,0)), 'KR_+8_L#1':(3,(0,0,0)),
 'KR_+8_L#2':(1,(0,)), 'KR_+8_R#2':(1,(0,)),
}

if __name__=='__main__':
    R=pickle.load(open('work/scores3.pkl','rb'))
    for cell,(n,flags) in MARK.items():
        want=(n,tuple(bool(x) for x in flags))
        exact=[]; loose=[]
        for c,v in R[cell][:1500]:
            S=sig(c)
            if want in S: exact.append((c,v))
            elif any(a==n for a,_ in S): loose.append((c,v))
        print(f'== {cell} need {want}')
        print('   exact: '+' '.join(f'{c}:{v:.3f}' for c,v in exact[:12]))
        print('   count-only: '+' '.join(f'{c}:{v:.3f}' for c,v in loose[:10]))

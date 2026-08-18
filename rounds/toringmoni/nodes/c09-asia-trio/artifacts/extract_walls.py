"""Extract the per-character 8x8 wall grid for every line-drawing on the card.

Grid convention (verified on JP_+5_L): each character cell is 72x72 px = 8x8 units
of 9 px; the drawing origin is (x0+1, y0+1) of the detected black bounding box.
"""
import numpy as np, json
from PIL import Image

A = np.array(Image.open('work/card_full.png').convert('L')).astype(int)
dark = A < 120
P = 9

WORDS = {
 'JP_+5_L': (829,128,3), 'JP_+5_R': (1117,128,2),
 'JP_+1_L': (829,272,2), 'JP_+1_R': (1045,273,4),
 'JP_+7_L': (829,417,2), 'JP_+7_R': (1045,417,2),
 'CN_+7_L': (250,600,2), 'CN_+7_R': (466,601,2),
 'CN_-6_L': (250,744,2), 'CN_-6_R': (467,744,3),
 'CN_+6_L': (250,888,2), 'CN_+6_R': (467,888,2),
 'CN_+2_L': (250,1032,2), 'CN_+2_R': (467,1032,3),
 'KR_-3_L': (872,1218,3), 'KR_-3_R': (1159,1218,2),
 'KR_+4_L': (872,1362,2), 'KR_+4_R': (1088,1362,3),
 'KR_+8_L': (872,1506,2), 'KR_+8_R': (1088,1506,2),
 'EXAMPLE': (158,129,1),
}

def edges(ox, oy, n):
    NX, NY = 8*n, 8
    def col(i): return ox + i*P
    def row(j): return oy + j*P
    V = [[0]*NY for _ in range(NX+1)]
    Hm = [[0]*NX for _ in range(NY+1)]
    for i in range(NX+1):
        for j in range(NY):
            hits = sum(1 for t in (0.3,0.5,0.7)
                       if dark[int(round(row(j)+P*t)), col(i)-1:col(i)+2].any())
            V[i][j] = int(hits>=2)
    for j in range(NY+1):
        for i in range(NX):
            hits = sum(1 for t in (0.3,0.5,0.7)
                       if dark[row(j)-1:row(j)+2, int(round(col(i)+P*t))].any())
            Hm[j][i] = int(hits>=2)
    return V, Hm, NX, NY

def render(V,Hm,NX,NY):
    out=[]
    for j in range(NY+1):
        out.append(''.join('+'+('--' if Hm[j][i] else '  ') for i in range(NX))+'+')
        if j<NY:
            out.append(''.join(('|' if V[i][j] else ' ')+('  ' if i<NX else '') for i in range(NX+1)))
    return out

def regions(V,Hm,NX,NY):
    lab=[[-1]*NX for _ in range(NY)]
    cur=0
    for sj in range(NY):
        for si in range(NX):
            if lab[sj][si]!=-1: continue
            st=[(sj,si)]; lab[sj][si]=cur
            while st:
                j,i=st.pop()
                if i+1<NX and not V[i+1][j] and lab[j][i+1]==-1: lab[j][i+1]=cur; st.append((j,i+1))
                if i-1>=0 and not V[i][j] and lab[j][i-1]==-1: lab[j][i-1]=cur; st.append((j,i-1))
                if j+1<NY and not Hm[j+1][i] and lab[j+1][i]==-1: lab[j+1][i]=cur; st.append((j+1,i))
                if j-1>=0 and not Hm[j][i] and lab[j-1][i]==-1: lab[j-1][i]=cur; st.append((j-1,i))
            cur+=1
    return lab,cur

out={}
for k,(ox,oy,n) in WORDS.items():
    V,Hm,NX,NY = edges(ox+1,oy+1,n)
    lab,cnt = regions(V,Hm,NX,NY)
    out[k]={'V':V,'H':Hm,'n':n,'regions':cnt,'lab':lab}
    print(f'==== {k}  cells={n} regions={cnt} ====')
    print('\n'.join(render(V,Hm,NX,NY)))
    print('labels:')
    for j in range(NY):
        print('  '+' '.join(f'{lab[j][i]:2d}' for i in range(NX)))
json.dump(out, open('work/walls.json','w'))

"""Extract the exact sub-box layout and colours of every marker / footer diagram."""
import numpy as np
from PIL import Image
from scipy import ndimage

A = np.array(Image.open('work/card_full.png').convert('RGB')).astype(int)
L = A.mean(axis=2); sat = A.max(axis=2)-A.min(axis=2)
BLACK = (L < 100) & (sat < 60)

BOXES = {
 'JP+5L_a':(920,84,956,120),'JP+5L_b':(991,84,1028,120),'JP+1L':(848,228,884,264),
 'JP+1R_a':(1208,228,1244,264),'JP+1R_b':(1280,228,1316,264),'JP+7R':(1064,372,1100,408),
 'JPfoot1':(1218,475,1254,503),'JPfoot2':(1263,475,1317,503),'JPfoot3':(1326,476,1362,503),
 'CN+7L':(332,565,386,593),'CN+7R':(476,565,530,593),'CN-6L':(332,709,387,737),
 'CN-6R':(557,709,594,737),'CN+6R':(485,853,522,881),'CN+2L':(269,997,306,1025),
 'CNfoot':(638,1137,737,1156),
 'KR-3L':(1034,1192,1071,1210),'KR+4L':(890,1336,927,1354),
 'KR+8L_a':(881,1480,936,1498),'KR+8L_b':(955,1480,1000,1498),'KR+8R':(1180,1474,1216,1502),
 'KRfoot1':(1183,1605,1255,1642),'KRfoot2':(1264,1605,1372,1642),
}

def analyse(name, x0,y0,x1,y1):
    sub = A[y0:y1+1, x0:x1+1]
    blk = BLACK[y0:y1+1, x0:x1+1]
    free = ~blk
    lab, n = ndimage.label(free)
    out = []
    H,W = blk.shape
    for i in range(1, n+1):
        ys, xs = np.nonzero(lab == i)
        if len(ys) < 25: continue
        if ys.min() == 0 or xs.min() == 0 or ys.max() == H-1 or xs.max() == W-1:
            # touching the outer edge: usually the paper outside the frame
            if len(ys) > 0.5*H*W: continue
        cols = sub[ys, xs]
        med = tuple(int(v) for v in np.median(cols, axis=0))
        out.append((xs.min(), ys.min(), xs.max(), ys.max(), len(ys), med))
    out.sort(key=lambda r: (r[0], r[1]))
    return out

if __name__ == '__main__':
    for k,(a,b,c,d) in BOXES.items():
        print(f'== {k}  size={c-a+1}x{d-b+1}')
        for x0,y0,x1,y1,n,rgb in analyse(k,a,b,c,d):
            print(f'   x[{x0:3d},{x1:3d}] y[{y0:3d},{y1:3d}] n={n:5d} rgb={rgb}')

"""Forward model v3: adds ink-bbox alignment and a scale factor."""
import sys, numpy as np
sys.path.insert(0,'work')
from PIL import Image, ImageDraw
from scipy import ndimage
import model as M

S8 = np.ones((3,3), int)
EM = 128

def grid(ch, fam='sansSC', em=EM, top=0.88, thresh=0.02, align='em', scale=1.0):
    f = M.font(fam, int(round(em*scale)))
    W = em*3
    img = Image.new('L',(W,W),255)
    ImageDraw.Draw(img).text((em, em*2), ch, font=f, fill=0, anchor='ls')
    m = np.array(img) < 128
    if not m.any(): return None
    lab,_ = ndimage.label(m, structure=S8)
    if align=='em':
        e = em*scale
        x0 = em - (e-em)/2.0
        y0 = em*2 - top*e + (0 if scale==1 else -(e-em)/2.0)
        ux = uy = e/8.0
    else:
        ys,xs = np.nonzero(m)
        x0 = xs.min(); y0 = ys.min()
        ux = (xs.max()-xs.min()+1)/8.0; uy = (ys.max()-ys.min()+1)/8.0
    g = np.full((8,8), -1, np.int32)
    for j in range(8):
        ya, yb = int(round(y0+j*uy)), int(round(y0+(j+1)*uy))
        for i in range(8):
            xa, xb = int(round(x0+i*ux)), int(round(x0+(i+1)*ux))
            blk = lab[max(0,ya):yb, max(0,xa):xb]
            v = blk[blk>0]
            if v.size and v.size >= thresh*max(1,(yb-ya)*(xb-xa)):
                g[j,i] = np.bincount(v).argmax()
    return g

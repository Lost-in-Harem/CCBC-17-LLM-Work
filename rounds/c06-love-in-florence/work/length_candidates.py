from pathlib import Path
from bs4 import BeautifulSoup
import re
s=BeautifulSoup((Path(__file__).parent/'all_sfzip'/'宣传页 - 旅行指南'/'index.html').read_text(encoding='utf8'),'html.parser')
for si,p in enumerate(s.select('.tg-poem-stanza'),1):
 ws=re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",p.find('span').get_text()); print('S',si)
 for sp in p.find_all('span')[1:]:
  bits=''.join('1' if c=='■' else '0' for c in sp.get_text() if c in '■□'); nums=[int(x) for x in re.findall(r'\d+',sp.get_text())]; a,b=(nums+[None,None])[:2]; b=a if b is None else b
  cs=[(j+1,w,w[a-1] if a<=len(w) else '?') for j,w in enumerate(ws) if len(re.sub("'",'',w))==b]
  print(sp.get_text(), 'b=',b,'a=',a,'v=',int(bits,2),cs)

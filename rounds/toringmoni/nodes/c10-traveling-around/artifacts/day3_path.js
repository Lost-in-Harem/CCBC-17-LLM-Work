const P=require("./day3_pieces.json");
const g=[[4,1,16,2],[3,6,7,10],[11,13,5,9],[12,14,15,8]];
const V=Array.from({length:12},()=>Array(13).fill(0));
const H=Array.from({length:13},()=>Array(12).fill(0));
const yl=[];
for(let R=0;R<4;R++)for(let C=0;C<4;C++){const p=P[g[R][C]];
  for(let i=0;i<4;i++)for(let j=0;j<3;j++){ if(p.v[i][j]) V[R*3+j][C*3+i]=1; if(p.h[i][j]) H[R*3+i][C*3+j]=1; }
  for(const [rr,cc] of p.y) yl.push([R*3+rr,C*3+cc]);
}
const ys=new Set(yl.map(a=>a.join(",")));
// draw maze
let art="";
for(let r=0;r<12;r++){
  let top="";
  for(let c=0;c<12;c++){ top += "+" + (H[r][c]?"---":"   "); }
  top+="+"; art+=top+"\n";
  let mid="";
  for(let c=0;c<12;c++){ mid += (V[r][c]?"|":" ") + (ys.has(r+","+c)?" Y ":"   "); }
  mid += (V[r][12]?"|":" "); art+=mid+"\n";
}
let bot=""; for(let c=0;c<12;c++) bot += "+" + (H[12][c]?"---":"   "); bot+="+"; art+=bot+"\n";
console.log(art);
// unique path
const adj=(r,c)=>{const a=[];if(c<11&&!V[r][c+1])a.push([r,c+1]);if(c>0&&!V[r][c])a.push([r,c-1]);if(r<11&&!H[r+1][c])a.push([r+1,c]);if(r>0&&!H[r][c])a.push([r-1,c]);return a;};
const prev={}; const seen=new Set(["0,0"]); const q=[[0,0]];
while(q.length){const [r,c]=q.shift(); for(const [nr,nc] of adj(r,c)){const k=nr+","+nc; if(!seen.has(k)){seen.add(k);prev[k]=r+","+c;q.push([nr,nc]);}}}
let cur="11,11"; const path=[];
while(cur){path.push(cur); cur=prev[cur];}
path.reverse();
console.log("path length",path.length);
console.log(path.join(" -> "));
const flags=path.map(p=>ys.has(p)?1:0);
console.log("flags:",flags.join(""));
console.log("yellow cells:",JSON.stringify(yl), "on path:",flags.reduce((a,b)=>a+b,0));
// runs of yellow
const runs=[]; let cnt=0;
for(const f of flags){ if(f) cnt++; else { if(cnt) runs.push(cnt); cnt=0; } }
if(cnt) runs.push(cnt);
console.log("yellow runs:",runs.join(","));
const morse=runs.map(n=>n>=2?"-":".").join("");
console.log("morse:",morse);

const P=require("./day3_pieces.json");
function perms(a){if(a.length<=1)return [a];const r=[];for(let i=0;i<a.length;i++){const rest=a.slice(0,i).concat(a.slice(i+1));for(const p of perms(rest))r.push([a[i]].concat(p));}return r;}
const topMid=[1,16], botMid=[14,15], leftMid=[3,11], rightMid=[9,10], inner=[5,6,7,13];
const out=[];
for(const tm of perms(topMid)) for(const bm of perms(botMid)) for(const lm of perms(leftMid)) for(const rm of perms(rightMid)) for(const im of perms(inner)){
  const g=[[4,tm[0],tm[1],2],[lm[0],im[0],im[1],rm[0]],[lm[1],im[2],im[3],rm[1]],[12,bm[0],bm[1],8]];
  const V=Array.from({length:12},()=>Array(13).fill(0));
  const H=Array.from({length:13},()=>Array(12).fill(0));
  const yl=[];
  for(let R=0;R<4;R++)for(let C=0;C<4;C++){const p=P[g[R][C]];
    for(let i=0;i<4;i++)for(let j=0;j<3;j++){ if(p.v[i][j]) V[R*3+j][C*3+i]=1; if(p.h[i][j]) H[R*3+i][C*3+j]=1; }
    for(const [rr,cc] of p.y) yl.push([R*3+rr,C*3+cc]);
  }
  // count open edges
  let edges=0;
  for(let r=0;r<12;r++)for(let c=0;c<11;c++) if(!V[r][c+1]) edges++;
  for(let r=0;r<11;r++)for(let c=0;c<12;c++) if(!H[r+1][c]) edges++;
  // connectivity
  const seen=Array.from({length:12},()=>Array(12).fill(false));
  const st=[[0,0]]; seen[0][0]=true; let cnt=1;
  while(st.length){const [r,c]=st.pop();
    const nb=[]; if(c<11&&!V[r][c+1])nb.push([r,c+1]); if(c>0&&!V[r][c])nb.push([r,c-1]); if(r<11&&!H[r+1][c])nb.push([r+1,c]); if(r>0&&!H[r][c])nb.push([r-1,c]);
    for(const [nr,nc] of nb) if(!seen[nr][nc]){seen[nr][nc]=true;cnt++;st.push([nr,nc]);}}
  out.push({g,edges,cnt,yl,V,H});
}
const trees=out.filter(o=>o.edges===143&&o.cnt===144);
console.log("total arrangements:",out.length,"perfect mazes:",trees.length);
const conn=out.filter(o=>o.cnt===144);
console.log("fully connected:",conn.length, "edge counts:",[...new Set(conn.map(o=>o.edges))].sort((a,b)=>a-b).slice(0,10));
console.log("min edges overall:",Math.min(...out.map(o=>o.edges)),"max:",Math.max(...out.map(o=>o.edges)));
for(const t of trees.slice(0,4)) console.log(JSON.stringify(t.g), t.edges, t.cnt);

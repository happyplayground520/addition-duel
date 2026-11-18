/* 藏寶圖字母：四線格上的字母筆畫（給虛線提示、示範動畫用）和手寫辨識
   座標：x 大約 0～1（M、W、m、w 比較寬）；y = 0 第一線、1 第二線、2 第三線（基線）、3 第四線
   辨識方式：把孩子寫的筆畫和每個字母的標準筆畫都變成一群點，比較兩群點有多接近（位置也要對，例如 g 要往下出格） */
(function(root){
  const A=(cx,cy,rx,ry,a0,a1)=>{const n=Math.max(6,Math.ceil(Math.abs(a1-a0)/12)),out=[];
    for(let i=0;i<=n;i++){const t=(a0+(a1-a0)*i/n)*Math.PI/180;out.push([cx+rx*Math.cos(t),cy+ry*Math.sin(t)])}return out};
  const S=(...parts)=>parts.flat().reduce((o,p)=>{if(typeof p[0]==="number")o.push(p);return o},[]);
  const L=(...pts)=>pts;
  const dot=(x,y)=>[[x,y],[x+.01,y+.01]];
  const U={
    A:[L([0,2],[.5,0],[1,2]),L([.22,1.35],[.78,1.35])],
    B:[L([0,0],[0,2]),S([[0,0],[.5,0]],A(.5,.5,.42,.5,-90,90),[[0,1]]),S([[0,1],[.55,1]],A(.55,1.5,.45,.5,-90,90),[[0,2]])],
    C:[A(.55,1,.55,1,-40,-320)],
    D:[L([0,0],[0,2]),S([[0,0],[.35,0]],A(.35,1,.6,1,-90,90),[[0,2]])],
    E:[L([.9,0],[0,0],[0,2],[.9,2]),L([0,1],[.75,1])],
    F:[L([.9,0],[0,0],[0,2]),L([0,1],[.75,1])],
    G:[S(A(.55,1,.55,1,-40,-360),[[.6,1]])],
    H:[L([0,0],[0,2]),L([1,0],[1,2]),L([0,1],[1,1])],
    I:[L([.5,0],[.5,2])],
    J:[S([[.75,0],[.75,1.45]],A(.4,1.45,.35,.55,0,180))],
    K:[L([0,0],[0,2]),L([.9,0],[0,1.15]),L([.3,.85],[.95,2])],
    L:[L([0,0],[0,2],[.85,2])],
    M:[L([0,2],[0,0],[.6,1.4],[1.2,0],[1.2,2])],
    N:[L([0,2],[0,0],[1,2],[1,0])],
    O:[A(.55,1,.55,1,-90,270)],
    P:[L([0,2],[0,0]),S([[0,0],[.5,0]],A(.5,.55,.45,.55,-90,90),[[0,1.1]])],
    Q:[A(.55,1,.55,1,-90,270),L([.6,1.4],[1.1,2.1])],
    R:[L([0,2],[0,0]),S([[0,0],[.5,0]],A(.5,.55,.45,.55,-90,90),[[0,1.1]]),L([.35,1.1],[.95,2])],
    S:[S(A(.5,.5,.42,.5,-25,-270),A(.5,1.5,.45,.5,-90,150))],
    T:[L([0,0],[1,0]),L([.5,0],[.5,2])],
    U:[S([[0,0],[0,1.4]],A(.5,1.4,.5,.6,180,0),[[1,0]])],
    V:[L([0,0],[.5,2],[1,0])],
    W:[L([0,0],[.3,2],[.6,.6],[.9,2],[1.2,0])],
    X:[L([0,0],[1,2]),L([1,0],[0,2])],
    Y:[L([0,0],[.5,1]),L([1,0],[.5,1],[.5,2])],
    Z:[L([0,0],[1,0],[0,2],[1,2])]
  };
  const ring=(cx,cy,rx,ry)=>A(cx,cy,rx,ry,-10,350);
  const Lo={
    a:[ring(.42,1.5,.42,.5),L([.84,1],[.84,2])],
    b:[L([0,0],[0,2]),ring(.45,1.5,.45,.5)],
    c:[A(.45,1.5,.45,.5,-40,-320)],
    d:[ring(.45,1.5,.45,.5),L([.9,0],[.9,2])],
    e:[S([[.02,1.5],[.9,1.5]],A(.45,1.5,.45,.5,0,-320))],
    f:[S(A(.72,.4,.27,.4,-30,-180),[[.45,2]]),L([.15,1],[.8,1])],
    g:[ring(.42,1.5,.42,.5),S([[.84,1],[.84,2.5]],A(.45,2.5,.39,.42,0,165))],
    h:[L([0,0],[0,2]),S([[0,1.45]],A(.42,1.45,.42,.45,180,360),[[.84,2]])],
    i:[L([.3,1],[.3,2]),dot(.3,.55)],
    j:[S([[.55,1],[.55,2.55]],A(.25,2.55,.3,.38,0,165)),dot(.55,.55)],
    k:[L([0,0],[0,2]),L([.75,1],[0,1.6]),L([.25,1.42],[.8,2])],
    l:[L([.3,0],[.3,2])],
    m:[L([0,1],[0,2]),S([[0,1.35]],A(.3,1.35,.3,.35,180,360),[[.6,2]]),S([[.6,1.35]],A(.9,1.35,.3,.35,180,360),[[1.2,2]])],
    n:[L([0,1],[0,2]),S([[0,1.45]],A(.42,1.45,.42,.45,180,360),[[.84,2]])],
    o:[A(.45,1.5,.45,.5,-90,270)],
    p:[L([0,1],[0,3]),ring(.45,1.5,.45,.5)],
    q:[ring(.45,1.5,.45,.5),L([.9,1],[.9,3])],
    r:[L([0,1],[0,2]),S([[0,1.5]],A(.42,1.5,.42,.45,180,310))],
    s:[S(A(.42,1.25,.36,.25,-25,-270),A(.42,1.75,.4,.25,-90,150))],
    t:[S([[.4,.35],[.4,1.75]],A(.65,1.75,.25,.25,180,90),[[.85,1.96]]),L([.1,1],[.8,1])],
    u:[S([[0,1],[0,1.55]],A(.42,1.55,.42,.45,180,0)),L([.84,1],[.84,2])],
    v:[L([0,1],[.45,2],[.9,1])],
    w:[L([0,1],[.3,2],[.6,1.2],[.9,2],[1.2,1])],
    x:[L([0,1],[.9,2]),L([.9,1],[0,2])],
    y:[L([0,1],[.45,2]),L([.9,1],[.2,3])],
    z:[L([0,1],[.9,1],[0,2],[.9,2])]
  };
  const T=Object.assign({},U,Lo);

  // ---- 點群 ----
  const len=st=>{let s=0;for(let i=1;i<st.length;i++)s+=Math.hypot(st[i][0]-st[i-1][0],st[i][1]-st[i-1][1]);return s};
  function cloud(strokes,N=64){
    const tot=strokes.reduce((s,st)=>s+Math.max(len(st),.02),0),out=[];
    strokes.forEach(st=>{
      const k=Math.max(2,Math.round(N*Math.max(len(st),.02)/tot));
      if(st.length<2){for(let i=0;i<k;i++)out.push(st[0]);return}
      const L=len(st)||1e-6;let seg=0,acc=0;
      for(let i=0;i<k;i++){
        const want=L*i/(k-1);
        while(seg<st.length-2&&acc+Math.hypot(st[seg+1][0]-st[seg][0],st[seg+1][1]-st[seg][1])<want){acc+=Math.hypot(st[seg+1][0]-st[seg][0],st[seg+1][1]-st[seg][1]);seg++}
        const a=st[seg],b=st[seg+1]||a,d=Math.hypot(b[0]-a[0],b[1]-a[1])||1e-6,t=Math.min(1,Math.max(0,(want-acc)/d));
        out.push([a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t]);
      }
    });
    return out;
  }
  const bbox=pts=>{let x0=1e9,x1=-1e9,y0=1e9,y1=-1e9;pts.forEach(([x,y])=>{x0=Math.min(x0,x);x1=Math.max(x1,x);y0=Math.min(y0,y);y1=Math.max(y1,y)});return{x0,x1,y0,y1}};
  function half(a,b){let s=0;for(const p of a){let m=1e9;for(const q of b){const d=(p[0]-q[0])**2+(p[1]-q[1])**2;if(d<m)m=d}s+=Math.sqrt(m)}return s/a.length}
  const TC={};Object.keys(T).forEach(k=>{TC[k]=cloud(T[k])});
  // 孩子寫的點群和某個字母的距離：左右位置對齊，上下位置保留（容許一點點偏差和大小差）
  function dist(user,k){
    const t=TC[k],bt=bbox(t),bu=bbox(user);
    const cxT=(bt.x0+bt.x1)/2,cxU=(bu.x0+bu.x1)/2,cyU=(bu.y0+bu.y1)/2;
    let best=1e9;
    for(const sc of [.85,1,1.15])for(const dy of [-.15,0,.15]){
      const u=user.map(([x,y])=>[(x-cxU)*sc+cxT,(y-cyU)*sc+cyU+dy]);
      const d=(half(u,t)+half(t,u))/2;if(d<best)best=d;
    }
    return best;
  }
  // 判斷：target 是不是前三名、而且距離夠近（放寬給小一）
  function judge(strokes,target){
    const pts=strokes.filter(s=>s.length);if(!pts.length)return{ok:false,rank:99,d:9};
    const user=cloud(pts);
    const b=bbox(user);if(b.x1-b.x0<.08&&b.y1-b.y0<.08)return{ok:false,rank:99,d:9};
    const ds=Object.keys(T).map(k=>[k,dist(user,k)]).sort((a,b)=>a[1]-b[1]);
    const rank=ds.findIndex(x=>x[0]===target),d=ds[rank][1];
    return{ok:(rank<=2&&d<.24)||(rank===0&&d<.32),rank,d,top:ds.slice(0,4)};
  }
  const width=k=>{const b=bbox(TC[k]);return b.x1-b.x0};
  const api={T,judge,width,bbox:k=>bbox(TC[k])};
  if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.INK=api;
})(typeof window!=="undefined"?window:globalThis);

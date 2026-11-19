/* 謎題星空的 3D 地圖：七顆小星球排成一條航道，一架小火箭沿著航道飛來飛去。
   每顆星球上有代表那一關的小東西（列車繞軌道、天秤會擺、外星人探頭、火箭、金字塔…）。
   還沒開放的星球是灰色、蓋著雲霧，點了只會搖一下。點開放的星球，鏡頭飛過去再進關卡。
   載入失敗（裝置不支援 3D、沒網路）時，畫面停在原本的 2D 星空地圖。 */
import * as THREE from "three";

const SPOTS=window.SKY_SPOTS||[];
const wrap=document.getElementById("w3d"),labs=document.getElementById("labs");
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:"low-power"});
renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));
renderer.outputColorSpace=THREE.SRGBColorSpace;
wrap.appendChild(renderer.domElement);
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(32,1,.1,200);
scene.add(new THREE.HemisphereLight(0xe8e4ff,0x3a2f86,2.1));
const sun=new THREE.DirectionalLight(0xffffff,2.6);sun.position.set(-5,8,9);scene.add(sun);
const world=new THREE.Group();scene.add(world);
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;

// ---- 小工具 ----
const gray=new THREE.Color(0x8c8aa8);
const mats={};
function M(c,lock){const k=c+(lock?"L":"");if(mats[k])return mats[k];const col=new THREE.Color(c);if(lock)col.lerp(gray,.82);
  return mats[k]=new THREE.MeshStandardMaterial({color:col,roughness:.7,metalness:0})}
let LOCK=false;
const mesh=(geo,c,x=0,y=0,z=0,p)=>{const m=new THREE.Mesh(geo,M(c,LOCK));m.position.set(x,y,z);p&&p.add(m);return m};
const cyl=(rt,rb,h,c,x,y,z,p,seg=20)=>mesh(new THREE.CylinderGeometry(rt,rb,h,seg),c,x,y,z,p);
const box=(w,h,d,c,x,y,z,p)=>mesh(new THREE.BoxGeometry(w,h,d),c,x,y,z,p);
const sph=(r,c,x,y,z,p,seg=20)=>mesh(new THREE.SphereGeometry(r,seg,Math.max(8,seg*.6|0)),c,x,y,z,p);
const cone=(r,h,c,x,y,z,p,seg=16)=>mesh(new THREE.ConeGeometry(r,h,seg),c,x,y,z,p);
const torus=(r,t,c,x,y,z,p,seg=48)=>mesh(new THREE.TorusGeometry(r,t,10,seg),c,x,y,z,p);
// 星球表面上的一點（緯度、經度）
const surf=(r,lat,lon)=>new THREE.Vector3(Math.cos(lat)*Math.sin(lon)*r,Math.sin(lat)*r,Math.cos(lat)*Math.cos(lon)*r);
// 發光的光暈（圓形漸層貼圖）
const glowTex=(()=>{const c=document.createElement("canvas");c.width=c.height=128;const x=c.getContext("2d");const g=x.createRadialGradient(64,64,10,64,64,64);
  g.addColorStop(0,"rgba(255,255,255,.85)");g.addColorStop(.45,"rgba(255,255,255,.25)");g.addColorStop(1,"rgba(255,255,255,0)");x.fillStyle=g;x.fillRect(0,0,128,128);
  const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;return t})();
const R=.62; // 星球半徑
function bands(c,ball){[[-.4,0],[.15,0],[.55,0]].forEach(([y])=>{const b=torus(R*Math.sqrt(1-y*y)+.004,.028,c,0,y*R,0,ball,40);b.rotation.x=Math.PI/2})}
function craters(c,ball,list){list.forEach(([lat,lon,s])=>{const p=surf(R*.97,lat,lon);const m=sph(s,c,p.x,p.y,p.z,ball,12);m.scale.set(1,1,.35);m.lookAt(p.clone().multiplyScalar(2))})}

// ---- 每一顆星球的樣子：做在 g 裡，回傳每格畫面要動的東西 ----
const BUILD={
  // 太空列車：橘色條紋星球，三節小列車沿著斜斜的軌道繞圈
  pattern(g,ball){bands(0xff8a3d,ball);
    const orbit=new THREE.Group();orbit.rotation.set(.35,0,-.25);g.add(orbit);
    const track=torus(R*1.45,.02,0xffe27a,0,0,0,orbit,64);track.rotation.x=Math.PI/2;
    const cars=[0xff6b6b,0x4dc3ff,0x7bd389].map((c,i)=>{const b=box(.2,.13,.13,c,0,0,0,orbit);sph(.035,0x2b2240,0,-.07,.06,b,8);return b});
    return t=>cars.forEach((b,i)=>{const a=t*.9-i*.3;b.position.set(Math.sin(a)*R*1.45,0,Math.cos(a)*R*1.45);b.rotation.y=a+Math.PI/2})},
  // 宇宙天秤：藍色有光環的星球，頂上一個小天秤左右擺
  balance(g,ball){bands(0x4da3ff,ball);
    const ring=torus(R*1.5,.05,0xffd23f,0,0,0,g,64);ring.rotation.set(Math.PI/2.6,0,.3);
    const st=new THREE.Group();st.position.y=R*.92;g.add(st);
    cyl(.025,.04,.42,0xffffff,0,.2,0,st,8);
    const beam=new THREE.Group();beam.position.y=.42;st.add(beam);box(.62,.035,.035,0xffd23f,0,0,0,beam);
    const pans=[-1,1].map(s=>{const p=new THREE.Group();p.position.x=s*.3;beam.add(p);cyl(.006,.006,.14,0xffffff,0,-.07,0,p,4);cyl(.1,.07,.04,0xffd23f,0,-.15,0,p,16);
      sph(.045,s<0?0xff8fc7:0x7bd389,0,-.1,0,p,10);return p});
    return t=>{beam.rotation.z=Math.sin(t*1.4)*.28;pans.forEach(p=>p.rotation.z=-beam.rotation.z)}},
  // 星際數獨：綠色有坑洞的星球，上面一個外星人探頭、揮天線
  sudoku(g,ball){craters(0x5cc24a,ball,[[.5,.7,.12],[-.2,-.6,.15],[-.55,.5,.09],[.1,1.6,.11],[-.2,3,.13]]);
    const al=new THREE.Group();al.position.y=R*.82;g.add(al);
    const head=sph(.2,0x9cf08a,0,.12,0,al,18);head.scale.set(1.15,1,1);
    [-1,1].forEach(s=>{sph(.06,0xffffff,s*.08,.15,.16,al,10);sph(.03,0x2b2240,s*.08,.15,.21,al,8)});
    const ants=[-1,1].map(s=>{const a=new THREE.Group();a.position.set(s*.08,.28,0);al.add(a);cyl(.012,.012,.16,0x5cc24a,0,.08,0,a,6);sph(.035,0xffe27a,0,.17,0,a,8);return a});
    return t=>{al.position.y=R*.82+Math.max(0,Math.sin(t*1.3))*.06;ants.forEach((a,i)=>a.rotation.z=Math.sin(t*4+i*2)*.35*(i?-1:1))}},
  // 火星探險車：紅色有坑洞的星球，頂上一台小車
  rover(g,ball){craters(0xc9443a,ball,[[.4,.4,.14],[-.3,-.8,.17],[-.5,.6,.1],[.2,2,.13],[0,3.4,.15]]);
    const car=new THREE.Group();car.position.y=R*.98;g.add(car);
    box(.34,.12,.22,0xffffff,0,.1,0,car);box(.14,.1,.18,0x7cc7ff,.04,.2,0,car);
    [[-.12,.12],[.12,.12],[-.12,-.12],[.12,-.12]].forEach(([x,z])=>{const w=cyl(.05,.05,.04,0x3a3a4a,x,.04,z,car,12);w.rotation.x=Math.PI/2});
    return t=>{car.rotation.y=Math.sin(t*.7)*.5}},
  // 外星密碼：紫色兩圈光環的星球，上面一顆閃亮的寶石
  code(g,ball){bands(0xa77bff,ball);
    [[1.42,.05,0x7cf0d8],[1.62,.025,0xffffff]].forEach(([r,t,c])=>{const ring=torus(R*r,t,c,0,0,0,g,64);ring.rotation.set(Math.PI/2.3,0,-.35)});
    const gem=mesh(new THREE.OctahedronGeometry(.13),0x7cf0d8,0,R*1.12,0,g);
    return t=>{gem.rotation.y=t*1.5;gem.position.y=R*1.12+Math.sin(t*2)*.04}},
  // 拼火箭：黃色星球，頂上站著一支小火箭
  tangram(g,ball){bands(0xf5c400,ball);
    const rk=new THREE.Group();rk.position.y=R*.9;g.add(rk);rocket(rk,.9);
    return t=>{rk.position.y=R*.9+Math.max(0,Math.sin(t*1.2))*.08}},
  // 星星金字塔：粉紅色有光環的星球，頂上一座小金字塔
  pyramid(g,ball){craters(0xf070b0,ball,[[.3,.5,.11],[-.3,-.7,.13],[-.1,2.4,.12]]);
    const ring=torus(R*1.48,.045,0x9fe8ff,0,0,0,g,64);ring.rotation.set(Math.PI/2.2,0,.45);
    const py=cone(.24,.3,0xffd23f,0,R*.98+.13,0,g,4);
    const st=mesh(new THREE.OctahedronGeometry(.06),0xfff6a8,0,R*.98+.36,0,g);
    return t=>{py.rotation.y=t*.6;st.rotation.y=-t*2;st.scale.setScalar(.8+Math.abs(Math.sin(t*2))*.5)}}
};
const PCOL={pattern:0xffb36b,balance:0x7cc7ff,sudoku:0x8ee08a,rover:0xff8a6b,code:0xc9a2ff,tangram:0xffe27a,pyramid:0xff9fd0};
function rocket(p,s=1){const r=new THREE.Group();r.scale.setScalar(s);p.add(r);
  cyl(.06,.07,.24,0xffffff,0,.14,0,r,12);cone(.06,.11,0xff4b55,0,.315,0,r,12);sph(.03,0x4dc3ff,0,.18,.06,r,8);
  [0,1,2].forEach(i=>{const f=box(.015,.08,.07,0xff4b55,0,.05,0,r);const a=i/3*Math.PI*2;f.position.set(Math.sin(a)*.07,.05,Math.cos(a)*.07);f.rotation.y=a});
  return r}

const PL=SPOTS.map((s,i)=>{
  LOCK=!s.href;
  const g=new THREE.Group(),inner=new THREE.Group();g.add(inner);
  const ball=sph(R,PCOL[s.k]||0xc9a2ff,0,0,0,inner,32);
  const tick=(BUILD[s.k]||(()=>()=>{}))(inner,ball)||(()=>{});
  const glow=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex,color:new THREE.Color(LOCK?0x8c8aa8:s.c),transparent:true,opacity:LOCK?.35:.75,depthWrite:false,blending:THREE.AdditiveBlending}));
  glow.scale.setScalar(R*3.6);glow.renderOrder=-1;g.add(glow);
  // 還沒開放：半透明的雲霧包住下半部
  if(LOCK){const fog=new THREE.MeshStandardMaterial({color:0xffffff,transparent:true,opacity:.82,roughness:1});
    [[-.5,-.35,.35,.32],[0,-.5,.45,.36],[.5,-.3,.32,.3],[-.2,-.2,.55,.24],[.35,-.05,.5,.2]].forEach(([x,y,z,r])=>{const m=new THREE.Mesh(new THREE.SphereGeometry(r,14,10),fog);m.position.set(x,y,z);g.add(m)})}
  LOCK=false;
  const it={s,g,inner,ball,tick,open:!!s.href,phase:i*1.1,i,shake:0};
  g.traverse(o=>{o.userData.pl=it});world.add(g);return it;
});

// ---- 背景的星星（會慢慢轉，有遠近的感覺） ----
{const n=500,pos=new Float32Array(n*3);for(let i=0;i<n;i++){pos[i*3]=(Math.random()-.5)*40;pos[i*3+1]=(Math.random()-.5)*28;pos[i*3+2]=-4-Math.random()*16}
  const geo=new THREE.BufferGeometry();geo.setAttribute("position",new THREE.BufferAttribute(pos,3));
  var starPts=new THREE.Points(geo,new THREE.PointsMaterial({color:0xfff6d8,size:.07,sizeAttenuation:true,transparent:true,opacity:.9}));scene.add(starPts)}

// ---- 航道：一顆一顆的小點連起來，小火箭沿著航道飛 ----
const route=new THREE.Group();world.add(route);
const ship=new THREE.Group();world.add(ship);const shipRk=rocket(ship,1.1);
let curve=null;

// ---- 名稱標籤（網頁文字，可以有注音） ----
const LAB=PL.map(it=>{const s=it.s,a=document.createElement(it.open?"a":"button");a.className="lab"+(it.open?"":" lock");a.style.setProperty("--c",s.c);
  if(it.open)a.href=s.href;else{a.type="button";a.setAttribute("aria-label",s.name+"（還沒開放）")}
  a.innerHTML=`<b><span data-zy>${s.name}</span>${it.open?"":"<em>🔒</em>"}</b><i data-zy>${s.tag}</i>`;
  a.addEventListener("click",e=>{e.preventDefault();enter(it)});labs.appendChild(a);return a});

// ---- 排列：橫的畫面上四下三；直的平板三三一；手機直放左右交錯一直排 ----
const head=document.querySelector("header");
let mode="";
// 很矮的手機橫放（例如 iPhone SE 橫拿）放不下七個名稱，就換回 2D 地圖
let tiny=false;
function resize(){
  tiny=innerWidth>innerHeight&&innerHeight<340;document.documentElement.classList.toggle("is3d",!tiny);if(tiny)return;
  const top=Math.round(head.getBoundingClientRect().bottom+6);wrap.style.top=labs.style.top=top+"px";
  const w=wrap.clientWidth,h=wrap.clientHeight;renderer.setSize(w,h,false);camera.aspect=w/h;
  const a=w/h;
  let P;
  if(a>1.05){mode="land";const yy=h<420?1.3:1.45;P=[[-4.2,yy],[-1.4,yy],[1.4,yy],[4.2,yy],[2.8,-yy],[0,-yy],[-2.8,-yy]]}
  else if(a>.62&&w>=600){mode="port";P=[[-2.2,2.75],[0,2.75],[2.2,2.75],[2.2,0],[0,0],[-2.2,0],[0,-2.75]]}
  else{mode="zig";P=[...Array(7)].map((_,i)=>[i%2?1.25:-1.25,4.65-i*1.55])}
  PL.forEach((it,i)=>{it.x=P[i][0];it.y=P[i][1];it.z=(i%2?-.35:.35);it.g.position.set(it.x,it.y,it.z)});
  // 鏡頭距離：全部星球＋下面的名稱都要放得進去
  const xs=P.map(p=>p[0]),ys=P.map(p=>p[1]);const cx=(Math.min(...xs)+Math.max(...xs))/2;
  const hx=(Math.max(...xs)-Math.min(...xs))/2+R*(mode=="zig"?1.25:1.75);
  const topY=Math.max(...ys)+R*(mode=="zig"?1.3:1.5),botY=Math.min(...ys)-R*(mode=="zig"?1.3:1)-(mode=="zig"?0:.85);const cy=(topY+botY)/2,hy=(topY-botY)/2;
  const f=Math.tan(THREE.MathUtils.degToRad(camera.fov/2));
  let d=Math.max(hy/f,hx/(f*camera.aspect))*1.04;
  const put=()=>{camera.position.set(cx,cy+d*.1,d);camera.lookAt(cx,cy,0);camera.updateProjectionMatrix();camera.updateMatrixWorld()};
  put();
  // 名稱是網頁文字（大小固定），畫面小的時候可能超出邊邊：超出就把鏡頭往後拉一點再試
  for(let k=0;k<14&&labelsOut(w,h);k++){d*=1.06;put()}
  homeLook.set(cx,cy,0);
  // 航道
  route.clear();
  const pts=PL.map(it=>new THREE.Vector3(it.x,it.y,it.z));
  curve=new THREE.CatmullRomCurve3(pts,false,"centripetal");
  const dotM=new THREE.MeshBasicMaterial({color:0xffe27a,transparent:true,opacity:.85}),dotG=new THREE.SphereGeometry(.035,8,6);
  curve.getSpacedPoints(Math.round(curve.getLength()/.16)).forEach(p=>{if(PL.some(it=>p.distanceTo(it.g.position)<R*1.25))return;const m=new THREE.Mesh(dotG,dotM);m.position.copy(p);route.add(m)});
  if(typeof placeLabels=="function")placeLabels();
}
const homeLook=new THREE.Vector3();
addEventListener("resize",()=>{clearTimeout(resize.t);resize.t=setTimeout(resize,120)});

// ---- 拖曳：整個畫面左右轉一點（放開會彈回來）；點一下：進那顆星球 ----
let rotY=0,rotTarget=0,drag=null,hover=null,flying=null;
const ray=new THREE.Raycaster(),ndc=new THREE.Vector2();
const hitList=()=>PL.map(it=>it.ball);
function pickAt(cx,cy){const r=renderer.domElement.getBoundingClientRect();ndc.set((cx-r.left)/r.width*2-1,-(cy-r.top)/r.height*2+1);ray.setFromCamera(ndc,camera);
  // 點在星球附近一點點也算（小朋友手指比較粗）
  let best=null,bd=1e9;PL.forEach(it=>{const p=it.g.getWorldPosition(new THREE.Vector3());const dd=ray.ray.distanceToPoint(p);if(dd<R*1.35&&dd<bd){bd=dd;best=it}});return best}
const cv=renderer.domElement;cv.style.touchAction="pan-y";
cv.addEventListener("pointerdown",e=>{drag={x:e.clientX,r:rotTarget,moved:false}});
cv.addEventListener("pointermove",e=>{
  if(drag){const dx=e.clientX-drag.x;if(Math.abs(dx)>8)drag.moved=true;rotTarget=Math.max(-.4,Math.min(.4,drag.r+dx*.003))}
  else if(e.pointerType==="mouse"){hover=pickAt(e.clientX,e.clientY);cv.style.cursor=hover?"pointer":"default"}});
cv.addEventListener("pointerup",e=>{if(!drag)return;const d=drag;drag=null;if(!d.moved){const it=pickAt(e.clientX,e.clientY);if(it)enter(it)}});
cv.addEventListener("pointercancel",()=>{drag=null});
cv.addEventListener("pointerleave",()=>{hover=null});
function enter(it){
  if(flying)return;
  if(!it.open){it.shake=1;window.skyToast&&skyToast("這顆星球快要開放囉！");return}
  flying={it,t0:performance.now(),from:camera.position.clone()};
  try{window.parkBurst&&parkBurst()}catch(e){}
  setTimeout(()=>{location.href=it.s.href},reduce?50:520);
}
addEventListener("pageshow",()=>{flying=null;resize()});

// ---- 每一格畫面 ----
const v=new THREE.Vector3(),up=new THREE.Vector3(0,1,0);let last=performance.now(),t=0,u=0,running=true;
document.addEventListener("visibilitychange",()=>{running=!document.hidden;if(running){last=performance.now();requestAnimationFrame(frame)}});
function frame(now){
  if(!running)return;
  if(tiny){requestAnimationFrame(frame);return}
  const dt=Math.min(.05,(now-last)/1000);last=now;t+=dt*(reduce?.3:1);
  if(!drag)rotTarget*=.92;rotY+=(rotTarget-rotY)*.12;world.rotation.y=rotY;
  PL.forEach(it=>{
    it.g.position.y=it.y+Math.sin(t*1.1+it.phase)*(reduce?.02:.08);
    it.ball.rotation.y=t*.35+it.phase;
    if(it.shake>0){it.shake=Math.max(0,it.shake-dt*1.8);it.g.rotation.z=Math.sin(it.shake*30)*.12*it.shake}else it.g.rotation.z=0;
    const s=it===hover?1.1:1;it.g.scale.lerp(v.set(s,s,s),.15);
    it.tick(t);
  });
  starPts.rotation.z=t*.006;
  // 小火箭沿著航道來回飛
  if(curve){u=(u+dt*.045)%2;const k=u<1?u:2-u,p=curve.getPointAt(k),q=curve.getPointAt(Math.min(1,Math.max(0,k+(u<1?.01:-.01))));
    ship.position.copy(p).add(v.set(0,.38+Math.sin(t*3)*.04,.25));const dir=q.sub(p).normalize();if(dir.lengthSq()>0)shipRk.quaternion.setFromUnitVectors(up,dir)}
  if(flying){const k=Math.min(1,(now-flying.t0)/500),e=k*k*(3-2*k),p=flying.it.g.getWorldPosition(v.set(0,0,0));
    camera.position.lerpVectors(flying.from,p.clone().add(new THREE.Vector3(0,.3,2.2)),e);camera.lookAt(p)}
  renderer.render(scene,camera);placeLabels();
  requestAnimationFrame(frame);
}
// 名稱放哪裡：一般放在星球下面；手機直放（左右交錯）放在星球旁邊、靠中間那一側
function anchor(it,x,y,z){const side=mode=="zig"?(it.x<0?1:-1):0;
  return side?v.set(x+side*R*1.08,y,z):v.set(x,y-R*1.12,z)}
function labelBox(it,i,p,W,H){const L=LAB[i],lw=L.offsetWidth,lh=L.offsetHeight,x=(p.x*.5+.5)*W,y=(-p.y*.5+.5)*H;
  if(mode!="zig")return [x-lw/2,y,x+lw/2,y+lh];return it.x<0?[x,y-lh/2,x+lw,y+lh/2]:[x-lw,y-lh/2,x,y+lh/2]}
function labelsOut(W,H){return PL.some((it,i)=>{const p=anchor(it,it.x,it.y-.1,it.z).project(camera);const b=labelBox(it,i,p,W,H);
  return b[0]<6||b[2]>W-6||b[3]>H-8||b[1]<2})}
function placeLabels(){const W=wrap.clientWidth,H=wrap.clientHeight;
  PL.forEach((it,i)=>{const w=it.g.getWorldPosition(new THREE.Vector3());const p=anchor(it,w.x,w.y,w.z).project(camera);const b=labelBox(it,i,p,W,H);
    const L=LAB[i];L.style.transform=`translate(${b[0]}px,${b[1]}px)`;L.classList.toggle("on",it===hover);
    L.classList.toggle("sl",mode=="zig"&&it.x<0);L.classList.toggle("sr",mode=="zig"&&it.x>0)})}
resize();renderer.render(scene,camera);placeLabels();
// 注音和字型載入後名稱會變寬，再排一次
if(window.ResizeObserver){let rt=0;const ro=new ResizeObserver(()=>{clearTimeout(rt);rt=setTimeout(resize,60)});LAB.forEach(L=>ro.observe(L))}
setTimeout(resize,400);setTimeout(resize,1500);
requestAnimationFrame(frame);

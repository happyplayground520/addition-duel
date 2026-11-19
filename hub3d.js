/* 選地圖的 3D 畫面：四座漂浮在天空中的小島（遊樂園、甜點小鎮、海盜灣、謎題星空）。
   每座島上有一個代表物在動：摩天輪會轉、海盜船會搖、星球會自轉。點小島（或下面的名稱）鏡頭會飛過去，再進那張地圖。
   用 Three.js 畫，所有形狀都是程式組出來的（沒有模型檔）。不支援 3D 的裝置，這個檔案載入失敗，畫面就停在原本的四張卡片。 */
import * as THREE from "three";

const wrap=document.getElementById("w3d"),labs=document.getElementById("labs");
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:"low-power"});
renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));
renderer.outputColorSpace=THREE.SRGBColorSpace;
wrap.appendChild(renderer.domElement);
const scene=new THREE.Scene();
const camera=new THREE.PerspectiveCamera(32,1,.1,200);
scene.add(new THREE.HemisphereLight(0xffffff,0x9bbad6,2.2));
const sun=new THREE.DirectionalLight(0xffffff,2.2);sun.position.set(6,12,8);scene.add(sun);
const world=new THREE.Group();scene.add(world);
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;

// ---- 小工具：做形狀 ----
const mats={};
const M=c=>mats[c]||(mats[c]=new THREE.MeshStandardMaterial({color:c,roughness:.75,metalness:0,flatShading:false}));
const mesh=(geo,c,x=0,y=0,z=0,parent)=>{const m=new THREE.Mesh(geo,M(c));m.position.set(x,y,z);parent&&parent.add(m);return m};
const cyl=(rt,rb,h,c,x,y,z,p,seg=32)=>mesh(new THREE.CylinderGeometry(rt,rb,h,seg),c,x,y,z,p);
const box=(w,h,d,c,x,y,z,p)=>mesh(new THREE.BoxGeometry(w,h,d),c,x,y,z,p);
const sph=(r,c,x,y,z,p,seg=20)=>mesh(new THREE.SphereGeometry(r,seg,Math.max(8,seg*.6|0)),c,x,y,z,p);
const cone=(r,h,c,x,y,z,p,seg=20)=>mesh(new THREE.ConeGeometry(r,h,seg),c,x,y,z,p);
const torus=(r,t,c,x,y,z,p,seg=40)=>mesh(new THREE.TorusGeometry(r,t,10,seg),c,x,y,z,p);
// 漂浮的小島：上面一層草地（或沙地、粉紅色），下面倒過來的岩石
function base(top,side,g){
  cyl(1.6,1.5,.34,top,0,0,0,g,40);
  cyl(1.5,1.35,.3,side,0,-.3,0,g,40);
  const rock=cone(1.32,1.7,side,0,-1.3,0,g,9);rock.rotation.x=Math.PI;
  [[.9,-.75,.5,.22],[-.8,-.8,-.4,.18],[.2,-1.9,.3,.14]].forEach(([x,y,z,r])=>sph(r,side,x,y,z,g,8));
}
function tree(x,z,g,s=1){cyl(.05*s,.06*s,.3*s,0x8a5a36,x,.32*s,z,g,8);cone(.24*s,.5*s,0x46b45c,x,.7*s,z,g,10);cone(.18*s,.38*s,0x5cc96e,x,.92*s,z,g,10)}

const ISLES=[];
// ---- 🎡 數學遊樂園：草地島、會轉的摩天輪、馬戲團帳篷 ----
{const g=new THREE.Group();base(0x8fd16a,0xa8683a,g);
  const fw=new THREE.Group();fw.position.set(-.15,1.25,0);g.add(fw);
  const wheel=new THREE.Group();fw.add(wheel);
  [-.13,.13].forEach(z=>torus(.85,.05,0xff6b6b,0,0,z,wheel));
  for(let i=0;i<8;i++){const a=i/8*Math.PI*2;const sp=box(.04,.85,.04,0xffffff,0,0,0,wheel);sp.position.set(Math.sin(a)*.42,Math.cos(a)*.42,0);sp.rotation.z=-a;}
  cyl(.1,.1,.34,0xffd23f,0,0,0,wheel,16).rotation.x=Math.PI/2;
  const cabs=[];const CC=[0x4dc3ff,0xffd23f,0x7bd389,0xc58cff,0xff9f43,0xff8fc7,0x4dd6c1,0xff6b6b];
  for(let i=0;i<8;i++){const c=box(.24,.2,.22,CC[i],0,0,0,fw);cabs.push(c)}
  [-1,1].forEach(s=>{const l=cyl(.04,.05,1.35,0x5a6b75,s*.42,-.6,.2,fw,8);l.rotation.z=s*.35;const l2=cyl(.04,.05,1.35,0x5a6b75,s*.42,-.6,-.2,fw,8);l2.rotation.z=s*.35});
  // 帳篷
  cyl(.42,.42,.35,0xffffff,.85,.35,.55,g,16);cone(.5,.45,0xe8434f,.85,.75,.55,g,16);sph(.06,0xffd23f,.85,1.0,.55,g,8);
  tree(-1.05,.75,g,.9);tree(1.05,-.7,g,.8);tree(-.95,-.85,g,.7);
  ISLES.push({g,href:"park.html",key:"park",tick:t=>{wheel.rotation.z=t*.5;cabs.forEach((c,i)=>{const a=i/8*Math.PI*2-t*.5;c.position.set(Math.sin(a)*.85,Math.cos(a)*.85-.14,0)})}})}
// ---- 🍓 甜點小鎮：粉紅色的島、兩層草莓蛋糕屋、棒棒糖 ----
{const g=new THREE.Group();base(0xffb3c7,0xc98a4b,g);
  const cake=new THREE.Group();cake.position.set(0,.17,0);g.add(cake);
  cyl(.78,.8,.5,0xfff3e0,0,.27,0,cake,32);torus(.78,.06,0xff8fb0,0,.52,0,cake).rotation.x=Math.PI/2;
  cyl(.55,.56,.42,0xfff3e0,0,.73,0,cake,32);torus(.55,.055,0xff8fb0,0,.94,0,cake).rotation.x=Math.PI/2;
  cyl(.56,.56,.06,0xffffff,0,.97,0,cake,32);
  // 門和窗
  box(.22,.3,.04,0xc98a4b,0,.2,.79,cake);sph(.07,0x7cc7ff,-.42,.32,.66,cake,10);sph(.07,0x7cc7ff,.42,.32,.66,cake,10);
  // 草莓（上面一圈＋最上面一顆）
  const berries=[];
  for(let i=0;i<6;i++){const a=i/6*Math.PI*2,s=new THREE.Group();s.position.set(Math.sin(a)*.36,1.08,Math.cos(a)*.36);cake.add(s);
    const b=sph(.11,0xff4b55,0,0,0,s,12);b.scale.y=1.2;cone(.09,.07,0x46c46a,0,.13,0,s,8);berries.push(s)}
  {const s=new THREE.Group();s.position.set(0,1.18,0);cake.add(s);const b=sph(.15,0xff4b55,0,0,0,s,14);b.scale.y=1.25;cone(.12,.09,0x46c46a,0,.18,0,s,8);berries.push(s)}
  // 棒棒糖
  [[1.05,.55,0xff6fb5],[-1.05,.4,0x7cc7ff],[.9,-.85,0xffd23f]].forEach(([x,z,c])=>{cyl(.03,.03,.7,0xffffff,x,.5,z,g,8);const l=cyl(.2,.2,.06,c,x,.95,z,g,20);l.rotation.x=Math.PI/2;torus(.13,.03,0xffffff,x,.95,z+.035,g,24)});
  ISLES.push({g,href:"town.html",key:"town",tick:t=>{berries.forEach((b,i)=>{b.position.y=(i<6?1.08:1.18)+Math.max(0,Math.sin(t*3-i*.6))*.05})}})}
// ---- ⛵ 海盜灣：沙灘島、小水池、椰子樹、會搖晃的海盜船、寶箱 ----
{const g=new THREE.Group();base(0xf4dc9c,0x8a6a4a,g);
  cyl(1.2,1.2,.05,0x4dc3ff,0,.17,0,g,40);cyl(1.62,1.62,.04,0xf4dc9c,0,.16,0,g,40);
  const ship=new THREE.Group();ship.position.set(-.1,.32,.1);g.add(ship);
  const hull=box(1.1,.28,.42,0xa8683a,0,0,0,ship);box(.25,.26,.36,0x8a5a36,-.5,.12,0,ship);
  cyl(.03,.03,1.0,0x6e4122,0,.6,0,ship,8);
  const sail=box(.02,.55,.62,0xffffff,0,.68,0,ship);sail.rotation.y=Math.PI/2;
  const flag=box(.01,.12,.22,0x2b2b3a,0,1.12,.11,ship);flag.rotation.y=Math.PI/2;
  // 椰子樹
  const palm=new THREE.Group();palm.position.set(1.1,.18,-.55);g.add(palm);
  for(let i=0;i<5;i++){const s=cyl(.06,.07,.2,0x9a6a3a,Math.sin(i*.35)*.05*i,.1+i*.18,0,palm,8);s.rotation.z=-.08*i}
  for(let i=0;i<5;i++){const a=i/5*Math.PI*2,l=box(.55,.04,.16,0x46b45c,Math.cos(a)*.25+.2,1.02,Math.sin(a)*.25,palm);l.rotation.y=-a;l.rotation.z=-.35}
  sph(.07,0x8a5a36,.25,.95,.05,palm,8);sph(.07,0x8a5a36,.15,.95,-.08,palm,8);
  // 寶箱
  box(.32,.2,.22,0xc46f36,-1.05,.3,-.6,g);box(.34,.06,.24,0xffd23f,-1.05,.42,-.6,g);
  ISLES.push({g,href:"cove.html",key:"cove",tick:t=>{ship.rotation.z=Math.sin(t*1.6)*.08;ship.rotation.x=Math.sin(t*1.1)*.04;ship.position.y=.32+Math.sin(t*1.6)*.03;flag.scale.z=1+Math.sin(t*6)*.15}})}
// ---- 🪐 謎題星空：不是島，是一顆有光環的星球，旁邊有小月亮和閃爍的星星 ----
{const g=new THREE.Group();
  const pl=new THREE.Group();pl.position.y=.25;g.add(pl);
  const ball=sph(1.05,0x8f7bff,0,0,0,pl,32);
  [[-.35,.95,0xb9a9ff],[.1,1.0,0x7a64f0],[.5,.86,0xb9a9ff]].forEach(([y,s,c])=>{const b=torus(1.05*Math.sqrt(1-y*y)+.005,.045,c,0,y,0,pl,48);b.rotation.x=Math.PI/2});
  const ring=torus(1.55,.1,0xffb347,0,0,0,pl,64);ring.rotation.set(Math.PI/2.9,0,.35);
  const ring2=torus(1.78,.045,0xffe27a,0,0,0,pl,64);ring2.rotation.set(Math.PI/2.9,0,.35);
  const moon=sph(.2,0xfff1a8,0,0,0,g,16);
  const stars=[];for(let i=0;i<7;i++){const s=mesh(new THREE.OctahedronGeometry(.09),0xffe27a,0,0,0,g);const a=i/7*Math.PI*2;s.position.set(Math.cos(a)*2,Math.sin(a*1.7)*.9+.4,Math.sin(a)*.8);stars.push(s)}
  ISLES.push({g,href:"sky.html",key:"sky",planet:true,tick:t=>{ball.rotation.y=t*.4;pl.rotation.y=t*.15;moon.position.set(Math.cos(t*.8)*1.9,.9+Math.sin(t*.8)*.25,Math.sin(t*.8)*1.1);
    stars.forEach((s,i)=>{const k=.6+Math.abs(Math.sin(t*2+i))*.8;s.scale.setScalar(k);s.rotation.y=t+i})}})}
ISLES.forEach((it,i)=>{it.i=i;it.phase=i*1.3;it.g.traverse(o=>{o.userData.isle=it});world.add(it.g)});

// ---- 雲朵：在後面慢慢飄 ----
const clouds=[];
function cloud(x,y,z,s){const c=new THREE.Group();[[0,0,.6],[.55,.05,.45],[-.55,0,.42],[.25,.3,.42],[-.2,.28,.38]].forEach(([dx,dy,r])=>sph(r,0xffffff,dx,dy,0,c,14));
  c.position.set(x,y,z);c.scale.setScalar(s);scene.add(c);clouds.push(c);return c}
[[-9,3.6,-8,1.2],[-2,-3.4,-9,1],[5,4.2,-10,1.4],[10,-2.2,-8,1.1],[0,5.6,-12,.9],[-12,-1,-10,1]].forEach(a=>cloud(...a));

// ---- 名稱標籤（網頁文字，可以有注音） ----
const cards=[...document.querySelectorAll(".maps .card")];
const LAB=ISLES.map(it=>{const c=cards.find(x=>x.classList.contains(it.key));const a=document.createElement("a");a.className="lab "+it.key;a.href=it.href;
  a.innerHTML=`<b data-zy>${c.querySelector("h2").textContent}</b><span class="lt">${[...c.querySelectorAll(".tags>span")].map(s=>`<i data-zy>${s.textContent}</i>`).join("")}</span>`;
  a.addEventListener("click",e=>{e.preventDefault();enter(it)});labs.appendChild(a);return a});

// ---- 排列：橫的畫面一排四座，直的畫面兩排兩座；鏡頭距離算到四座都看得到 ----
let layout=[];
function resize(){
  const w=wrap.clientWidth,h=wrap.clientHeight;renderer.setSize(w,h,false);camera.aspect=w/h;
  const port=w/h<1.05;
  layout=port?[[-1.85,2.75],[1.85,2.75],[-1.85,-2.35],[1.85,-2.35]]:[[-5.1,0],[-1.7,0],[1.7,0],[5.1,0]];
  const W=port?3.9:6.8,H=port?5.6:2.6,f=Math.tan(THREE.MathUtils.degToRad(camera.fov/2));
  const d=Math.max(H/f,W/(f*camera.aspect))*1.12;
  camera.position.set(0,d*.22,d);camera.lookAt(0,port?.1:-.3,0);camera.updateProjectionMatrix();
  home.copy(camera.position);
  ISLES.forEach((it,i)=>{it.x=layout[i][0];it.y=layout[i][1];it.g.position.set(it.x,it.y,0);it.g.scale.setScalar(port?.95:1)});
}
const home=new THREE.Vector3();
addEventListener("resize",resize);

// ---- 拖曳：整個畫面左右轉一點（放開會彈回來）；點一下：進那座島 ----
let rotY=0,rotTarget=0,drag=null,hover=null,flying=null;
const ray=new THREE.Raycaster(),ndc=new THREE.Vector2();
function pickAt(cx,cy){const r=renderer.domElement.getBoundingClientRect();ndc.set((cx-r.left)/r.width*2-1,-(cy-r.top)/r.height*2+1);ray.setFromCamera(ndc,camera);
  const hit=ray.intersectObjects(world.children,true)[0];return hit?hit.object.userData.isle:null}
const cv=renderer.domElement;cv.style.touchAction="pan-y";
cv.addEventListener("pointerdown",e=>{drag={x:e.clientX,y:e.clientY,r:rotTarget,moved:false}});
cv.addEventListener("pointermove",e=>{
  if(drag){const dx=e.clientX-drag.x;if(Math.abs(dx)>8)drag.moved=true;rotTarget=Math.max(-.5,Math.min(.5,drag.r+dx*.004))}
  else if(e.pointerType==="mouse"){hover=pickAt(e.clientX,e.clientY);cv.style.cursor=hover?"pointer":"default"}});
const up=e=>{if(!drag)return;const d=drag;drag=null;if(!d.moved){const it=pickAt(e.clientX,e.clientY);if(it)enter(it)}};
cv.addEventListener("pointerup",up);cv.addEventListener("pointercancel",()=>{drag=null});
cv.addEventListener("pointerleave",()=>{hover=null});
// 鍵盤也可以用：標籤是連結，按 Tab 選、Enter 進入
function enter(it){
  if(flying)return;flying={it,t0:performance.now(),from:camera.position.clone()};
  try{window.parkBurst&&parkBurst()}catch(e){}
  setTimeout(()=>{location.href=it.href},reduce?50:850);
}
// 從地圖按「回選地圖」回來時（瀏覽器快取的頁面），鏡頭要回原位
addEventListener("pageshow",()=>{flying=null;resize()});

// ---- 每一格畫面 ----
const v=new THREE.Vector3();let last=performance.now(),t=0,running=true;
document.addEventListener("visibilitychange",()=>{running=!document.hidden;if(running){last=performance.now();requestAnimationFrame(frame)}});
function frame(now){
  if(!running)return;
  const dt=Math.min(.05,(now-last)/1000);last=now;t+=dt*(reduce?.3:1);
  if(!drag)rotTarget*=.92;rotY+=(rotTarget-rotY)*.12;world.rotation.y=rotY;
  ISLES.forEach(it=>{
    it.g.position.y=it.y+Math.sin(t*1.1+it.phase)*(reduce?.03:.12);
    it.g.rotation.y=Math.sin(t*.35+it.phase)*.18+(it===hover?.15:0);
    const s=(it===hover?1.07:1)*(layout.length&&camera.aspect<1.05?.95:1);it.g.scale.lerp(v.set(s,s,s),.15);
    it.tick(t);
  });
  clouds.forEach((c,i)=>{c.position.x+=dt*(.18+i*.03);if(c.position.x>14)c.position.x=-14});
  if(flying){const k=Math.min(1,(now-flying.t0)/800),e=k*k*(3-2*k),p=flying.it.g.getWorldPosition(v.set(0,0,0));
    camera.position.lerpVectors(flying.from,p.clone().add(new THREE.Vector3(0,.6,3.2)),e);camera.lookAt(p)}
  renderer.render(scene,camera);
  // 名稱標籤跟著小島（放在小島下面）
  ISLES.forEach((it,i)=>{const p=it.g.getWorldPosition(v.set(0,0,0));p.y-=it.planet?1.75:2.05;p.project(camera);
    const L=LAB[i];L.style.transform=`translate(-50%,0) translate(${(p.x*.5+.5)*wrap.clientWidth}px,${(-p.y*.5+.5)*wrap.clientHeight}px)`;L.classList.toggle("on",it===hover)});
  requestAnimationFrame(frame);
}
resize();renderer.render(scene,camera);
document.body.classList.add("is3d");
requestAnimationFrame(frame);

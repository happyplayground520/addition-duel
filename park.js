/* 數學遊樂園：共用的小動畫（答對噴星星、結束畫面的星星一顆一顆跳出來） */
(function(){
  let lx=innerWidth/2,ly=innerHeight/2;
  addEventListener("pointerdown",e=>{lx=e.clientX;ly=e.clientY},{capture:true,passive:true});
  const reduce=()=>{try{return matchMedia("(prefers-reduced-motion: reduce)").matches}catch(e){return false}};
  // 答對時從最後點的位置噴出星星
  window.parkBurst=function(x,y){
    if(reduce()||!document.body)return;
    const box=document.createElement("div");box.className="pk-burst";
    box.style.left=(x==null?lx:x)+"px";box.style.top=(y==null?ly:y)+"px";
    const E=["⭐","✨","🌟","⭐","💖","✨"];
    for(let i=0;i<12;i++){
      const s=document.createElement("span"),a=Math.PI*2*i/12+Math.random()*.4,d=70+Math.random()*70;
      s.textContent=E[i%E.length];s.style.setProperty("--dx",Math.cos(a)*d+"px");s.style.setProperty("--dy",Math.sin(a)*d+"px");
      s.style.animationDelay=(Math.random()*.08).toFixed(2)+"s";box.appendChild(s);
    }
    document.body.appendChild(box);setTimeout(()=>box.remove(),1200);
    try{window.parkTicket&&parkTicket(x,y)}catch(e){}
  };
  // ---- 門票：答對一題，一張彩色門票飛進右上角的分數牌（只有 body 有 data-park 的單人關卡才有） ----
  const TC=["#ff6f9f","#ffb02e","#34c27a","#3d9bff","#a070ff","#ff7a45"];
  const TIX=c=>`<svg viewBox="0 0 60 36" width="100%" height="100%"><path d="M4 3h52v10a5 5 0 0 0 0 10v10H4V23a5 5 0 0 0 0-10z" fill="${c}" stroke="#fff" stroke-width="3" stroke-linejoin="round"/><path d="M41 6v24" stroke="#fff" stroke-width="2.5" stroke-dasharray="3 3"/><path d="M21 9l2.6 5.4 5.9.8-4.3 4.1 1 5.9-5.2-2.8-5.2 2.8 1-5.9-4.3-4.1 5.9-.8z" fill="#fff"/></svg>`;
  let tix=0;
  const isPark=()=>document.body&&document.body.hasAttribute("data-park");
  window.parkTicket=function(x,y){
    const sc=document.getElementById("score");if(!isPark()||!sc)return;
    const c=TC[tix%TC.length];tix++;
    const done=()=>{sc.dataset.tix=Math.min(tix,3);sc.style.setProperty("--t1",c);
      sc.classList.remove("pk-bump");void sc.offsetWidth;sc.classList.add("pk-bump")};
    if(reduce()){done();return}
    const r=sc.getBoundingClientRect(),t=document.createElement("div");t.className="pk-tix";t.innerHTML=TIX(c);
    const sx=x==null?lx:x,sy=y==null?ly:y;t.style.left=sx+"px";t.style.top=sy+"px";document.body.appendChild(t);
    const dx=r.left+18-sx,dy=r.top+r.height/2-sy;
    try{t.animate([{transform:"translate(-50%,-50%) scale(.4) rotate(-30deg)"},{transform:`translate(calc(-50% + ${dx*.4}px),calc(-50% + ${dy*.4-70}px)) scale(1.3) rotate(10deg)`,offset:.45},
      {transform:`translate(calc(-50% + ${dx}px),calc(-50% + ${dy}px)) scale(.55) rotate(360deg)`}],{duration:850,easing:"ease-in-out",fill:"forwards"})}catch(e){}
    setTimeout(()=>{t.remove();done()},850);
  };
  // 每次開始或再玩一次，門票歸零
  function resetTix(){tix=0;const sc=document.getElementById("score");if(sc){delete sc.dataset.tix}}

  // ---- 煙火遊行：單人關卡的結束畫面要出現前，先放煙火、小動物坐花車經過 ----
  let ac;
  function boom(d){try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();if(ac.state!=="running")ac.resume();
    const t=ac.currentTime+d,len=.35,b=ac.createBuffer(1,Math.floor(ac.sampleRate*len),ac.sampleRate),ch=b.getChannelData(0);
    for(let i=0;i<ch.length;i++)ch[i]=(Math.random()*2-1)*Math.pow(1-i/ch.length,3);
    const src=ac.createBufferSource(),g=ac.createGain(),f=ac.createBiquadFilter();f.type="lowpass";f.frequency.value=1800;
    src.buffer=b;g.gain.value=.35;src.connect(f);f.connect(g);g.connect(ac.destination);src.start(t)}catch(e){}}
  const FWC=["#ff5c8a","#ffd23f","#5ce1ff","#9dff6b","#c58bff","#ff9f43"];
  function firework(o,x,y,c,delay){
    const fw=document.createElement("div");fw.className="pk-fw";fw.style.cssText=`left:${x}%;top:${y}%;--c:${c};--d:${delay}s`;
    for(let i=0;i<16;i++){const s=document.createElement("i");const a=Math.PI*2*i/16;s.style.cssText=`--dx:${(Math.cos(a)*90).toFixed(1)}px;--dy:${(Math.sin(a)*90).toFixed(1)}px`;fw.appendChild(s)}
    o.appendChild(fw);boom(delay+.45);
  }
  window.parkFinale=function(done){
    const o=document.createElement("div");o.className="pk-finale";
    o.innerHTML=`<div class="pk-float"><span class="pk-riders"><b>🐻</b><b>🐰</b><b>🐼</b><b>🐥</b></span><span class="pk-cart"><i></i><i></i></span></div>
      <p class="pk-ftxt" data-zy>全部玩完了！放煙火慶祝！</p>`;
    document.body.appendChild(o);
    [[22,22,0],[74,18,.35],[48,12,.75],[30,36,1.15],[70,34,1.5],[52,24,1.9]].forEach(([x,y,d],i)=>firework(o,x,y,FWC[i%FWC.length],d));
    let fin=false;const end=()=>{if(fin)return;fin=true;o.classList.add("out");setTimeout(()=>{o.remove();done&&done()},300)};
    o.addEventListener("pointerdown",end);setTimeout(end,3600);
  };
  function finaleHook(){
    if(!isPark())return;
    const end=document.getElementById("end");if(!end)return;let busy=false;
    new MutationObserver(()=>{if(end.hidden||busy||end.dataset.shown)return;busy=true;end.hidden=true;
      parkFinale(()=>{end.dataset.shown="1";end.hidden=false;busy=false})}).observe(end,{attributes:true,attributeFilter:["hidden"]});
    ["replay","go"].forEach(id=>{const b=document.getElementById(id);b&&b.addEventListener("click",()=>{delete end.dataset.shown;resetTix()},true)});
  }

  // ---- 雙人對戰：贏的那一邊掉下一座獎盃，噴彩帶 ----
  window.parkWin=function(ov){
    if(!ov)return;ov.querySelectorAll(".pk-win").forEach(e=>e.remove());if(reduce())return;
    const w=document.createElement("div");w.className="pk-win";
    let h=`<span class="pk-trophy">🏆</span>`;
    for(let i=0;i<22;i++)h+=`<i style="left:${(Math.random()*100).toFixed(1)}%;--c:${FWC[i%FWC.length]};animation-delay:${(Math.random()*.6).toFixed(2)}s;--r:${Math.round(Math.random()*720-360)}deg"></i>`;
    w.innerHTML=h;ov.appendChild(w);setTimeout(()=>w.remove(),3300);
  };
  // 結束畫面的星星：拆成一顆一顆，依序跳出來
  function popStars(el){
    const t=el.textContent;if(!t||el.dataset.pk===t)return;
    el.innerHTML=[...t].map((c,i)=>`<span style="--i:${i}" class="${c==="⭐"?"on":"off"}">${c}</span>`).join("");
    el.dataset.pk=el.textContent;
  }
  // ---- 學習紀錄：單人關卡每玩完一回，記下關卡、設定、答對幾題（或限時得幾分）、花多久。只存在這台裝置，家長紀錄頁（record.html）讀這裡 ----
  const LOGK="park-log",LOGMAX=800;
  let t0=0;
  const plain=el=>{if(!el)return"";const c=el.cloneNode(true);c.querySelectorAll(".zy-b,.zy-t,.zy-lt,rt").forEach(x=>x.remove());return c.textContent.replace(/\s+/g," ").trim()};
  function settings(){
    const out=[];
    document.querySelectorAll('#start [aria-pressed="true"]').forEach(b=>{
      if(b.closest("#counts"))return;
      for(let e=b.parentElement;e&&e.id!=="start";e=e.parentElement)if(e.hidden)return;
      const st=b.querySelector(".lvst"),sm=b.querySelector("small");
      let t=st||sm?[plain(st),plain(sm)].filter(Boolean).join(" "):plain(b);
      if(!t)t=b.getAttribute("aria-label")||"";if(t&&!/^👤/.test(t))out.push(t);
    });
    return out.join("・");
  }
  window.parkRec=function(o){
    try{
      if(!isPark())return;
      const h=document.querySelector("#start h2"),g=location.pathname.split("/").pop().replace(/\.html$/,"")||"?";
      const r={g,name:plain(h)||document.title,s:settings(),t:Date.now()};
      if(t0)r.d=Math.max(1,Math.round((Date.now()-t0)/1000));
      if(o.n!=null){r.ok=+o.ok||0;r.n=+o.n}else{r.sc=+o.sc||0;r.miss=+o.miss||0;if(o.u)r.u=o.u}
      let L;try{L=JSON.parse(localStorage.getItem(LOGK))||[]}catch(e){L=[]}
      L.push(r);if(L.length>LOGMAX)L=L.slice(-LOGMAX);
      localStorage.setItem(LOGK,JSON.stringify(L));
    }catch(e){}
    t0=0;
  };
  function recHook(){
    ["go","replay"].forEach(id=>{const b=document.getElementById(id);b&&b.addEventListener("click",()=>{t0=Date.now()},true)});
  }
  function init(){
    finaleHook();recHook();
    const st=document.getElementById("stars");
    if(st){popStars(st);new MutationObserver(()=>popStars(st)).observe(st,{childList:true,characterData:true,subtree:true})}
    const r=document.getElementById("result");
    if(r)new MutationObserver(()=>{r.style.animation="none";void r.offsetWidth;r.style.animation=""}).observe(r,{childList:true});
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();

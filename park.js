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
  };
  // 結束畫面的星星：拆成一顆一顆，依序跳出來
  function popStars(el){
    const t=el.textContent;if(!t||el.dataset.pk===t)return;
    el.innerHTML=[...t].map((c,i)=>`<span style="--i:${i}" class="${c==="⭐"?"on":"off"}">${c}</span>`).join("");
    el.dataset.pk=el.textContent;
  }
  function init(){
    const st=document.getElementById("stars");
    if(st){popStars(st);new MutationObserver(()=>popStars(st)).observe(st,{childList:true,characterData:true,subtree:true})}
    const r=document.getElementById("result");
    if(r)new MutationObserver(()=>{r.style.animation="none";void r.offsetWidth;r.style.animation=""}).observe(r,{childList:true});
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();

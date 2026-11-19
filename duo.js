/* 兩人搶答（共用）：畫面分成上下兩半，上面那半轉 180 度，兩個人面對面玩。
   每個人各答各的題目，先答對 Duo.TARGET 題的人贏。可以讓分：每個人選自己的難度，或打開「🐢 慢 3 秒」（選項晚 3 秒才出現）。
   用法：Duo.start({
     title:"太空列車排排看", levels:{1:"⭐ ...",2:"...",3:"..."},
     gen(lv) → 題目 q（要有 q.ans）,
     options(q) → [{v,label}],            // 選項
     render(q, el, player) → 把題目的圖畫進 el,
     ask(q) → 題目文字（可以有 HTML）,
     reveal(q, el, v, ok) → 選了某個答案之後（可省略）,
     onExit() → 回到原本的開始畫面
   }) */
(function(){
  const Duo={TARGET:6};
  const NAMES=["藍色","橘色"],ICON=["🔵","🟠"];
  let ac=null;
  function tone(fs,dur=.12,type="triangle",vol=.15){try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();if(ac.state!=="running")ac.resume();
    fs.forEach((f,i)=>{const o=ac.createOscillator(),g=ac.createGain(),t=ac.currentTime+i*dur;o.type=type;o.frequency.value=f;
      g.gain.setValueAtTime(vol,t);g.gain.exponentialRampToValueAtTime(.001,t+dur*1.6);o.connect(g).connect(ac.destination);o.start(t);o.stop(t+dur*1.7)})}catch(e){}}
  const sfx={good:()=>tone([784,1175],.12,"sine",.25),bad:()=>tone([150],.25,"square",.13),tick:()=>tone([600],.1),go:()=>tone([900],.25),win:()=>tone([523,659,784,1047],.16)};
  const pref=(k,v)=>{try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}};

  Duo.start=function(cfg){
    const key="duo-"+(cfg.key||"x");
    const root=document.createElement("div");root.className="duo";root.innerHTML=[1,0].map(p=>`
      <section class="half p${p}" data-p="${p}">
        <div class="in"><div class="hd"><span class="nm">${ICON[p]} <span data-zy>${NAMES[p]}</span></span><span class="prog"></span></div>
        <div class="ask" data-zy></div>
        <div class="vis"></div>
        <div class="opts"></div>
        <div class="dmsg" data-zy></div></div>
        <div class="ready">
          <h2 data-zy>${NAMES[p]}</h2>
          <div class="lvs">${[1,2,3].map(l=>`<button type="button" class="dopt" data-lv="${l}">${cfg.levels[l]}</button>`).join("")}</div>
          <button type="button" class="dopt slow" aria-pressed="false"><span data-zy>🐢 慢 3 秒</span></button>
          <div class="row"><button type="button" class="dgo">READY</button><button type="button" class="dhome" aria-label="離開">✖</button></div>
          <p class="note" data-zy>先答對 ${Duo.TARGET} 題的人贏！</p>
        </div>
      </section>`).join("")+`<div class="count" hidden></div>`;
    document.body.appendChild(root);document.body.classList.add("duo-on");
    const P=[0,1].map(p=>{const el=root.querySelector(`.half.p${p}`);
      return{el,p,lv:+pref(key+"-lv"+p)||(p?3:1),slow:pref(key+"-slow"+p)==="1",ready:false,score:0,q:null,lock:false,timer:0,
        ask:el.querySelector(".ask"),vis:el.querySelector(".vis"),opts:el.querySelector(".opts"),msg:el.querySelector(".dmsg"),prog:el.querySelector(".prog"),rd:el.querySelector(".ready"),
        go:el.querySelector(".dgo"),slowB:el.querySelector(".slow")}});
    let phase="ready";
    const sync=pl=>{pl.rd.querySelectorAll(".lvs .dopt").forEach(b=>b.setAttribute("aria-pressed",+b.dataset.lv===pl.lv));pl.slowB.setAttribute("aria-pressed",pl.slow);
      pl.go.textContent=pl.ready?"✅":"READY";pl.go.classList.toggle("on",pl.ready)};
    const prog=pl=>{pl.prog.textContent="⭐".repeat(pl.score)+"☆".repeat(Math.max(0,Duo.TARGET-pl.score))};
    P.forEach(pl=>{
      pl.rd.querySelectorAll(".lvs .dopt").forEach(b=>b.onclick=()=>{if(phase!=="ready")return;pl.lv=+b.dataset.lv;pref(key+"-lv"+pl.p,pl.lv);sync(pl)});
      pl.slowB.onclick=()=>{if(phase!=="ready")return;pl.slow=!pl.slow;pref(key+"-slow"+pl.p,pl.slow?"1":"0");sync(pl)};
      pl.go.onclick=()=>{if(phase==="over"){again();return}if(phase!=="ready")return;pl.ready=!pl.ready;sync(pl);tone([600],.08);if(P.every(x=>x.ready))countdown()};
      pl.el.querySelector(".dhome").onclick=exit;
      sync(pl);prog(pl);
    });
    function exit(){P.forEach(pl=>clearTimeout(pl.timer));root.remove();document.body.classList.remove("duo-on");cfg.onExit&&cfg.onExit()}
    function countdown(){
      phase="count";P.forEach(pl=>{pl.rd.hidden=true;pl.score=0;prog(pl)});
      const c=root.querySelector(".count");let n=3;c.hidden=false;c.textContent=n;sfx.tick();
      const iv=setInterval(()=>{n--;if(n>0){c.textContent=n;sfx.tick();return}clearInterval(iv);c.hidden=true;sfx.go();phase="play";P.forEach(ask)},800);
    }
    // 出一題給這個人
    function ask(pl){
      if(phase!=="play")return;
      const q=pl.q=cfg.gen(pl.lv);pl.lock=false;
      pl.ask.innerHTML=cfg.ask(q);pl.msg.textContent="";pl.msg.className="dmsg";
      pl.vis.innerHTML="";cfg.render(q,pl.vis,pl.p);
      const opts=cfg.options(q);
      pl.opts.innerHTML=opts.map(o=>`<button type="button" class="dch" data-v="${o.v}">${o.label}</button>`).join("");
      pl.opts.querySelectorAll(".dch").forEach(b=>b.onclick=()=>pick(pl,b));
      // 讓分：選項晚 3 秒才出現（畫面上有倒數的小烏龜）
      clearTimeout(pl.timer);
      if(pl.slow){pl.opts.classList.add("wait");pl.msg.textContent="🐢 3 秒後可以回答";pl.timer=setTimeout(()=>{if(pl.q===q){pl.opts.classList.remove("wait");pl.msg.textContent=""}},3000)}
      else pl.opts.classList.remove("wait");
    }
    function pick(pl,b){
      if(phase!=="play"||pl.lock||pl.opts.classList.contains("wait"))return;
      const q=pl.q,v=b.dataset.v,ok=String(q.ans)===v;
      cfg.reveal&&cfg.reveal(q,pl.vis,v,ok);
      if(ok){
        pl.lock=true;pl.score++;prog(pl);b.classList.add("right");sfx.good();pl.msg.textContent="答對了！";pl.msg.className="dmsg good";
        try{window.parkBurst&&parkBurst(...center(b))}catch(e){}
        if(pl.score>=Duo.TARGET)return finish(pl.p);
        pl.timer=setTimeout(()=>ask(pl),cfg.revealMs||1000);
      }else{
        // 答錯：抖一下，等 1 秒才能再選
        pl.lock=true;sfx.bad();b.classList.add("wrong");pl.msg.textContent=cfg.wrongMsg?cfg.wrongMsg(q,v):"再想一想";pl.msg.className="dmsg bad";
        pl.timer=setTimeout(()=>{if(pl.q===q){pl.lock=false;cfg.unreveal&&cfg.unreveal(q,pl.vis)}},1000);
      }
    }
    const center=el=>{const r=el.getBoundingClientRect();return[r.left+r.width/2,r.top+r.height/2]};
    function finish(w){
      phase="over";sfx.win();P.forEach(pl=>clearTimeout(pl.timer));
      P.forEach(pl=>{pl.rd.hidden=false;pl.rd.classList.add("over");
        pl.rd.querySelector("h2").textContent=pl.p===w?"你贏了！🏆":"再接再厲！";
        pl.rd.querySelector(".note").textContent=`${NAMES[0]} ${P[0].score} 題，${NAMES[1]} ${P[1].score} 題`;
        pl.go.textContent="🔁";pl.go.classList.remove("on")});
      try{window.parkWin&&parkWin(P[w].rd)}catch(e){}
    }
    function again(){phase="ready";P.forEach(pl=>{pl.ready=false;pl.score=0;pl.rd.classList.remove("over");pl.rd.querySelector("h2").textContent=NAMES[pl.p];
      pl.rd.querySelector(".note").textContent=`先答對 ${Duo.TARGET} 題的人贏！`;sync(pl);prog(pl)})}
  };
  window.Duo=Duo;
})();

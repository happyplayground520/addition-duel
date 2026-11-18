/* 甜點小鎮共用：版本和課次範圍、注音（考試內容的注音一律手動標，不用自動判斷）、題庫 */
(function(){
  const Z=window.ZI,TZ={};
  const pref=(k,v)=>{try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}};
  TZ.pref=pref;
  // ---- 版本和範圍 ----
  TZ.ver=()=>pref("town-ver")==="B"?"B":"A";
  TZ.lessons=v=>Z.L[v||TZ.ver()];
  const NUM="一二三四五六七八九十";
  TZ.short=n=>n.split("：")[0];
  TZ.range=()=>{const n=TZ.lessons().length,fa=pref("town-from"),fb=pref("town-to");let a=fa==null?0:+fa,b=fb==null?n-1:+fb;
    if(!(a>=0&&a<n))a=0;if(!(b>=0&&b<n))b=n-1;if(b<a)b=a;return[a,b]};
  TZ.setRange=(a,b)=>{pref("town-from",a);pref("town-to",b)};
  // 範圍裡的字（只要生字，或生字＋認讀字）
  TZ.pool=(withRead)=>{const [a,b]=TZ.range();return TZ.lessons().slice(a,b+1).flatMap(l=>[...l.s,...(withRead?l.r:"")])};
  // 學過的字：範圍最後一課以前的所有字（題目裡學過的字不加注音）
  TZ.learned=()=>{const [,b]=TZ.range();return new Set(TZ.lessons().slice(0,b+1).flatMap(l=>[...l.s,...l.r]))};
  TZ.rangeLabel=()=>{const [a,b]=TZ.range(),L=TZ.lessons();return `${TZ.ver()} 版・${TZ.short(L[a].n)}${a===b?"":"～"+TZ.short(L[b].n)}`};

  // ---- 注音 ----
  // 和數學遊樂園一樣的直式注音；加上 zy-keep，首頁把注音關掉時，考試內容的注音還是會顯示
  const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  function charHTML(ch,z,cls=""){
    if(!z)return `<span class="tz ${cls}"><span class="tz-h">${esc(ch)}</span></span>`;
    const light=z[0]==="˙",syms=[...(light?z.slice(1):z)];
    const tone=/[ˊˇˋ]/.test(syms[syms.length-1])?syms.pop():"";
    const col=syms.map((s,k)=>`<span>${s}${k===syms.length-1&&tone?`<span class="zy-t">${tone}</span>`:""}</span>`).join("");
    return `<span class="tz ${cls}"><span class="tz-h">${esc(ch)}</span><span class="tz-b" aria-hidden="true">${light?'<span class="zy-lt">˙</span>':""}${col}</span></span>`;
  }
  TZ.charHTML=charHTML;
  TZ.zyOf=c=>Z.ZY[c]||(Z.buzy&&Z.buzy[c])||"";
  // text 裡：＿ 是空格，字[注音] 指定讀音；skip 是不加注音的字（Set）
  TZ.zy=function(text,o={}){
    const out=[];const cs=[...text];
    for(let i=0;i<cs.length;i++){
      const c=cs[i];
      if(c==="＿"){out.push(`<span class="blank" id="${o.blankId||"blank"}"></span>`);continue}
      if(c==="["||c==="]")continue;
      let z=null;if(cs[i+1]==="["){const j=cs.indexOf("]",i);z=cs.slice(i+2,j).join("");i=j}
      if(!/[一-鿿]/.test(c)){out.push(`<span class="tp">${esc(c)}</span>`);continue}
      const skip=o.skip&&o.skip.has(c);
      out.push(charHTML(c,skip?"":(z||Z.ZY[c]||""),o.cls||""));
    }
    return out.join("");
  };
  // 念句子：把 [注音] 和空格拿掉
  TZ.plain=t=>t.replace(/\[[^\]]*\]/g,"");
  // 念中文。有 onend（念完要做下一步）時加保險：就算被別的聲音打斷，時間到也一定會接下去
  TZ.say=(t,o={})=>{if(!window.EN)return;const txt=TZ.plain(t);
    if(o.onend){let done=false;const cb=o.onend,once=()=>{if(done)return;done=true;cb()};o=Object.assign({},o,{onend:once});setTimeout(once,2600+[...txt].length*330)}
    EN.say(txt,Object.assign({zh:true,rate:.85},o))};
  TZ.shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
  // 依題數輪流出題：題庫不夠時重複，但不會連續一樣
  TZ.deal=(items,n)=>{const out=[];let bag=[];while(out.length<n&&items.length){if(!bag.length)bag=TZ.shuffle(items.slice());const x=bag.pop();if(items.length>1&&out[out.length-1]===x)continue;out.push(x)}return out};

  // ---- 開始畫面：版本、從第幾課到第幾課（每一關共用） ----
  TZ.setupPanel=function(box,onChange){
    // 版本和範圍：用左右箭頭換課（下拉選單沒辦法加注音）
    box.innerHTML=`<div class="row" id="verRow"><button type="button" class="opt ver" data-v="A">${TZ.zy("A 版")}</button><button type="button" class="opt ver" data-v="B">${TZ.zy("B 版")}</button></div>
      <div class="rangeRow"><span class="rlab">${TZ.zy("從")}</span><div class="stepper" id="sFrom"><button type="button" class="sbtn" data-d="-1" aria-label="前一課">◀</button><span class="sname"></span><button type="button" class="sbtn" data-d="1" aria-label="後一課">▶</button></div></div>
      <div class="rangeRow"><span class="rlab">${TZ.zy("到")}</span><div class="stepper" id="sTo"><button type="button" class="sbtn" data-d="-1" aria-label="前一課">◀</button><span class="sname"></span><button type="button" class="sbtn" data-d="1" aria-label="後一課">▶</button></div></div>`;
    box.setAttribute("data-zy-skip","");
    const name=l=>TZ.zy(l.n.replace("：","　"));
    const fill=()=>{
      const L=TZ.lessons(),[a,b]=TZ.range();
      box.querySelectorAll("#verRow .opt").forEach(x=>x.setAttribute("aria-pressed",x.dataset.v===TZ.ver()));
      box.querySelector("#sFrom .sname").innerHTML=name(L[a]);box.querySelector("#sTo .sname").innerHTML=name(L[b]);
      box.querySelectorAll("#sFrom .sbtn").forEach(x=>x.disabled=(+x.dataset.d<0?a<=0:a>=L.length-1));
      box.querySelectorAll("#sTo .sbtn").forEach(x=>x.disabled=(+x.dataset.d<0?b<=0:b>=L.length-1));
      onChange&&onChange();
    };
    box.querySelectorAll("#verRow .opt").forEach(x=>x.onclick=()=>{pref("town-ver",x.dataset.v);pref("town-from",0);pref("town-to",TZ.lessons(x.dataset.v).length-1);fill()});
    box.querySelectorAll("#sFrom .sbtn").forEach(x=>x.onclick=()=>{const [a,b]=TZ.range(),na=a+ +x.dataset.d;TZ.setRange(na,Math.max(na,b));fill()});
    box.querySelectorAll("#sTo .sbtn").forEach(x=>x.onclick=()=>{const [a,b]=TZ.range(),nb=b+ +x.dataset.d;TZ.setRange(Math.min(a,nb),nb);fill()});
    fill();
  };

  // ---- 動作：收集計數、飛到計數、結尾動畫、聲調音高 ----
  // 標題列的收集計數（例如 🍪×3），每答對一題加一
  TZ.got=function(icon){let g=document.getElementById("got");
    if(!g){g=document.createElement("span");g.id="got";g.className="pill gotpill";const mid=document.querySelector(".top .mid");mid&&mid.appendChild(g);g.dataset.n="0"}
    if(icon!==undefined){g.dataset.icon=icon}const n=+g.dataset.n;g.innerHTML=`<span class="gi">${g.dataset.icon||""}</span>×${n}`;return g};
  TZ.gotAdd=function(){const g=TZ.got();g.dataset.n=+g.dataset.n+1;TZ.got();g.classList.remove("bump");void g.offsetWidth;g.classList.add("bump")};
  TZ.gotReset=icon=>{const g=TZ.got(icon);g.dataset.n="0";TZ.got()};
  // 從某個元素的位置變出一個小圖，飛到收集計數
  TZ.flyGot=function(fromEl,html,done){
    const r=fromEl.getBoundingClientRect(),m=document.createElement("span");m.className="flymini";m.innerHTML=html;
    m.style.cssText=`position:fixed;left:${r.left+r.width/2-28}px;top:${r.top+r.height/2-28}px;width:56px;height:56px;z-index:70;pointer-events:none`;document.body.appendChild(m);
    TZ.fly(m,TZ.got(),()=>{TZ.gotAdd();EN.sfx.pop();done&&done()},{dur:.65,scale:.5});setTimeout(()=>m.remove(),1100)};
  // 結尾動畫：畫面中間跳出一張卡片（圖＋一句話），播完才進結束畫面
  TZ.finale=function(html,text,done,ms=2600){
    const o=document.createElement("div");o.className="finale";o.innerHTML=`<div class="fcard">${html}<p>${TZ.zy(text)}</p></div>`;document.body.appendChild(o);
    EN.sfx.clear();try{window.parkBurst&&parkBurst(innerWidth/2,innerHeight/2)}catch(e){}TZ.say(text);
    setTimeout(()=>{o.classList.add("out");setTimeout(()=>{o.remove();done&&done()},300)},ms)};
  // 聲調的音高：一聲平、二聲往上、三聲先降再升、四聲往下、輕聲短短的
  let ac2=null;
  TZ.toneSound=function(t){try{ac2=ac2||new (window.AudioContext||window.webkitAudioContext)();if(ac2.state!=="running")ac2.resume();
    const o=ac2.createOscillator(),g=ac2.createGain(),now=ac2.currentTime,f=o.frequency;o.type="sine";
    const P={1:[[0,520],[.5,520]],2:[[0,330],[.5,560]],3:[[0,400],[.22,260],[.55,470]],4:[[0,600],[.4,280]],0:[[0,380],[.18,360]]}[t]||[[0,440],[.3,440]];
    f.setValueAtTime(P[0][1],now);P.slice(1).forEach(([x,v])=>f.linearRampToValueAtTime(v,now+x));
    const end=now+P[P.length-1][0];g.gain.setValueAtTime(.0001,now);g.gain.exponentialRampToValueAtTime(.25,now+.04);g.gain.setValueAtTime(.25,end-.05);g.gain.exponentialRampToValueAtTime(.0001,end+.08);
    o.connect(g).connect(ac2.destination);o.start(now);o.stop(end+.1)}catch(e){}};
  // ---- 共用的遊戲流程：開始畫面 → 出題 → 結束畫面 ----
  // cfg: {key, help, build(n)→題目陣列（不夠就回傳空陣列）, show(q)→畫出一題, empty:"題庫不夠時的提示"}
  TZ.run=function(cfg){
    const $=id=>document.getElementById(id),S={total:+pref(cfg.key+"-total")||10,i:0,score:0,tries:0,qs:[],busy:false,phase:"start"};
    if(![5,10,15].includes(S.total))S.total=10;
    const syncT=()=>document.querySelectorAll("#totals .opt").forEach(b=>b.setAttribute("aria-pressed",+b.dataset.n===S.total));
    document.querySelectorAll("#totals .opt").forEach(b=>b.onclick=()=>{S.total=+b.dataset.n;pref(cfg.key+"-total",S.total);syncT()});syncT();
    const note=$("note");
    // 版本和範圍在甜點小鎮地圖上設定，這裡只顯示
    if(cfg.noRange)$("setup").innerHTML="";else{$("setup").setAttribute("data-zy-skip","");$("setup").innerHTML=`<span class="scopeTag">📖 ${TZ.zy(TZ.rangeLabel())}</span>`}
    EN.helpBtn($("help"),()=>cfg.help);
    const api={
      S,
      ok(){if(S.busy)return;S.busy=true;if(S.tries===0)S.score++;$("score").textContent=`⭐ ${S.score}`;EN.sfx.good()},
      bad(){S.tries++;EN.sfx.bad()},
      next(delay=900){setTimeout(()=>{if(S.i+1>=S.total&&cfg.finale&&!S.fin){S.fin=true;cfg.finale(()=>{S.i++;finish()});return}S.i++;if(S.i>=S.total)finish();else show()},delay)}
    };
    function show(){S.tries=0;S.busy=false;$("prog").textContent=`${S.i+1} / ${S.total}`;cfg.show(S.qs[S.i],api)}
    function start(){
      EN.unlock();
      const qs=cfg.build(S.total);
      if(!qs.length){if(note)note.textContent=cfg.empty||"這個範圍的題目不夠，請多選幾課。";EN.sfx.bad();return}
      S.qs=qs;S.i=0;S.score=0;S.fin=false;S.phase="play";if(cfg.gotIcon)TZ.gotReset(cfg.gotIcon);$("score").textContent="⭐ 0";$("start").hidden=true;$("end").hidden=true;
      const sc=$("scopeTop");if(sc)sc.textContent=cfg.noRange?"":TZ.rangeLabel();
      show();
    }
    function finish(){
      S.phase="end";const r=S.score/S.total,st=r>=.9?3:r>=.6?2:1;
      $("stars").textContent="⭐".repeat(st)+"☆".repeat(3-st);$("result").textContent=`${S.score} / ${S.total}`;
      EN.sfx.end();TZ.say(st===3?"太厲害了！":st===2?"做得很好！":"很努力喔，再練習一次！");$("end").hidden=false;
    }
    $("go").onclick=start;$("replay").onclick=start;
    return api;
  };

  // 讓一個東西從 a 飛到 b（用複製的元素做動畫），飛到後執行 done
  TZ.fly=function(a,b,done,o={}){
    const ra=a.getBoundingClientRect(),rb=b.getBoundingClientRect(),c=a.cloneNode(true);
    c.classList.remove("yes","glow","no","shake");c.style.cssText=`position:fixed;left:${ra.left}px;top:${ra.top}px;width:${ra.width}px;height:${ra.height}px;margin:0;z-index:60;pointer-events:none;transition:transform ${o.dur||.7}s cubic-bezier(.4,-0.3,.4,1.2),opacity .2s ease ${o.dur||.7}s`;
    document.body.appendChild(c);a.style.visibility="hidden";
    const s=o.scale||Math.min(rb.width/ra.width,rb.height/ra.height,1);
    requestAnimationFrame(()=>requestAnimationFrame(()=>{c.style.transform=`translate(${rb.left+rb.width/2-ra.left-ra.width/2}px,${rb.top+rb.height/2-ra.top-ra.height/2}px) scale(${s}) rotate(${o.spin||0}deg)`}));
    setTimeout(()=>{c.style.opacity="0";done&&done();setTimeout(()=>{c.remove();if(o.keepHidden!==true)a.style.visibility=""},250)},(o.dur||.7)*1000);
  };
  window.TZ=TZ;
})();

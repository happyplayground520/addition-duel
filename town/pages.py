# 產生甜點小鎮的四關頁面：python pages.py（每一關共用標題列、開始畫面、結束畫面，只有題目區和玩法不同）
import os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
V="20261118n"
HEAD='''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Chiron+GoRound+TC:wght@400;700;900&display=swap">
<link rel="stylesheet" href="en.css?v={V}">
<link rel="stylesheet" href="town/town.css?v={V}">
<style>
{style}
</style>
<script src="zhuyin.js?v={V}"></script>
<link rel="stylesheet" href="park.css?v={V}">
<script src="park.js?v={V}"></script>
<script src="en.js?v={V}"></script>
<script src="town/zi-data.js?v={V}"></script>
<script src="town/town.js?v={V}"></script>
<style>body{{font-family:var(--text)}}</style>
</head>
<body>
<header class="top">
  <a class="ibtn" href="town.html" aria-label="回甜點小鎮">🏠</a>
  <div class="mid"><span class="pill" id="prog">1 / 10</span><span class="scope" id="scopeTop"></span></div>
  <div class="right"><span class="pill" id="score">⭐ 0</span></div>
</header>
<main class="stage2" id="main" data-zy-skip>
{main}
</main>

<section class="panel" id="start">
  <div class="box">
    <h2>{icon} {title}</h2>
    <p class="sub" data-zy>{sub}</p>
    <button type="button" class="helpbtn" id="help">🔊 中文說明</button>
    <div id="setup"></div>
    <div class="row" id="totals">
      <button type="button" class="opt" data-n="5" aria-label="5 題"><span class="dots"><i></i><i></i><i></i><i></i><i></i></span><small>5</small></button>
      <button type="button" class="opt" data-n="10" aria-label="10 題"><span class="dots"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span><small>10</small></button>
      <button type="button" class="opt" data-n="15" aria-label="15 題"><span class="dots"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span><small>15</small></button>
    </div>
    <span class="note" id="note" data-zy></span>
    <button type="button" class="big" id="go">READY</button>
    <p class="source">字型：全字庫正楷體（數位發展部「CNS11643中文標準交換碼全字庫」，依政府資料開放授權條款第1版使用）<br>生字：教育部教育百科「生字詞彙表」；部首、讀音：教育部《國語辭典簡編本》；筆畫：教育部《國字標準字體筆順學習網》</p>
  </div>
</section>
<section class="panel" id="end" hidden>
  <div class="box">
    <h2>做完了！</h2>
    <div id="stars">⭐⭐⭐</div>
    <div id="result">0 / 10</div>
    <div class="endrow">
      <button type="button" class="big ico-btn" id="replay" aria-label="再玩一次">🔁</button>
      <a class="big alt ico-btn" href="town.html" aria-label="回甜點小鎮">🏠</a>
    </div>
  </div>
</section>
<script>
{script}
</script>
</body>
</html>
'''
COMMON_STYLE='''main.stage2{position:relative;flex:1;min-height:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(12px,2.6vh,28px);
  padding:0 max(14px,env(safe-area-inset-right,0px)) max(12px,env(safe-area-inset-bottom,0px)) max(14px,env(safe-area-inset-left,0px))}
.top .mid{flex-direction:column;gap:2px}
.top .scope{font-size:13px}
#start .source{margin-top:4px}
@media (max-height:500px){main.stage2{flex-direction:row;gap:24px}.qline{font-size:19px;line-height:1.4}.qcard{gap:6px}}
@media (orientation:portrait) and (max-height:740px){.qline{font-size:20px;line-height:1.4}.qcard{gap:8px}main.stage2{gap:12px}}'''
PAGES={}
def page(fn,**k):PAGES[fn]=k

# ---------- 1. 餅乾模子（部首） ----------
page("town-bu.html",title="餅乾模子",icon="🍪",sub="看餅乾上的字，選出它的部首模子！",
style='''.cookie{position:relative;width:clamp(150px,30vmin,250px);aspect-ratio:1;border-radius:50%;display:grid;place-items:center;
  background:radial-gradient(circle at 35% 30%,#f7c98b,#e2a560 60%,#c98a4b);border:6px solid var(--choc);box-shadow:0 10px 0 rgba(0,0,0,.15),inset 0 -10px 0 rgba(0,0,0,.08)}
.cookie::before{content:"";position:absolute;inset:10%;border-radius:50%;border:4px dotted rgba(107,63,34,.35)}
.cookie b{font-family:var(--kai);font-weight:400;font-size:clamp(90px,19vmin,160px);line-height:1;color:var(--choc)}
.cookie.stamp{animation:stamp .5s}
@keyframes stamp{40%{transform:scale(.9)}70%{transform:scale(1.08)}}
.cutter{width:clamp(96px,17vmin,140px);aspect-ratio:1;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.18)}
.cutter.s0{border-radius:50%}.cutter.s1{border-radius:28px}.cutter.s2{border-radius:50% 50% 22px 22px}.cutter.s3{border-radius:22px 50% 22px 50%}
.cutter .bu{font-family:var(--kai);font-size:clamp(50px,9vmin,76px);color:var(--ink)}
.cutter .tz-b{font-size:17px}''',
main='''<div class="qcard"><div class="qline" id="q"></div><div class="cookie" id="cookie"><b id="ch"></b></div></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffb3c7","#a8e6cf","#ffe08a","#b9d7ff"];
  const api=TZ.run({key:"town-bu",
    help:"餅乾模子。餅乾上有一個字，請你想一想，這個字的部首是哪一個，點那個部首的餅乾模子。部首都是照教育部的寫法，例如三點水寫成「水」，草字頭寫成「艸」。",
    build:n=>TZ.deal(TZ.pool(false),n),
    show:(c)=>{
      const info=Z.chars[c],bu=info.bu;
      // 選項：正確的部首、字裡看得到但不是部首的部件、再補其他字的部首
      const opts=[bu];const tr=Z.trick[c];if(tr&&tr!==bu)opts.push(tr);
      const others=TZ.shuffle([...new Set(Object.values(Z.chars).map(v=>v.bu))].filter(b=>!opts.includes(b)));
      while(opts.length<4)opts.push(others.pop());
      $("ch").textContent=c;
      $("q").innerHTML=TZ.zy("「")+`<b class="kai" style="font-size:1.3em">${c}</b>`+TZ.zy("」的部首是哪一個？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
      $("say").onclick=()=>TZ.say(`${c}，的部首是哪一個？`);
      $("choices").innerHTML=TZ.shuffle(opts).map((b,i)=>`<button type="button" class="choice cutter s${i}" style="--c:${COL[i]}" data-b="${b}" aria-label="${b}">${TZ.charHTML(b,Z.buzy[b]||"","bu")}</button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.b===bu){api.ok();el.classList.add("yes");const ck=$("cookie");ck.classList.remove("stamp");void ck.offsetWidth;ck.classList.add("stamp");
          TZ.say(`答對了！${c}的部首是${bu}。`,{onend:()=>api.next(400)})}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-b="${bu}"]`).classList.add("glow")}
      });
      setTimeout(()=>TZ.say(`${c}，的部首是哪一個？`),300);
    }});
})();''')

# ---------- 2. 數糖果（筆畫） ----------
page("town-n.html",title="數糖果",icon="🍬",sub="這個字有幾畫？一畫一顆糖果！",
style='''.jar{position:relative;width:clamp(170px,32vmin,270px);aspect-ratio:.86;border:6px solid var(--choc);border-radius:30px 30px 40px 40px;background:rgba(255,255,255,.75);
  display:grid;place-items:center;box-shadow:0 10px 0 rgba(0,0,0,.12)}
.jar::before{content:"";position:absolute;left:12%;right:12%;top:-22px;height:22px;border-radius:12px 12px 0 0;background:var(--berry);border:6px solid var(--choc);border-bottom:0}
.jar b{font-family:var(--kai);font-weight:400;font-size:clamp(100px,20vmin,170px);line-height:1;color:var(--choc)}
.count{position:absolute;right:-18px;top:-18px;min-width:56px;height:56px;border-radius:999px;background:var(--lemon);border:4px solid var(--choc);display:grid;place-items:center;
  font-family:var(--num);font-weight:800;font-size:28px;color:var(--choc);opacity:0;transform:scale(.6);transition:.2s}
.count.on{opacity:1;transform:none}
.sweets{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;max-width:min(560px,90vw);min-height:26px}
.sweets i{width:22px;height:22px;border-radius:50%;background:var(--c);border:3px solid var(--choc);animation:bpop .25s}
.moe{margin-top:2px}
@media (max-height:500px){.jar{width:120px}.jar b{font-size:84px}.sweets{min-height:22px}.sweets i{width:16px;height:16px}.candy{min-width:84px;height:72px;font-size:36px}.moe{min-height:40px;font-size:14px;padding:2px 10px}}
@media (orientation:portrait) and (max-height:740px){.jar{width:150px}.jar b{font-size:100px}}
.candy{min-width:clamp(96px,17vmin,130px);height:clamp(84px,14vmin,110px);border-radius:999px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.18);
  font-family:var(--num);font-weight:800;font-size:clamp(40px,7vmin,58px);color:var(--choc);position:relative;display:flex;align-items:center;justify-content:center;gap:4px}
.moe{font-weight:800;font-size:16px;color:var(--zyc);text-decoration:none;background:#fff;border:3px solid #cfe0f5;border-radius:999px;padding:4px 14px;min-height:44px;display:inline-flex;align-items:center}
.candy::before,.candy::after{content:"";position:absolute;top:50%;width:26px;height:34px;background:var(--c);border:4px solid var(--choc);transform:translateY(-50%)}
.candy::before{left:-24px;clip-path:polygon(0 0,100% 50%,0 100%);border:0}.candy::after{right:-24px;clip-path:polygon(100% 0,0 50%,100% 100%);border:0}
.candy small{font-family:var(--text);font-size:.42em;margin-left:2px}''',
main='''<div class="qcard"><div class="qline" id="q"></div><div class="jar" id="jar"><b id="ch"></b><span class="count" id="count">0</span></div><div class="sweets" id="sweets"></div><a class="moe" id="moe" target="_blank" rel="noopener"></a></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ff9fb2","#9ef0b9","#ffe08a","#9fd3ff","#d7b4ff"];
  // 答完：一顆一顆放糖果數到總筆畫（字形一直是教育部標準字體，不放其他來源的筆順動畫）
  function countUp(c,n,done){
    const sw=$("sweets"),cnt=$("count");sw.innerHTML="";cnt.textContent="0";cnt.classList.add("on");
    let k=0;const t=setInterval(()=>{k++;cnt.textContent=k;sw.insertAdjacentHTML("beforeend",`<i style="--c:${COL[k%COL.length]}"></i>`);EN.sfx.pop();
      if(k>=n){clearInterval(t);TZ.say(`${n}畫`);setTimeout(done,1100)}},300);
  }
  const api=TZ.run({key:"town-n",
    help:"數糖果。看糖果罐上的字，數一數這個字有幾畫，點對的數字。答完以後，一畫會放一顆糖果，一起數一數。想看怎麼寫，可以按「看教育部的筆順」。",
    build:n=>TZ.deal(TZ.pool(false),n),
    show:(c)=>{
      const n=Z.chars[c].n;$("sweets").innerHTML="";$("count").classList.remove("on");
      $("moe").href="https://stroke-order.learningweb.moe.edu.tw/dictView.jsp?ID="+c.codePointAt(0);$("moe").innerHTML="✍️ "+TZ.zy("看教育部的筆順");
      $("ch").textContent=c;
      $("q").innerHTML=TZ.zy("「")+`<b class="kai" style="font-size:1.3em">${c}</b>`+TZ.zy("」有幾畫？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
      $("say").onclick=()=>TZ.say(`${c}，有幾畫？`);
      const set=new Set([n]);const d=[-2,-1,1,2,3];TZ.shuffle(d);for(const x of d){if(set.size>=3)break;if(n+x>=1)set.add(n+x)}
      $("choices").innerHTML=TZ.shuffle([...set]).map((v,i)=>`<button type="button" class="choice candy" style="--c:${COL[i]}" data-v="${v}" aria-label="${v} 畫">${v}<small>${TZ.charHTML("畫",ZI.ZY["畫"])}</small></button>`).join("");
      const finish=()=>countUp(c,n,()=>api.next(200));
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(+el.dataset.v===n){api.ok();el.classList.add("yes");TZ.say(`答對了！${c}有${n}畫。`);setTimeout(finish,500)}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2){api.S.busy=true;document.querySelector(`.choice[data-v="${n}"]`).classList.add("glow");TZ.say(`${c}有${n}畫，我們一起數一數。`);setTimeout(finish,800)}}
      });
      setTimeout(()=>TZ.say(`${c}，有幾畫？`),300);
    }});
})();''')

# ---------- 3. 麵包店送貨（選詞填空） ----------
page("town-fill.html",title="麵包店送貨",icon="🥐",sub="句子少了一個字，把對的麵包送過去！",
style='''.order{background:#fff;border:5px solid var(--choc);border-radius:24px;padding:clamp(14px,3vmin,26px) clamp(16px,3vmin,30px);box-shadow:0 8px 0 rgba(0,0,0,.12);
  max-width:min(900px,94vw);position:relative}
.order .tag{position:absolute;left:18px;top:-18px;background:var(--berry);color:#fff;font-weight:900;font-size:16px;border-radius:999px;padding:1px 12px;border:3px solid #fff}
.order .tag .tz-b{color:#fff}
.order .sent{font-family:var(--kai);font-size:clamp(30px,5.6vmin,52px);line-height:1.9;text-align:center}
.order .sent .tz-b{font-size:max(.34em,11px)}
.order .ibtn{position:absolute;right:-14px;top:-18px;width:48px;height:48px;font-size:24px;background:#ffe9a8;box-shadow:0 3px 0 #d18e0a}
.bread{width:clamp(110px,19vmin,150px);height:clamp(90px,15vmin,120px);border-radius:46% 46% 22px 22px;background:linear-gradient(#e8a24a,#d9893a);border:5px solid var(--choc);
  box-shadow:0 6px 0 rgba(0,0,0,.18),inset 0 8px 0 rgba(255,255,255,.25)}
.bread b{font-family:var(--kai);font-weight:400;font-size:clamp(56px,10vmin,80px);color:#fff;text-shadow:0 3px 0 rgba(107,63,34,.6);line-height:1}
.bread.hop{animation:hop .55s ease}
@keyframes hop{35%{transform:translateY(-60px) rotate(-8deg)}60%{transform:translateY(-30px) rotate(6deg)}}
.road{position:relative;width:min(900px,94vw);height:clamp(96px,15vmin,130px);pointer-events:none}
.road::after{content:"";position:absolute;left:0;right:0;bottom:4px;height:6px;border-radius:3px;background:repeating-linear-gradient(90deg,#c98a4b 0 26px,transparent 26px 40px);opacity:.6}
.truck{position:absolute;bottom:8px;left:50%;width:clamp(200px,34vmin,280px);transform:translateX(-50%)}
.truck svg{width:100%;height:auto;display:block}
.cargo{position:absolute;left:6%;top:12%;width:58%;height:52%;display:flex;flex-wrap:wrap-reverse;align-content:flex-start;gap:2px;padding:4px;overflow:hidden}
.cargo .ic{width:22%;height:auto;animation:bpop .3s}
.truck.go{animation:drive 2s cubic-bezier(.5,0,.6,1) forwards}
@keyframes drive{0%{transform:translateX(-50%)}15%{transform:translateX(-52%) rotate(-1deg)}100%{transform:translateX(160%)}}
.truck.bump{animation:tbump .35s}
@keyframes tbump{40%{transform:translateX(-50%) translateY(-6px)}}
.order.done{animation:yes .5s}
@media (max-height:500px){.road{height:90px;width:260px}.truck{width:170px}main.stage2{flex-wrap:wrap;align-content:center}}''',
main='''<div class="order" id="order" data-zy-skip><span class="tag" id="tag"></span><div class="sent" id="sent"></div><button type="button" class="ibtn" id="say" aria-label="念句子">🔊</button></div>
<div class="road" id="road"><div class="truck" id="truck"></div></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  const TRUCK=`<svg viewBox="0 0 220 120" aria-hidden="true"><g stroke="#3a2a22" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
  <rect x="8" y="10" width="140" height="80" rx="10" fill="#fff3e0"/><path d="M8 26h140" stroke="#e8577a" stroke-width="10"/>
  <path d="M148 40h34q12 0 18 14l10 22v14H148z" fill="#ff8fb0"/><path d="M158 48h22q6 0 9 8l6 14h-37z" fill="#bfe6ff" stroke-width="4"/>
  <rect x="200" y="78" width="12" height="10" rx="3" fill="#ffe14d" stroke-width="3"/>
  <circle cx="48" cy="96" r="15" fill="#3a2a22"/><circle cx="48" cy="96" r="6" fill="#d9dee5" stroke="none"/><circle cx="176" cy="96" r="15" fill="#3a2a22"/><circle cx="176" cy="96" r="6" fill="#d9dee5" stroke="none"/></g></svg><div class="cargo" id="cargo"></div>`;
  $("tag").innerHTML=TZ.zy("訂單");
  const api=TZ.run({key:"town-fill",
    help:"麵包店送貨。訂單上的句子少了一個字，看看注音，想一想哪一個字才對，點那個麵包。答對的麵包會裝上送貨車，全部答完，車子就會出發送貨。按喇叭可以聽句子。",
    build:n=>TZ.deal(TZ.pool(true).filter(c=>Z.sent[c]),n),
    show:(c)=>{
      const [t,o]=Z.sent[c];
      $("sent").innerHTML=TZ.zy(t);$("order").classList.remove("done");
      if(api.S.i===0){const tk=$("truck");tk.classList.remove("go","bump");tk.innerHTML=TRUCK}
      $("say").onclick=()=>TZ.say(t.replace("＿",c));
      $("choices").innerHTML=TZ.shuffle([...o]).map(x=>`<button type="button" class="choice bread" data-c="${x}" aria-label="${x}"><b>${x}</b></button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.c===c){api.ok();el.classList.add("yes");const b=$("blank"),last=api.S.i>=api.S.total-1;
          // 麵包先補進句子的空格，再裝上送貨車；全部答完，車子才開走
          TZ.fly(el,b,()=>{b.classList.add("fill");b.textContent=c;EN.sfx.pop();$("order").classList.add("done")},{dur:.7,spin:-20,keepHidden:true});
          setTimeout(()=>{const tk=$("truck");if(!tk.offsetParent)return;const m=document.createElement("span");m.innerHTML=EN.icon("bread");m.style.cssText="position:fixed;width:56px;height:56px;z-index:61;pointer-events:none";
            const r=b.getBoundingClientRect();m.style.left=r.left+"px";m.style.top=r.top+"px";document.body.appendChild(m);
            TZ.fly(m,$("cargo"),()=>{$("cargo").insertAdjacentHTML("beforeend",EN.icon("bread"));tk.classList.remove("bump");void tk.offsetWidth;tk.classList.add("bump");EN.sfx.pop()},{dur:.6,scale:.4});
            setTimeout(()=>m.remove(),1000)},900);
          setTimeout(()=>TZ.say(t.replace("＿",c),{onend:()=>{
            if(!last){api.next(300);return}
            const tk=$("truck");EN.sfx.coin();setTimeout(()=>EN.sfx.coin(),220);tk.classList.remove("bump");tk.classList.add("go");
            TZ.say("麵包全部裝好了，出發送貨囉！",{onend:()=>api.next(600)});
          }}),1500)}
        else{api.bad();el.classList.remove("hop");void el.offsetWidth;el.classList.add("hop");setTimeout(()=>el.classList.add("no"),500);
          if(api.S.tries>=2)document.querySelector(`.choice[data-c="${c}"]`).classList.add("glow")}
      });
    }});
})();''')

# ---------- 4. 冰火飲料店（相反字） ----------
page("town-anti.html",title="冰火飲料店",icon="🧋",sub="冰的配熱的，找出意思相反的字！",
style='''.cup{position:relative;width:var(--w,clamp(110px,19vmin,150px));aspect-ratio:.8;border:5px solid var(--choc);border-radius:10px 10px 34px 34px;
  background:linear-gradient(transparent 18%,var(--c) 18%);box-shadow:0 6px 0 rgba(0,0,0,.15);display:grid;place-items:center}
.cup::before{content:"";position:absolute;left:-8%;right:-8%;top:-14px;height:18px;border-radius:10px;background:#fff;border:5px solid var(--choc)}
.cup::after{content:"";position:absolute;left:58%;top:-46px;width:9px;height:44px;border-radius:5px;background:var(--berry);border:3px solid var(--choc);transform:rotate(12deg)}
.cup b{font-family:var(--kai);font-weight:400;font-size:clamp(54px,9.5vmin,80px);line-height:1;color:var(--ink);margin-top:10%}
.cup .tz-b{font-size:17px}
.cup.big{--w:clamp(150px,27vmin,220px)}.cup.big b{font-size:clamp(84px,15vmin,130px)}
.ice{position:absolute;left:12%;top:24%;font-size:26px}
.vs{display:flex;align-items:center;gap:18px}
.vs .arrow{font-size:clamp(34px,6vmin,52px);color:var(--choc);font-weight:900}
.choices{margin-top:34px}
.vs{margin-top:30px}
.cup.big{--w:clamp(150px,27vmin,220px)}
@media (max-height:740px),(max-width:420px){.cup{--w:92px}.cup.big{--w:118px}.cup b{font-size:52px}.cup.big b{font-size:76px}.vs .q{width:92px!important;font-size:36px!important}.choices{margin-top:26px}.vs{margin-top:22px}}
@media (max-height:500px){.cup{--w:84px}.cup.big{--w:104px}.cup.big b{font-size:64px}.cup b{font-size:46px}.vs{margin-top:30px}.choices{margin-top:30px}.vs .arrow{font-size:28px}}
.vs .q{width:clamp(110px,19vmin,150px);aspect-ratio:.8;border:5px dashed var(--berry);border-radius:10px 10px 34px 34px;display:grid;place-items:center;font-size:48px;color:var(--berry);background:#fff}''',
main='''<div class="qcard"><div class="qline" id="q"></div><div class="vs"><div class="cup big" id="pcup" style="--c:#bfe6ff"><span class="ice">🧊</span><b id="ch"></b></div><span class="arrow">⇄</span><div class="q" id="slot">？</div></div></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffc27a","#ffb3c7","#c9f2d8","#fff1a8"];
  // 題目：範圍裡的字，有相反字的才出
  function questions(n){
    const pool=new Set(TZ.pool(true)),items=[];
    Z.anti.forEach(([a,b])=>{if(pool.has(a))items.push([a,b]);if(pool.has(b))items.push([b,a])});
    return TZ.deal(items,n);
  }
  const api=TZ.run({key:"town-anti",
    help:"冰火飲料店。左邊的冰飲料上有一個字，請你找出意思和它相反的字，例如大和小、上和下。點那一杯飲料。",
    empty:"這個範圍沒有足夠的相反字題目，請多選幾課。",
    build:questions,
    show:([q,a])=>{
      const learned=TZ.learned(),zyIf=c=>learned.has(c)?"":(Z.ZY[c]||"");
      $("ch").innerHTML=TZ.charHTML(q,zyIf(q));$("slot").textContent="？";$("slot").style.cssText="";
      $("q").innerHTML=TZ.zy("和「")+`<b class="kai" style="font-size:1.3em">${q}</b>`+TZ.zy("」意思相反的是哪一個字？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
      $("say").onclick=()=>TZ.say(`和${q}，意思相反的是哪一個字？`);
      // 干擾選項：學過的字，但不能是其他相反字組裡和題目相反的字
      const bad=new Set([q,a]);Z.anti.forEach(([x,y])=>{if(x===q)bad.add(y);if(y===q)bad.add(x)});
      const pool=TZ.shuffle([...TZ.learned()].filter(c=>!bad.has(c)&&Z.ZY[c]));
      const opts=TZ.shuffle([a,pool[0],pool[1]]);
      $("choices").innerHTML=opts.map((c,i)=>`<button type="button" class="choice cup" style="--c:${COL[i]}" data-c="${c}" aria-label="${c}"><b>${c}</b></button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.c===a){api.ok();el.classList.add("yes");const s=$("slot");s.style.cssText="border-style:solid;border-color:#1f9d61;background:#eafff2;color:#2b2320;font-family:var(--kai);font-size:clamp(54px,9.5vmin,80px)";s.textContent=a;
          TZ.say(`答對了！${q}的相反是${a}。`,{onend:()=>api.next(400)})}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${a}"]`).classList.add("glow")}
      });
      setTimeout(()=>TZ.say(`和${q}，意思相反的是哪一個字？`),300);
    }});
})();''')

# ---------- 5. 挑壞蘋果（找錯字、形近字） ----------
page("town-wrong.html",title="挑壞蘋果",icon="🍎",sub="句子裡有一個寫錯的字，把壞蘋果挑出來！",
style=""".basket{background:#fff;border:5px solid var(--choc);border-radius:24px;padding:clamp(12px,2.6vmin,22px) clamp(12px,2.6vmin,24px);box-shadow:0 8px 0 rgba(0,0,0,.12);max-width:min(940px,96vw);position:relative}
.basket .ibtn{position:absolute;right:-14px;top:-18px;width:48px;height:48px;font-size:24px;background:#ffe9a8;box-shadow:0 3px 0 #d18e0a}
.sent2{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:6px 6px;font-family:var(--kai);font-size:clamp(28px,5.2vmin,48px)}
.ap{position:relative;display:inline-flex;align-items:center;border:0;background:#fff3f3;border-radius:18px;padding:6px 16px 6px 8px;cursor:pointer;font:inherit;color:var(--ink);min-width:44px;min-height:56px;box-shadow:inset 0 0 0 2px #ffd6d6}
.ap .tz-b{font-size:max(.38em,14px);margin-left:.12em}
.ap .tz-b .zy-t{font-size:1.15em;left:100%;top:-.55em}
.ap.bad{animation:wig .4s}
.ap.rot{background:#c9a27a;box-shadow:inset 0 0 0 3px #8a5a36}
.ap.rot::after{content:"🐛";position:absolute;right:-12px;top:-16px;font-size:24px}
.ap.fixed{background:#eafff2;box-shadow:inset 0 0 0 3px var(--good)}
.ap.fixed::after{content:none}
.ap.glow{animation:glow 1s infinite}
.sent2 .tp{font-size:.9em}
.step{font-size:clamp(18px,3vmin,24px);font-weight:800;color:var(--choc)}
.apple{width:clamp(92px,16vmin,128px);aspect-ratio:1;border-radius:46% 46% 50% 50%;background:radial-gradient(circle at 35% 30%,#ff8a8a,#e8302a 70%);border:5px solid #8a2a20;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.apple::before{content:"";position:absolute;top:-16px;left:50%;width:6px;height:18px;background:#6b3f22;border-radius:3px}
.apple::after{content:"";position:absolute;top:-14px;left:56%;width:22px;height:12px;background:#5cc24a;border-radius:0 12px 0 12px;border:2px solid #2e7d32}
.apple b{font-family:var(--kai);font-weight:400;font-size:clamp(50px,9vmin,72px);color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.25)}
@media (max-height:500px){.sent2{font-size:26px}main.stage2{flex-direction:column;gap:8px}}""",
main="""<div class="basket" id="basket"><div class="sent2" id="sent"></div><button type="button" class="ibtn" id="say" aria-label="念句子">🔊</button></div>
<div class="step" id="step"></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  const api=TZ.run({key:"town-wrong",
    help:"挑壞蘋果。句子裡有一個字寫錯了，注音是對的，看注音想一想，哪一個字不對，先點那個壞蘋果。找到以後，再從下面的蘋果裡選出正確的字。",
    build:n=>TZ.deal(TZ.pool(true).filter(c=>Z.sent[c]&&Z.wrong[c]),n),
    show:(c)=>{
      const [t]=Z.sent[c],w=Z.wrong[c];let step=1;
      // 句子：空格換成錯字，注音標正確的讀音
      const cs=[...t],items=[];
      for(let i=0;i<cs.length;i++){const ch=cs[i];let z=null;
        if(cs[i+1]==="["){const j=cs.indexOf("]",i);z=cs.slice(i+2,j).join("");i=j}
        if(ch==="＿")items.push({show:w,zy:Z.ZY[c],bad:true});
        else if(/[\\u4e00-\\u9fff]/.test(ch))items.push({show:ch,zy:z||Z.ZY[ch]||""});
        else items.push({p:ch})}
      $("sent").innerHTML=items.map((x,i)=>x.p?`<span class="tp">${x.p}</span>`:`<button type="button" class="ap" data-i="${i}">${TZ.charHTML(x.show,x.zy)}</button>`).join("");
      $("say").onclick=()=>TZ.say(t.replace("＿",c));
      $("step").innerHTML=TZ.zy("哪一個字寫錯了？點一下壞蘋果。");$("choices").innerHTML="";
      const badIdx=items.findIndex(x=>x.bad),badBtn=document.querySelector(`.ap[data-i="${badIdx}"]`);
      document.querySelectorAll(".ap").forEach(b=>b.onclick=()=>{
        if(api.S.busy||step!==1)return;
        if(+b.dataset.i===badIdx){EN.sfx.pop();b.classList.add("rot");step=2;showFix()}
        else{api.bad();b.classList.remove("bad");void b.offsetWidth;b.classList.add("bad");if(api.S.tries>=2)badBtn.classList.add("glow")}
      });
      function showFix(){
        badBtn.classList.remove("glow");
        $("step").innerHTML=TZ.zy("換成哪一個字才對？");
        const others=Object.values(Z.wrong).concat(TZ.pool(true)).filter(x=>x!==c&&x!==w&&Z.ZY[x]);
        const opts=TZ.shuffle([c,w,TZ.shuffle(others)[0]]);
        $("choices").innerHTML=opts.map(x=>`<button type="button" class="choice apple" data-c="${x}" aria-label="${x}"><b>${x}</b></button>`).join("");
        document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
          if(api.S.busy)return;
          if(el.dataset.c===c){api.ok();el.classList.add("yes");badBtn.classList.remove("rot");badBtn.classList.add("fixed");badBtn.innerHTML=TZ.charHTML(c,Z.ZY[c]);
            TZ.say(`答對了！要寫${c}。`+TZ.plain(t.replace("＿",c)),{onend:()=>api.next(400)})}
          else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${c}"]`).classList.add("glow")}
        });
      }
    }});
})();""")

# ---------- 6. 市場秤一秤（量詞） ----------
page("town-mw.html",title="市場秤一秤",icon="⚖️",sub="一隻小狗、一條魚，選出對的量詞！",
style=""".scale{position:relative;width:clamp(200px,36vmin,300px);display:flex;flex-direction:column;align-items:center}
.plate{width:100%;height:clamp(110px,20vmin,170px);border-radius:0 0 50% 50%/0 0 40% 40%;background:linear-gradient(#e6f3ff,#b9d7ff);border:5px solid var(--choc);display:grid;place-items:center;position:relative;z-index:1}
.plate .ic{width:clamp(90px,16vmin,140px);height:clamp(90px,16vmin,140px);margin-top:-40px}
.pole{width:18px;height:clamp(30px,6vmin,50px);background:#c98a4b;border:4px solid var(--choc);border-top:0}
.base{width:70%;height:22px;border-radius:12px;background:#c98a4b;border:4px solid var(--choc)}
.phrase{font-size:clamp(34px,6.4vmin,58px);font-weight:800}
.phrase .blank{width:1.2em;height:1.2em}
.tagp{min-width:clamp(96px,16vmin,128px);height:clamp(78px,13vmin,100px);border-radius:14px 34px 34px 14px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16)}
.tagp::before{content:"";position:absolute;left:12px;top:50%;width:14px;height:14px;border-radius:50%;background:#fff;border:3px solid var(--choc);transform:translateY(-50%)}
.tagp b{font-family:var(--kai);font-weight:400;font-size:clamp(44px,8vmin,64px);padding-left:20px}
.tagp .tz-b{font-size:16px}
@media (max-height:500px){.plate{height:100px}.plate .ic{width:84px;height:84px}.pole{height:24px}.phrase{font-size:30px}}""",
main="""<div class="qcard"><div class="scale"><div class="plate" id="plate"></div><div class="pole"></div><div class="base"></div></div><div class="phrase" id="phrase"></div></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffe08a","#ffb3c7","#a8e6cf","#b9d7ff"];
  const api=TZ.run({key:"town-mw",noRange:true,
    help:"市場秤一秤。看秤子上的東西，想一想要用哪一個量詞，例如一隻小狗、一條魚、一輛汽車。點對的價格牌。",
    build:n=>TZ.deal(Z.mw,n),
    show:([noun,m,ic])=>{
      $("plate").innerHTML=EN.icon(ic);
      $("phrase").innerHTML=TZ.zy("一＿"+noun);
      const others=TZ.shuffle([...Z.mwPool].filter(x=>x!==m));
      const opts=TZ.shuffle([m,others[0],others[1]]);
      $("choices").innerHTML=opts.map((x,i)=>`<button type="button" class="choice tagp" style="--c:${COL[i]}" data-c="${x}" aria-label="${x}"><b>${TZ.charHTML(x,Z.ZY[x])}</b></button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.c===m){api.ok();el.classList.add("yes");const b=$("blank");b.classList.add("fill");b.innerHTML=TZ.charHTML(m,Z.ZY[m]);
          TZ.say(`答對了！一${m}${TZ.plain(noun)}。`,{onend:()=>api.next(400)})}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${m}"]`).classList.add("glow")}
      });
      setTimeout(()=>TZ.say("一什麼"+TZ.plain(noun)+"？"),300);
    }});
})();""")

# ---------- 7. 串糖葫蘆（句子重組） ----------
page("town-order.html",title="串糖葫蘆",icon="🍡",sub="把詞語一顆一顆串起來，變成一句話！",
style=""".stickbox{position:relative;width:min(960px,96vw);display:flex;align-items:center;justify-content:center;padding:12px 0}
.stickbox::before{content:"";position:absolute;left:2%;right:2%;top:50%;height:10px;margin-top:-5px;border-radius:5px;background:#e8b06a;border:3px solid var(--choc)}
.slots{position:relative;display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.slot{min-width:clamp(90px,15vmin,120px);min-height:clamp(70px,11vmin,88px);border-radius:999px;border:4px dashed rgba(107,63,34,.45);background:rgba(255,255,255,.7);display:grid;place-items:center;padding:0;cursor:pointer}
.slot.next{border-color:#fff;background:rgba(255,255,255,.95);animation:blink 1.1s infinite}
@keyframes blink{50%{background:rgba(255,255,255,.4)}}
.ball{min-height:clamp(70px,11vmin,88px);padding:4px 18px;border-radius:999px;background:radial-gradient(circle at 30% 30%,#ff8a8a,#e8302a 70%);border:4px solid #8a2a20;
  box-shadow:0 6px 0 rgba(0,0,0,.18),inset 0 -6px 0 rgba(0,0,0,.12);font-family:var(--kai);font-size:clamp(30px,5.4vmin,46px);color:#fff;display:inline-flex!important;flex-direction:row;align-items:center;white-space:nowrap}
.ball .tz-b{color:#fff}
.ball.used{visibility:hidden}
.slot .ball{box-shadow:inset 0 -6px 0 rgba(0,0,0,.12)}
.slot .ball.ok{background:radial-gradient(circle at 30% 30%,#7fe0a8,#1f9d61 70%);border-color:#136b41}
.ball.bad{animation:wig .4s}
@media (max-height:500px){.ball{font-size:26px;min-height:58px;padding:2px 12px}.slot{min-height:58px;min-width:72px}main.stage2{flex-direction:column;gap:10px}}""",
main="""<div class="qline" id="q"></div>
<div class="stickbox"><div class="slots" id="slots"></div></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  $("q").innerHTML=TZ.zy("把糖葫蘆照順序串起來，變成一句話。")+`<button type="button" class="ibtn" id="say" aria-label="念句子">🔊</button>`;
  let cur="";$("say").onclick=()=>{if(cur)TZ.say(cur.split("/").join(""))};
  const api=TZ.run({key:"town-order",
    help:"串糖葫蘆。下面有幾顆糖葫蘆，每一顆上面是一個詞語。照句子的順序一顆一顆點，把它們串到竹籤上。串錯的會掉下來，再試一次。學過的字沒有注音，沒學過的字有注音。",
    empty:"這個範圍沒有句子，請多選幾課。",
    build:n=>{const [a,b]=TZ.range();return TZ.deal(Z.order[TZ.ver()].slice(a,b+1).flat(),n)},
    show:(t)=>{
      cur=t;const parts=t.split("/"),learned=TZ.learned();
      let order;do{order=TZ.shuffle(parts.map((_,i)=>i))}while(order.every((v,i)=>v===i)&&parts.length>1);
      $("slots").innerHTML=parts.map((_,k)=>`<button type="button" class="slot" data-k="${k}" aria-label="第${k+1}顆"></button>`).join("");
      $("choices").innerHTML=order.map(i=>`<button type="button" class="choice ball" data-i="${i}">${TZ.zy(parts[i],{skip:learned})}</button>`).join("");
      const slots=[...document.querySelectorAll(".slot")],balls=[...document.querySelectorAll("#choices .ball")];
      const mark=()=>{const n=slots.find(s=>!s.firstChild);slots.forEach(s=>s.classList.toggle("next",s===n))};mark();
      balls.forEach(b=>b.onclick=()=>{
        if(api.S.busy||b.classList.contains("used"))return;const s=slots.find(x=>!x.firstChild);if(!s)return;
        EN.sfx.pop();const c=b.cloneNode(true);c.classList.remove("choice");c.onclick=null;s.appendChild(c);b.classList.add("used");mark();
        if(slots.every(x=>x.firstChild))setTimeout(check,350);
      });
      slots.forEach(s=>s.onclick=()=>{if(api.S.busy||!s.firstChild||s.firstChild.classList.contains("ok"))return;
        balls.find(b=>b.dataset.i===s.firstChild.dataset.i).classList.remove("used");s.innerHTML="";mark()});
      function check(){
        let all=true;slots.forEach(s=>{const k=+s.dataset.k,b=s.firstChild;if(+b.dataset.i===k)b.classList.add("ok");else all=false});
        if(all){api.ok();TZ.say(t.split("/").join(""),{onend:()=>api.next(500)});return}
        api.bad();api.S.busy=true;
        slots.forEach(s=>{const b=s.firstChild;if(b&&!b.classList.contains("ok"))b.classList.add("bad")});
        setTimeout(()=>{slots.forEach(s=>{const b=s.firstChild;if(b&&!b.classList.contains("ok")){balls.find(x=>x.dataset.i===b.dataset.i).classList.remove("used");s.innerHTML=""}});
          api.S.busy=false;mark()},550);
      }
    }});
})();""")

# ---------- 8. 音樂甜筒（選注音、聲調） ----------
page("town-tone.html",title="音樂甜筒",icon="🍦",sub="選出對的注音，聽聽看是第幾聲！",
style=""".cone{position:relative;display:flex;flex-direction:column;align-items:center}
.scoop{width:clamp(150px,27vmin,220px);aspect-ratio:1.1;border-radius:50% 50% 44% 44%;background:radial-gradient(circle at 35% 30%,#fff,#ffc2dc 60%,#ff9fc4);border:6px solid var(--choc);
  display:grid;place-items:center;box-shadow:inset 0 -10px 0 rgba(0,0,0,.06);position:relative;z-index:1}
.scoop .bigc{font-family:var(--kai);font-size:clamp(84px,16vmin,130px);line-height:1;color:var(--ink);display:inline-flex;align-items:center}
.scoop .bigc .tz-b{font-size:max(.3em,16px)}
.waffle{width:0;height:0;border-left:clamp(56px,10vmin,80px) solid transparent;border-right:clamp(56px,10vmin,80px) solid transparent;border-top:clamp(80px,14vmin,120px) solid #e8b06a;margin-top:-14px;filter:drop-shadow(0 6px 0 rgba(0,0,0,.12))}
.notes{position:absolute;right:-30px;top:-10px;font-size:30px;animation:nt 2s ease-in-out infinite}
@keyframes nt{50%{transform:translateY(-8px) rotate(10deg)}}
.zyopt{min-width:clamp(84px,14vmin,110px);min-height:clamp(110px,19vmin,150px);border-radius:999px 999px 26px 26px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16);padding:8px 14px}
.zyopt .tz-b{font-size:clamp(28px,5vmin,40px);color:var(--ink);line-height:1.05}
.tonebtn{min-width:clamp(84px,14vmin,110px);height:clamp(84px,14vmin,104px);border-radius:24px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.tonebtn .mk{font-size:clamp(36px,6vmin,50px);line-height:.9;font-weight:900;color:var(--choc);min-height:.9em}
.tonebtn .lb{font-size:18px;font-weight:800}
@media (max-height:500px){.waffle{border-top-width:60px;border-left-width:46px;border-right-width:46px}.scoop{width:130px}.scoop .bigc{font-size:76px}.zyopt{min-height:92px}.zyopt .tz-b{font-size:24px}}""",
main="""<div class="qcard"><div class="qline" id="q"></div><div class="cone"><div class="scoop" id="scoop"><span class="bigc" id="big"></span></div><div class="waffle"></div><span class="notes">🎵</span></div></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffe08a","#a8e6cf","#b9d7ff","#ffc2dc","#d7b4ff"];
  const TONES=["ˊ","ˇ","ˋ"],noT=z=>z.replace(/[ˊˇˋ˙]/g,"");
  const toneOf=z=>z[0]==="˙"?0:z.includes("ˊ")?2:z.includes("ˇ")?3:z.includes("ˋ")?4:1;
  const withTone=(base,t)=>t===0?"˙"+base:t===1?base:base+TONES[t-2];
  // 容易混的注音：ㄓㄗ、ㄔㄘ、ㄕㄙ、ㄣㄥ、ㄢㄤ……
  const SW={ㄓ:"ㄗ",ㄗ:"ㄓ",ㄔ:"ㄘ",ㄘ:"ㄔ",ㄕ:"ㄙ",ㄙ:"ㄕ",ㄣ:"ㄥ",ㄥ:"ㄣ",ㄢ:"ㄤ",ㄤ:"ㄢ",ㄈ:"ㄏ",ㄏ:"ㄈ",ㄋ:"ㄌ",ㄌ:"ㄋ",ㄅ:"ㄆ",ㄆ:"ㄅ",ㄉ:"ㄊ",ㄊ:"ㄉ",ㄍ:"ㄎ",ㄎ:"ㄍ",ㄛ:"ㄡ",ㄡ:"ㄛ",ㄧ:"ㄩ",ㄩ:"ㄧ",ㄜ:"ㄝ",ㄝ:"ㄜ"};
  function fakes(z){
    const base=noT(z),t=toneOf(z),out=new Set();
    [1,2,3,4].filter(x=>x!==t).forEach(x=>out.add(withTone(base,x)));
    [...base].forEach((ch,i)=>{if(SW[ch]){const b=[...base];b[i]=SW[ch];out.add(withTone(b.join(""),t))}});
    out.delete(z);return TZ.shuffle([...out]);
  }
  const zyHTML=z=>{const light=z[0]==="˙",syms=[...(light?z.slice(1):z)],tone=/[ˊˇˋ]/.test(syms[syms.length-1])?syms.pop():"";
    return `<span class="tz-b">${light?'<span class="zy-lt">˙</span>':""}${syms.map((s,k)=>`<span>${s}${k===syms.length-1&&tone?`<span class="zy-t">${tone}</span>`:""}</span>`).join("")}</span>`};
  const api=TZ.run({key:"town-tone",
    help:"音樂甜筒。有兩種題目。第一種，看甜筒上的字，選出它正確的注音。第二種，字的注音沒有聲調，請你念念看，想一想它是第幾聲，點一聲、二聲、三聲、四聲或輕聲。",
    build:n=>TZ.deal(TZ.pool(true).filter(c=>Z.ZY[c]&&!Z.poly.includes(c)),n).map((c,i)=>({c,type:i%2?"tone":"pick"})),
    show:({c,type})=>{
      const z=Z.ZY[c];
      if(type==="pick"){
        $("big").textContent=c;
        $("q").innerHTML=TZ.zy("這個字的注音是哪一個？")+`<button type="button" class="ibtn" id="say" aria-label="念這個字">🔊</button>`;
        $("say").onclick=()=>TZ.say(c);
        const opts=TZ.shuffle([z,...fakes(z).slice(0,2)]);
        $("choices").innerHTML=opts.map((x,i)=>`<button type="button" class="choice zyopt" style="--c:${COL[i]}" data-z="${x}" aria-label="注音選項${i+1}">${zyHTML(x)}</button>`).join("");
        document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
          if(api.S.busy)return;
          if(el.dataset.z===z){api.ok();el.classList.add("yes");$("big").innerHTML=TZ.charHTML(c,z);TZ.say(`答對了！${c}。`,{onend:()=>api.next(400)})}
          else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-z="${z}"]`).classList.add("glow")}
        });
      }else{
        const t=toneOf(z);
        $("big").innerHTML=TZ.charHTML(c,noT(z));
        $("q").innerHTML=TZ.zy("念念看，這個字是第幾聲？")+`<button type="button" class="ibtn" id="say" aria-label="念這個字">🔊</button>`;
        $("say").onclick=()=>TZ.say(c);
        const L=[[1,"ˉ","一聲"],[2,"ˊ","二聲"],[3,"ˇ","三聲"],[4,"ˋ","四聲"]];if(t===0)L.push([0,"˙","輕聲"]);
        $("choices").innerHTML=L.map(([v,mk,lb],i)=>`<button type="button" class="choice tonebtn" style="--c:${COL[i]}" data-t="${v}" aria-label="${lb}"><span class="mk">${mk}</span><span class="lb">${TZ.zy(lb)}</span></button>`).join("");
        document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
          if(api.S.busy)return;
          if(+el.dataset.t===t){api.ok();el.classList.add("yes");$("big").innerHTML=TZ.charHTML(c,z);TZ.say(`答對了！${c}是${["輕聲","一聲","二聲","三聲","四聲"][t]}。`,{onend:()=>api.next(400)})}
          else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-t="${t}"]`).classList.add("glow")}
        });
        setTimeout(()=>TZ.say(c),300);
      }
    }});
})();""")

# ---------- 9. 擺餐桌（看圖擺位置） ----------
page("town-place.html",title="擺餐桌",icon="🍽️",sub="照著這段話，把東西放到桌子的上面、下面、左邊、右邊！",
style=""".lines{background:#fff;border:5px solid var(--choc);border-radius:20px;padding:8px 18px;box-shadow:0 6px 0 rgba(0,0,0,.1);display:flex;flex-direction:column;gap:2px;max-width:96vw}
.ln{font-size:clamp(20px,3.4vmin,28px);font-weight:800;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.ln.done{color:var(--good)}
.ln .ck{width:28px;text-align:center}
.stage3{position:relative;width:var(--sw,600px);aspect-ratio:4/3;max-width:96vw;border-radius:22px;background:linear-gradient(#fff3e0 0 70%,#e8c38a 70%);border:5px solid var(--choc);overflow:hidden;touch-action:none}
.stage3>svg{position:absolute;inset:0;width:100%;height:100%}
.zone{position:absolute;border:4px dashed transparent;border-radius:16px;pointer-events:none}
.zone.hot{border-color:#ff8fb0;background:rgba(255,143,176,.15)}
.zone.hint{border-color:#ffd23f;background:rgba(255,226,120,.3);animation:glow 1s infinite}
.thing{position:absolute;width:17%;aspect-ratio:1;transform:translate(-50%,-100%);pointer-events:none}
.thing .ic{width:100%;height:100%}
.tray{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;min-height:96px}
.item{width:clamp(78px,13vmin,104px);aspect-ratio:1;border-radius:20px;background:#fff;border:4px solid var(--choc);box-shadow:0 5px 0 rgba(0,0,0,.14);cursor:grab;touch-action:none;padding:6px;display:grid;place-items:center}
.item .ic{width:100%;height:100%}
.item.used{visibility:hidden}
.item.float{position:fixed;z-index:40;cursor:grabbing;box-shadow:0 14px 20px rgba(0,0,0,.25);pointer-events:none}
.item.back{animation:wig .4s}
@media (max-height:500px){main.stage2{display:grid;grid-template-columns:auto auto;align-content:center;justify-content:center;gap:8px 16px}.lines{grid-column:1;grid-row:1}.tray{grid-column:1;grid-row:2;min-height:0}.stage3{grid-column:2;grid-row:1/3}.ln{font-size:16px}.item{width:62px}}""",
main="""<div class="lines" id="lines"></div>
<div class="stage3" id="stage"><svg viewBox="0 0 400 300" aria-hidden="true"><g stroke="#6b3f22" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
  <rect x="120" y="150" width="160" height="18" rx="6" fill="#c98a4b"/><path d="M110 150h180" stroke-width="7"/><path d="M135 168v74M265 168v74" stroke-width="10"/>
  <path d="M112 150q88 22 176 0" fill="#ffb3c7" stroke-width="3" opacity=".9"/></g>
  <g fill="#fff" opacity=".7"><circle cx="40" cy="40" r="10"/><circle cx="60" cy="36" r="14"/><circle cx="80" cy="42" r="9"/><circle cx="330" cy="50" r="12"/><circle cx="350" cy="46" r="15"/></g></svg>
  <div class="zone" data-p="上面" style="left:28%;top:8%;width:44%;height:42%"></div><div class="zone" data-p="下面" style="left:35%;top:57%;width:30%;height:26%"></div>
  <div class="zone" data-p="左邊" style="left:2%;top:30%;width:25%;height:56%"></div><div class="zone" data-p="右邊" style="left:73%;top:30%;width:25%;height:56%"></div></div>
<div class="tray" id="tray"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI,POS=["上面","下面","左邊","右邊"];
  // 放好的位置（東西底部的中間，% ）
  const ANCHOR={上面:[50,49],下面:[50,80],左邊:[15,80],右邊:[85,80]};
  function fit(){const m=$("main").getBoundingClientRect(),land=innerHeight<=500;
    const w=land?Math.min(innerWidth*.46,(innerHeight-100)*4/3):Math.min(innerWidth-32,(m.height-($("lines").offsetHeight+130))*4/3,720);
    document.documentElement.style.setProperty("--sw",Math.max(240,w)+"px")}
  addEventListener("resize",fit);
  const api=TZ.run({key:"town-place",noRange:true,
    help:"擺餐桌。上面的一段話說了東西要放在哪裡，例如桌子上面、桌子下面、桌子左邊、桌子右邊。請你看看注音，把下面的東西一個一個拖到對的位置。",
    build:n=>[...Array(n)].map(()=>{const ps=TZ.shuffle(POS.slice()).slice(0,3),its=TZ.shuffle(Z.place.slice()).slice(0,3);return ps.map((p,i)=>({p,it:its[i]}))}),
    show:(round)=>{
      document.querySelectorAll(".thing").forEach(e=>e.remove());
      const text=x=>`桌子[˙ㄗ]${x.p}有一${x.it[1]}${x.it[0]}。`;
      $("lines").innerHTML=round.map((x,i)=>`<div class="ln" data-i="${i}"><span class="ck">🍽️</span>${TZ.zy(text(x))}</div>`).join("");
      $("tray").innerHTML=TZ.shuffle(round.map((x,i)=>i)).map(i=>`<div class="item" data-i="${i}" role="button" aria-label="${TZ.plain(round[i].it[0])}">${EN.icon(round[i].it[2])}</div>`).join("");
      fit();let left=round.length;
      setTimeout(()=>TZ.say(round.map(x=>TZ.plain(text(x))).join("")),300);
      document.querySelectorAll(".item").forEach(el=>{
        let fl=null,ox=0,oy=0;
        el.addEventListener("pointerdown",e=>{if(api.S.busy||el.classList.contains("used"))return;e.preventDefault();try{el.setPointerCapture(e.pointerId)}catch(err){}
          const r=el.getBoundingClientRect();ox=e.clientX-r.left;oy=e.clientY-r.top;fl=el.cloneNode(true);fl.classList.add("float");fl.style.width=r.width+"px";fl.style.left=r.left+"px";fl.style.top=r.top+"px";
          document.body.appendChild(fl);el.classList.add("used");EN.sfx.pop();TZ.say(TZ.plain(round[+el.dataset.i].it[0]))});
        el.addEventListener("pointermove",e=>{if(!fl)return;fl.style.left=(e.clientX-ox)+"px";fl.style.top=(e.clientY-oy)+"px";const z=zoneAt(e.clientX,e.clientY);document.querySelectorAll(".zone").forEach(x=>x.classList.toggle("hot",x===z))});
        const up=e=>{if(!fl)return;const z=e&&zoneAt(e.clientX,e.clientY);fl.remove();fl=null;document.querySelectorAll(".zone").forEach(x=>x.classList.remove("hot"));
          const i=+el.dataset.i,x=round[i];
          if(z&&z.dataset.p===x.p){
            const [ax,ay]=ANCHOR[x.p],t=document.createElement("div");t.className="thing";t.style.left=ax+"%";t.style.top=ay+"%";t.innerHTML=EN.icon(x.it[2]);$("stage").appendChild(t);
            const ln=document.querySelector(`.ln[data-i="${i}"]`);ln.classList.add("done");ln.querySelector(".ck").textContent="✅";EN.sfx.good();
            document.querySelectorAll(".zone").forEach(q=>q.classList.remove("hint"));
            left--;if(left===0){api.ok();TZ.say("全部擺好了！",{onend:()=>api.next(600)})}else TZ.say(TZ.plain(text(x)));
          }else{el.classList.remove("used");if(z){api.bad();el.classList.remove("back");void el.offsetWidth;el.classList.add("back");
            if(api.S.tries>=2)document.querySelector(`.zone[data-p="${x.p}"]`).classList.add("hint");TZ.say(TZ.plain(text(x)))}}};
        el.addEventListener("pointerup",up);el.addEventListener("pointercancel",()=>up(null));
      });
    }});
  function zoneAt(x,y){return [...document.querySelectorAll(".zone")].find(z=>{const r=z.getBoundingClientRect();return x>=r.left&&x<=r.right&&y>=r.top&&y<=r.bottom})}
})();""")

# ---------- 10. 蛋糕寫字（看注音寫國字） ----------
page("town-write.html",title="蛋糕寫字",icon="🎂",sub="看注音，在蛋糕上寫出國字！",
style=""".word{display:flex;align-items:center;gap:6px;font-family:var(--kai);font-size:clamp(46px,8vmin,72px);background:#fff;border:5px solid var(--choc);border-radius:22px;padding:6px 20px;box-shadow:0 6px 0 rgba(0,0,0,.1);position:relative}
.word .tz-b{font-size:max(.3em,14px)}
.zbox{display:inline-grid;place-items:center;min-width:1.1em;min-height:1.25em;border:4px dashed var(--berry);border-radius:14px;padding:2px 6px;background:#fff5f8}
.zbox .tz-b{font-size:clamp(22px,3.8vmin,32px)!important;color:var(--berry)}
.word .ibtn{position:absolute;right:-16px;top:-18px;width:46px;height:46px;font-size:22px;background:#ffe9a8;box-shadow:0 3px 0 #d18e0a}
.cakebox{position:relative;padding:14px;border-radius:30px;background:#ffd1e3;border:5px solid var(--choc);box-shadow:0 8px 0 #c98a4b,0 14px 20px rgba(0,0,0,.12)}
.cakebox::before{content:"";position:absolute;left:-5px;right:-5px;top:-5px;height:26px;border-radius:30px 30px 0 0;background:radial-gradient(circle at 18px 26px,#fff 0 14px,transparent 15px) 0 0/36px 26px repeat-x}
.cakebox canvas{display:block;border-radius:16px;background:#fffdf6;touch-action:none}
.adult{position:absolute;right:20px;bottom:20px;width:40px;height:40px;border-radius:12px;border:2px solid #d8c9ae;background:#fff;color:#9a8a70;font-size:20px;cursor:pointer;opacity:.75}
.wbar{display:flex;gap:14px;align-items:center}
.wbar .big{min-height:56px}
.tip{font-weight:800;color:var(--choc);font-size:clamp(17px,2.8vmin,22px);min-height:1.4em}
@media (max-height:500px){main.stage2{flex-direction:row;gap:16px}.side{display:flex;flex-direction:column;gap:10px;align-items:center}.word{font-size:36px;padding:4px 14px}.wbar{flex-direction:column}.tip{font-size:15px;max-width:150px;text-align:center}}
.side{display:contents}
@media (max-height:500px){.side{display:flex}}""",
main="""<div class="side"><div class="word" id="word"></div><div class="tip" id="tip"></div></div>
<div class="cakebox"><canvas id="cv"></canvas><button type="button" class="adult" id="adult" aria-label="大人幫忙算對">✓</button></div>
<div class="side"><div class="wbar"><button type="button" class="big alt ico-btn" id="clr" aria-label="擦掉">🧹</button><button type="button" class="big ok" id="ok">OK</button></div></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  // ---- 手寫比對：孩子寫的和每個字的標準楷書都縮成一樣大、瘦成一條條骨架，量兩邊骨架的距離；
  //      正確的字要排在最像的前 12 名（和所有生字、易混字比），而且距離不能太遠 ----
  const N=64;
  function bm(src){const w=src.width,h=src.height,d=src.getContext("2d").getImageData(0,0,w,h).data;let x0=w,x1=-1,y0=h,y1=-1;
    for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(d[(y*w+x)*4+3]>100){if(x<x0)x0=x;if(x>x1)x1=x;if(y<y0)y0=y;if(y>y1)y1=y}
    if(x1<0)return null;const c=document.createElement("canvas");c.width=c.height=N;const g=c.getContext("2d");const bw=x1-x0+1,bh=y1-y0+1,s=(N-8)/Math.max(bw,bh);
    g.drawImage(src,x0,y0,bw,bh,(N-bw*s)/2,(N-bh*s)/2,bw*s,bh*s);const e=g.getImageData(0,0,N,N).data,b=new Uint8Array(N*N);for(let i=0;i<N*N;i++)b[i]=e[i*4+3]>90?1:0;return b}
  function thin(b){b=b.slice();let ch=true;const at=(x,y)=>x<0||y<0||x>=N||y>=N?0:b[y*N+x];
    while(ch){ch=false;for(const step of [0,1]){const del=[];for(let y=0;y<N;y++)for(let x=0;x<N;x++){if(!b[y*N+x])continue;
      const p=[at(x,y-1),at(x+1,y-1),at(x+1,y),at(x+1,y+1),at(x,y+1),at(x-1,y+1),at(x-1,y),at(x-1,y-1)],B=p.reduce((a,c)=>a+c,0);if(B<2||B>6)continue;
      let A=0;for(let k=0;k<8;k++)if(!p[k]&&p[(k+1)%8])A++;if(A!==1)continue;
      if(step===0?(p[0]*p[2]*p[4]===0&&p[2]*p[4]*p[6]===0):(p[0]*p[2]*p[6]===0&&p[0]*p[4]*p[6]===0))del.push(y*N+x)}if(del.length){ch=true;del.forEach(i=>b[i]=0)}}}return b}
  function dt(b){const d=new Float32Array(N*N).fill(1e9),q=[];for(let i=0;i<N*N;i++)if(b[i]){d[i]=0;q.push(i)}
    for(let h=0;h<q.length;h++){const i=q[h],x=i%N,y=(i/N)|0;for(const [dx,dy] of [[1,0],[-1,0],[0,1],[0,-1]]){const X=x+dx,Y=y+dy;if(X<0||Y<0||X>=N||Y>=N)continue;const j=Y*N+X;if(d[j]>d[i]+1){d[j]=d[i]+1;q.push(j)}}}return d}
  const pts=b=>{const p=[];for(let i=0;i<N*N;i++)if(b[i])p.push(i);return p};
  const GL={};
  function glyph(ch){if(GL[ch])return GL[ch];const c=document.createElement("canvas");c.width=c.height=220;const g=c.getContext("2d");
    g.fillStyle="#000";g.font='180px "TWKaiSub"';g.textAlign="center";g.textBaseline="middle";g.fillText(ch,110,118);const b=thin(bm(c)||new Uint8Array(N*N));return GL[ch]={p:pts(b),d:dt(b)}}
  const CAND=[...new Set([...Z.L.A,...Z.L.B].flatMap(l=>[...l.s]).concat(Object.values(Z.wrong)))];
  // 字型載入後，慢慢先算好每個字的骨架，按 OK 時才不會等太久
  (document.fonts?document.fonts.load('40px "TWKaiSub"',CAND.join("")):Promise.resolve()).then(()=>{let i=0;const step=()=>{const t=performance.now();while(i<CAND.length&&performance.now()-t<12)glyph(CAND[i++]);if(i<CAND.length)setTimeout(step,30)};setTimeout(step,500)});
  function userBitmap(){const c=document.createElement("canvas");c.width=cv.width;c.height=cv.height;const g=c.getContext("2d");
    g.strokeStyle="#000";g.lineCap=g.lineJoin="round";g.lineWidth=Math.max(8,W*.05)*dpr;
    strokes.forEach(st=>{g.beginPath();st.forEach(([x,y],i)=>i?g.lineTo(x*dpr,y*dpr):g.moveTo(x*dpr,y*dpr));if(st.length===1)g.lineTo(st[0][0]*dpr+.5,st[0][1]*dpr);g.stroke()});
    const b=bm(c);return b&&thin(b)}
  function judge(target){
    const u=userBitmap();if(!u)return{ok:false};const up=pts(u),ud=dt(u);if(up.length<3)return{ok:false};
    const ds=CAND.concat(CAND.includes(target)?[]:[target]).map(c=>{const g=glyph(c);if(!g.p.length)return[c,99];let s1=0,s2=0;for(const i of up)s1+=Math.min(g.d[i],12);for(const i of g.p)s2+=Math.min(ud[i],12);return[c,(s1/up.length+s2/g.p.length)/2]}).sort((a,b)=>a[1]-b[1]);
    const r=ds.findIndex(x=>x[0]===target),d=ds[r][1];
    return{ok:r<12&&d<4.6,rank:r,d,top:ds.slice(0,5).map(x=>x[0]).join("")};
  }
  window.__judge=(t)=>judge(t);
  // ---- 寫字格 ----
  const cv=$("cv"),ctx=cv.getContext("2d");let W=300,dpr=1,strokes=[],cur=null,stage="write",target="",guide=false;
  function setup(){const m=$("main").getBoundingClientRect(),land=innerHeight<=500;
    W=Math.max(180,Math.min(land?m.height-40:Math.min(innerWidth-70,m.height-310),400));dpr=Math.min(2,devicePixelRatio||1);
    cv.width=W*dpr;cv.height=W*dpr;cv.style.width=W+"px";cv.style.height=W+"px";draw()}
  function draw(){ctx.setTransform(dpr,0,0,dpr,0,0);ctx.clearRect(0,0,W,W);
    ctx.strokeStyle="#f3b2c6";ctx.lineWidth=2;ctx.setLineDash([8,8]);ctx.beginPath();ctx.moveTo(W/2,6);ctx.lineTo(W/2,W-6);ctx.moveTo(6,W/2);ctx.lineTo(W-6,W/2);ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle="#e8577a";ctx.lineWidth=3;ctx.strokeRect(4,4,W-8,W-8);
    if(guide){ctx.fillStyle="rgba(232,87,122,.18)";ctx.font=`${W*.82}px "TWKaiSub"`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(target,W/2,W*.54)}
    ctx.strokeStyle="#3a2a22";ctx.lineCap=ctx.lineJoin="round";ctx.lineWidth=Math.max(8,W*.05);
    strokes.forEach(st=>{ctx.beginPath();st.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));if(st.length===1)ctx.lineTo(st[0][0]+.1,st[0][1]);ctx.stroke()})}
  let down=false;const pt=e=>{const r=cv.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};
  cv.onpointerdown=e=>{if(api.S.busy)return;e.preventDefault();down=true;try{cv.setPointerCapture(e.pointerId)}catch(err){}cur=[pt(e)];strokes.push(cur);draw()};
  cv.onpointermove=e=>{if(!down)return;const p=pt(e),l=cur[cur.length-1];if(Math.hypot(p[0]-l[0],p[1]-l[1])>2){cur.push(p);draw()}};
  cv.onpointerup=cv.onpointercancel=()=>{down=false};
  $("clr").onclick=()=>{strokes=[];draw()};
  const tip=t=>{$("tip").innerHTML=TZ.zy(t)};
  // ---- 題目：課本語詞裡有這個生字，其他字照常顯示，這個字只給注音 ----
  function pickWord(c){
    const L=TZ.lessons(),[a,b]=TZ.range(),ok=w=>w.includes(c)&&[...w].filter(x=>x===c).length===1;
    const near=L.slice(a,b+1).flatMap(l=>l.ci).filter(ok),all=L.flatMap(l=>l.ci).filter(ok);
    const w=TZ.shuffle(near.length?near:all)[0];return w?{w,idx:[...w].indexOf(c)}:null;
  }
  let api;
  api=TZ.run({key:"town-write",
    help:"蛋糕寫字。看注音，想一想是哪一個字，在蛋糕上的格子裡寫出來，不用照筆順，寫出來就好。寫完按 OK。寫不出來也沒關係，會出現淡淡的字讓你描一次，再自己寫一次。旁邊的大人可以按勾勾直接算對。",
    build:n=>TZ.deal(TZ.pool(false),n).map(c=>({c,...(pickWord(c)||{})})),
    show:(q)=>{
      target=q.c;strokes=[];guide=false;stage="write";setup();
      const learned=TZ.learned();let html="";
      if(q.w){const zs=Z.ciZy[q.w];[...q.w].forEach((ch,i)=>{html+=i===q.idx?`<span class="zbox">${TZ.charHTML("",zs[i])}</span>`:TZ.charHTML(ch,learned.has(ch)?"":zs[i])})}
      else html=`<span class="zbox">${TZ.charHTML("",Z.ZY[q.c])}</span>`;
      $("word").innerHTML=html+`<button type="button" class="ibtn" id="say" aria-label="念語詞">🔊</button>`;
      $("say").onclick=()=>TZ.say(q.w||q.c);
      tip("看注音，寫出這個字。");
      document.fonts&&document.fonts.load('40px "TWKaiSub"',q.c);
      setTimeout(()=>TZ.say(q.w||q.c),300);
    }});
  function success(first){api.S.tries=first?0:1;api.ok();guide=false;strokes=[];draw();
    ctx.fillStyle="#1f9d61";ctx.font=`${W*.78}px "TWKaiSub"`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(target,W/2,W*.54);
    TZ.say(`寫對了！是${target}。`,{onend:()=>api.next(500)})}
  $("ok").onclick=async()=>{
    if(api.S.busy)return;if(!strokes.length){tip("先在格子裡寫字喔。");return}
    if(stage==="trace"){stage="write2";guide=false;strokes=[];draw();tip("這次自己寫寫看！");TZ.say("這次自己寫寫看");return}
    try{await document.fonts.load('40px "TWKaiSub"',target)}catch(e){}
    const r=judge(target);
    if(r.ok){success(stage==="write");return}
    EN.sfx.bad();
    if(stage==="write"){api.S.tries++;stage="trace";strokes=[];guide=true;draw();tip("照著淡淡的字描一次。");TZ.say("照著淡淡的字描一次")}
    else{api.S.busy=true;guide=false;strokes=[];draw();ctx.fillStyle="#3a2a22";ctx.font=`${W*.78}px "TWKaiSub"`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(target,W/2,W*.54);
      tip("是這個字，看一看。");TZ.say(`是${target}，看一看。`,{onend:()=>api.next(900)})}
  };
  $("adult").onclick=()=>{if(!api.S.busy)success(stage==="write")};
  addEventListener("resize",()=>{const keep=strokes;setup();strokes=keep;draw()});
})();""")

for fn,k in PAGES.items():
    html=HEAD.format(V=V,title=k["title"],icon=k["icon"],sub=k["sub"],style=COMMON_STYLE+"\n"+k["style"],main=k["main"],script=k["script"])
    open(os.path.join(ROOT,fn),"w",encoding="utf-8").write(html)
    print("寫出",fn)

# 產生甜點小鎮的四關頁面：python pages.py（每一關共用標題列、開始畫面、結束畫面，只有題目區和玩法不同）
import os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
V="20261125b"
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
<script src="rest.js?v={V}"></script>
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
    <p class="source">字型：全字庫正楷體（數位發展部「CNS11643中文標準交換碼全字庫」，依政府資料開放授權條款第1版使用）<br>生字：教育部教育百科「生字詞彙表」；部首、讀音：教育部《國語辭典簡編本》；筆畫：教育部《國字標準字體筆順學習網》<br>本網站與各教科書出版社無關。生字依教育部教育百科公開資料整理，僅供孩子非營利學習使用。</p>
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
.oven{position:relative;width:min(340px,80vw);padding:16px;border-radius:22px;background:#9aa8b8;border:6px solid var(--choc)}
.ovwin{border-radius:14px;background:radial-gradient(#ffe7a8,#ffb36b);border:5px solid var(--choc);min-height:120px;display:grid;place-items:center;padding:8px;animation:heat 1s ease-in-out 2}
@keyframes heat{50%{filter:brightness(1.25)}}
.ding{position:absolute;right:-16px;top:-22px;background:var(--lemon);border:4px solid var(--choc);border-radius:999px;padding:2px 12px;font-weight:900;font-size:24px;animation:bpop .4s 1.6s both}
@keyframes stamp{40%{transform:scale(.9)}70%{transform:scale(1.08)}}
.cutter{width:clamp(96px,17vmin,140px);aspect-ratio:1;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.18)}
.cutter.s0{border-radius:50%}.cutter.s1{border-radius:28px}.cutter.s2{border-radius:50% 50% 22px 22px}.cutter.s3{border-radius:22px 50% 22px 50%}
.cutter .bu{font-family:var(--kai);font-size:clamp(50px,9vmin,76px);color:var(--ink)}
.cutter .tz-b{font-size:17px}''',
main='''<div class="qcard"><div class="qline" id="q"></div><div class="cookie" id="cookie"><b id="ch"></b></div></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffb3c7","#a8e6cf","#ffe08a","#b9d7ff"];
  const api=TZ.run({key:"town-bu",gotIcon:EN.icon("cookie"),
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="oven"><div class="ovwin"><div class="frow">${Array(Math.min(n,10)).fill(EN.icon("cookie")).join("")}</div></div><span class="ding">${TZ.zy("叮！")}</span></div>`,"烤盤進烤箱，叮！餅乾烤好了！",done,3000)},
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
        if(el.dataset.b===bu){api.ok();el.classList.add("yes");const ck=$("cookie");
          TZ.fly(el,ck,()=>{ck.classList.remove("stamp");void ck.offsetWidth;ck.classList.add("stamp");EN.sfx.pop();setTimeout(()=>TZ.flyGot(ck,EN.icon("cookie")),350)},{dur:.55,scale:1.1});
          api.next(1300)}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-b="${bu}"]`).classList.add("glow")}
      });
      setTimeout(()=>{if(!api.S.busy)TZ.say(`${c}，的部首是哪一個？`)},300);
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
.count2{min-width:56px;height:44px;border-radius:999px;background:var(--lemon);border:4px solid var(--choc);display:none;place-items:center;font-family:var(--num);font-weight:800;font-size:26px;color:var(--choc);margin-top:-6px}
.count2.on{display:grid;animation:bpop .3s}
.sweets{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;max-width:min(560px,90vw);min-height:26px}
.sweets i{width:22px;height:22px;border-radius:50%;background:var(--c);border:3px solid var(--choc);animation:bpop .25s}
.moe{margin-top:2px}
.jar{overflow:hidden}
.jar .drop{position:absolute;width:13%;aspect-ratio:1;border-radius:50%;background:var(--c);border:3px solid var(--choc);z-index:0;animation:drop .45s cubic-bezier(.5,0,.7,1.4) both}
@keyframes drop{from{transform:translateY(-260px)}}
.jar b{position:relative;z-index:1}
.bigjar{position:relative;width:200px;padding:30px 14px 14px;border:6px solid var(--choc);border-radius:26px 26px 36px 36px;background:rgba(255,255,255,.8)}
.bigjar .lid{position:absolute;left:10%;right:10%;top:-30px;height:26px;border-radius:12px 12px 0 0;background:var(--berry);border:6px solid var(--choc);animation:lid .6s .9s both}
@keyframes lid{from{transform:translateY(-120px) rotate(-20deg);opacity:0}}
.bigjar .dot{width:34px;height:34px;border-radius:50%;background:var(--c);border:3px solid var(--choc);display:inline-block;animation:bpop .3s both}
@media (max-height:500px){.jar{width:120px}.jar b{font-size:84px}.sweets{min-height:22px}.sweets i{width:16px;height:16px}.candy{min-width:84px;height:72px;font-size:36px}.moe{min-height:40px;font-size:14px;padding:2px 10px}}
@media (orientation:portrait) and (max-height:740px){.jar{width:150px}.jar b{font-size:100px}}
.candy{min-width:clamp(96px,17vmin,130px);height:clamp(84px,14vmin,110px);border-radius:999px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.18);
  font-family:var(--num);font-weight:800;font-size:clamp(40px,7vmin,58px);color:var(--choc);position:relative;display:flex;align-items:center;justify-content:center;gap:4px}
.moe{font-weight:800;font-size:16px;color:var(--zyc);text-decoration:none;background:#fff;border:3px solid #cfe0f5;border-radius:999px;padding:4px 14px;min-height:44px;display:inline-flex;align-items:center}
.candy::before,.candy::after{content:"";position:absolute;top:50%;width:26px;height:34px;background:var(--c);border:4px solid var(--choc);transform:translateY(-50%)}
.candy::before{left:-24px;clip-path:polygon(0 0,100% 50%,0 100%);border:0}.candy::after{right:-24px;clip-path:polygon(100% 0,0 50%,100% 100%);border:0}
.candy small{font-family:var(--text);font-size:.42em;margin-left:2px}''',
main='''<div class="qcard"><div class="qline" id="q"></div><div class="jar" id="jar"><b id="ch"></b></div><span class="count2" id="count">0</span><div class="sweets" id="sweets" hidden></div><a class="moe" id="moe" target="_blank" rel="noopener"></a></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ff9fb2","#9ef0b9","#ffe08a","#9fd3ff","#d7b4ff"];
  // 答完：一顆一顆放糖果數到總筆畫（字形一直是教育部標準字體，不放其他來源的筆順動畫）
  function countUp(c,n,done){
    const cnt=$("count"),jar=$("jar");jar.querySelectorAll(".drop").forEach(x=>x.remove());cnt.textContent="0";cnt.classList.add("on");
    let k=0;const t=setInterval(()=>{k++;cnt.textContent=k;
      // 糖果從罐子上面掉下去，堆在罐底
      const d=document.createElement("i");d.className="drop";const row=Math.floor((k-1)/6),col=(k-1)%6;
      d.style.cssText=`--c:${COL[k%COL.length]};left:${10+col*14+(row%2)*6}%;bottom:${6+row*11}%`;jar.appendChild(d);EN.sfx.pop();
      if(k>=n){clearInterval(t);setTimeout(()=>{TZ.flyGot(jar,'<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="14" fill="#ff9fb2" stroke="#6b3f22" stroke-width="4"/></svg>');setTimeout(done,700)},700)}},300);
  }
  const CANDY='<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="14" fill="#ff9fb2" stroke="#6b3f22" stroke-width="4"/></svg>';
  const api=TZ.run({key:"town-n",gotIcon:CANDY,
    finale:done=>TZ.finale(`<div class="bigjar"><span class="lid"></span><div class="frow">${Array(12).fill(0).map((_,i)=>`<i class="dot" style="--c:${COL[i%COL.length]}"></i>`).join("")}</div></div>`,"糖果罐裝滿了，蓋上蓋子！",done,2800),
    help:"數糖果。看糖果罐上的字，數一數這個字有幾畫，點對的數字。答完以後，一畫會放一顆糖果，一起數一數。想看怎麼寫，可以按「看教育部的筆順」。",
    build:n=>TZ.deal(TZ.pool(false),n),
    show:(c)=>{
      const n=Z.chars[c].n;$("jar").querySelectorAll(".drop").forEach(x=>x.remove());$("count").classList.remove("on");
      $("moe").href="https://stroke-order.learningweb.moe.edu.tw/dictView.jsp?ID="+c.codePointAt(0);$("moe").innerHTML="✍️ "+TZ.zy("看教育部的筆順");
      $("ch").textContent=c;
      $("q").innerHTML=TZ.zy("「")+`<b class="kai" style="font-size:1.3em">${c}</b>`+TZ.zy("」有幾畫？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
      $("say").onclick=()=>TZ.say(`${c}，有幾畫？`);
      const set=new Set([n]);const d=[-2,-1,1,2,3];TZ.shuffle(d);for(const x of d){if(set.size>=3)break;if(n+x>=1)set.add(n+x)}
      $("choices").innerHTML=TZ.shuffle([...set]).map((v,i)=>`<button type="button" class="choice candy" style="--c:${COL[i]}" data-v="${v}" aria-label="${v} 畫">${v}<small>${TZ.charHTML("畫",ZI.ZY["畫"])}</small></button>`).join("");
      const finish=()=>countUp(c,n,()=>api.next(200));
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(+el.dataset.v===n){api.ok();el.classList.add("yes");setTimeout(finish,500)}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2){api.S.busy=true;document.querySelector(`.choice[data-v="${n}"]`).classList.add("glow");TZ.say(`${c}有${n}畫，我們一起數一數。`);setTimeout(finish,800)}}
      });
      setTimeout(()=>{if(!api.S.busy)TZ.say(`${c}，有幾畫？`)},300);
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
.order{padding-top:max(34px,clamp(14px,3vmin,26px))}   /* 上緣留位子給右上角的 🔊，句子才不會被蓋到 */
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
          setTimeout(()=>{
            if(!last){api.next(300);return}
            const tk=$("truck");EN.sfx.coin();setTimeout(()=>EN.sfx.coin(),220);tk.classList.remove("bump");tk.classList.add("go");
            api.next(1800);
          },1500)}
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
.cup.big{--w:clamp(150px,27vmin,220px)}
.walker{display:inline-block;animation:walk 1.4s ease-out both}.walker .ic{width:110px!important;height:110px!important}
@keyframes walk{from{transform:translateX(-60vw)}}
.trayx{display:flex;gap:4px;padding:8px 12px;border-radius:14px;background:#c98a4b;border:4px solid var(--choc);align-items:flex-end}.cup.big b{font-size:clamp(84px,15vmin,130px)}
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
  const DRINK=EN.icon("juice");
  const api=TZ.run({key:"town-anti",gotIcon:DRINK,
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="frow"><span class="walker">${EN.icon("Tom")}</span><div class="trayx">${Array(Math.min(n,8)).fill(DRINK).join("")}</div></div>`,"客人來拿飲料囉，謝謝光臨！",done,3000)},
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
        if(el.dataset.c===a){api.ok();el.classList.add("yes");const s=$("slot");
          TZ.fly(el,s,()=>{s.style.cssText="border-style:solid;border-color:#1f9d61;background:#eafff2;color:#2b2320;font-family:var(--kai);font-size:clamp(54px,9.5vmin,80px)";s.textContent=a;EN.sfx.pop();
            setTimeout(()=>TZ.flyGot(s,DRINK),400)},{dur:.6,keepHidden:true});
          api.next(1500)}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${a}"]`).classList.add("glow")}
      });
      setTimeout(()=>{if(!api.S.busy)TZ.say(`和${q}，意思相反的是哪一個字？`)},300);
    }});
})();''')

# ---------- 5. 挑壞蘋果（找錯字、形近字） ----------
page("town-wrong.html",title="挑壞蘋果",icon="🍎",sub="句子裡有一個寫錯的字，把壞蘋果挑出來！",
style=""".basket{background:#fff;border:5px solid var(--choc);border-radius:24px;padding:clamp(12px,2.6vmin,22px) clamp(12px,2.6vmin,24px);box-shadow:0 8px 0 rgba(0,0,0,.12);max-width:min(940px,96vw);position:relative}
.bin{position:absolute;left:-16px;top:-30px;width:48px;height:56px;z-index:2}
.bin.gulp{animation:gulp .4s}
@keyframes gulp{40%{transform:scale(1.2) rotate(-8deg)}}
.rotap{display:grid;place-items:center;border-radius:18px;background:#c9a27a;font-family:var(--kai);font-size:40px;color:#5a3a20;z-index:70;pointer-events:none}
.bask{padding:14px 18px 22px;border-radius:12px 12px 40px 40px;background:repeating-linear-gradient(45deg,#e8b06a 0 10px,#d39a5c 10px 20px);border:6px solid var(--choc);min-width:220px}
.basket .ibtn{position:absolute;right:-14px;top:-18px;width:48px;height:48px;font-size:24px;background:#ffe9a8;box-shadow:0 3px 0 #d18e0a}
.basket{padding-top:max(36px,clamp(12px,2.6vmin,22px))}
.sent2{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:4px 8px;font-family:var(--kai);font-size:clamp(28px,5.2vmin,48px)}
/* 句子裡每個字都是一顆蘋果：紅色、上面有梗和葉子；字和注音用白色 */
.ap{position:relative;display:inline-flex;align-items:center;border:0;cursor:pointer;font:inherit;color:#fff;min-width:44px;min-height:56px;margin-top:12px;
  padding:8px 16px 6px 10px;border-radius:46% 46% 50% 50%/40% 40% 60% 60%;text-shadow:0 2px 0 rgba(120,20,15,.45);
  background:radial-gradient(circle at 18% 24%,rgba(255,255,255,.8) 0 4%,transparent 5%),radial-gradient(circle at 50% 50%,#ff8f86,#e8392f 80%);
  box-shadow:inset 0 -5px 0 rgba(0,0,0,.14),0 3px 0 #a8261e}
.ap::before{content:"";position:absolute;left:50%;top:-14px;width:30px;height:18px;transform:translateX(-40%);pointer-events:none;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 18'%3E%3Cpath d='M9 17q0-8 3-14' fill='none' stroke='%236b3f22' stroke-width='3.5' stroke-linecap='round'/%3E%3Cpath d='M12 8q6-8 16-5q-5 9-16 5z' fill='%235cc24a' stroke='%232e7d32' stroke-width='1.6'/%3E%3C/svg%3E") no-repeat center/contain}
.ap .tz-b{font-size:max(.38em,14px);margin-left:.12em;color:#fff}
.ap .tz-b .zy-t{font-size:1.15em;left:100%;top:-.55em}
.ap.bad{animation:wig .4s}
.ap.rot{background:radial-gradient(circle at 60% 40%,#8a5a36 0 9%,transparent 10%),radial-gradient(circle at 50% 50%,#d2a878,#9a6a3e 80%);box-shadow:inset 0 -5px 0 rgba(0,0,0,.18),0 3px 0 #6b3f22}
.ap.rot::after{content:"🐛";position:absolute;right:-12px;top:-16px;font-size:24px}
.ap.fixed{box-shadow:inset 0 -5px 0 rgba(0,0,0,.14),0 3px 0 #a8261e,0 0 0 4px #1f9d61}
.ap.fixed::after{content:none}
.ap.glow{animation:glow 1s infinite}
.sent2 .tp{font-size:.9em}
.step{font-size:clamp(18px,3vmin,24px);font-weight:800;color:var(--choc)}
.apple{width:clamp(92px,16vmin,128px);aspect-ratio:1;border-radius:46% 46% 50% 50%;background:radial-gradient(circle at 35% 30%,#ff8a8a,#e8302a 70%);border:5px solid #8a2a20;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.apple::before{content:"";position:absolute;top:-16px;left:50%;width:6px;height:18px;background:#6b3f22;border-radius:3px}
.apple::after{content:"";position:absolute;top:-14px;left:56%;width:22px;height:12px;background:#5cc24a;border-radius:0 12px 0 12px;border:2px solid #2e7d32}
.apple b{font-family:var(--kai);font-weight:400;font-size:clamp(50px,9vmin,72px);color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.25)}
@media (max-height:500px){.sent2{font-size:26px}main.stage2{flex-direction:column;gap:8px}}""",
main="""<div class="basket" id="basket"><div class="sent2" id="sent"></div><span class="bin" id="bin"><svg viewBox="0 0 60 70" width="100%" height="100%"><g stroke="#3a2a22" stroke-width="4" stroke-linejoin="round"><rect x="6" y="12" width="48" height="8" rx="3" fill="#9aa8b8"/><path d="M10 20h40l-5 46H15z" fill="#b9c7d6"/><path d="M22 28v30M30 28v30M38 28v30" stroke-width="3" opacity=".5"/><rect x="24" y="5" width="12" height="7" rx="2" fill="#9aa8b8"/></g></svg></span><button type="button" class="ibtn" id="say" aria-label="念句子">🔊</button></div>
<div class="step" id="step"></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  const api=TZ.run({key:"town-wrong",gotIcon:EN.icon("apple"),
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="bask"><div class="frow">${Array(Math.min(n,12)).fill(EN.icon("apple")).join("")}</div></div>`,"壞蘋果都挑出來了，籃子裝滿好蘋果！",done,2800)},
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
        if(+b.dataset.i===badIdx){EN.sfx.pop();b.classList.add("rot");step=2;
          // 壞蘋果被丟進垃圾桶
          const m=document.createElement("span");m.className="rotap";m.textContent=b.querySelector(".tz-h").textContent;const r=b.getBoundingClientRect();m.style.cssText=`position:fixed;left:${r.left}px;top:${r.top}px;width:${r.width}px;height:${r.height}px`;document.body.appendChild(m);
          TZ.fly(m,$("bin"),()=>{const bn=$("bin");bn.classList.remove("gulp");void bn.offsetWidth;bn.classList.add("gulp");EN.sfx.bad()},{dur:.7,spin:200,scale:.3});setTimeout(()=>m.remove(),1100);
          showFix()}
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
          if(el.dataset.c===c){api.ok();el.classList.add("yes");
            TZ.fly(el,badBtn,()=>{badBtn.classList.remove("rot");badBtn.classList.add("fixed");badBtn.innerHTML=TZ.charHTML(c,Z.ZY[c]);EN.sfx.pop();setTimeout(()=>TZ.flyGot(badBtn,EN.icon("apple")),300)},{dur:.6,keepHidden:true});
            api.next(1600)}
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
.plate.land .ic{animation:land .5s cubic-bezier(.5,0,.6,1.5)}
@keyframes land{from{transform:translateY(-160px)}}
.plate.land{animation:pbounce .5s .35s}
@keyframes pbounce{40%{transform:translateY(10px)}}
.dial{position:relative;width:54px;height:30px;border-radius:30px 30px 0 0;background:#fff;border:4px solid var(--choc);border-bottom:0;margin-top:-2px;z-index:2}
.needle{position:absolute;left:50%;bottom:0;width:4px;height:22px;margin-left:-2px;background:#e8302a;border-radius:2px;transform-origin:50% 100%}
.needle.swing{animation:swing 1s ease-out}
@keyframes swing{20%{transform:rotate(55deg)}45%{transform:rotate(-30deg)}70%{transform:rotate(15deg)}}
.bigbag{width:160px;height:180px;animation:wob 1s ease-in-out 2}
.pole{width:18px;height:clamp(30px,6vmin,50px);background:#c98a4b;border:4px solid var(--choc);border-top:0}
.base{width:70%;height:22px;border-radius:12px;background:#c98a4b;border:4px solid var(--choc)}
.phrase{font-size:clamp(34px,6.4vmin,58px);font-weight:800}
.phrase .blank{width:1.2em;height:1.2em}
.tagp{min-width:clamp(96px,16vmin,128px);height:clamp(78px,13vmin,100px);border-radius:14px 34px 34px 14px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16)}
.tagp::before{content:"";position:absolute;left:12px;top:50%;width:14px;height:14px;border-radius:50%;background:#fff;border:3px solid var(--choc);transform:translateY(-50%)}
.tagp b{font-family:var(--kai);font-weight:400;font-size:clamp(44px,8vmin,64px);padding-left:20px}
.tagp .tz-b{font-size:16px}
@media (max-height:500px){.plate{height:100px}.plate .ic{width:84px;height:84px}.pole{height:24px}.phrase{font-size:30px}}""",
main="""<div class="qcard"><div class="scale"><div class="plate" id="plate"></div><div class="dial"><i class="needle" id="needle"></i></div><div class="pole"></div><div class="base"></div></div><div class="phrase" id="phrase"></div></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI,COL=["#ffe08a","#ffb3c7","#a8e6cf","#b9d7ff"];
  const BAG='<svg viewBox="0 0 60 70" width="100%" height="100%"><g stroke="#3a2a22" stroke-width="4" stroke-linejoin="round"><path d="M20 22q0-14 10-14t10 14" fill="none"/><path d="M8 22h44l-4 42H12z" fill="#ffd08a"/><circle cx="30" cy="42" r="8" fill="#ff8fb0" stroke-width="3"/></g></svg>';
  const api=TZ.run({key:"town-mw",noRange:true,gotIcon:BAG,
    finale:done=>TZ.finale(`<div class="bigbag">${BAG}</div>`,"東西都買好了，裝進購物袋！",done,2600),
    help:"市場秤一秤。看秤子上的東西，想一想要用哪一個量詞，例如一隻小狗、一條魚、一輛汽車。點對的價格牌。",
    build:n=>TZ.deal(Z.mw,n),
    show:([noun,m,ic])=>{
      $("plate").innerHTML=EN.icon(ic);const pl=$("plate"),nd=$("needle");pl.classList.remove("land");nd.classList.remove("swing");void pl.offsetWidth;pl.classList.add("land");nd.classList.add("swing");
      $("phrase").innerHTML=TZ.zy("一＿"+noun);
      const others=TZ.shuffle([...Z.mwPool].filter(x=>x!==m));
      const opts=TZ.shuffle([m,others[0],others[1]]);
      $("choices").innerHTML=opts.map((x,i)=>`<button type="button" class="choice tagp" style="--c:${COL[i]}" data-c="${x}" aria-label="${x}"><b>${TZ.charHTML(x,Z.ZY[x])}</b></button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.c===m){api.ok();el.classList.add("yes");const b=$("blank");
          TZ.fly(el,$("plate"),()=>{b.classList.add("fill");b.innerHTML=TZ.charHTML(m,Z.ZY[m]);EN.sfx.pop();setTimeout(()=>TZ.flyGot($("plate"),EN.icon(ic)),300)},{dur:.6,scale:.5,keepHidden:true});
          api.next(1500)}
        else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${m}"]`).classList.add("glow")}
      });
      setTimeout(()=>{if(!api.S.busy)TZ.say("一什麼"+TZ.plain(noun)+"？")},300);
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
.slots.glaze::after{content:"";position:absolute;inset:-6px;border-radius:999px;background:linear-gradient(100deg,transparent 30%,rgba(255,255,255,.85) 45%,transparent 60%) -200% 0/200% 100% no-repeat;animation:glaze .9s ease-out;pointer-events:none}
@keyframes glaze{to{background-position:200% 0}}
.stand{padding:10px 18px 14px;border-bottom:14px solid #c98a4b;border-radius:0 0 10px 10px}
.stand .ic{height:90px!important;width:40px!important}
.slot .ball{box-shadow:inset 0 -6px 0 rgba(0,0,0,.12)}
.slot .ball.ok{background:radial-gradient(circle at 30% 30%,#7fe0a8,#1f9d61 70%);border-color:#136b41}
.ball.bad{animation:wig .4s}
@media (max-height:500px){.ball{font-size:26px;min-height:58px;padding:2px 12px}.slot{min-height:58px;min-width:72px}main.stage2{flex-direction:column;gap:10px}}""",
main="""<div class="qline" id="q"></div>
<div class="stickbox"><div class="slots" id="slots"></div></div>
<div class="choices" id="choices"></div>""",
script="""(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  $("q").innerHTML=TZ.zy("把糖葫蘆照順序串起來，變成一句話。")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
  // 喇叭念題目（不念答案的句子）
  let cur="";$("say").onclick=()=>TZ.say("把糖葫蘆照順序串起來，變成一句話。");
  // 糖葫蘆回到下面原來的位置（飛上去時原本那顆被藏起來，回來要再顯示）
  const back=b=>{b.classList.remove("used","bad");b.style.visibility=""};
  const api=TZ.run({key:"town-order",gotIcon:EN.icon("candied fruit"),
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="stand"><div class="frow">${Array(Math.min(n,10)).fill(EN.icon("candied fruit")).join("")}</div></div>`,"糖葫蘆都串好了，插上展示架！",done,2800)},
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
        EN.sfx.pop();const c=b.cloneNode(true);c.classList.remove("choice");c.onclick=null;c.style.visibility="hidden";s.appendChild(c);
        TZ.fly(b,s,()=>{c.style.visibility=""},{dur:.4,scale:1,keepHidden:true});b.classList.add("used");mark();
        if(slots.every(x=>x.firstChild))setTimeout(check,350);
      });
      slots.forEach(s=>s.onclick=()=>{if(api.S.busy||!s.firstChild||s.firstChild.classList.contains("ok"))return;
        back(balls.find(b=>b.dataset.i===s.firstChild.dataset.i));s.innerHTML="";mark()});
      function check(){
        let all=true;slots.forEach(s=>{const k=+s.dataset.k,b=s.firstChild;if(+b.dataset.i===k)b.classList.add("ok");else all=false});
        if(all){api.ok();const sl=$("slots");sl.classList.remove("glaze");void sl.offsetWidth;sl.classList.add("glaze");EN.sfx.clear();setTimeout(()=>TZ.flyGot(sl,EN.icon("candied fruit")),700);
          api.next(1700);return}
        api.bad();api.S.busy=true;
        slots.forEach(s=>{const b=s.firstChild;if(b&&!b.classList.contains("ok"))b.classList.add("bad")});
        setTimeout(()=>{slots.forEach(s=>{const b=s.firstChild;if(b&&!b.classList.contains("ok")){back(balls.find(x=>x.dataset.i===b.dataset.i));s.innerHTML=""}});
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
.tower{position:absolute;bottom:clamp(70px,13vmin,110px);left:calc(100% + 34px);display:flex;flex-direction:column-reverse;align-items:center;z-index:2;pointer-events:none}
.tower i{width:clamp(40px,7vmin,56px);height:clamp(28px,4.6vmin,38px);margin-top:-10px;border-radius:50% 50% 40% 40%;background:var(--c);border:4px solid var(--choc);animation:plop .35s cubic-bezier(.3,1.6,.5,1)}
@keyframes plop{from{transform:translateY(-80px) scale(.6)}}
.bigcone{display:flex;flex-direction:column-reverse;align-items:center}
.bigcone i{width:90px;height:60px;margin-top:-18px;border-radius:50% 50% 40% 40%;background:var(--c);border:5px solid var(--choc);animation:plop .35s both}
.bigcone i:nth-child(2){animation-delay:.15s}.bigcone i:nth-child(3){animation-delay:.3s}.bigcone i:nth-child(4){animation-delay:.45s}.bigcone i:nth-child(5){animation-delay:.6s}
.bigcone b{order:-1;width:0;height:0;border-left:44px solid transparent;border-right:44px solid transparent;border-top:80px solid #e8b06a;margin-top:-6px}
.notes{position:absolute;right:-30px;top:-10px;font-size:30px;animation:nt 2s ease-in-out infinite}
@keyframes nt{50%{transform:translateY(-8px) rotate(10deg)}}
.zyopt{min-width:clamp(84px,14vmin,110px);min-height:clamp(110px,19vmin,150px);border-radius:999px 999px 26px 26px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16);padding:8px 14px}
.zyopt .tz-b{font-size:clamp(28px,5vmin,40px);color:var(--ink);line-height:1.05}
.tonebtn{min-width:clamp(84px,14vmin,110px);height:clamp(84px,14vmin,104px);border-radius:24px;background:var(--c);border:5px solid var(--choc);box-shadow:0 6px 0 rgba(0,0,0,.16);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.tonebtn .mk{font-size:clamp(36px,6vmin,50px);line-height:.9;font-weight:900;color:var(--choc);min-height:.9em}
.tonebtn .lb{font-size:18px;font-weight:800}
@media (max-height:500px){.waffle{border-top-width:60px;border-left-width:46px;border-right-width:46px}.scoop{width:130px}.scoop .bigc{font-size:76px}.zyopt{min-height:92px}.zyopt .tz-b{font-size:24px}}""",
main="""<div class="qcard"><div class="qline" id="q"></div><div class="cone"><div class="tower" id="tower"></div><div class="scoop" id="scoop"><span class="bigc" id="big"></span></div><div class="waffle"></div><span class="notes">🎵</span></div></div>
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
  const SC=["#ffc2dc","#c9f2d8","#fff1a8","#cfe4ff","#e6d4ff","#ffd8b0"];
  // 答對就在甜筒上多疊一球（畫面上最多疊 6 球，其他算在計數裡）
  function addScoop(){const tw=$("tower");if(tw.children.length>=4)tw.firstElementChild.remove();
    tw.insertAdjacentHTML("beforeend",`<i style="--c:${SC[(+TZ.got().dataset.n)%SC.length]}"></i>`);TZ.gotAdd();EN.sfx.pop()}
  const api=TZ.run({key:"town-tone",gotIcon:'<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="#ffc2dc" stroke="#6b3f22" stroke-width="4"/></svg>',
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="bigcone wobble">${Array(Math.min(n,8)).fill(0).map((_,i)=>`<i style="--c:${SC[i%SC.length]}"></i>`).join("")}<b></b></div>`,"冰淇淋疊得好高，唱一首歌慶祝！",done,3000);
      [1,2,3,4].forEach((x,i)=>setTimeout(()=>TZ.toneSound(x),300+i*550))},
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
          if(el.dataset.z===z){api.ok();el.classList.add("yes");$("big").innerHTML=TZ.charHTML(c,z);addScoop();api.next(1200)}
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
          if(api.S.busy)return;TZ.toneSound(+el.dataset.t);
          if(+el.dataset.t===t){api.ok();el.classList.add("yes");$("big").innerHTML=TZ.charHTML(c,z);addScoop();api.next(1200)}
          else{api.bad();el.classList.add("no");if(api.S.tries>=2)document.querySelector(`.choice[data-t="${t}"]`).classList.add("glow")}
        });
        setTimeout(()=>{if(!api.S.busy)TZ.say(c)},300);
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
.thing.plop{animation:tplop .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes tplop{from{transform:translate(-50%,-140%) scale(.6)}}
.guest{position:absolute;bottom:4%;width:15%;aspect-ratio:1;z-index:3;pointer-events:none}
.guest .ic{width:100%;height:100%}
.guest.fromL{left:-20%;animation:gl 1.1s ease-out forwards}.guest.fromR{right:-20%;animation:gr 1.1s ease-out forwards}
@keyframes gl{to{left:22%}}@keyframes gr{to{right:22%}}
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
  const api=TZ.run({key:"town-place",noRange:true,gotIcon:EN.icon("table"),
    finale:done=>TZ.finale(`<div class="frow">${["dog","cat","rabbit","bear"].map(w=>EN.icon(w)).join("")}</div><div class="frow">${EN.icon("cake")}${EN.icon("apple")}${EN.icon("juice")}</div>`,"餐桌都擺好了，大家一起開派對！",done,2800),
    help:"擺餐桌。上面的一段話說了東西要放在哪裡，例如桌子上面、桌子下面、桌子左邊、桌子右邊。請你看看注音，把下面的東西一個一個拖到對的位置。",
    build:n=>[...Array(n)].map(()=>{const ps=TZ.shuffle(POS.slice()).slice(0,3),its=TZ.shuffle(Z.place.slice()).slice(0,3);return ps.map((p,i)=>({p,it:its[i]}))}),
    show:(round)=>{
      document.querySelectorAll(".thing,.guest").forEach(e=>e.remove());
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
            const [ax,ay]=ANCHOR[x.p],t=document.createElement("div");t.className="thing plop";t.style.left=ax+"%";t.style.top=ay+"%";t.innerHTML=EN.icon(x.it[2]);$("stage").appendChild(t);
            const ln=document.querySelector(`.ln[data-i="${i}"]`);ln.classList.add("done");ln.querySelector(".ck").textContent="✅";EN.sfx.good();
            document.querySelectorAll(".zone").forEach(q=>q.classList.remove("hint"));
            left--;if(left===0){api.ok();guests();TZ.flyGot($("stage"),EN.icon("table"));api.next(1800)}
          }else{el.classList.remove("used");if(z){api.bad();el.classList.remove("back");void el.offsetWidth;el.classList.add("back");
            if(api.S.tries>=2)document.querySelector(`.zone[data-p="${x.p}"]`).classList.add("hint");TZ.say(TZ.plain(text(x)))}}};
        el.addEventListener("pointerup",up);el.addEventListener("pointercancel",()=>up(null));
      });
    }});
  // 小動物客人從兩邊跑進來，在桌子旁邊坐下
  function guests(){const st=$("stage");st.querySelectorAll(".guest").forEach(g=>g.remove());
    const who=TZ.shuffle(["dog","cat","rabbit","bear","pig","duck"]).slice(0,2);
    who.forEach((w,i)=>{const g=document.createElement("div");g.className="guest "+(i?"fromR":"fromL");g.innerHTML=EN.icon(w);st.appendChild(g)});EN.sfx.clear()}
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
.candles{position:absolute;left:0;right:0;top:-40px;display:flex;justify-content:center;gap:28px;pointer-events:none;z-index:3}
.candles i{width:12px;height:34px;border-radius:4px;background:#7ec8ff;border:3px solid var(--choc);position:relative;animation:plop .35s both}
.candles i:nth-child(2){background:#ffd23f;animation-delay:.15s}.candles i:nth-child(3){background:#9ef0b9;animation-delay:.3s}
.candles i::after{content:"";position:absolute;left:50%;top:-20px;width:14px;height:18px;margin-left:-7px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:#ffc53d;box-shadow:0 0 12px 4px rgba(255,197,61,.7);animation:flick .3s ease-in-out infinite alternate}
@keyframes flick{to{transform:scale(.85) rotate(4deg)}}
.pipe{position:absolute;width:30px;height:46px;pointer-events:none;z-index:4}
.pipe svg{width:100%;height:100%}
.shelf2{padding:10px 18px 0;border-bottom:14px solid #c98a4b}
.adult{position:absolute;right:20px;bottom:20px;width:40px;height:40px;border-radius:12px;border:2px solid #d8c9ae;background:#fff;color:#9a8a70;font-size:20px;cursor:pointer;opacity:.75}
.wbar{display:flex;gap:14px;align-items:center}
.wbar .big{min-height:56px}
.tip{font-weight:800;color:var(--choc);font-size:clamp(17px,2.8vmin,22px);min-height:1.4em}
@media (max-height:500px){main.stage2{flex-direction:row;gap:16px}.side{display:flex;flex-direction:column;gap:10px;align-items:center}.word{font-size:36px;padding:4px 14px}.wbar{flex-direction:column}.tip{font-size:15px;max-width:150px;text-align:center}}
.side{display:contents}
@media (max-height:500px){.side{display:flex}}""",
main="""<div class="side"><div class="word" id="word"></div><div class="tip" id="tip"></div></div>
<div class="cakebox"><div class="candles" id="candles"></div><canvas id="cv"></canvas><span class="pipe" id="pipe" hidden><svg viewBox="0 0 40 60"><path d="M6 4h28l-10 44h-8z" fill="#ffd1e6" stroke="#6b3f22" stroke-width="4" stroke-linejoin="round"/><path d="M16 48l4 10 4-10z" fill="#c0c7d0" stroke="#6b3f22" stroke-width="3"/></svg></span><button type="button" class="adult" id="adult" aria-label="大人幫忙算對">✓</button></div>
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
    ctx.strokeStyle="#6b3f22";ctx.lineCap=ctx.lineJoin="round";ctx.lineWidth=Math.max(8,W*.05);
    strokes.forEach(st=>{ctx.beginPath();st.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));if(st.length===1)ctx.lineTo(st[0][0]+.1,st[0][1]);ctx.stroke()})}
  let down=false;const pt=e=>{const r=cv.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};
  // 擠花袋跟著手指走
  const pipe=$("pipe"),movePipe=p=>{pipe.hidden=false;pipe.style.left=(cv.offsetLeft+p[0]-12)+"px";pipe.style.top=(cv.offsetTop+p[1]-58)+"px"};
  cv.onpointerdown=e=>{if(api.S.busy)return;e.preventDefault();down=true;try{cv.setPointerCapture(e.pointerId)}catch(err){}cur=[pt(e)];strokes.push(cur);movePipe(cur[0]);draw()};
  cv.onpointermove=e=>{if(!down)return;const p=pt(e),l=cur[cur.length-1];movePipe(p);if(Math.hypot(p[0]-l[0],p[1]-l[1])>2){cur.push(p);draw()}};
  cv.onpointerup=cv.onpointercancel=()=>{down=false;pipe.hidden=true};
  $("clr").onclick=()=>{strokes=[];draw()};
  const tip=t=>{$("tip").innerHTML=TZ.zy(t)};
  // ---- 題目：課本語詞裡有這個生字，其他字照常顯示，這個字只給注音 ----
  function pickWord(c){
    const L=TZ.lessons(),[a,b]=TZ.range(),ok=w=>w.includes(c)&&[...w].filter(x=>x===c).length===1;
    const near=L.slice(a,b+1).flatMap(l=>l.ci).filter(ok),all=L.flatMap(l=>l.ci).filter(ok);
    const w=TZ.shuffle(near.length?near:all)[0];return w?{w,idx:[...w].indexOf(c)}:null;
  }
  let api;
  api=TZ.run({key:"town-write",gotIcon:EN.icon("cake"),
    finale:done=>{const n=+TZ.got().dataset.n;TZ.finale(`<div class="shelf2"><div class="frow">${Array(Math.max(1,Math.min(n,8))).fill(EN.icon("cake")).join("")}</div></div>`,"蛋糕都做好了，擺上架子！",done,2800)},
    help:"蛋糕寫字。看注音，想一想是哪一個字，在蛋糕上的格子裡寫出來，不用照筆順，寫出來就好。寫完按 OK。寫不出來也沒關係，會出現淡淡的字讓你描一次，再自己寫一次。旁邊的大人可以按勾勾直接算對。",
    build:n=>TZ.deal(TZ.pool(false),n).map(c=>({c,...(pickWord(c)||{})})),
    show:(q)=>{
      target=q.c;strokes=[];guide=false;stage="write";setup();$("candles").innerHTML="";$("candles").classList.remove("on");
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
    $("candles").innerHTML="<i></i><i></i><i></i>";$("candles").classList.add("on");setTimeout(()=>TZ.flyGot($("cv"),EN.icon("cake")),700);
    ctx.fillStyle="#1f9d61";ctx.font=`${W*.78}px "TWKaiSub"`;ctx.textAlign="center";ctx.textBaseline="middle";ctx.fillText(target,W/2,W*.54);
    api.next(1600)}
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

# ---------- 點餐櫃台（說出造詞） ----------
# 點餐單上有一個字，小朋友用這個字說一個語詞：按麥克風說，瀏覽器的語音辨識聽到含有這個字（或同音字）的詞就算對。
# 沒有語音辨識（或麥克風不能用）時，說給大人聽，大人按 ✓。說不出來可以按 💡 看例子。
page("town-say.html",title="點餐櫃台",icon="🛎️",sub="看點餐單上的字，用它說一個語詞！",
style='''.counter{display:flex;align-items:flex-end;justify-content:center;gap:clamp(14px,4vmin,40px)}
.guest{display:inline-block}.guest .ic{width:clamp(84px,15vmin,124px);height:clamp(84px,15vmin,124px);display:block}
.guest.in{animation:gin .7s cubic-bezier(.3,1.4,.5,1) both}
@keyframes gin{from{transform:translateX(-45vw) rotate(-8deg)}60%{transform:translateX(6px) rotate(3deg)}}
.guest.happy{animation:ghop .5s 2}
@keyframes ghop{50%{transform:translateY(-16px)}}
.ticket{position:relative;background:#fff;border:5px solid var(--choc);border-radius:16px 16px 8px 8px;padding:34px 20px 12px;min-width:clamp(140px,25vmin,190px);
  text-align:center;box-shadow:0 6px 0 rgba(0,0,0,.12);transform:rotate(2deg)}
.ticket .tk{position:absolute;left:0;right:0;top:0;min-height:28px;padding:1px 0;background:#7a4fd6;color:#fff;font-weight:900;font-size:15px;border-radius:10px 10px 0 0;display:flex;align-items:center;justify-content:center;gap:2px}
.ticket .tk .tz-b{color:#fff}
.ticket b{font-family:var(--kai);font-weight:400;font-size:clamp(84px,16vmin,132px);line-height:1.05;color:var(--ink)}
.ticket b .tz-b{font-size:max(.2em,17px)}
.ticket.pop{animation:tpop .45s cubic-bezier(.3,1.6,.5,1)}
@keyframes tpop{from{transform:rotate(2deg) scale(.6);opacity:0}}
.bar{position:relative;width:min(440px,90vw);height:22px;margin-top:-14px;border-radius:10px;background:linear-gradient(#d9a467,#a86c38);border:4px solid var(--choc)}
.bell{position:absolute;right:8%;bottom:14px;font-size:34px;line-height:1;transform-origin:50% 90%}
.bell.ring{animation:ring .5s 2}
@keyframes ring{25%{transform:rotate(-18deg)}75%{transform:rotate(18deg)}}
.talkwrap{display:flex;flex-direction:column;align-items:center;gap:10px}
.talk{display:flex;align-items:center;gap:18px;justify-content:center}
.mic{position:relative;width:clamp(100px,17vmin,132px);aspect-ratio:1;border-radius:50%;border:5px solid var(--choc);color:#fff;cursor:pointer;padding:0;font:inherit;
  background:radial-gradient(circle at 35% 30%,#b294ff,#7a4fd6);box-shadow:0 7px 0 #4b2a99;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.mic .mi{font-size:clamp(36px,6.5vmin,50px);line-height:1}
.mic .ml{font-size:15px;font-weight:900;white-space:nowrap}.mic .ml .tz-b{color:#fff}
.mic:active{transform:translateY(3px);box-shadow:0 4px 0 #4b2a99}
.mic[data-st=on]{background:radial-gradient(circle at 35% 30%,#ff9fbd,#e8577a);box-shadow:0 7px 0 #a8324f}
.mic[data-st=on]::after{content:"";position:absolute;inset:-12px;border-radius:50%;border:5px solid #e8577a;animation:ping 1s infinite;pointer-events:none}
@keyframes ping{from{transform:scale(.9);opacity:1}to{transform:scale(1.28);opacity:0}}
.tb{min-width:58px;height:58px;border-radius:18px;border:3px solid #e3d3b8;background:#fff;font:inherit;font-size:26px;cursor:pointer;box-shadow:0 4px 0 rgba(0,0,0,.1);color:#1f9d61;font-weight:900}
#adult.big{padding:0 16px;background:#1f9d61;color:#fff;border-color:#1f9d61;font-size:20px;box-shadow:0 4px 0 #136b41}
#adult.big .tz-b{color:#fff}
.dish{display:flex;align-items:center;gap:10px;background:#fff;border:4px solid var(--choc);border-radius:999px;padding:4px 20px 4px 8px;
  font-family:var(--kai);font-size:clamp(36px,6vmin,52px);box-shadow:0 5px 0 rgba(0,0,0,.12)}
.dish .plate{display:inline-flex}.dish .plate .ic{width:58px;height:58px}
.dish .hit .tz-h,.hw .hit .tz-h{color:var(--berry)}
.dish.serve{animation:serve .6s cubic-bezier(.3,1.6,.5,1)}
@keyframes serve{from{transform:translateY(30px) scale(.5);opacity:0}}
.heard{background:#fff;border:3px dashed #c9b8a0;border-radius:18px;padding:6px 16px;font-weight:800;font-size:18px;text-align:center;line-height:1.6}
.heard .kai{font-size:1.5em}
.hints{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;align-items:center}
.hints .hl{font-weight:900;font-size:18px}
.hw{font:inherit;font-family:var(--kai);font-size:clamp(30px,5vmin,42px);background:#fff8d6;border:3px solid var(--lemon);border-radius:16px;padding:2px 12px;cursor:pointer;
  display:flex;align-items:center;gap:6px;color:var(--ink);box-shadow:0 4px 0 #e0b730}
.hw .spk{font-size:18px}
.tip{min-height:1.6em;font-weight:800;font-size:17px;color:var(--choc2);text-align:center;max-width:92vw}
@media (max-width:420px){.qline{font-size:18px;gap:6px}.hints .hl{display:none}.hw{font-size:28px}}
@media (orientation:portrait) and (max-height:740px){.ticket{padding-top:30px;min-width:124px}.ticket b{font-size:68px}.guest .ic{width:66px;height:66px}.counter{gap:24px}
  .mic{width:84px}.mic .mi{font-size:30px}.mic .ml{font-size:13px}.tb{min-width:50px;height:50px;font-size:22px}.talkwrap{gap:6px}.dish{font-size:30px}.dish .plate .ic{width:44px;height:44px}
  .heard{font-size:15px;padding:2px 12px;line-height:1.4}.hw{font-size:26px}.tip{font-size:15px;min-height:1.3em}.qcard{gap:8px}}
@media (max-height:500px){.qline{font-size:17px;line-height:1.3}.qline .ibtn{width:42px;height:42px;font-size:20px}.qcard{gap:6px}.ticket{padding:30px 14px 6px;min-width:110px}.ticket b{font-size:56px}.heard{font-size:15px;padding:2px 12px}.guest .ic{width:68px;height:68px}.bar{width:min(300px,44vw)}
  .mic{width:86px}.mic .mi{font-size:32px}.tb{min-width:50px;height:50px;font-size:22px}.dish{font-size:30px}.dish .plate .ic{width:44px;height:44px}.hw{font-size:28px}.talkwrap{gap:6px}.tip{font-size:15px}}''',
main='''<div class="qcard"><div class="qline" id="q"></div>
  <div class="counter"><span class="guest" id="guest"></span><div class="ticket" id="ticket"><span class="tk" id="tk"></span><b id="ch"></b></div></div>
  <div class="bar"><span class="bell" id="bell">🛎️</span></div></div>
<div class="talkwrap">
  <div class="dish" id="dish" hidden></div>
  <div class="heard" id="heard" hidden></div>
  <div class="talk"><button type="button" class="tb" id="hint" aria-label="提示">💡</button>
    <button type="button" class="mic" id="mic" data-st="idle"><span class="mi">🎤</span><span class="ml" id="micLbl"></span></button>
    <button type="button" class="tb" id="adult" aria-label="大人聽到說對了">✓</button></div>
  <div class="hints" id="hints" hidden></div>
  <div class="tip" id="tip"></div>
</div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,ZC={"日":["生日","日出"],"月":["月光","月亮[˙ㄌㄧㄤ]"],"山":["高山","山洞"],"木":["木頭[˙ㄊㄡ]","樹木"],"水":["喝水","水果"],"人":["大人","好人"],"手":["小手","招手"],"門":["開門","大門"],"小":["小船","小草"],"上":["地上","天上"],"走":["走路","走開"],"左":["左手","左邊"],"右":["右手","右邊"],"向":["向前","方向"],"魚":["金魚","小魚"],"也":["也是","我也要"],"來":["回來","來玩"],"加":["加油","加法"],"開":["張開","開心"],"出":["出去","日出"],"招":["招手","招呼[˙ㄏㄨ]"],"車":["火車","車子[˙ㄗ]"],"子":["車子[˙ㄗ]","房子[˙ㄗ]"],"地":["地上","草地"],"花":["紅花","花朵"],"朵":["花朵","雲朵"],"在":["現在","在家"],"笑":["笑臉","大笑"],"泡":["泡泡[˙ㄆㄠ]","水泡"],"玩":["好玩","玩具"],"大":["大家","大人"],"起":["一起","起來[˙ㄌㄞ]"],"好":["你好","好多"],"多":["好多","多少"],"我":["我們[˙ㄇㄣ]","我家"],"的":["我的[˙ㄉㄜ]","紅的[˙ㄉㄜ]"],"你":["你好","你們[˙ㄇㄣ]"],"抱":["抱抱","抱住"],"爸":["爸爸[˙ㄅㄚ]"],"到":["看到","到家"],"青":["青草","青菜"],"叫":["大叫","叫人"],"下":["下雨","一下子[˙ㄗ]"],"那":["那裡[˙ㄌㄧ]","那個[˙ㄍㄜ]"],"和":["和好","和平"],"要":["要去","想要"],"他":["他們[˙ㄇㄣ]","其他"],"朋":["朋友[˙ㄧㄡ]"],"友":["朋友[˙ㄧㄡ]","好友"],"外":["外面[˙ㄇㄧㄢ]","外星人"],"住":["住家","住在"],"個":["一個[˙ㄍㄜ]","個子[˙ㄗ]"],"們":["我們[˙ㄇㄣ]","你們[˙ㄇㄣ]"],"這":["這裡[˙ㄌㄧ]","這個[˙ㄍㄜ]"],"裡":["家裡[˙ㄌㄧ]","這裡[˙ㄌㄧ]"],"有":["有人","沒有"],"沒":["沒有","沒事"],"是":["不是","是的[˙ㄉㄜ]"],"什":["什麼[˙ㄇㄜ]"],"麼":["什麼[˙ㄇㄜ]","怎麼[˙ㄇㄜ]"],"金":["金魚","黃金"],"說":["說話","小說"],"句":["句子[˙ㄗ]","一句"],"話":["說話","電話"],"兩":["兩個[˙ㄍㄜ]","兩人"],"都":["都是","全都"],"悄":["悄悄話"],"尾":["尾巴[˙ㄅㄚ]","結尾"],"巴":["尾巴[˙ㄅㄚ]","嘴巴[˙ㄅㄚ]"],"滿":["滿天","滿滿"],"紅":["紅花","紅色"],"春":["春天","春風"],"貼":["貼紙","貼上"],"呢":["你呢[˙ㄋㄜ]","我呢[˙ㄋㄜ]"],"了":["好了[˙ㄌㄜ]","走了[˙ㄌㄜ]"],"請":["請問","請坐"],"天":["天空","春天"],"家":["大家","回家"],"把":["一把","把手"],"不":["不要","不好"],"房":["房子[˙ㄗ]","房間"],"福":["幸福","福氣"],"前":["向前","前面[˙ㄇㄧㄢ]"],"風":["大風","風車"],"吹":["吹風","吹氣"],"停":["不停","停車"],"跑":["跑步","快跑"],"火":["火車","火山"],"洞":["山洞","洞口"],"又":["又來","又是"],"堆":["一堆","沙堆"],"心":["開心","小心"],"問":["請問","問題"],"草":["小草","草地"],"高":["高山","很高"],"星":["星星[˙ㄒㄧㄥ]","星球"],"少":["多少","很少"],"太":["太陽","太多"],"去":["出去","回去"],"彩":["彩色","七彩"],"想":["想要","想家"],"爬":["爬山","爬樹"],"看":["好看","看見"],"棉":["棉花","棉花糖"],"池":["水池","池子[˙ㄗ]"],"秋":["秋天","秋千"],"千":["秋千","一千"],"空":["天空","空氣"],"早":["早上[˙ㄕㄤ]","早安"],"田":["田地","水田"],"誰":["是誰"],"陪":["陪我","陪伴[ㄅㄢˋ]"],"回":["回家","回音"],"音":["回音","音樂[ㄩㄝˋ]"],"谷":["山谷"],"嗎":["好嗎[˙ㄇㄚ]","是嗎[˙ㄇㄚ]"],"哈":["哈哈","哈哈大笑"]};
  // 這一關說明文字用到、但題庫注音表沒有的字
  Object.entries({語:"ㄩˇ",詞:"ㄘˊ",按:"ㄢˋ",辦:"ㄅㄢˋ",使:"ㄕˇ",克:"ㄎㄜˋ",網:"ㄨㄤˇ",板:"ㄅㄢˇ",換:"ㄏㄨㄢˋ"}).forEach(([k,v])=>{if(!Z.ZY[k])Z.ZY[k]=v});
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  let canMic=!!SR;
  const GUESTS=["cat","dog","rabbit","bear","pig","duck","monkey","frog","tiger","elephant"];
  const FOOD=["hamburger","noodles","pizza","juice","cake","ice cream","cookie","bread","milk","spaghetti"];
  const GOT=EN.icon("hamburger");
  // 「字[注音]」寫法拆成 [字, 注音]
  const toks=w=>{const out=[],cs=[...w];for(let i=0;i<cs.length;i++){if(cs[i+1]==="["){const j=cs.indexOf("]",i);out.push([cs[i],cs.slice(i+2,j).join("")]);i=j}else out.push([cs[i],Z.ZY[cs[i]]||""])}return out};
  const ALL=[...new Set(Object.values(ZC).flat())];
  // 一個語詞（標好注音）：課本語詞用課本的注音，範例詞用標好的注音；要說的那個字變紅色
  function wordHTML(w,c){const p=TZ.plain(w);let t;
    if(Z.ciZy[p])t=[...p].map((ch,i)=>[ch,Z.ciZy[p][i]]);else t=toks(ALL.find(x=>TZ.plain(x)===p)||p);
    return t.map(([ch,z])=>TZ.charHTML(ch,z,ch===c?"hit":"")).join("")}
  // 提示的語詞：先找範圍裡課本的語詞，再用範例詞
  function hintsFor(c){
    const L=TZ.lessons(),[a,b]=TZ.range(),seen=new Set(),out=[];
    [...L.slice(a,b+1).flatMap(l=>l.ci),...(ZC[c]||[])].forEach(w=>{const p=TZ.plain(w);if(p.includes(c)&&[...p].length>=2&&!seen.has(p)){seen.add(p);out.push(w)}});
    return out.slice(0,2)}
  const tip=t=>{$("tip").innerHTML=t?TZ.zy(t):""};
  let cur="",food="",guest="",rec=null,listening=false,served=[];
  function setMic(st){$("mic").dataset.st=st;$("micLbl").innerHTML=TZ.zy(st==="on"?"我在聽":canMic?"按我說":"說出來")}
  function needAdult(t){canMic=false;setMic("idle");$("adult").classList.add("big");$("adult").innerHTML="✓ "+TZ.zy("說對了");if(t)tip(t)}
  $("tk").innerHTML=TZ.zy("點餐單");
  const prompt=()=>TZ.say(`${cur}。用${cur}，說一個語詞。`);

  const api=TZ.run({key:"town-say",gotIcon:GOT,
    finale:done=>{TZ.finale(`<div class="frow">${served.slice(-6).map(g=>EN.icon(g)).join("")}</div>`,"客人都點好餐了，謝謝光臨！",done,3000)},
    help:"點餐櫃台。點餐單上有一個字，請你用這個字說一個語詞，例如看到「火」，可以說「火車」。按一下紫色的麥克風再說，說完等一下。說不出來可以按燈泡看例子。如果平板聽不懂，大人聽到說對了，可以按旁邊的勾勾。",
    build:n=>{served=[];return TZ.deal(TZ.pool(false).filter(c=>hintsFor(c).length),n)},
    show:(c)=>{
      cur=c;food=FOOD[api.S.i%FOOD.length];guest=GUESTS[Math.floor(Math.random()*GUESTS.length)];
      const g=$("guest");g.innerHTML=EN.icon(guest);g.className="guest";void g.offsetWidth;g.classList.add("in");
      const tk=$("ticket");tk.classList.remove("pop");void tk.offsetWidth;tk.classList.add("pop");
      $("ch").innerHTML=TZ.charHTML(c,Z.ZY[c]||"");
      $("q").innerHTML=TZ.zy("用這個字，說一個語詞。")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
      $("say").onclick=prompt;
      ["dish","heard","hints"].forEach(id=>$(id).hidden=true);
      if(canMic){$("adult").classList.remove("big");$("adult").textContent="✓"}
      setMic("idle");tip(canMic?"按麥克風，說出一個有這個字的語詞。":"說出來給大人聽，說對了請大人按 ✓。");
      setTimeout(()=>{if(!api.S.busy&&cur===c)prompt()},700);
    }});

  // 聽到的話裡有沒有這個字（或同音字）
  const hanOnly=alts=>alts.map(t=>(String(t).match(/[\\u4e00-\\u9fff]/g)||[]).join("")).filter(Boolean);
  // 聽到的話裡有說對的語詞就回傳那個詞，沒有就回傳 null
  function hit(cands){
    const c=cur,trim=t=>{const a=[...t];if(a.length<=5)return t;const i=a.indexOf(c);return a.slice(Math.max(0,i-2),Math.max(0,i-2)+5).join("")};
    for(const t of cands)if([...t].length>=2&&t.includes(c))return trim(t);
    // 平板常把字聽成同音的別字，同音也算對（顯示成正確的字）
    const zc=Z.ZY[c];
    if(zc)for(const t of cands){const a=[...t],i=a.findIndex(ch=>Z.ZY[ch]===zc);if(a.length>=2&&i>=0){a[i]=c;return trim(a.join(""))}}
    return null;
  }
  function judge(alts){
    if(api.S.busy)return;
    const c=cur,zc=Z.ZY[c],cands=hanOnly(alts);
    if(!cands.length){tip("沒有聽到，再按一次麥克風說說看。");TZ.say("沒有聽到，再說一次");return}
    const w=hit(cands);if(w)return success(w);
    const t0=cands[0];api.bad();
    $("heard").innerHTML=TZ.zy("我聽到：")+`<span class="kai">${TZ.zy(t0)}</span>`;$("heard").hidden=false;
    if([...t0].length<2&&(t0===c||Z.ZY[t0]===zc)){tip("要說兩個字以上的語詞喔！");TZ.say(`要說兩個字以上的語詞喔，${c}什麼？`)}
    else{tip(`裡面沒有「${c}」喔，再說一次！`);TZ.say(`裡面沒有${c}喔，再說一次`)}
    if(api.S.tries>=2)setTimeout(()=>{if(!api.S.busy)showHints()},1600);
  }
  function success(word){
    if(api.S.busy)return;api.ok();listening=false;try{rec&&rec.abort()}catch(e){}setMic("idle");served.push(guest);
    const d=$("dish");d.innerHTML=`<span class="plate">${EN.icon(food)}</span><span class="dw">${word?wordHTML(word,cur):TZ.charHTML(cur,Z.ZY[cur]||"","hit")}</span>`;
    d.hidden=false;d.classList.remove("serve");void d.offsetWidth;d.classList.add("serve");
    ["heard","hints"].forEach(id=>$(id).hidden=true);tip("");
    const b=$("bell");b.classList.remove("ring");void b.offsetWidth;b.classList.add("ring");EN.sfx.coin();
    const g=$("guest");g.classList.remove("in","happy");void g.offsetWidth;g.classList.add("happy");
    setTimeout(()=>TZ.flyGot(d.querySelector(".plate"),GOT),700);
    api.next(1800);
  }
  function showHints(){
    if(api.S.busy)return;const hs=hintsFor(cur);if(!hs.length)return;api.S.tries=Math.max(api.S.tries,1);
    $("hints").innerHTML=`<span class="hl">${TZ.zy("可以說：")}</span>`+hs.map(w=>`<button type="button" class="hw" data-w="${TZ.plain(w)}">${wordHTML(w,cur)}<span class="spk">🔊</span></button>`).join("");
    $("hints").hidden=false;$("hints").querySelectorAll(".hw").forEach(x=>x.onclick=()=>TZ.say(x.dataset.w));
    tip(canMic?"聽一聽，再按麥克風說一次！":"說出來給大人聽，說對了請大人按 ✓。");
    TZ.say("可以說，"+hs.map(w=>TZ.plain(w)).join("，或是")+"。換你說說看！");
  }
  $("hint").onclick=()=>showHints();
  $("adult").onclick=()=>{if(!api.S.busy&&cur)success(null)};
  // ---- 聽小朋友說話 ----
  // 一直聽到說完為止（小朋友常常想一下才開口），邊聽邊把聽到的字顯示出來；聽到說對的詞就馬上停。
  // 有些平板一按就馬上結束（還沒開始聽），這時自動再聽一次。
  let live="",judged=false,startAt=0,retried=false,stopT=null;
  const stopRec=()=>{clearTimeout(stopT);try{rec&&rec.stop()}catch(e){}};
  function showLive(t){const h=hanOnly([t])[0];if(!h)return;$("heard").innerHTML=TZ.zy("我聽到：")+`<span class="kai">${TZ.zy(h)}</span>`;$("heard").hidden=false}
  function listen(){
    if(api.S.busy||!cur)return;
    try{rec=new SR();rec.lang="zh-TW";rec.interimResults=true;rec.maxAlternatives=5;rec.continuous=true}catch(e){needAdult("這台平板不能聽，說給大人聽，說對了請大人按 ✓。");return}
    live="";judged=false;
    rec.onresult=e=>{
      const alts=[];let fin=false;
      live=[...e.results].map(r=>r[0].transcript).join("");alts.push(live);
      for(let i=e.resultIndex;i<e.results.length;i++){const r=e.results[i];for(let k=0;k<r.length;k++)alts.push(r[k].transcript);if(r.isFinal)fin=true}
      showLive(live);
      if(hit(hanOnly(alts))){judged=true;stopRec();judge(alts);return}
      if(fin){judged=true;stopRec();judge(alts)}
    };
    rec.onerror=e=>{const er=e.error;
      if(er==="not-allowed"||er==="service-not-allowed"||er==="audio-capture"){judged=true;needAdult("沒辦法使用麥克風。說給大人聽，說對了請大人按 ✓。")}
      else if(er==="network"){judged=true;needAdult("連不上網路，聽不到。說給大人聽，說對了請大人按 ✓。")}};
    rec.onend=()=>{listening=false;clearTimeout(stopT);if(api.S.busy)return;setMic("idle");
      if(judged)return;
      if(live){judge([live]);return}
      if(canMic&&!retried&&Date.now()-startAt<1500){retried=true;setTimeout(listen,300);return}
      tip("沒有聽到聲音，按一下麥克風，再大聲說一次。")};
    try{rec.start();listening=true;startAt=Date.now();setMic("on");tip("說吧！我在聽。");stopT=setTimeout(stopRec,8000)}
    catch(e){needAdult("這台平板不能聽，說給大人聽，說對了請大人按 ✓。")}
  }
  $("mic").onclick=()=>{
    if(api.S.busy||!cur)return;EN.unlock();
    if(!canMic){tip("說出來給大人聽，說對了請大人按 ✓。");TZ.say("說出來給大人聽，說對了請大人按勾勾");$("adult").classList.add("big");return}
    if(listening){stopRec();return}
    // 先停掉念題目的聲音，等一下下再開始聽（平板要先把喇叭切到麥克風）
    EN.stop();retried=false;$("heard").hidden=true;setMic("on");tip("");
    setTimeout(listen,300);
  };
  setMic("idle");
})();''')

# ---------- 午茶說故事（成語故事） ----------
# 一題一個成語：先一頁一頁聽故事（圖＋句子，會念出來），聽完選出是哪一個成語，再看成語的意思。
# 題數超過 10 題時，後面改成「成語少了一個字」：看缺字的注音和意思，選出那個字。
page("town-story.html",title="午茶說故事",icon="🫖",sub="喝杯下午茶，聽成語故事，或是考考成語少了哪一個字！",
style='''.book{position:relative;width:min(640px,94vw);background:#fffdf6;border:5px solid var(--choc);border-radius:26px;padding:28px clamp(14px,3vmin,26px) 14px;
  box-shadow:0 8px 0 rgba(0,0,0,.12);display:flex;flex-direction:column;align-items:center;gap:10px}
.book .bt{position:absolute;left:18px;top:-18px;background:#14a99c;color:#fff;font-weight:900;font-size:16px;border-radius:999px;padding:1px 12px;border:3px solid #fff}
.book .bt .tz-b{color:#fff}
.book .pot{position:absolute;right:-10px;top:-30px;font-size:42px;line-height:1;transform-origin:50% 90%;animation:pot 2.4s ease-in-out infinite}
@keyframes pot{0%,70%,100%{transform:none}80%{transform:rotate(-14deg)}90%{transform:rotate(6deg)}}
.scene{display:flex;gap:.12em;justify-content:center;align-items:flex-end;font-size:clamp(56px,11vmin,92px);line-height:1.15;min-height:1.2em}
.scene span{display:inline-block;animation:spop .5s cubic-bezier(.3,1.6,.5,1) both}
@keyframes spop{from{transform:scale(.2) translateY(30px);opacity:0}}
.stx{font-size:clamp(22px,4vmin,30px);font-weight:800;line-height:1.9;max-width:100%;text-align:left}
.stx.in{animation:sfade .35s both}
@keyframes sfade{from{opacity:0;transform:translateY(8px)}}
.nav{display:flex;align-items:center;gap:12px}
.pdots{display:flex;gap:6px}.pdots i{width:11px;height:11px;border-radius:50%;background:#e3d3b8}.pdots i.on{background:#14a99c}
.tb{min-width:54px;height:54px;border-radius:16px;border:3px solid #e3d3b8;background:#fff;font:inherit;font-size:24px;cursor:pointer;box-shadow:0 4px 0 rgba(0,0,0,.1);color:var(--choc);font-weight:900;padding:0 12px}
.tb:disabled{opacity:.3}
.opt.mode{min-width:120px}.opt.mode .mi{display:block;font-size:30px;line-height:1.1}.opt.mode small{display:block;font-size:16px;font-weight:800;opacity:1}
.opt.mode[aria-pressed="true"] .tz-b{color:#fff}
.tb.go{background:#14a99c;border-color:#14a99c;color:#fff;box-shadow:0 4px 0 #0b6f66;font-size:20px}.tb.go .tz-b{color:#fff}
.tb.ready{animation:nudge 1.1s ease-in-out infinite}
@keyframes nudge{50%{transform:translateX(5px);box-shadow:0 0 0 6px rgba(20,169,156,.3),0 4px 0 rgba(0,0,0,.1)}}
.quiz{display:flex;flex-direction:column;align-items:center;gap:clamp(10px,2.2vmin,20px)}
.idi{display:flex;align-items:center;gap:2px;font-family:var(--kai);font-size:clamp(36px,6vmin,50px);background:#fff;border:4px solid var(--choc);border-radius:18px;
  padding:4px 14px;box-shadow:0 5px 0 rgba(0,0,0,.12);color:var(--ink);line-height:1.1}
.idi .tz-b{font-size:max(.3em,12px)}
.choices.col{flex-direction:column;align-items:center}
.big4{font-size:clamp(48px,9vmin,72px);padding:6px 18px}
.big4 .hole{display:inline-grid;place-items:center;width:1.15em;height:1.2em;border:3px dashed var(--berry);border-radius:12px;background:#fff7fa;margin:0 2px}
.big4 .hole .tz-b{font-size:.3em}
.big4 .hole.fill{border-style:solid;border-color:#1f9d61;background:#eafff2}
.cc{width:clamp(84px,14vmin,112px);aspect-ratio:1;background:#fff;border:4px solid var(--choc);border-radius:20px;font-family:var(--kai);font-size:clamp(48px,8vmin,66px);box-shadow:0 5px 0 rgba(0,0,0,.12)}
.cc .tz-b{font-size:14px}
.mean{background:#e9fbf6;border:3px solid #14a99c;border-radius:18px;padding:6px 16px;font-weight:800;font-size:clamp(18px,3vmin,24px);line-height:1.8;max-width:min(640px,94vw);text-align:center}
.mean .kai{font-weight:400;font-size:1.2em}
.mean.pop{animation:serve .5s cubic-bezier(.3,1.6,.5,1)}
@keyframes serve{from{transform:scale(.6);opacity:0}}
@media (max-width:420px){.qline{font-size:19px;gap:6px}}
@media (orientation:portrait) and (max-height:740px){.scene{font-size:56px}.stx{font-size:20px;line-height:1.75}.book{gap:6px;padding-top:24px}.idi{font-size:34px}.big4{font-size:50px}.cc{width:80px;font-size:46px}.mean{font-size:17px}}
@media (max-height:500px){.book{width:min(760px,94vw);gap:4px;padding:22px 16px 8px}.scene{font-size:44px}.stx{font-size:18px;line-height:1.65}.tb{min-width:46px;height:46px;font-size:20px}
  .quiz{gap:6px}.idi{font-size:28px;padding:2px 10px}.big4{font-size:42px}.cc{width:68px;font-size:40px}.mean{font-size:15px;line-height:1.6;padding:4px 12px}.choices{gap:8px}}''',
main='''<div class="book" id="book"><span class="bt" id="bt"></span><span class="pot">🫖</span>
  <div class="scene" id="scene"></div><div class="stx" id="stx"></div>
  <div class="nav"><button type="button" class="tb" id="prev" aria-label="上一頁">◀</button><span class="pdots" id="pdots"></span>
    <button type="button" class="tb" id="rep" aria-label="再念一次">🔊</button><button type="button" class="tb" id="next" aria-label="下一頁">▶</button></div></div>
<div class="quiz" id="quiz" hidden><div class="qline" id="q"></div><div class="idi big4" id="show4" hidden></div><div class="choices" id="choices"></div><div class="mean" id="mean" hidden></div><button type="button" class="tb go" id="skip" hidden>下一題 ▶</button></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI,ST=[{"w":"守株待兔","zy":"ㄕㄡˇ ㄓㄨ ㄉㄞˋ ㄊㄨˋ","m":"不努力，只想等好運氣自己來。","p":[["👨‍🌾🌳🐇","有一個農夫在田裡工作，一隻兔子[˙ㄗ]跑過來，撞到樹昏倒了。"],["👨‍🌾🐇😄","農夫撿到兔子[˙ㄗ]，好高興。"],["🪑👨‍🌾🌳","從此他不工作了，天天坐在樹旁邊，等兔子[˙ㄗ]再撞過來。"],["🌾🌾🌳","田裡長[ㄓㄤˇ]滿了[˙ㄌㄜ]草，兔子[˙ㄗ]再也沒有來。"]]},{"w":"揠苗助長","zy":"ㄧㄚˋ ㄇㄧㄠˊ ㄓㄨˋ ㄓㄤˇ","m":"太心急，不照順序做，反而把事情[˙ㄑㄧㄥ]弄壞了。","p":[["👨🌱🌱","有一個人種[ㄓㄨㄥˋ]了[˙ㄌㄜ]稻子[˙ㄗ]，他覺[ㄐㄩㄝˊ]得[˙ㄉㄜ]稻子[˙ㄗ]長[ㄓㄤˇ]得[˙ㄉㄜ]太慢了[˙ㄌㄜ]。","有一個人，眾了稻子，他覺得稻子長得太慢了。"],["💪🌱⬆️","他把每一株小苗都往上拔高一點。"],["🥀🥀😢","第二天，小苗全都枯死了[˙ㄌㄜ]。"]]},{"w":"畫蛇添足","zy":"ㄏㄨㄚˋ ㄕㄜˊ ㄊㄧㄢ ㄗㄨˊ","m":"做了不需要做的事，反而不好。","p":[["🖌️🐍🎁","大家比賽畫蛇，先畫好的[˙ㄉㄜ]人可以得[ㄉㄜˊ]到獎品。"],["🐍🦶😏","有一個人很快就畫好了[˙ㄌㄜ]，他說：「我還[ㄏㄞˊ]可以幫蛇畫上腳！」"],["🎁🏃😮","別人說：「蛇沒有腳！」獎品就被拿走了[˙ㄌㄜ]。"]]},{"w":"狐假虎威","zy":"ㄏㄨˊ ㄐㄧㄚˇ ㄏㄨˇ ㄨㄟ","m":"靠別人的力量來嚇人。","p":[["🐯🦊","老虎抓到一隻狐狸[˙ㄌㄧ]，狐狸[˙ㄌㄧ]說：「我是森林之王，不信你跟我走！」"],["🦊🐯🐰🐿️","狐狸[˙ㄌㄧ]走在前面[˙ㄇㄧㄢ]，老虎跟在後面[˙ㄇㄧㄢ]，動物們[˙ㄇㄣ]看到都跑走了[˙ㄌㄜ]。"],["🐯🤔","老虎以為[ㄨㄟˊ]大家怕狐狸[˙ㄌㄧ]，其實大家怕的[˙ㄉㄜ]是老虎。"]]},{"w":"井底之蛙","zy":"ㄐㄧㄥˇ ㄉㄧˇ ㄓ ㄨㄚ","m":"看到的東西[˙ㄒㄧ]很少，就以為[ㄨㄟˊ]自己什麼[˙ㄇㄜ]都知道[˙ㄉㄠ]。","p":[["🕳️🐸","有一隻青蛙住在一口井的[˙ㄉㄜ]底下。"],["🐸⭕☁️","牠抬頭往上看，天空只有井口那麼[˙ㄇㄜ]大。"],["🐢🌊🐸","海龜告訴[˙ㄙㄨ]牠，外面[˙ㄇㄧㄢ]的[˙ㄉㄜ]世界很大很大，青蛙一點也不相信。"]]},{"w":"亡羊補牢","zy":"ㄨㄤˊ ㄧㄤˊ ㄅㄨˇ ㄌㄠˊ","m":"事情[˙ㄑㄧㄥ]做錯了[˙ㄌㄜ]，趕快改正還來得及。","p":[["🐑🕳️🐺","有一個人的[˙ㄉㄜ]羊圈[ㄐㄩㄢˋ]破了[˙ㄌㄜ]一個[˙ㄍㄜ]洞，晚上[˙ㄕㄤ]野狼跑進來，叼走一隻羊。"],["👨🐑","鄰居說：「快把洞補好吧[˙ㄅㄚ]！」他說：「羊都丟了[˙ㄌㄜ]，補也沒有用。」"],["🔨🐑🐑","第二天羊又少了[˙ㄌㄜ]一隻，他趕快把洞補好，羊就再也沒有少了[˙ㄌㄜ]。"]]},{"w":"對牛彈琴","zy":"ㄉㄨㄟˋ ㄋㄧㄡˊ ㄊㄢˊ ㄑㄧㄣˊ","m":"說話不看對象，對方聽不懂。","p":[["🧑🎵🐂","有一個人很會彈琴，他對一頭牛彈好聽的[˙ㄉㄜ]曲[ㄑㄩˇ]子[˙ㄗ]。"],["🐂🌿","牛只顧低頭吃草，一點也聽不懂。"],["🦟🐄🐂","他改彈像蚊子[˙ㄗ]和小牛叫的[˙ㄉㄜ]聲音，牛才搖搖尾巴[˙ㄅㄚ]，抬起頭來聽。","他改談，像蚊子和小牛叫的聲音，牛才搖搖尾巴，抬起頭來聽。"]]},{"w":"葉公好龍","zy":"ㄕㄜˋ ㄍㄨㄥ ㄏㄠˋ ㄌㄨㄥˊ","m":"嘴巴[˙ㄅㄚ]說喜歡[˙ㄏㄨㄢ]，其實不是真的[˙ㄉㄜ]喜歡[˙ㄏㄨㄢ]。","p":[["🧓🐉🖼️","葉[ㄕㄜˋ]公說他最喜歡[˙ㄏㄨㄢ]龍，家裡[˙ㄌㄧ]到處[ㄔㄨˋ]都畫了[˙ㄌㄜ]龍。","社公說他最喜歡龍，家裡到處都畫了龍。"],["☁️🐉","天上的[˙ㄉㄜ]真龍知道[˙ㄉㄠ]了[˙ㄌㄜ]，就飛來看他。"],["🐉😱🏃","葉[ㄕㄜˋ]公一看到真的[˙ㄉㄜ]龍，嚇得[˙ㄉㄜ]趕快逃走了[˙ㄌㄜ]。","社公一看到真的龍，嚇得趕快逃走了。"]],"sw":"社公浩龍"},{"w":"盲人摸象","zy":"ㄇㄤˊ ㄖㄣˊ ㄇㄛ ㄒㄧㄤˋ","m":"只知[ㄓ]道[˙ㄉㄠ]一小部分，就以為[ㄨㄟˊ]知道[˙ㄉㄠ]全部。","p":[["🧑‍🦯🧑‍🦯🐘","幾個看不見的[˙ㄉㄜ]人，想知道[˙ㄉㄠ]大象長[ㄓㄤˇ]什麼[˙ㄇㄜ]樣子[˙ㄗ]。"],["🐘👃🦵","摸到鼻子[˙ㄗ]的[˙ㄉㄜ]人說：「大象像水管。」摸到腿的[˙ㄉㄜ]人說：「大象像柱子[˙ㄗ]。」"],["🐘❓","他們[˙ㄇㄣ]都只摸到一點點，就以為[ㄨㄟˊ]知道[˙ㄉㄠ]大象的[˙ㄉㄜ]樣子[˙ㄗ]。"]]},{"w":"愚公移山","zy":"ㄩˊ ㄍㄨㄥ ㄧˊ ㄕㄢ","m":"做事不怕困難，一直努力就會成功。","p":[["🏔️🏠🏔️","愚公家門前有兩座大山，出門很不方便。"],["👴⛏️🪨","他和家人每天一起挖山、搬石頭[˙ㄊㄡ]。"],["👴👦👶","他說：「我做不完，還[ㄏㄞˊ]有兒子[˙ㄗ]、孫子[˙ㄗ]會一直做下去！」"],["✨🏔️🕊️","天神被他感動了[˙ㄌㄜ]，就把大山搬走了[˙ㄌㄜ]。"]]},{"w":"刻舟求劍","zy":"ㄎㄜˋ ㄓㄡ ㄑㄧㄡˊ ㄐㄧㄢˋ","m":"不知道[˙ㄉㄠ]變通，方法用錯了[˙ㄌㄜ]。","p":[["⛵🗡️💦","有一個人坐船過河，他的[˙ㄉㄜ]劍不小心掉進水裡了[˙ㄌㄜ]。"],["🔪⛵","他在船邊刻了[˙ㄌㄜ]一個記號，說：「我的[˙ㄉㄜ]劍是從這裡掉下去的[˙ㄉㄜ]。」"],["🏝️🤿❓","船停了[˙ㄌㄜ]，他從記號那裡跳下水找劍，可是船早就開走了[˙ㄌㄜ]，劍找不到了[˙ㄌㄜ]。"]]},{"w":"掩耳盜鈴","zy":"ㄧㄢˇ ㄦˇ ㄉㄠˋ ㄌㄧㄥˊ","m":"自己騙自己，以為[ㄨㄟˊ]別人不知道[˙ㄉㄠ]。","p":[["🔔🚪","有一個小偷，想偷別人家門口的[˙ㄉㄜ]大鈴鐺[˙ㄉㄤ]。"],["🙉🔔","他怕鈴鐺[˙ㄉㄤ]會響，就用手把自己的[˙ㄉㄜ]耳朵[˙ㄉㄨㄛ]蓋起來。"],["🔔👂👮","他以為[ㄨㄟˊ]自己聽不到，別人也聽不到，結果大家都聽到了[˙ㄌㄜ]，馬上抓住他。"]]},{"w":"杞人憂天","zy":"ㄑㄧˇ ㄖㄣˊ ㄧㄡ ㄊㄧㄢ","m":"擔心不會發生的[˙ㄉㄜ]事。","p":[["👨☁️😟","杞國有一個人，每天都擔心天會掉下來。"],["😰🍚🌙","他擔心得[˙ㄉㄜ]吃不下飯，晚上[˙ㄕㄤ]也睡不好。"],["👫☀️","朋友[˙ㄧㄡ]告訴[˙ㄙㄨ]他：「天很高很高，不會掉下來的[˙ㄉㄜ]。」他才放心了[˙ㄌㄜ]。"]]},{"w":"鷸蚌相爭","zy":"ㄩˋ ㄅㄤˋ ㄒㄧㄤ ㄓㄥ","m":"兩個人爭來爭去，讓別人得[ㄉㄜˊ]到好處[ㄔㄨˋ]。","p":[["🐚☀️🐦","一隻河蚌張開殼曬太陽，一隻鷸鳥飛來啄牠的[˙ㄉㄜ]肉。"],["🐚🐦😠","河蚌馬上把殼合起來，夾住鷸鳥的[˙ㄉㄜ]嘴，兩個都不肯放開。"],["🎣👴","一個漁夫走過來，一下子[˙ㄗ]就把牠們[˙ㄇㄣ]兩個都抓走了[˙ㄌㄜ]。"]]},{"w":"自相矛盾","zy":"ㄗˋ ㄒㄧㄤ ㄇㄠˊ ㄉㄨㄣˋ","m":"說的[˙ㄉㄜ]話前後不一樣。","p":[["🧑🗡️🛡️","有一個人在市場賣矛和盾。"],["🗡️💪🛡️","他說：「我的[˙ㄉㄜ]矛最利，什麼[˙ㄇㄜ]都刺得[˙ㄉㄜ]穿！我的[˙ㄉㄜ]盾最硬，什麼[˙ㄇㄜ]都刺不穿！」"],["🤔❓","有人問：「用你的[˙ㄉㄜ]矛刺你的[˙ㄉㄜ]盾，會怎麼[˙ㄇㄜ]樣呢[˙ㄋㄜ]？」他就說不出話來了[˙ㄌㄜ]。"]]},{"w":"濫竽充數","zy":"ㄌㄢˋ ㄩˊ ㄔㄨㄥ ㄕㄨˋ","m":"沒有真本事，混在裡面湊數。","p":[["👑🎶🎶","國王喜歡[˙ㄏㄨㄢ]聽很多人一起吹竽。"],["😅🎶","有一個人不會吹，也混在裡面假裝吹，一直沒有被發現。"],["👑🎵😱","新國王喜歡[˙ㄏㄨㄢ]一個一個聽，這個人只好偷偷逃走了[˙ㄌㄜ]。"]]},{"w":"塞翁失馬","zy":"ㄙㄞˋ ㄨㄥ ㄕ ㄇㄚˇ","m":"壞事也可能變成好事。","p":[["👴🐎💨","塞[ㄙㄞˋ]翁家的[˙ㄉㄜ]馬跑走了[˙ㄌㄜ]，鄰居都替他難過。","賽翁家的馬跑走了，鄰居都替他難過。"],["🐎🐎😃","過了[˙ㄌㄜ]幾天，馬回來了[˙ㄌㄜ]，還帶回一匹好馬。"],["🤕🏠😊","後來兒子[˙ㄗ]騎馬摔傷了[˙ㄌㄜ]腳，卻因為這樣不用去打仗，平平安安的[˙ㄉㄜ]。"]],"sw":"賽翁失馬"},{"w":"朝三暮四","zy":"ㄓㄠ ㄙㄢ ㄇㄨˋ ㄙˋ","m":"說法換來換去，其實都一樣。","p":[["👴🐒🌰","有一個老爺爺[˙ㄧㄝ]養了[˙ㄌㄜ]很多猴子[˙ㄗ]，每天餵牠們[˙ㄇㄣ]吃栗子[˙ㄗ]。"],["🐒😠","他說：「早上[˙ㄕㄤ]給三顆，晚上[˙ㄕㄤ]給四顆。」猴子[˙ㄗ]都很生氣。"],["🐒😄","他改說：「早上[˙ㄕㄤ]給四顆，晚上[˙ㄕㄤ]給三顆。」猴子[˙ㄗ]就高興了[˙ㄌㄜ]，其實一天還是七顆。"]],"sw":"招三暮四"},{"w":"磨杵成針","zy":"ㄇㄛˊ ㄔㄨˇ ㄔㄥˊ ㄓㄣ","m":"只要不放棄，再難的[˙ㄉㄜ]事也能做到。","p":[["👦📚💤","李白小時候[˙ㄏㄡ]不愛念書，常常跑出去玩。"],["👵🪨","他看到一位老奶奶[˙ㄋㄞ]，在石頭[˙ㄊㄡ]上磨一根鐵棒。"],["🪡✨📖","老奶奶[˙ㄋㄞ]說：「我要把它磨成一根針。」李白聽了[˙ㄌㄜ]，從此認真念書。"]]},{"w":"指鹿為馬","zy":"ㄓˇ ㄌㄨˋ ㄨㄟˊ ㄇㄚˇ","m":"故意把對的[˙ㄉㄜ]說成錯的[˙ㄉㄜ]。","p":[["🦌🤴","有一個壞大臣，牽了[˙ㄌㄜ]一隻鹿給皇帝看。"],["🦌🐎❓","他說：「這是一匹馬。」皇帝說：「這明明是鹿呀[˙ㄧㄚ]！」"],["😨🙊","大臣們[˙ㄇㄣ]都怕他，有的[˙ㄉㄜ]說是馬，不敢說是鹿。"]]},{"w":"南轅北轍","zy":"ㄋㄢˊ ㄩㄢˊ ㄅㄟˇ ㄓㄜˊ","m":"做的[˙ㄉㄜ]事和想要的[˙ㄉㄜ]相反，越做越遠。","p":[["🧑🐎🧭","有一個人要去南方，卻坐馬車一直往北走。"],["🙋❗","別人提醒他：「你走錯方向了[˙ㄌㄜ]！」"],["🐎💨😄","他說：「沒關係[˙ㄒㄧ]，我的[˙ㄉㄜ]馬跑得[˙ㄉㄜ]快！」結果離南方越來越遠。"]]},{"w":"驚弓之鳥","zy":"ㄐㄧㄥ ㄍㄨㄥ ㄓ ㄋㄧㄠˇ","m":"被嚇過一次，以後一點小事就很害怕。","p":[["🏹🐦","有一個射箭高手，看到一隻受傷的[˙ㄉㄜ]鳥飛過。"],["🏹🎵","他沒有放箭，只拉了[˙ㄌㄜ]一下弓弦，發出「嗡」的[˙ㄉㄜ]一聲。"],["🐦⬇️","那隻鳥嚇了[˙ㄌㄜ]一大跳，用力往上飛，傷口裂開，就掉下來了[˙ㄌㄜ]。"]]},{"w":"鑿壁偷光","zy":"ㄗㄠˊ ㄅㄧˋ ㄊㄡ ㄍㄨㄤ","m":"家裡很窮，也想辦法努力讀書。","p":[["👦🕯️❌","匡衡家裡很窮，晚上[˙ㄕㄤ]沒有燈可以看書。"],["🧱🔨💡","他在牆上挖了[˙ㄌㄜ]一個小洞，鄰居家的[˙ㄉㄜ]燈光就照過來了[˙ㄌㄜ]。"],["📖👦✨","他靠這一點點光每天讀書，後來變成很有學問[˙ㄨㄣ]的[˙ㄉㄜ]人。"]]},{"w":"孟母三遷","zy":"ㄇㄥˋ ㄇㄨˇ ㄙㄢ ㄑㄧㄢ","m":"好的[˙ㄉㄜ]環境對學習很重要。","p":[["👩👦🪦","孟子[˙ㄗ]小時候[˙ㄏㄡ]住在墓地旁邊，就學大人哭哭啼啼。"],["🏪📢","媽媽[˙ㄇㄚ]搬到市場旁邊，孟子[˙ㄗ]又學商人大聲叫賣。"],["🏫📚😊","媽媽[˙ㄇㄚ]再搬到學校旁邊，孟子[˙ㄗ]就學大家讀書、有禮貌。"]]},{"w":"聞雞起舞","zy":"ㄨㄣˊ ㄐㄧ ㄑㄧˇ ㄨˇ","m":"把握時間，認真努力。","p":[["🐓🌅","祖逖每天一聽到雞叫，就馬上起床。"],["🗡️👬","他和好朋友[˙ㄧㄡ]在院子[˙ㄗ]裡練劍，一天也不偷懶。"],["🛡️🏆","後來他變成很厲害的[˙ㄉㄜ]大將[ㄐㄧㄤ]軍。"]]},{"w":"熟能生巧","zy":"ㄕㄡˊ ㄋㄥˊ ㄕㄥ ㄑㄧㄠˇ","m":"做得[˙ㄉㄜ]多、練得[˙ㄉㄜ]熟[ㄕㄡˊ]，就會又快又好。","p":[["🏹🎯👏","有一個人射箭很準，大家都拍手。"],["👴🛢️🪙","一個賣油的[˙ㄉㄜ]老爺爺[˙ㄧㄝ]，把油從銅錢的[˙ㄉㄜ]小洞倒進葫蘆[˙ㄌㄨ]，一滴也沒有沾到錢。"],["👴😊","老爺爺[˙ㄧㄝ]說：「這沒什麼[˙ㄇㄜ]，只是做得[˙ㄉㄜ]多，就熟[ㄕㄡˊ]練了[˙ㄌㄜ]。」"]]},{"w":"囫圇吞棗","zy":"ㄏㄨˊ ㄌㄨㄣˊ ㄊㄨㄣ ㄗㄠˇ","m":"讀書不想清楚[˙ㄔㄨ]，只是整個吞下去。","p":[["🍐🦷","有人說：「吃梨對牙齒好，可是對胃不好。」"],["🍒😟","又說：「吃棗子[˙ㄗ]對胃好，可是對牙齒不好。」"],["😋","一個人說：「那我吃梨只咬不吞，吃棗子[˙ㄗ]不咬，整顆吞下去！」"]]},{"w":"老馬識途","zy":"ㄌㄠˇ ㄇㄚˇ ㄕˋ ㄊㄨˊ","m":"有經驗的[˙ㄉㄜ]人，知道[˙ㄉㄠ]該怎麼[˙ㄇㄜ]做。","p":[["🪖🐎❄️","軍隊在雪地裡迷路了[˙ㄌㄜ]，找不到回家的[˙ㄉㄜ]路。"],["👴🐎","管仲說：「讓老馬走在前面[˙ㄇㄧㄢ]吧[˙ㄅㄚ]！」"],["🐎🏠🎉","老馬帶大家走，真的[˙ㄉㄜ]找到了[˙ㄌㄜ]回家的[˙ㄉㄜ]路。"]]},{"w":"望梅止渴","zy":"ㄨㄤˋ ㄇㄟˊ ㄓˇ ㄎㄜˇ","m":"用想像來安慰自己。","p":[["🪖☀️😩","士兵走了[˙ㄌㄜ]很久，天氣很熱，大家都好渴。"],["🤴👉🌳","曹操說：「前面[˙ㄇㄧㄢ]有一大片梅子[˙ㄗ]林，梅子[˙ㄗ]又酸又甜！」"],["😋💧","大家一想到酸酸的[˙ㄉㄜ]梅子[˙ㄗ]，嘴裡就流出口水，不那麼[˙ㄇㄜ]渴了[˙ㄌㄜ]。"]]},{"w":"胸有成竹","zy":"ㄒㄩㄥ ㄧㄡˇ ㄔㄥˊ ㄓㄨˊ","m":"做事以前，心裡已經想好了[˙ㄌㄜ]。","p":[["🎋🧑‍🎨","文與可很喜歡[˙ㄏㄨㄢ]畫竹子[˙ㄗ]，常常到竹林裡看竹子[˙ㄗ]。"],["👀☀️🌧️","晴天看，雨天也看，把竹子[˙ㄗ]的[˙ㄉㄜ]樣子[˙ㄗ]都記在心裡。"],["🖌️🎋✨","所以他一拿起筆，就能很快畫出漂亮[˙ㄌㄧㄤ]的[˙ㄉㄜ]竹子[˙ㄗ]。"]]}];
  // 故事用到、但題庫注音表沒有的字
  Object.entries({"努":"ㄋㄨˇ","撞":"ㄓㄨㄤˋ","昏":"ㄏㄨㄣ","撿":"ㄐㄧㄢˇ","興":"ㄒㄧㄥˋ","此":"ㄘˇ","旁":"ㄆㄤˊ","急":"ㄐㄧˊ","序":"ㄒㄩˋ","而":"ㄦˊ","弄":"ㄋㄨㄥˋ","稻":"ㄉㄠˋ","拔":"ㄅㄚˊ","枯":"ㄎㄨ","死":"ㄙˇ","需":"ㄒㄩ","賽":"ㄙㄞˋ","品":"ㄆㄧㄣˇ","靠":"ㄎㄠˋ","量":"ㄌㄧㄤˋ","嚇":"ㄒㄧㄚˋ","虎":"ㄏㄨˇ","抓":"ㄓㄨㄚ","狐":"ㄏㄨˊ","王":"ㄨㄤˊ","信":"ㄒㄧㄣˋ","實":"ㄕˊ","知":"ㄓ","井":"ㄐㄧㄥˇ","底":"ㄉㄧˇ","牠":"ㄊㄚ","抬":"ㄊㄞˊ","海":"ㄏㄞˇ","龜":"ㄍㄨㄟ","世":"ㄕˋ","界":"ㄐㄧㄝˋ","趕":"ㄍㄢˇ","及":"ㄐㄧˊ","破":"ㄆㄛˋ","野":"ㄧㄝˇ","狼":"ㄌㄤˊ","叼":"ㄉㄧㄠ","鄰":"ㄌㄧㄣˊ","居":"ㄐㄩ","補":"ㄅㄨˇ","吧":"˙ㄅㄚ","丟":"ㄉㄧㄡ","懂":"ㄉㄨㄥˇ","彈":"ㄊㄢˊ","琴":"ㄑㄧㄣˊ","牛":"ㄋㄧㄡˊ","顧":"ㄍㄨˋ","蚊":"ㄨㄣˊ","才":"ㄘㄞˊ","龍":"ㄌㄨㄥˊ","逃":"ㄊㄠˊ","摸":"ㄇㄛ","鼻":"ㄅㄧˊ","管":"ㄍㄨㄢˇ","腿":"ㄊㄨㄟˇ","柱":"ㄓㄨˋ","困":"ㄎㄨㄣˋ","難":"ㄋㄢˊ","功":"ㄍㄨㄥ","愚":"ㄩˊ","便":"ㄅㄧㄢˋ","挖":"ㄨㄚ","搬":"ㄅㄢ","兒":"ㄦˊ","孫":"ㄙㄨㄣ","神":"ㄕㄣˊ","感":"ㄍㄢˇ","午":"ㄨˇ","茶":"ㄔㄚˊ","語":"ㄩˇ","揠":"ㄧㄚˋ","仗":"ㄓㄤˋ","仲":"ㄓㄨㄥˋ","位":"ㄨㄟˋ","假":"ㄐㄧㄚˇ","偷":"ㄊㄡ","傷":"ㄕㄤ","兵":"ㄅㄧㄥ","利":"ㄌㄧˋ","刺":"ㄘˋ","劍":"ㄐㄧㄢˋ","北":"ㄅㄟˇ","匡":"ㄎㄨㄤ","匹":"ㄆㄧ","南":"ㄋㄢˊ","卻":"ㄑㄩㄝˋ","受":"ㄕㄡˋ","合":"ㄏㄜˊ","吞":"ㄊㄨㄣ","咬":"ㄧㄠˇ","啄":"ㄓㄨㄛˊ","商":"ㄕㄤ","啼":"ㄊㄧˊ","嗡":"ㄨㄥ","國":"ㄍㄨㄛˊ","境":"ㄐㄧㄥˋ","墓":"ㄇㄨˋ","士":"ㄕˋ","夾":"ㄐㄧㄚˊ","孟":"ㄇㄥˋ","射":"ㄕㄜˋ","帝":"ㄉㄧˋ","弦":"ㄒㄧㄢˊ","慰":"ㄨㄟˋ","懶":"ㄌㄢˇ","所":"ㄙㄨㄛˇ","拍":"ㄆㄞ","掉":"ㄉㄧㄠˋ","提":"ㄊㄧˊ","換":"ㄏㄨㄢˋ","摔":"ㄕㄨㄞ","擔":"ㄉㄢ","敢":"ㄍㄢˇ","整":"ㄓㄥˇ","晴":"ㄑㄧㄥˊ","曬":"ㄕㄞˋ","曹":"ㄘㄠˊ","替":"ㄊㄧˋ","李":"ㄌㄧˇ","杞":"ㄑㄧˇ","栗":"ㄌㄧˋ","梅":"ㄇㄟˊ","梨":"ㄌㄧˊ","棄":"ㄑㄧˋ","棗":"ㄗㄠˇ","沾":"ㄓㄢ","混":"ㄏㄨㄣˋ","清":"ㄑㄧㄥ","湊":"ㄘㄡˋ","滴":"ㄉㄧ","漁":"ㄩˊ","爭":"ㄓㄥ","爺":"ㄧㄝˊ","環":"ㄏㄨㄢˊ","皇":"ㄏㄨㄤˊ","盾":"ㄉㄨㄣˋ","矛":"ㄇㄠˊ","硬":"ㄧㄥˋ","磨":"ㄇㄛˊ","祖":"ㄗㄨˇ","窮":"ㄑㄩㄥˊ","竽":"ㄩˊ","箭":"ㄐㄧㄢˋ","翁":"ㄨㄥ","肯":"ㄎㄣˇ","胃":"ㄨㄟˋ","臣":"ㄔㄣˊ","與":"ㄩˇ","蚌":"ㄅㄤˋ","衡":"ㄏㄥˊ","裂":"ㄌㄧㄝˋ","該":"ㄍㄞ","賣":"ㄇㄞˋ","越":"ㄩㄝˋ","跳":"ㄊㄧㄠˋ","軍":"ㄐㄩㄣ","辦":"ㄅㄢˋ","逖":"ㄊㄧˋ","通":"ㄊㄨㄥ","酸":"ㄙㄨㄢ","重":"ㄓㄨㄥˋ","針":"ㄓㄣ","鈴":"ㄌㄧㄥˊ","銅":"ㄊㄨㄥˊ","鐵":"ㄊㄧㄝˇ","院":"ㄩㄢˋ","離":"ㄌㄧˊ","雪":"ㄒㄩㄝˇ","餵":"ㄨㄟˋ","騎":"ㄑㄧˊ","騙":"ㄆㄧㄢˋ","鷸":"ㄩˋ","齒":"ㄔˇ","法":"ㄈㄚˇ"}).forEach(([k,v])=>{if(!Z.ZY[k])Z.ZY[k]=v});
  const GOT=EN.icon("cookie");
  const idiomHTML=(s,hole)=>{const z=s.zy.split(" ");return [...s.w].map((ch,i)=>i===hole?`<span class="hole" id="hole">${TZ.charHTML("",z[i])}</span>`:TZ.charHTML(ch,z[i])).join("")};
  let cur=null,page=0,tok=0,listened=false,moved=false,mode=TZ.pref("town-story-mode")==="blank"?"blank":"story";
  const sayW=w=>{const x=ST.find(y=>y.w===w);return (x&&x.sw)||w};
  // 換下一題（念完自動換，或按「下一題」馬上換，只會換一次）
  // q：是哪一題要換（上一題的語音晚一點念完，不能讓它再多換一題）
  const go=(delay,q)=>{if(moved||(q&&q!==cur))return;moved=true;$("skip").hidden=true;api.next(delay)};
  $("skip").onclick=()=>{EN.stop();go(150)};
  const api=TZ.run({key:"town-story",noRange:true,gotIcon:GOT,
    finale:done=>{const n=Math.max(1,Math.min(+TZ.got().dataset.n,8));TZ.finale(`<div class="frow"><span style="font-size:clamp(50px,9vmin,72px);line-height:1">🫖</span>${Array(n).fill(GOT).join("")}</div>`,"故事都聽完了，一起喝下午茶吧！",done,3000)},
    help:"午茶說故事有兩種玩法。聽故事：故事會自己一頁一頁念下去，想再聽一次就按喇叭，聽完按「聽完了」，再選出這是哪一個成語，答對了會告訴你成語的意思。成語填空：成語少了一個字，看空格裡的注音和成語的意思，選出少的那個字。",
    // 每一題都是不同的成語（成語比題數多，不會重複）
    build:n=>TZ.shuffle(ST.map((_,i)=>i)).slice(0,n).map(i=>({t:mode==="blank"?"B":"A",i})),
    show:(q)=>{cur=q;moved=false;$("skip").hidden=true;const s=ST[q.i];$("mean").hidden=true;$("show4").hidden=true;
      if(q.t==="A"){$("quiz").hidden=true;$("book").hidden=false;listened=false;
        $("bt").innerHTML=TZ.zy("午茶故事");$("pdots").innerHTML=s.p.map(()=>"<i></i>").join("");turn(0)}
      else blankQ(s)}});

  // ---- 開始畫面：選玩法 ----
  const st=$("setup");st.setAttribute("data-zy-skip","");
  st.innerHTML=`<span class="lbl">${TZ.zy("玩法")}</span><div class="row" id="modeRow"><button type="button" class="opt mode" data-m="story"><span class="mi">📖</span><small>${TZ.zy("聽故事")}</small></button><button type="button" class="opt mode" data-m="blank"><span class="mi">✏️</span><small>${TZ.zy("成語填空")}</small></button></div>`;
  const syncMode=()=>st.querySelectorAll(".mode").forEach(b=>b.setAttribute("aria-pressed",b.dataset.m===mode));
  st.querySelectorAll(".mode").forEach(b=>b.onclick=()=>{mode=b.dataset.m;TZ.pref("town-story-mode",mode);syncMode()});syncMode();

  // ---- 說故事：一頁一頁 ----
  function turn(k){
    // 第三個欄位是給語音念的寫法（平板會念錯的破音字，換成同音字念）
    const s=ST[cur.i];page=k;const [pic,txt,spk]=s.p[k];const my=++tok;
    $("scene").innerHTML=[...pic.matchAll(/\\p{Extended_Pictographic}(\\u200d\\p{Extended_Pictographic}|\\ufe0f)*/gu)].map((m,i)=>`<span style="animation-delay:${i*.12}s">${m[0]}</span>`).join("");
    const t=$("stx");t.innerHTML=TZ.zy(txt);t.classList.remove("in");void t.offsetWidth;t.classList.add("in");
    $("pdots").querySelectorAll("i").forEach((d,i)=>d.classList.toggle("on",i<=k));
    $("prev").disabled=k===0;
    const last=k===s.p.length-1,nx=$("next");
    nx.classList.toggle("go",last);nx.innerHTML=last?TZ.zy("聽完了")+" ✓":"▶";nx.classList.remove("ready");
    EN.sfx.pop();
    // 一頁念完自動翻到下一頁；最後一頁念完，按「聽完了」才出題目（也可以自己按箭頭）
    setTimeout(()=>{if(my===tok)TZ.say(spk||txt,{onend:()=>autoNext(my)})},350);
  }
  function autoNext(my){if(my!==tok)return;const s=ST[cur.i];
    $("next").classList.add("ready");
    // 最後一頁念完不自動出題，等小朋友按「聽完了」
    if(page<s.p.length-1)setTimeout(()=>{if(my!==tok||$("book").hidden)return;turn(page+1)},700);else listened=true}
  $("prev").onclick=()=>{if(page>0)turn(page-1)};
  $("rep").onclick=()=>{const my=++tok,pg=ST[cur.i].p[page];TZ.say(pg[2]||pg[1],{onend:()=>autoNext(my)})};
  $("next").onclick=()=>{const s=ST[cur.i];if(page<s.p.length-1)turn(page+1);else{tok++;EN.stop();pickQ(s)}};

  // ---- 這個故事是哪一個成語？ ----
  function pickQ(s){
    $("book").hidden=true;$("quiz").hidden=false;
    $("q").innerHTML=TZ.zy("這個故事是哪一個成語？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button><button type="button" class="ibtn" id="again" aria-label="再聽一次故事">📖</button>`;
    $("say").onclick=()=>TZ.say("這個故事是哪一個成語？");
    $("again").onclick=()=>{if(api.S.busy)return;$("quiz").hidden=true;$("book").hidden=false;turn(0)};
    const others=TZ.shuffle(ST.filter(x=>x!==s)).slice(0,2),opts=TZ.shuffle([s,...others]);
    const ch=$("choices");ch.className="choices col";
    ch.innerHTML=opts.map(o=>`<button type="button" class="choice idi" data-w="${o.w}" aria-label="${o.w}">${idiomHTML(o)}</button>`).join("");
    ch.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
      if(api.S.busy)return;
      if(el.dataset.w===s.w){api.ok();el.classList.add("yes");ch.querySelectorAll(".choice").forEach(x=>{if(x!==el)x.classList.add("no")});
        setTimeout(()=>TZ.flyGot(el,GOT),500);showMean(s)}
      else{api.bad();el.classList.add("no");TZ.say(`不是${sayW(el.dataset.w)}喔，再想一想`);if(api.S.tries>=2)ch.querySelector(`.choice[data-w="${s.w}"]`).classList.add("glow")}
    });
    TZ.say("這個故事是哪一個成語？");
  }
  function showMean(s){const q0=cur;
    const m=$("mean");m.innerHTML=`<span class="kai">${idiomHTML(s)}</span>${TZ.zy("：")}${TZ.zy(s.m)}`;m.hidden=false;m.classList.remove("pop");void m.offsetWidth;m.classList.add("pop");
    $("skip").innerHTML=TZ.zy("下一題")+" ▶";$("skip").hidden=false;
    // 念出成語的意思，念完再換下一題（也可以按「下一題」）
    setTimeout(()=>{if(cur===q0&&!moved)TZ.say(`答對了！${sayW(s.w)}，意思是：${TZ.plain(s.m)}`,{onend:()=>go(1200,q0)})},700);
  }
  // ---- 成語少了一個字 ----
  function blankQ(s){
    $("book").hidden=true;$("quiz").hidden=false;
    const hole=Math.floor(Math.random()*4),ans=[...s.w][hole];
    $("q").innerHTML=TZ.zy("成語少了哪一個字？")+`<button type="button" class="ibtn" id="say" aria-label="念題目">🔊</button>`;
    $("say").onclick=()=>TZ.say("看注音，成語少了哪一個字？");
    const sh=$("show4");sh.innerHTML=idiomHTML(s,hole);sh.hidden=false;
    $("mean").innerHTML=TZ.zy("意思：")+TZ.zy(s.m);$("mean").hidden=false;$("mean").classList.remove("pop");
    const pool=TZ.shuffle([...new Set(ST.flatMap(x=>[...x.w]))].filter(c=>c!==ans)),opts=TZ.shuffle([ans,pool[0],pool[1]]);
    const zyOf=c=>{for(const x of ST){const i=[...x.w].indexOf(c);if(i>=0)return x.zy.split(" ")[i]}return Z.ZY[c]||""};
    const ch=$("choices");ch.className="choices";
    ch.innerHTML=opts.map(c=>`<button type="button" class="choice cc" data-c="${c}" aria-label="${c}">${TZ.charHTML(c,c===ans?s.zy.split(" ")[hole]:zyOf(c))}</button>`).join("");
    ch.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
      if(api.S.busy)return;
      if(el.dataset.c===ans){api.ok();el.classList.add("yes");const h=$("hole");
        TZ.fly(el,h,()=>{h.classList.add("fill");h.innerHTML=TZ.charHTML(ans,s.zy.split(" ")[hole]);EN.sfx.pop();setTimeout(()=>TZ.flyGot(h,GOT),300)},{dur:.55,keepHidden:true});
        const q0=cur;$("skip").innerHTML=TZ.zy("下一題")+" ▶";$("skip").hidden=false;
        // 填好後念出整個成語，念完再換下一題
        setTimeout(()=>{if(cur===q0&&!moved)TZ.say(sayW(s.w),{onend:()=>go(900,q0)})},800)}
      else{api.bad();el.classList.add("no");if(api.S.tries>=2)ch.querySelector(`.choice[data-c="${ans}"]`).classList.add("glow")}
    });
    setTimeout(()=>{if(!api.S.busy)TZ.say("看注音，成語少了哪一個字？")},300);
  }
})();''')
for fn,k in PAGES.items():
    html=HEAD.format(V=V,title=k["title"],icon=k["icon"],sub=k["sub"],style=COMMON_STYLE+"\n"+k["style"],main=k["main"],script=k["script"])
    open(os.path.join(ROOT,fn),"w",encoding="utf-8").write(html)
    print("寫出",fn)

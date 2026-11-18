# 產生甜點小鎮的四關頁面：python pages.py（每一關共用標題列、開始畫面、結束畫面，只有題目區和玩法不同）
import os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
V="20261118g"
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
    <span class="earn" id="earn"></span>
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
.bread b{font-family:var(--kai);font-weight:400;font-size:clamp(56px,10vmin,80px);color:#fff;text-shadow:0 3px 0 rgba(107,63,34,.6);line-height:1}''',
main='''<div class="order" id="order" data-zy-skip><span class="tag" id="tag"></span><div class="sent" id="sent"></div><button type="button" class="ibtn" id="say" aria-label="念句子">🔊</button></div>
<div class="choices" id="choices"></div>''',
script='''(()=>{
  const $=id=>document.getElementById(id),Z=ZI;
  $("tag").innerHTML=TZ.zy("訂單");
  const api=TZ.run({key:"town-fill",
    help:"麵包店送貨。訂單上的句子少了一個字，看看注音，想一想哪一個字才對，把那個麵包送過去。按喇叭可以聽句子。",
    build:n=>TZ.deal(TZ.pool(true).filter(c=>Z.sent[c]),n),
    show:(c)=>{
      const [t,o]=Z.sent[c];
      $("sent").innerHTML=TZ.zy(t);
      $("say").onclick=()=>TZ.say(t.replace("＿",c));
      $("choices").innerHTML=TZ.shuffle([...o]).map(x=>`<button type="button" class="choice bread" data-c="${x}" aria-label="${x}"><b>${x}</b></button>`).join("");
      document.querySelectorAll(".choice").forEach(el=>el.onclick=()=>{
        if(api.S.busy)return;
        if(el.dataset.c===c){api.ok();el.classList.add("yes");const b=$("blank");b.classList.add("fill");b.textContent=c;
          TZ.say(t.replace("＿",c),{onend:()=>api.next(500)})}
        else{api.bad();el.classList.add("no");el.classList.add("shake");if(api.S.tries>=2)document.querySelector(`.choice[data-c="${c}"]`).classList.add("glow")}
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
    help:"冰火飲料店。左邊的冰飲料上有一個字，請你找出意思和它相反的字，例如大和小、上和下。點那一杯飲料。沒學過的字會有注音。",
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
      $("choices").innerHTML=opts.map((c,i)=>`<button type="button" class="choice cup" style="--c:${COL[i]}" data-c="${c}" aria-label="${c}"><b>${TZ.charHTML(c,zyIf(c))}</b></button>`).join("");
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
.sent2{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:4px 2px;font-family:var(--kai);font-size:clamp(28px,5.2vmin,48px)}
.ap{position:relative;display:inline-flex;align-items:center;border:0;background:#fff3f3;border-radius:18px;padding:4px 4px 4px 6px;cursor:pointer;font:inherit;color:var(--ink);min-width:44px;min-height:52px;box-shadow:inset 0 0 0 3px #ffd0d0}
.ap .tz-b{font-size:max(.34em,11px)}
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

for fn,k in PAGES.items():
    html=HEAD.format(V=V,title=k["title"],icon=k["icon"],sub=k["sub"],style=COMMON_STYLE+"\n"+k["style"],main=k["main"],script=k["script"])
    open(os.path.join(ROOT,fn),"w",encoding="utf-8").write(html)
    print("寫出",fn)

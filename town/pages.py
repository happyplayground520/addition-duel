# 產生甜點小鎮的四關頁面：python pages.py（每一關共用標題列、開始畫面、結束畫面，只有題目區和玩法不同）
import os
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.dirname(HERE)
V="20261118f"
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

for fn,k in PAGES.items():
    html=HEAD.format(V=V,title=k["title"],icon=k["icon"],sub=k["sub"],style=COMMON_STYLE+"\n"+k["style"],main=k["main"],script=k["script"])
    open(os.path.join(ROOT,fn),"w",encoding="utf-8").write(html)
    print("寫出",fn)

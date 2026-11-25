/* 休息提醒：整個網站一起算時間（換頁、換地圖都會接著算），玩滿 10 分鐘跳出「休息一下」，按 ✕ 或「好」關掉，再重新算 10 分鐘。
   畫面沒在看（切到別的 App、螢幕關掉）不算時間；離開超過 20 分鐘再回來，當作已經休息過，從 0 開始算。 */
(()=>{
  const LIMIT=10*60*1000,RESTED=20*60*1000,KEY="rest-play";
  const read=()=>{try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return{}}};
  const save=o=>{try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}};
  let st=read();const now0=Date.now();
  if(!st.last||now0-st.last>RESTED)st={ms:0,last:now0};
  let tick=now0,box=null;
  function step(){
    const now=Date.now();
    if(document.hidden||box){tick=now;return}
    const s=read();// 別的分頁也在算的話，用比較大的那個
    let ms=Math.max(st.ms||0,(s.last&&now-s.last<RESTED)?s.ms||0:0)+Math.min(now-tick,15000);
    tick=now;st={ms,last:now};save(st);
    if(ms>=LIMIT)show();
  }
  function css(){if(document.getElementById("rest-css"))return;const c=document.createElement("style");c.id="rest-css";c.textContent=`
body.rest-paused>:not(.rest-bg),body.rest-paused>:not(.rest-bg) *{animation-play-state:paused!important}
.rest-bg{position:fixed;inset:0;z-index:2147483000;display:grid;place-items:center;background:rgba(30,30,60,.45);padding:16px;animation:rest-in .3s both;
  font-family:"Chiron GoRound TC","PingFang TC","Microsoft JhengHei","Noto Sans TC",system-ui,sans-serif}
@keyframes rest-in{from{opacity:0}}
.rest-card{position:relative;width:min(420px,100%);background:#fffdf6;border:5px solid #fff;border-radius:28px;padding:26px 20px 20px;text-align:center;color:#2b2b3a;
  box-shadow:0 0 0 4px #ffb3c7,0 14px 40px rgba(0,0,0,.35);animation:rest-pop .5s cubic-bezier(.3,1.6,.5,1) both}
@keyframes rest-pop{from{transform:scale(.5)}}
.rest-x{position:absolute;right:10px;top:10px;width:48px;height:48px;border-radius:50%;border:0;background:#ffe3ea;color:#c2185b;font-size:26px;font-weight:900;line-height:1;cursor:pointer;display:grid;place-items:center}
.rest-x:active{transform:scale(.92)}
.rest-pic{font-size:64px;line-height:1.1;display:flex;justify-content:center;gap:8px;padding:0 40px}
.rest-pic span{display:inline-block;animation:rest-bob 2s ease-in-out infinite}
.rest-pic span:nth-child(2){animation-delay:-.7s}.rest-pic span:nth-child(3){animation-delay:-1.4s}
@keyframes rest-bob{50%{transform:translateY(-8px) rotate(-6deg)}}
.rest-t{margin:8px 0 4px;font-size:28px;font-weight:900;color:#e8577a}
.rest-p{margin:0 0 16px;font-size:20px;font-weight:800;line-height:1.9}
.rest-ok{border:0;border-radius:999px;background:#3cb371;color:#fff;font:inherit;font-size:22px;font-weight:900;padding:8px 30px;box-shadow:0 5px 0 #23804f;cursor:pointer}
.rest-ok:active{transform:translateY(3px);box-shadow:0 2px 0 #23804f}
.rest-ok .zy .b,.rest-ok rt{color:#fff}
@media (max-height:480px){.rest-card{padding:14px 16px 14px}.rest-pic{font-size:44px}.rest-t{font-size:22px;margin:2px 0}.rest-p{font-size:17px;margin-bottom:10px;line-height:1.7}}
@media (prefers-reduced-motion:reduce){.rest-bg,.rest-card,.rest-pic span{animation:none}}`;document.head.appendChild(c)}
  function show(){
    if(box)return;css();
    box=document.createElement("div");box.className="rest-bg";box.setAttribute("role","dialog");box.setAttribute("aria-modal","true");box.setAttribute("aria-label","休息一下");
    box.innerHTML=`<div class="rest-card"><button type="button" class="rest-x" aria-label="關掉">✕</button>
      <div class="rest-pic" aria-hidden="true"><span>🧸</span><span>🌳</span><span>👀</span></div>
      <div class="rest-t" data-zy>休息一下吧！</div>
      <p class="rest-p" data-zy>已經玩了十分鐘囉！<br>看看遠方，<br>喝口水、動一動身體。</p>
      <button type="button" class="rest-ok" data-zy>好，休息一下</button></div>`;
    const close=()=>{if(!box)return;box.remove();box=null;document.body.classList.remove("rest-paused");try{dispatchEvent(new Event("rest:close"))}catch(e){}st={ms:0,last:Date.now()};save(st);tick=Date.now();try{speechSynthesis.cancel()}catch(e){}};
    box.querySelector(".rest-x").onclick=close;box.querySelector(".rest-ok").onclick=close;
    box.addEventListener("keydown",e=>{if(e.key==="Escape")close()});
    document.body.appendChild(box);box.querySelector(".rest-ok").focus({preventScroll:true});
    // 告訴計時的小遊戲先暫停（時間不要跑、東西不要動），按「好」或 ✕ 之後再繼續
    document.body.classList.add("rest-paused");try{dispatchEvent(new Event("rest:open"))}catch(e){}
    try{const u=new SpeechSynthesisUtterance("已經玩了十分鐘囉，休息一下，看看遠方吧！");u.lang="zh-TW";u.rate=.95;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}
  }
  // 測試用：網址加 #rest 馬上跳出來
  window.restShow=show;
  const start=()=>{if(location.hash==="#rest")show();setInterval(step,5000)};
  document.addEventListener("visibilitychange",()=>{tick=Date.now()});
  addEventListener("pagehide",()=>{if(!document.hidden&&!box){step()}});
  if(document.body)start();else addEventListener("DOMContentLoaded",start);
})();

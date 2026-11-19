/* 地圖頁用：小朋友在看地圖的時候，趁空檔先把這張地圖上每一關的網頁、程式、字型下載好放進瀏覽器的快取，
   點進關卡時就不用等下載，比較不會卡。一次只下載一個、用低優先順序，不會跟地圖搶網路；省流量模式或很慢的網路就不做。
   手指按下（或滑鼠移到）某一關時，那一關會插隊先下載。 */
(()=>{
  const c=navigator.connection;
  if(c&&(c.saveData||/(^|-)2g$/.test(c.effectiveType||"")))return;
  const done=new Set(),queue=[];let busy=false;
  const same=u=>{try{const x=new URL(u,location.href);return x.origin===location.origin?x.href.split("#")[0]:null}catch(e){return null}};
  function add(u,front){u=same(u);if(!u||done.has(u))return;done.add(u);front?queue.unshift(u):queue.push(u);pump()}
  async function pump(){
    if(busy||!queue.length)return;busy=true;
    const u=queue.shift();
    try{
      const r=await fetch(u,{priority:"low",credentials:"same-origin"});
      const type=r.headers.get("content-type")||"";
      if(/html|css/.test(type)){const t=await r.text();
        // 網頁裡用到的程式和樣式；樣式裡用到的字型
        if(/html/.test(type))for(const m of t.matchAll(/<(?:script[^>]*\ssrc|link[^>]*\shref)="([^"]+\.(?:js|css)(?:\?[^"]*)?)"/g))add(new URL(m[1],u).href);
        else for(const m of t.matchAll(/url\(["']?([^"')]+\.woff2?(?:\?[^"')]*)?)["']?\)/g))add(new URL(m[1],u).href);
      }else await r.arrayBuffer();
    }catch(e){}
    busy=false;
    // 讓出一點時間給畫面（動畫才不會頓）
    setTimeout(pump,120);
  }
  const links=()=>[...document.querySelectorAll("a[href]")].map(a=>a.getAttribute("href")).filter(h=>/\.html(\?|$)/.test(h));
  function start(){links().forEach(h=>add(h))}
  // 手指按下或滑鼠移到某一關：那一關先下載
  const jump=e=>{const a=e.target.closest&&e.target.closest("a[href]");if(a&&/\.html(\?|$)/.test(a.getAttribute("href")))add(a.getAttribute("href"),true)};
  addEventListener("pointerdown",jump,{passive:true,capture:true});
  addEventListener("pointerover",jump,{passive:true});
  // 地圖畫好、動畫開始以後再開始（不跟地圖本身搶）
  const idle=window.requestIdleCallback||(f=>setTimeout(f,1));
  const go=()=>setTimeout(()=>idle(start,{timeout:3000}),1200);
  if(document.readyState==="complete")go();else addEventListener("load",go);
  window.warmPage=u=>add(u,true);
})();

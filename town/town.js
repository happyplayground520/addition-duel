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
  TZ.say=(t,o={})=>window.EN&&EN.say(TZ.plain(t),Object.assign({zh:true,rate:.85},o));
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
      next(delay=900){setTimeout(()=>{S.i++;if(S.i>=S.total)finish();else show()},delay)}
    };
    function show(){S.tries=0;S.busy=false;$("prog").textContent=`${S.i+1} / ${S.total}`;cfg.show(S.qs[S.i],api)}
    function start(){
      EN.unlock();
      const qs=cfg.build(S.total);
      if(!qs.length){if(note)note.textContent=cfg.empty||"這個範圍的題目不夠，請多選幾課。";EN.sfx.bad();return}
      S.qs=qs;S.i=0;S.score=0;S.phase="play";$("score").textContent="⭐ 0";$("start").hidden=true;$("end").hidden=true;
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
  window.TZ=TZ;
})();

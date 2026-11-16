/* 數學遊樂園：標題和題目的注音（每個字右邊一小排直式注音）
   首頁可以統一開關，設定存在 localStorage「park-zhuyin」（預設開）。
   會自動幫 h1、h2、.ttl、.title、[data-zy] 裡的國字加注音，題目換了也會跟著更新。 */
(function(){
  const D={
    數:"ㄕㄨˋ",學:"ㄒㄩㄝˊ",遊:"ㄧㄡˊ",樂:"ㄌㄜˋ",園:"ㄩㄢˊ",點:"ㄉㄧㄢˇ",一:"ㄧ",個:"ㄍㄜˋ",設:"ㄕㄜˋ",施:"ㄕ",
    開:"ㄎㄞ",始:"ㄕˇ",玩:"ㄨㄢˊ",售:"ㄕㄡˋ",票:"ㄆㄧㄠˋ",亭:"ㄊㄧㄥˊ",小:"ㄒㄧㄠˇ",火:"ㄏㄨㄛˇ",車:"ㄔㄜ",碰:"ㄆㄥˋ",
    摩:"ㄇㄛˊ",天:"ㄊㄧㄢ",輪:"ㄌㄨㄣˊ",旋:"ㄒㄩㄢˊ",轉:"ㄓㄨㄢˋ",木:"ㄇㄨˋ",馬:"ㄇㄚˇ",套:"ㄊㄠˋ",圈:"ㄑㄩㄢ",射:"ㄕㄜˋ",
    氣:"ㄑㄧˋ",球:"ㄑㄧㄡˊ",甜:"ㄊㄧㄢˊ",攤:"ㄊㄢ",雲:"ㄩㄣˊ",霄:"ㄒㄧㄠ",飛:"ㄈㄟ",搶:"ㄑㄧㄤˇ",答:"ㄉㄚˊ",對:"ㄉㄨㄟˋ",
    決:"ㄐㄩㄝˊ",入:"ㄖㄨˋ",口:"ㄎㄡˇ",買:"ㄇㄞˇ",門:"ㄇㄣˊ",時:"ㄕˊ",鐘:"ㄓㄨㄥ",找:"ㄓㄠˇ",出:"ㄔㄨ",等:"ㄉㄥˇ",
    於:"ㄩˊ",的:"˙ㄉㄜ",廂:"ㄒㄧㄤ",排:"ㄆㄞˊ",看:"ㄎㄢˋ",乘:"ㄔㄥˊ",法:"ㄈㄚˇ",速:"ㄙㄨˋ",算:"ㄙㄨㄢˋ",九:"ㄐㄧㄡˇ",
    快:"ㄎㄨㄞˋ",間:"ㄐㄧㄢ",到:"ㄉㄠˋ",太:"ㄊㄞˋ",厲:"ㄌㄧˋ",害:"ㄏㄞˋ",了:"˙ㄌㄜ",做:"ㄗㄨㄛˋ",得:"ㄉㄜˊ",很:"ㄏㄣˇ",
    好:"ㄏㄠˇ",再:"ㄗㄞˋ",練:"ㄌㄧㄢˋ",習:"ㄒㄧˊ",下:"ㄒㄧㄚˋ",藍:"ㄌㄢˊ",色:"ㄙㄜˋ",橘:"ㄐㄩˊ",你:"ㄋㄧˇ",贏:"ㄧㄥˊ",
    接:"ㄐㄧㄝ",家:"ㄐㄧㄚ",平:"ㄆㄧㄥˊ",手:"ㄕㄡˇ",定:"ㄉㄧㄥˋ",上:"ㄕㄤˋ",現:"ㄒㄧㄢˋ",在:"ㄗㄞˋ",是:"ㄕˋ",幾:"ㄐㄧˇ",
    請:"ㄑㄧㄥˇ",把:"ㄅㄚˇ",撥:"ㄅㄛ",半:"ㄅㄢˋ",分:"ㄈㄣ",盤:"ㄆㄢˊ",子:"ㄗˇ",有:"ㄧㄡˇ",每:"ㄇㄟˇ",共:"ㄍㄨㄥˋ",
    成:"ㄔㄥˊ",坐:"ㄗㄨㄛˋ",隻:"ㄓ",動:"ㄉㄨㄥˋ",物:"ㄨˋ",總:"ㄗㄨㄥˇ",戲:"ㄒㄧˋ",團:"ㄊㄨㄢˊ",表:"ㄅㄧㄠˇ",演:"ㄧㄢˇ",
    船:"ㄔㄨㄢˊ",鬼:"ㄍㄨㄟˇ",屋:"ㄨ",探:"ㄊㄢˋ",險:"ㄒㄧㄢˇ",張:"ㄓㄤ",錢:"ㄑㄧㄢˊ",幣:"ㄅㄧˋ",加:"ㄐㄧㄚ",減:"ㄐㄧㄢˇ",
    零:"ㄌㄧㄥˊ",二:"ㄦˋ",兩:"ㄌㄧㄤˇ",三:"ㄙㄢ",四:"ㄙˋ",五:"ㄨˇ",六:"ㄌㄧㄡˋ",七:"ㄑㄧ",八:"ㄅㄚ",十:"ㄕˊ",百:"ㄅㄞˇ",
    元:"ㄩㄢˊ",準:"ㄓㄨㄣˇ",備:"ㄅㄟˋ",大:"ㄉㄚˋ",富:"ㄈㄨˋ",翁:"ㄨㄥ",賽:"ㄙㄞˋ",跑:"ㄆㄠˇ",戰:"ㄓㄢˋ",鈔:"ㄔㄠ",
    圖:"ㄊㄨˊ",少:"ㄕㄠˇ",多:"ㄉㄨㄛ",前:"ㄑㄧㄢˊ",進:"ㄐㄧㄣˋ",格:"ㄍㄜˊ",擲:"ㄓˋ",輪:"ㄌㄨㄣˊ",誰:"ㄕㄟˊ",
    又:"ㄧㄡˋ",來:"ㄌㄞˊ",走:"ㄗㄡˇ",還:"ㄏㄞˊ",剩:"ㄕㄥˋ",幫:"ㄅㄤ",忙:"ㄇㄤˊ",和:"ㄏㄜˊ",給:"ㄍㄟˇ",它:"ㄊㄚ",
    麼:"˙ㄇㄜ",什:"ㄕㄣˊ",哪:"ㄋㄚˇ",裡:"ㄌㄧˇ",要:"ㄧㄠˋ",付:"ㄈㄨˋ",剛:"ㄍㄤ",長:"ㄔㄤˊ",短:"ㄉㄨㄢˇ",針:"ㄓㄣ",
    草:"ㄘㄠˇ",莓:"ㄇㄟˊ",巧:"ㄑㄧㄠˇ",克:"ㄎㄜˋ",力:"ㄌㄧˋ",抹:"ㄇㄛˇ",茶:"ㄔㄚˊ",香:"ㄒㄧㄤ",焦:"ㄐㄧㄠ",糖:"ㄊㄤˊ",
    檸:"ㄋㄧㄥˊ",檬:"ㄇㄥˊ",注:"ㄓㄨˋ",音:"ㄧㄣ",
    提:"ㄊㄧˊ",示:"ㄕˋ",第:"ㄉㄧˋ",沒:"ㄇㄟˊ",喔:"ㄛ",也:"ㄧㄝˇ",樣:"ㄧㄤˋ",棒:"ㄅㄤˋ",吃:"ㄔ",放:"ㄈㄤˋ",拿:"ㄋㄚˊ",回:"ㄏㄨㄟˊ"
  };
  // 詞語裡讀音不一樣的字（輕聲、破音字）
  const W={"一數":["ㄧ","ㄕㄨˇ"],"，數":["","ㄕㄨˇ"],"排得":["ㄆㄞˊ","˙ㄉㄜ"],"樣子":["ㄧㄤˋ","˙ㄗ"],"盤子":["ㄆㄢˊ","˙ㄗ"],"做得":["ㄗㄨㄛˋ","˙ㄉㄜ"],"什麼":["ㄕㄣˊ","˙ㄇㄜ"],"長針":["ㄔㄤˊ","ㄓㄣ"],"還有":["ㄏㄞˊ","ㄧㄡˇ"]};
  const KEY="park-zhuyin";
  const isOn=()=>{try{return localStorage.getItem(KEY)!=="off"}catch(e){return true}};
  const root=document.documentElement;
  root.classList.toggle("zy-off",!isOn());

  const st=document.createElement("style");
  st.textContent=`
.zy{display:inline-flex;align-items:center;vertical-align:middle;line-height:1;margin-right:.05em;white-space:nowrap}
.zy .h{display:inline-block}
.zg{white-space:nowrap}
.zy .b{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;margin-left:.05em;
  font-family:"PingFang TC","Microsoft JhengHei","Noto Sans TC",sans-serif;font-weight:400;font-size:max(.36em,9px);
  line-height:1.02;letter-spacing:0;font-style:normal;text-shadow:none}
.zy .b>span{position:relative;display:block}
.zy .t{position:absolute;left:92%;top:-.45em;font-size:1em}
.zy .lt{line-height:.7}
html.zy-off .zy .b{display:none}
html.zy-off .zy{margin-right:0}`;
  (document.head||root).appendChild(st);

  const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  function charHTML(ch,z){
    if(!z)return esc(ch);
    const light=z[0]==="˙";
    const syms=[...(light?z.slice(1):z)];
    const tone=/[ˊˇˋ]/.test(syms[syms.length-1])?syms.pop():"";
    const col=syms.map((s,k)=>`<span>${s}${k===syms.length-1&&tone?`<span class="t">${tone}</span>`:""}</span>`).join("");
    return `<span class="zy"><span class="h">${ch}</span><span class="b" aria-hidden="true">${light?'<span class="lt">˙</span>':""}${col}</span></span>`;
  }
  const HAN=/[一-鿿]/;
  function textHTML(text){
    const cs=[...text],out=[];
    for(let i=0;i<cs.length;){
      const w=Object.keys(W).find(k=>cs.slice(i,i+[...k].length).join("")===k);
      if(w){[...w].forEach((ch,j)=>out.push(charHTML(ch,W[w][j])));i+=[...w].length;continue}
      out.push(charHTML(cs[i],D[cs[i]]));i++;
    }
    // 標點符號跟前一個字黏在一起，不要自己換到下一行
    const PUN=/^[，。！？、：；」）…!?,.:;)]$/;
    const glued=[];
    out.forEach((h,i)=>{
      const ch=cs.length===out.length?cs[i]:null;
      if(ch&&PUN.test(ch)&&glued.length)glued[glued.length-1]=`<span class="zg">${glued[glued.length-1]}${h}</span>`;
      else glued.push(h);
    });
    return glued.join("");
  }
  const SEL="h1,h2,.ttl,.title,[data-zy]";
  function annotate(el){
    if(el.closest("svg,[data-zy-skip]"))return;
    const tw=document.createTreeWalker(el,NodeFilter.SHOW_TEXT),nodes=[];
    for(let n;(n=tw.nextNode());){
      const p=n.parentElement;
      if(!p||p.closest(".zy,svg,script,style,[data-zy-skip]"))continue;
      if(HAN.test(n.nodeValue)&&[...n.nodeValue].some(c=>D[c]))nodes.push(n);
    }
    nodes.forEach(n=>{
      const tpl=document.createElement("template");tpl.innerHTML=textHTML(n.nodeValue);
      n.parentNode.replaceChild(tpl.content,n);
    });
  }
  let mo=null;
  function scan(rootEl){
    const list=[];
    if(rootEl.nodeType===1&&rootEl.matches(SEL))list.push(rootEl);
    if(rootEl.querySelectorAll)list.push(...rootEl.querySelectorAll(SEL));
    return list;
  }
  function run(targets){
    if(mo)mo.disconnect();
    targets.forEach(annotate);
    if(mo)mo.observe(document.body,{childList:true,subtree:true,characterData:true});
  }
  function onMut(ms){
    const set=new Set();
    ms.forEach(m=>{
      const node=m.target.nodeType===3?m.target.parentElement:m.target;
      const t=node&&node.closest&&node.closest(SEL);if(t)set.add(t);
      m.addedNodes.forEach(a=>{if(a.nodeType===1)scan(a).forEach(x=>set.add(x));
        else if(a.nodeType===3){const p=a.parentElement&&a.parentElement.closest(SEL);if(p)set.add(p)}});
    });
    if(set.size)run([...set]);
  }
  function init(){mo=new MutationObserver(onMut);run(scan(document.body))}
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();

  window.parkZhuyin={
    isOn,
    set(on){try{localStorage.setItem(KEY,on?"on":"off")}catch(e){}root.classList.toggle("zy-off",!on)}
  };
  // 別的分頁改了設定，這頁也跟著變
  addEventListener("storage",e=>{if(e.key===KEY)root.classList.toggle("zy-off",!isOn())});
  addEventListener("pageshow",()=>root.classList.toggle("zy-off",!isOn()));
})();

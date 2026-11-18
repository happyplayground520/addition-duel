// 產生甜點小鎮的資料檔 zi-data.js：node build.js
// 來源：zi-lessons.json（教育百科生字詞彙表）、zi-chars.json（部首、筆畫）、_jingling.js（字精靈森林的注音和例句）、extra.js（補充）
const fs=require("fs"),path=require("path");
const here=p=>path.join(__dirname,p);
const lessons=JSON.parse(fs.readFileSync(here("zi-lessons.json"),"utf8"));
const chars=JSON.parse(fs.readFileSync(here("zi-chars.json"),"utf8"));
const extra=require("./extra.js");
const src=fs.readFileSync(here("_jingling.js"),"utf8");
const JL=new Function(src+";return{ZY,LESSONS}")();
const ZY=Object.assign({},JL.ZY);
extra.zy.split(/\s+/).forEach(p=>{if(p)ZY[p[0]]=p.slice(1)});
// 例句：字精靈森林（A 版）＋補充（B 版）
const sent={};
const MAGIC={日:"日月山",月:"月日木",山:"山水人",木:"木水手",水:"水木門",人:"人手山",手:"手門人",門:"門日手"};
JL.LESSONS.forEach(l=>l.chars.forEach(c=>{const o=c.opts?c.opts.join(""):MAGIC[c.c];if(c.sent&&o&&!sent[c.c])sent[c.c]=[c.sent,o]}));
Object.entries(extra.sent).forEach(([c,v])=>{sent[c]=v});
// 一上：A 版、B 版
const L={A:lessons.A1.map(l=>({n:l.n,s:l.sheng,r:l.ren})),B:lessons.B1.map(l=>({n:l.n,s:l.sheng,r:l.ren}))};
// 檢查：每個字都有部首、筆畫、例句；例句裡的字都有注音
const all=new Set([...L.A,...L.B].flatMap(l=>[...l.s,...l.r]));
const miss={noInfo:[],noSent:[],noZy:new Set(),optBad:[]};
all.forEach(c=>{if(!chars.chars[c])miss.noInfo.push(c);if(!sent[c])miss.noSent.push(c)});
const strip=t=>t.replace(/\[[^\]]*\]/g,"");
Object.entries(sent).forEach(([c,[t,o]])=>{
  [...strip(t)].forEach(ch=>{if(/[一-鿿]/.test(ch)&&!ZY[ch])miss.noZy.add(ch)});
  if(!o.includes(c)||o.length<3)miss.optBad.push(c);
});
const buzy=Object.assign({},chars.buzy,extra.buzy);
Object.values(extra.trick).forEach(b=>{if(!buzy[b])miss.noZy.add("部件"+b)});
Object.values(chars.chars).forEach(v=>{if(!buzy[v.bu])miss.noZy.add("部首"+v.bu)});
// 課名和畫面上要加注音的字
[...L.A,...L.B].forEach(l=>[...l.n].forEach(ch=>{if(/[一-鿿]/.test(ch)&&!ZY[ch])miss.noZy.add("課名"+ch)}));
[..."從到訂單畫和「」的部首是哪一個？有幾意思相反字答對了相反"].forEach(ch=>{if(/[一-鿿]/.test(ch)&&!ZY[ch])miss.noZy.add("畫面"+ch)});
const anti=extra.anti;anti.flat().forEach(c=>{if(!ZY[c])miss.noZy.add(c)});
// 第二批：錯字、量詞、句子重組
Object.entries(extra.wrong).forEach(([c,w])=>{if(c===w)miss.optBad.push("錯字對到自己"+c)});
extra.mw.forEach(([n,m])=>[...strip(n)+m].forEach(ch=>{if(/[一-鿿]/.test(ch)&&!ZY[ch])miss.noZy.add("量詞"+ch)}));
[...extra.mwPool].forEach(ch=>{if(!ZY[ch])miss.noZy.add("量詞"+ch)});
["A","B"].forEach(v=>{if(extra.order[v].length!==L[v].length)miss.optBad.push(v+"版重組句子課數不對");
  extra.order[v].flat().forEach(t=>[...strip(t)].forEach(ch=>{if(/[一-鿿]/.test(ch)&&!ZY[ch])miss.noZy.add("重組"+ch)}))});
const out={L,chars:chars.chars,buzy,ZY,sent,anti,trick:extra.trick,wrong:extra.wrong,mw:extra.mw,mwPool:extra.mwPool,order:extra.order};
fs.writeFileSync(here("zi-data.js"),"/* 甜點小鎮資料（自動產生，請改 build.js 的來源） */\nwindow.ZI="+JSON.stringify(out)+";\n");
console.log("字數",all.size,"例句",Object.keys(sent).length,"注音",Object.keys(ZY).length);
console.log("缺部首筆畫:",miss.noInfo.join(""),"| 缺例句:",miss.noSent.join(""),"| 缺注音:",[...miss.noZy].join(" "),"| 選項有問題:",miss.optBad.join(""));

global.window={};eval(require('fs').readFileSync(process.argv[2],'utf8'));const Z=window.ZI;const s=new Set();
const add=t=>[...t].forEach(c=>s.add(c));
Object.values(Z.sent).forEach(([t,o])=>{add(t.replace(/\[[^\]]*\]/g,""));add(o)});
[...Z.L.A,...Z.L.B].forEach(l=>{add(l.s);add(l.r)});Object.keys(Z.buzy).forEach(add);Object.values(Z.trick).forEach(add);Z.anti.flat().forEach(add);Object.keys(Z.ZY).forEach(add);
add("「」？，。！、：0123456789");Object.keys(Z.ciZy||{}).forEach(add);(Z.place||[]).forEach(([n,m])=>add(n.replace(/\[[^\]]*\]/g,"")+m));Object.entries(Z.wrong||{}).forEach(([a,b])=>add(a+b));(Z.mw||[]).forEach(([n,m])=>add(n.replace(/\[[^\]]*\]/g,"")+m));add(Z.mwPool||"");Object.values(Z.order||{}).flat(2).forEach(t=>add(t.replace(/\[[^\]]*\]/g,"").replace(/\//g,"")));
// 頁面裡直接寫的字（成語故事、造詞範例等）也要放進字型
{const fs=require('fs'),path=require('path'),root=path.dirname(path.dirname(path.resolve(process.argv[2])));fs.readdirSync(root).filter(f=>/^town.*\.html$/.test(f)).forEach(f=>(fs.readFileSync(path.join(root,f),'utf8').match(/[㐀-鿿]/g)||[]).forEach(c=>s.add(c)))}
require('fs').writeFileSync(process.argv[3],[...s].join(""));console.log(s.size);

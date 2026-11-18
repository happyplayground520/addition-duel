global.window={};eval(require('fs').readFileSync(process.argv[2],'utf8'));const Z=window.ZI;const s=new Set();
const add=t=>[...t].forEach(c=>s.add(c));
Object.values(Z.sent).forEach(([t,o])=>{add(t.replace(/\[[^\]]*\]/g,""));add(o)});
[...Z.L.A,...Z.L.B].forEach(l=>{add(l.s);add(l.r)});Object.keys(Z.buzy).forEach(add);Object.values(Z.trick).forEach(add);Z.anti.flat().forEach(add);Object.keys(Z.ZY).forEach(add);
add("「」？，。！、：0123456789");
require('fs').writeFileSync(process.argv[3],[...s].join(""));console.log(s.size);

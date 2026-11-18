/* 海盜灣（英文區）共用：英文語音（美式、慢速）、中文說明語音、音效、單字和自己畫的圖示、鸚鵡主角、金幣和帽子 */
(function(){
  const EN={};
  EN.pref=(k,v)=>{try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}};
  EN.rnd=(a,b)=>a+Math.floor(Math.random()*(b-a+1));
  EN.shuffle=a=>{for(let i=a.length-1;i>0;i--){const j=EN.rnd(0,i);[a[i],a[j]]=[a[j],a[i]]}return a};
  EN.pick=a=>a[EN.rnd(0,a.length-1)];

  // ---------- 語音 ----------
  // 英文：美式、慢一點；中文說明：台灣國語
  const synth=window.speechSynthesis;let enV=null,zhV=null;
  const NOVELTY=/albert|bad news|bahh|bells|boing|bubbles|cellos|wobble|good news|jester|organ|superstar|trinoids|whisper|zarvox|fred|junior|ralph|kathy|grandma|grandpa|rocko|shelley|flo\b|eddy|reed|sandy|hysterical/i;
  const quality=v=>{const u=(v.voiceURI||"")+" "+v.name;
    if(/eloquence|speech\.synthesis\.voice/i.test(u)||NOVELTY.test(v.name))return 0;
    return /\.premium\.|premium/i.test(u)?3:/enhanced|natural|neural|online/i.test(u)?2:1};
  const LIKE=/samantha|ava|allison|susan|aria|jenny|zira|google us english/i;
  function pickVoices(){
    if(!synth)return;const vs=synth.getVoices();
    const us=vs.filter(v=>/^en[-_]US/i.test(v.lang)&&quality(v)>0)
      .sort((a,b)=>(quality(b)+(LIKE.test(b.name)?1.5:0))-(quality(a)+(LIKE.test(a.name)?1.5:0)));
    enV=us[0]||vs.find(v=>/^en/i.test(v.lang)&&quality(v)>0)||null;
    const zh=vs.filter(v=>/^(zh|cmn)/i.test(v.lang));
    zhV=zh.filter(v=>/TW|Hant/i.test(v.lang)&&quality(v)>0).sort((a,b)=>quality(b)-quality(a))[0]||zh.find(v=>quality(v)>0)||zh[0]||null;
  }
  if(synth){pickVoices();try{synth.addEventListener("voiceschanged",pickVoices)}catch(e){}}
  EN.rate=.72;
  let sayId=0;
  // say("cat") 念英文；say("中文",{zh:true}) 念中文。新的會蓋掉舊的
  EN.say=function(text,o={}){
    if(!synth||!text){o.onend&&setTimeout(o.onend,10);return}
    const id=++sayId;
    try{
      const u=new SpeechSynthesisUtterance(text),v=o.zh?zhV:enV;
      u.lang=v?v.lang.replace("_","-"):(o.zh?"zh-TW":"en-US");if(v)u.voice=v;
      u.rate=o.rate||(o.zh?.95:EN.rate);u.pitch=o.zh?1.1:1.05;
      if(o.onend){let done=false;const fin=()=>{if(done||id!==sayId)return;done=true;o.onend()};u.onend=fin;
        setTimeout(fin,1500+String(text).length*(o.zh?260:130))}
      if(synth.speaking||synth.pending){synth.cancel();setTimeout(()=>{try{synth.speak(u)}catch(e){}},90)}else synth.speak(u);
    }catch(e){o.onend&&o.onend()}
  };
  EN.stop=()=>{sayId++;try{synth&&synth.cancel()}catch(e){}};

  // ---------- 音效 ----------
  let ac=null;
  function tone(fs,dur=.12,type="triangle",vol=.15){
    try{
      ac=ac||new (window.AudioContext||window.webkitAudioContext)();if(ac.state!=="running")ac.resume();
      fs.forEach((f,i)=>{const o=ac.createOscillator(),g=ac.createGain(),t=ac.currentTime+i*dur;
        o.type=type;o.frequency.value=f;g.gain.setValueAtTime(vol,t);g.gain.exponentialRampToValueAtTime(.001,t+dur*1.6);
        o.connect(g).connect(ac.destination);o.start(t);o.stop(t+dur*1.7)});
    }catch(e){}
  }
  EN.sfx={
    good:()=>{try{window.parkBurst&&parkBurst()}catch(e){}tone([784,1175],.14,"sine",.3)},
    bad:()=>tone([150],.3,"square",.16),
    pop:()=>tone([660],.06,"sine",.15),
    splash:()=>tone([420,300,520],.05,"sine",.12),
    coin:()=>tone([988,1319],.09,"square",.08),
    clear:()=>tone([523,659,784,1047],.12,"sine",.2),
    end:()=>tone([784,659,523,784,1047],.14)
  };
  // iPad 要先點一下才能出聲：第一次點畫面時解鎖
  function unlock(){
    try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();if(ac.state!=="running")ac.resume()}catch(e){}
    try{if(synth&&!synth.speaking){const u=new SpeechSynthesisUtterance(" ");u.volume=0;synth.speak(u)}}catch(e){}
  }
  addEventListener("pointerdown",unlock,{once:true,capture:true});
  EN.unlock=unlock;

  // ---------- 自己畫的單字圖示（100×100，深咖啡色圓角外框） ----------
  const K="#3a2a22";
  const e=(x,y,r=4.3)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${K}" stroke="none"/><circle cx="${x+r*.32}" cy="${y-r*.36}" r="${r*.36}" fill="#fff" stroke="none"/>`;
  const ch=(x,y)=>`<ellipse cx="${x}" cy="${y}" rx="5" ry="3.2" fill="#ff9db5" stroke="none" opacity=".75"/>`;
  const wheel=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${K}"/><circle cx="${x}" cy="${y}" r="${r*.42}" fill="#d9dee5" stroke="none"/>`;
  const ICON={
    // 動物
    cat:`<path d="M21 46 26 13 45 30Z M79 46 74 13 55 30Z" fill="#ffb24d"/><path d="M28 34 29 22 38 30Z M72 34 71 22 62 30Z" fill="#ff9db5" stroke="none"/>
      <ellipse cx="50" cy="56" rx="32" ry="28" fill="#ffb24d"/><path d="M50 30v8M42 31l2 6M58 31l-2 6" fill="none" stroke-width="3"/>
      ${e(39,54)}${e(61,54)}<path d="M46 62h8l-4 4z" fill="#ff7a9a" stroke-width="2"/><path d="M50 66q-4 5-8 2M50 66q4 5 8 2" fill="none" stroke-width="3"/>
      <path d="M14 60l15 2M14 69l15-3M86 60l-15 2M86 69l-15-3" fill="none" stroke-width="2.5"/>${ch(31,64)}${ch(69,64)}`,
    dog:`<ellipse cx="50" cy="54" rx="28" ry="27" fill="#f2c28f"/><ellipse cx="23" cy="52" rx="10" ry="20" fill="#a8683a" transform="rotate(18 23 52)"/>
      <ellipse cx="77" cy="52" rx="10" ry="20" fill="#a8683a" transform="rotate(-18 77 52)"/><ellipse cx="50" cy="67" rx="15" ry="11" fill="#fff3e0"/>
      <ellipse cx="50" cy="60" rx="6.5" ry="4.6" fill="${K}"/><path d="M47 70q3 8 6 0z" fill="#ff7a9a" stroke-width="2"/><path d="M50 64v4q-4 4-8 1M50 68q4 4 8 1" fill="none" stroke-width="3"/>
      ${e(40,47)}${e(60,47)}${ch(33,60)}${ch(67,60)}`,
    bird:`<path d="M42 30q0-12 10-14q-2 6 0 10" fill="#5cb8ff"/><circle cx="46" cy="56" r="28" fill="#5cb8ff"/><ellipse cx="50" cy="67" rx="16" ry="13" fill="#d7f0ff" stroke="none"/>
      <path d="M28 52q-8 18 12 24q4-14-12-24z" fill="#3a8fe0"/><path d="M72 49l15 7-15 7z" fill="#ffb02e"/>${e(60,47)}${ch(63,58)}<path d="M42 84v9M54 84v9" fill="none"/>`,
    fish:`<path d="M40 31q10-15 23-3" fill="#ff6a1a"/><path d="M25 50 6 33v34z" fill="#ff6a1a"/><ellipse cx="50" cy="50" rx="30" ry="22" fill="#ff8a3d"/>
      <path d="M42 40q6 10 0 20M52 40q6 10 0 20" fill="none" stroke-width="3" opacity=".45"/>${e(66,45)}<path d="M79 55q-3 3-7 1" fill="none" stroke-width="3"/>`,
    pig:`<path d="M24 36 26 14 44 28Z M76 36 74 14 56 28Z" fill="#ff9fbb"/><circle cx="50" cy="55" r="30" fill="#ffc2d4"/><ellipse cx="50" cy="63" rx="14" ry="10" fill="#ff9fbb"/>
      <ellipse cx="45" cy="63" rx="2.5" ry="3.6" fill="${K}" stroke="none"/><ellipse cx="55" cy="63" rx="2.5" ry="3.6" fill="${K}" stroke="none"/>${e(38,47)}${e(62,47)}${ch(29,62)}${ch(71,62)}`,
    cow:`<path d="M30 28q-10-8-6-18q6 6 12 12zM70 28q10-8 6-18q-6 6-12 12z" fill="#fff3c4"/><ellipse cx="17" cy="43" rx="11" ry="6" fill="#fff" transform="rotate(-20 17 43)"/>
      <ellipse cx="83" cy="43" rx="11" ry="6" fill="#fff" transform="rotate(20 83 43)"/><rect x="25" y="22" width="50" height="58" rx="23" fill="#fff"/>
      <path d="M32 31q9-5 14 3q-2 10-13 8z" fill="${K}" stroke="none"/><path d="M62 52q8-4 10 4q-2 6-8 4z" fill="${K}" stroke="none"/>
      <ellipse cx="50" cy="70" rx="23" ry="13" fill="#ffb3c7"/><ellipse cx="42" cy="70" rx="2.6" ry="3.6" fill="${K}" stroke="none"/><ellipse cx="58" cy="70" rx="2.6" ry="3.6" fill="${K}" stroke="none"/>${e(40,48)}${e(60,48)}`,
    duck:`<path d="M20 62l-9-9 14 1z" fill="#ffd93d"/><ellipse cx="45" cy="67" rx="30" ry="20" fill="#ffd93d"/><circle cx="58" cy="38" r="17" fill="#ffd93d"/>
      <path d="M72 38q15-3 17 4q-6 7-17 2z" fill="#ff9a1f"/>${e(60,34)}${ch(56,45)}<path d="M28 62q15-7 27 4q-13 12-27-4z" fill="#ffc21a"/>`,
    rabbit:`<ellipse cx="38" cy="27" rx="8.5" ry="22" fill="#fff"/><ellipse cx="62" cy="27" rx="8.5" ry="22" fill="#fff"/>
      <ellipse cx="38" cy="27" rx="3.6" ry="15" fill="#ffb3c7" stroke="none"/><ellipse cx="62" cy="27" rx="3.6" ry="15" fill="#ffb3c7" stroke="none"/>
      <ellipse cx="50" cy="62" rx="29" ry="25" fill="#fff"/>${e(40,58)}${e(60,58)}<path d="M47 66h6l-3 3z" fill="#ff7a9a" stroke-width="2"/>
      <path d="M50 69q-3 4-6 2M50 69q3 4 6 2" fill="none" stroke-width="3"/>${ch(32,68)}${ch(68,68)}`,
    bear:`<circle cx="26" cy="31" r="11" fill="#b9773e"/><circle cx="74" cy="31" r="11" fill="#b9773e"/><circle cx="26" cy="31" r="5" fill="#f2d3a8" stroke="none"/><circle cx="74" cy="31" r="5" fill="#f2d3a8" stroke="none"/>
      <circle cx="50" cy="56" r="30" fill="#b9773e"/><ellipse cx="50" cy="66" rx="14" ry="11" fill="#f2d3a8"/><ellipse cx="50" cy="62" rx="5.5" ry="4" fill="${K}"/>
      <path d="M50 66v3q-3 3-6 1M50 69q3 3 6 1" fill="none" stroke-width="3"/>${e(39,51)}${e(61,51)}${ch(32,62)}${ch(68,62)}`,
    monkey:`<circle cx="19" cy="52" r="11" fill="#f2c9a0"/><circle cx="81" cy="52" r="11" fill="#f2c9a0"/><circle cx="50" cy="50" r="30" fill="#9a5b32"/>
      <path d="M50 42q-6-8-14-7q-12 2-12 16q0 22 26 25q26-3 26-25q0-14-12-16q-8-1-14 7z" fill="#f2c9a0"/>${e(41,50)}${e(59,50)}
      <circle cx="47" cy="59" r="1.4" fill="${K}" stroke="none"/><circle cx="53" cy="59" r="1.4" fill="${K}" stroke="none"/><path d="M40 65q10 8 20 0" fill="none" stroke-width="3"/>`,
    tiger:`<circle cx="26" cy="29" r="10" fill="#ff9a2e"/><circle cx="74" cy="29" r="10" fill="#ff9a2e"/><ellipse cx="50" cy="56" rx="32" ry="29" fill="#ff9a2e"/>
      <path d="M50 28v10M40 30l3 8M60 30l-3 8M19 51h9M20 61h8M81 51h-9M80 61h-8" fill="none" stroke-width="4"/>
      <ellipse cx="43" cy="68" rx="10" ry="8" fill="#fff"/><ellipse cx="57" cy="68" rx="10" ry="8" fill="#fff"/><path d="M45 61h10l-5 5z" fill="${K}" stroke-width="2"/>${e(39,51)}${e(61,51)}`,
    lion:`<circle cx="50" cy="52" r="38" fill="#c8742a" stroke-dasharray="7 4"/><circle cx="32" cy="34" r="7" fill="#ffd36b"/><circle cx="68" cy="34" r="7" fill="#ffd36b"/>
      <circle cx="50" cy="55" r="25" fill="#ffd36b"/>${e(41,51)}${e(59,51)}<path d="M45 59h10l-5 5z" fill="${K}" stroke-width="2"/>
      <path d="M50 64v2q-4 4-8 1M50 66q4 4 8 1" fill="none" stroke-width="3"/>${ch(35,62)}${ch(65,62)}`,
    elephant:`<ellipse cx="22" cy="50" rx="18" ry="23" fill="#a9b8c9"/><ellipse cx="78" cy="50" rx="18" ry="23" fill="#a9b8c9"/>
      <ellipse cx="22" cy="50" rx="10" ry="14" fill="#ffc2d4" stroke="none"/><ellipse cx="78" cy="50" rx="10" ry="14" fill="#ffc2d4" stroke="none"/>
      <path d="M43 60q-3 20 7 28q9 4 11-3q-7-2-7-11V60z" fill="#b9c7d6"/><ellipse cx="50" cy="46" rx="25" ry="25" fill="#b9c7d6"/>${e(40,44)}${e(60,44)}${ch(34,54)}${ch(66,54)}`,
    frog:`<circle cx="32" cy="33" r="13" fill="#6cc24a"/><circle cx="68" cy="33" r="13" fill="#6cc24a"/><ellipse cx="50" cy="60" rx="37" ry="27" fill="#6cc24a"/>
      <circle cx="32" cy="33" r="8" fill="#fff" stroke="none"/><circle cx="68" cy="33" r="8" fill="#fff" stroke="none"/>${e(33,34,4.6)}${e(69,34,4.6)}
      <path d="M30 63q20 16 40 0" fill="none"/>${ch(22,64)}${ch(78,64)}`,
    // 食物
    apple:`<path d="M50 30q0-10 6-16" fill="none"/><path d="M54 22q10-11 21-6q-7 12-21 6z" fill="#5cc24a"/>
      <path d="M50 31q-11-8-22-2q-14 8-10 30q4 22 20 28q6 2 12-2q6 4 12 2q16-6 20-28q4-22-10-30q-11-6-22 2z" fill="#ff4d4d"/>
      <ellipse cx="33" cy="46" rx="5" ry="9" fill="#fff" stroke="none" opacity=".55"/>`,
    banana:`<path d="M24 29l-3-10 9 3z" fill="#8a6a3a"/><path d="M25 29Q15 70 52 80Q78 85 90 64Q84 58 78 62Q62 71 46 61Q32 51 32 29Z" fill="#ffe14d"/>
      <path d="M28 44q4 24 26 30" fill="none" stroke-width="3" opacity=".4"/><path d="M90 64l3 3" fill="none"/>`,
    orange:`<path d="M50 28q0-6 3-10" fill="none"/><path d="M52 24q7-12 19-10q-4 12-19 10z" fill="#5cc24a"/><circle cx="50" cy="57" r="30" fill="#ffa62b"/>
      <g fill="#e88a10" stroke="none"><circle cx="40" cy="52" r="1.7"/><circle cx="58" cy="48" r="1.7"/><circle cx="62" cy="66" r="1.7"/><circle cx="44" cy="70" r="1.7"/><circle cx="52" cy="60" r="1.7"/></g>
      <ellipse cx="36" cy="44" rx="5" ry="8" fill="#fff" stroke="none" opacity=".5"/>`,
    egg:`<path d="M50 14q27 0 29 46q0 27-29 27q-29 0-29-27q2-46 29-46z" fill="#fff6e0"/><ellipse cx="38" cy="40" rx="5" ry="10" fill="#fff" stroke="none"/>`,
    cake:`<ellipse cx="50" cy="85" rx="42" ry="7" fill="#d7f0ff"/><rect x="18" y="48" width="64" height="34" rx="6" fill="#ffe0b0"/>
      <path d="M18 57q0-9 9-9h46q9 0 9 9q-5 7-10 0q-5 7-11 0q-5 7-11 0q-5 7-11 0q-5 7-11 0q-4 6-10 0z" fill="#ffb3c7"/>
      <rect x="47" y="25" width="6" height="22" rx="2" fill="#7ec8ff"/><path d="M50 12q7 7 0 12q-7-5 0-12z" fill="#ffc53d" stroke-width="2.5"/>
      <circle cx="31" cy="44" r="6" fill="#ff4d4d"/><circle cx="69" cy="44" r="6" fill="#ff4d4d"/>`,
    milk:`<rect x="38" y="11" width="24" height="9" rx="2" fill="#fff"/><path d="M30 37l8-17h24l8 17z" fill="#e6f3ff"/><path d="M30 37h40v51H30z" fill="#fff"/>
      <rect x="30" y="53" width="40" height="19" fill="#4da3ff"/><path d="M50 55q6 7 0 13q-6-6 0-13z" fill="#fff" stroke="none"/>`,
    bread:`<path d="M24 47q-11-22 10-29q16-6 32 0q21 7 10 29v35H24z" fill="#d9954a"/><path d="M31 49q-8-15 8-21q11-4 22 0q16 6 8 21v27H31z" fill="#ffe3a8" stroke="none"/>`,
    rice:`<path d="M20 55q3-25 30-25t30 25z" fill="#fff"/><g fill="#e2e2e2" stroke="none"><ellipse cx="38" cy="44" rx="2" ry="3.4"/><ellipse cx="52" cy="38" rx="2" ry="3.4"/><ellipse cx="62" cy="46" rx="2" ry="3.4"/><ellipse cx="46" cy="50" rx="2" ry="3.4"/></g>
      <path d="M15 55h70q-2 31-35 31t-35-31z" fill="#5ca8ff"/><path d="M24 67q26 8 52 0" fill="none" stroke="#fff" stroke-width="3"/>
      <path d="M62 22l30-12M66 28l30-10" fill="none" stroke="#a8683a" stroke-width="5"/>`,
    juice:`<path d="M58 28V14l11-6" fill="none" stroke="#ff4d8a" stroke-width="5"/><rect x="30" y="28" width="40" height="59" rx="5" fill="#ffa62b"/>
      <circle cx="50" cy="59" r="12" fill="#fff"/><circle cx="50" cy="59" r="7.5" fill="#ffc53d" stroke="none"/><path d="M50 47q4-6 9-5" fill="none" stroke="#5cc24a" stroke-width="3"/>`,
    candy:`<path d="M31 50 12 37v26zM69 50 88 37v26z" fill="#ff7ab0"/><circle cx="50" cy="50" r="21" fill="#ff4d8a"/>
      <path d="M50 50m-10 0a10 10 0 1 1 10 10" fill="none" stroke="#fff" stroke-width="4.5"/>`,
    pizza:`<path d="M50 89 18 25q32-15 64 0z" fill="#ffd36b"/><path d="M18 25q32-15 64 0l-4 8q-28-12-56 0z" fill="#d9954a"/>
      <circle cx="43" cy="44" r="6" fill="#e8433a"/><circle cx="58" cy="52" r="6" fill="#e8433a"/><circle cx="49" cy="67" r="5" fill="#e8433a"/>`,
    "ice cream":`<path d="M33 50l17 41 17-41z" fill="#e8b06a"/><path d="M38 60l20 10M42 72l12 6M62 60l-20 10" fill="none" stroke-width="2.5" opacity=".6"/>
      <path d="M29 52q-7-31 21-33q28 2 21 33z" fill="#ffb3c7"/><circle cx="50" cy="16" r="5.5" fill="#ff4d4d"/>`,
    hamburger:`<path d="M18 70h64q0 15-14 15H32q-14 0-14-15z" fill="#e8a24a"/><rect x="15" y="55" width="70" height="13" rx="6.5" fill="#8a4a22"/>
      <path d="M15 53q6 7 12 0q6 7 12 0q6 7 12 0q6 7 12 0q6 7 12 0q5 6 10 0" fill="#7ed957" stroke-width="3"/>
      <path d="M17 49q2-31 33-31t33 31z" fill="#e8a24a"/><g fill="#fff6d6" stroke="none"><ellipse cx="38" cy="32" rx="2.5" ry="1.5"/><ellipse cx="52" cy="27" rx="2.5" ry="1.5"/><ellipse cx="62" cy="36" rx="2.5" ry="1.5"/><ellipse cx="45" cy="40" rx="2.5" ry="1.5"/></g>`,
    noodles:`<path d="M30 20q-4-6 0-12M42 20q-4-6 0-12" fill="none" stroke-width="3" opacity=".5"/>
      <path d="M48 24q-5 15 0 30M54 24q5 15 0 30M60 26q2 12 0 28" fill="none" stroke="#f2b84a" stroke-width="4"/>
      <path d="M58 8l-9 30M68 8l-10 30" fill="none" stroke="#a8683a" stroke-width="4.5"/>
      <path d="M13 53h74q-2 33-37 33t-37-33z" fill="#ff6b5a"/><path d="M20 66q30 9 60 0" fill="none" stroke="#fff" stroke-width="3"/>`,
    strawberry:`<path d="M50 89q-31-20-31-45q0-14 31-14t31 14q0 25-31 45z" fill="#ff4d4d"/><path d="M29 33q11 7 21-2q10 9 21 2q-6-11-21-9q-15-2-21 9z" fill="#5cc24a"/>
      <g fill="#ffe14d" stroke="none"><ellipse cx="38" cy="48" rx="1.8" ry="2.6"/><ellipse cx="50" cy="46" rx="1.8" ry="2.6"/><ellipse cx="62" cy="48" rx="1.8" ry="2.6"/><ellipse cx="44" cy="60" rx="1.8" ry="2.6"/><ellipse cx="56" cy="60" rx="1.8" ry="2.6"/><ellipse cx="50" cy="72" rx="1.8" ry="2.6"/></g>`,
    "cotton candy":`<path d="M50 58v36" fill="none" stroke="#e8b06a" stroke-width="6"/>
      <path d="M30 58q-15-4-11-19q2-12 15-12q4-15 19-13q14-2 18 13q13 0 15 12q4 15-11 19q-8 8-22 6q-14 2-23-6z" fill="#ffc2e0"/>
      <path d="M33 42q4-6 10-5M56 30q6-2 9 3" fill="none" stroke="#fff" stroke-width="3.5"/>`,
    "candied fruit":`<path d="M50 6v90" fill="none" stroke="#e8b06a" stroke-width="5"/>
      <circle cx="50" cy="20" r="12" fill="#e8302a"/><circle cx="50" cy="43" r="12" fill="#e8302a"/><circle cx="50" cy="66" r="12" fill="#e8302a"/>
      <g fill="#fff" stroke="none" opacity=".85"><ellipse cx="45" cy="15" rx="3" ry="4.5"/><ellipse cx="45" cy="38" rx="3" ry="4.5"/><ellipse cx="45" cy="61" rx="3" ry="4.5"/></g>`,
    cookie:`<circle cx="50" cy="50" r="34" fill="#e8b06a"/><g fill="#6e4122" stroke="none"><ellipse cx="38" cy="38" rx="5" ry="4"/><ellipse cx="60" cy="34" rx="4" ry="3.5"/><ellipse cx="64" cy="58" rx="5" ry="4"/><ellipse cx="42" cy="62" rx="4.5" ry="3.5"/><ellipse cx="52" cy="48" rx="3.5" ry="3"/></g>`,
    spaghetti:`<path d="M84 22 72 52" fill="none" stroke="#9aa8b8" stroke-width="4"/><ellipse cx="48" cy="67" rx="40" ry="16" fill="#fff"/>
      <path d="M22 64q0-24 26-24t26 24z" fill="#ffe08a"/><path d="M29 58q6-8 12 0t12 0 12 0M33 50q5-6 10 0t10 0" fill="none" stroke="#e8b84a" stroke-width="3"/>
      <path d="M35 46q13-10 26 0q-4 8-13 8t-13-8z" fill="#e8433a"/><circle cx="48" cy="42" r="7" fill="#8a4a22"/>`,
    tomato:`<circle cx="50" cy="57" r="31" fill="#ff4d3a"/><path d="M50 32l-14-8 8 10-14 3 14 3 6 8 6-8 14-3-14-3 8-10z" fill="#5cc24a" stroke-width="3"/>
      <path d="M50 28v-10" fill="none"/><ellipse cx="34" cy="50" rx="5" ry="8" fill="#fff" stroke="none" opacity=".5"/>`,
    // 交通與玩具
    car:`<path d="M9 66V52q0-6 6-8l13-2 10-14q4-4 10-4h21q6 0 10 6l8 12 8 2q6 2 6 8v14z" fill="#ff4d4d"/>
      <path d="M41 30h12v12H32zM59 30h10l8 12H59z" fill="#bfe6ff" stroke-width="3"/>${wheel(30,67,10)}${wheel(72,67,10)}<circle cx="88" cy="56" r="3" fill="#ffe14d" stroke="none"/>`,
    bus:`<rect x="7" y="22" width="86" height="46" rx="9" fill="#ffc72e"/><g fill="#bfe6ff" stroke-width="3"><rect x="14" y="29" width="14" height="15" rx="2"/><rect x="33" y="29" width="14" height="15" rx="2"/><rect x="52" y="29" width="14" height="15" rx="2"/><rect x="71" y="29" width="15" height="15" rx="2"/></g>
      <path d="M7 54h86" fill="none" stroke="#e89a10" stroke-width="4"/>${wheel(27,70,9)}${wheel(73,70,9)}`,
    bike:`<circle cx="25" cy="64" r="16" fill="none" stroke-width="5"/><circle cx="75" cy="64" r="16" fill="none" stroke-width="5"/>
      <path d="M25 64l17-24h25M42 40l12 24 13-24 8 24M54 64H25" fill="none" stroke="#ff4d4d" stroke-width="5"/>
      <path d="M36 32h12M67 40l-3-10h9" fill="none" stroke-width="5"/>`,
    boat:`<path d="M50 64V12" fill="none"/><path d="M53 15v43h30z" fill="#fff"/><path d="M47 23v35H24z" fill="#ff6b5a"/><path d="M11 64h78l-13 19H24z" fill="#a8683a"/>
      <path d="M5 90q8-6 15 0t15 0 15 0 15 0 15 0 15 0" fill="none" stroke="#4da3ff" stroke-width="4"/>`,
    train:`<circle cx="25" cy="14" r="5" fill="#fff" stroke-width="2.5"/><circle cx="16" cy="8" r="4" fill="#fff" stroke-width="2.5"/>
      <rect x="20" y="25" width="11" height="18" fill="${K}"/><rect x="11" y="42" width="42" height="27" rx="7" fill="#4da3ff"/>
      <rect x="51" y="27" width="35" height="42" rx="4" fill="#ff4d4d"/><rect x="47" y="20" width="43" height="8" rx="3" fill="${K}"/>
      <rect x="59" y="34" width="19" height="14" rx="2" fill="#bfe6ff" stroke-width="3"/>${wheel(23,73,9)}${wheel(45,73,9)}${wheel(72,71,12)}`,
    plane:`<path d="M17 48l-5-19h10l11 16z" fill="#ff4d4d"/><path d="M39 54l18-27h11l-6 27z" fill="#4da3ff"/>
      <path d="M9 55q0-8 13-8h56q15 0 17 8q-2 8-17 8H22q-13 0-13-8z" fill="#fff"/><path d="M39 57l14 22h11l-4-22z" fill="#4da3ff"/>
      <g fill="#4da3ff" stroke="none"><circle cx="58" cy="53" r="2.6"/><circle cx="67" cy="53" r="2.6"/><circle cx="76" cy="53" r="2.6"/></g><path d="M85 50q6 2 8 5h-8z" fill="#bfe6ff" stroke-width="2"/>`,
    scooter:`<path d="M10 65q0-21 25-21h18l4 21z" fill="#4dc3a0"/><rect x="16" y="35" width="34" height="10" rx="5" fill="${K}"/>
      <path d="M44 65h28" fill="none" stroke-width="7"/><path d="M65 67l8-40h9l-4 40z" fill="#4dc3a0"/><path d="M72 25h15" fill="none" stroke-width="5"/>
      <circle cx="83" cy="35" r="4" fill="#ffe14d"/>${wheel(24,72,10)}${wheel(77,72,10)}`,
    ball:`<circle cx="50" cy="52" r="34" fill="#ffd93d" stroke="none"/><path d="M50 18q-22 34 0 68q-34-6-34-34t34-34z" fill="#ff4d4d" stroke="none"/>
      <path d="M50 18q22 34 0 68q34-6 34-34t-34-34z" fill="#4da3ff" stroke="none"/><path d="M50 18q-22 34 0 68M50 18q22 34 0 68" fill="none" stroke-width="3"/>
      <circle cx="50" cy="52" r="34" fill="none"/><ellipse cx="36" cy="34" rx="5" ry="3" fill="#fff" stroke="none" opacity=".7" transform="rotate(-35 36 34)"/>`,
    kite:`<path d="M50 74q-9 7 0 13t0 11" fill="none" stroke-width="3"/><path d="M44 84l-6-3v6zM56 92l6-3v6z" fill="#4da3ff" stroke-width="2"/>
      <path d="M50 8l27 31-27 35-27-35z" fill="#ff6b9a"/><path d="M50 8v66M23 39h54" fill="none" stroke-width="3"/><path d="M50 8l27 31H50z" fill="#ffd93d" stroke="none" opacity=".9"/>`,
    doll:`<path d="M25 46q0-32 25-32t25 32v26H25z" fill="#a8683a"/><path d="M34 64h32l11 28H23z" fill="#ff6b9a"/><circle cx="50" cy="45" r="18" fill="#ffe0c2"/>
      <path d="M32 41q4-17 18-17t18 17q-10-7-18-7t-18 7z" fill="#a8683a" stroke-width="3"/>${e(43,47,3.6)}${e(57,47,3.6)}<path d="M46 54q4 3 8 0" fill="none" stroke-width="3"/>${ch(38,53)}${ch(62,53)}
      <path d="M64 26l11-7v13zM64 26l-1-10 8 4z" fill="#ff4d8a" stroke-width="3"/>`,
    robot:`<path d="M50 21v-9" fill="none"/><circle cx="50" cy="10" r="4.5" fill="#ff4d4d"/><rect x="18" y="30" width="8" height="14" rx="3" fill="#9aa8b8"/><rect x="74" y="30" width="8" height="14" rx="3" fill="#9aa8b8"/>
      <rect x="25" y="20" width="50" height="37" rx="9" fill="#b9c7d6"/><circle cx="40" cy="36" r="6" fill="#4dc3ff"/><circle cx="60" cy="36" r="6" fill="#4dc3ff"/>
      <rect x="40" y="46" width="20" height="5" rx="2.5" fill="${K}" stroke="none"/><rect x="30" y="59" width="40" height="30" rx="6" fill="#9aa8b8"/>
      <circle cx="42" cy="72" r="3.5" fill="#ffd93d"/><circle cx="58" cy="72" r="3.5" fill="#ff4d4d"/>`,
    hat:`<ellipse cx="50" cy="67" rx="41" ry="12" fill="#f2c26b"/><path d="M28 66q0-35 22-35t22 35z" fill="#f2c26b"/><path d="M29 55q21 5 42 0v9q-21 5-42 0z" fill="#ff6b5a" stroke-width="3"/>`,
    umbrella:`<path d="M50 50v31q0 9-8 9t-8-9" fill="none" stroke-width="5"/><path d="M50 15V9" fill="none" stroke-width="4"/>
      <path d="M9 51q0-37 41-37t41 37q-7-6-13 0q-7-6-14 0q-7-6-14 0q-7-6-14 0q-7-6-13 0q-7-6-13 0z" fill="#7b5cff"/>
      <path d="M50 14q-14 14-14 37M50 14q14 14 14 37" fill="none" stroke-width="3"/>`
  };
  // 顏色：一團可愛的顏料
  const COLOR={red:"#ff4136",blue:"#2f7bff",yellow:"#ffd60a",green:"#2ecc40",black:"#2b2b2b",white:"#ffffff",pink:"#ff8fc7",purple:"#9b51e0",brown:"#9a5b32",orange:"#ff8c1a"};
  const blob=c=>`<path d="M50 14q10 0 13 10q10-7 17 1t-2 16q12 4 10 14t-14 8q2 12-8 16t-17-4q-8 10-18 4t-4-16q-12 0-14-10t10-15q-8-10 0-16t17 1q1-9 10-9z" fill="${c}"/>
    <ellipse cx="38" cy="36" rx="6" ry="4" fill="#fff" stroke="none" opacity="${c==="#ffffff"?0:.55}" transform="rotate(-30 38 36)"/>`;
  // 數字：點點（不用阿拉伯數字）
  const NUM=["zero","one","two","three","four","five","six","seven","eight","nine","ten"];
  function dots(n){
    const rows=n<=5?[n]:[5,n-5],R=8,gap=17.6;let s=`<rect x="3" y="16" width="94" height="68" rx="12" fill="#fffaf0"/>`;
    rows.forEach((k,ri)=>{const y=rows.length===1?50:37+ri*26;for(let i=0;i<k;i++)s+=`<circle cx="${50+(i-(k-1)/2)*gap}" cy="${y}" r="${R}" fill="#ff6b5a"/>`});
    return s;
  }
  EN.icon=function(w,cls=""){
    let body=ICON[w];
    if(!body&&COLOR[w])body=blob(COLOR[w]);
    if(!body&&NUM.indexOf(w)>0)body=dots(NUM.indexOf(w));
    if(!body)return `<span class="ic-miss">${w}</span>`;
    return `<svg class="ic ${cls}" viewBox="0 0 100 100" aria-hidden="true"><g stroke="${K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">${body}</g></svg>`;
  };
  // 同一個字在不同主題（orange 是水果也是顏色）：用 theme 決定圖
  EN.iconIn=function(w,theme,cls){
    if(theme==="colors"&&COLOR[w])return `<svg class="ic ${cls||""}" viewBox="0 0 100 100" aria-hidden="true"><g stroke="${K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">${blob(COLOR[w])}</g></svg>`;
    return EN.icon(w,cls);
  };
  EN.THEMES=[
    {id:"animals",name:"Animals",rep:"cat",words:["cat","dog","bird","fish","pig","cow","duck","rabbit","bear","monkey","tiger","lion","elephant","frog"]},
    {id:"food",name:"Food",rep:"apple",words:["apple","banana","orange","egg","cake","milk","bread","rice","juice","candy","pizza","ice cream","hamburger","noodles","strawberry","cotton candy","candied fruit","cookie","spaghetti","tomato"]},
    {id:"colors",name:"Colors",rep:"red",words:["red","blue","yellow","green","black","white","pink","purple","brown","orange"]},
    {id:"numbers",name:"Numbers",rep:"three",words:NUM.slice(1)},
    {id:"toys",name:"Toys",rep:"car",words:["car","bus","bike","boat","train","plane","scooter","ball","kite","doll","robot","hat","umbrella"]}
  ];

  // ---------- 鸚鵡主角（可以戴帽子） ----------
  EN.HATS={
    none:{price:0,svg:""},
    pirate:{price:10,svg:`<path d="M24 22q26-24 54 0q-6 6-27 6t-27-6z" fill="#2b2b3a"/><path d="M27 21q24 6 48 0" fill="none" stroke="#ffd23f" stroke-width="3"/><path d="M51 9l2.2 4.6 5 .6-3.7 3.4 1 5-4.5-2.5-4.5 2.5 1-5-3.7-3.4 5-.6z" fill="#ffd23f" stroke="none"/>`},
    sailor:{price:15,svg:`<path d="M30 22q2-14 21-14t21 14z" fill="#fff"/><rect x="29" y="19" width="44" height="7" rx="3" fill="#2f7bff"/><circle cx="51" cy="8" r="3.5" fill="#ff4136" stroke="none"/>`},
    flower:{price:20,svg:`<g transform="translate(66 14)"><circle r="5.5" cx="0" cy="-6" fill="#ff8fc7"/><circle r="5.5" cx="6" cy="-1" fill="#ff8fc7"/><circle r="5.5" cx="4" cy="6" fill="#ff8fc7"/><circle r="5.5" cx="-4" cy="6" fill="#ff8fc7"/><circle r="5.5" cx="-6" cy="-1" fill="#ff8fc7"/><circle r="4" fill="#ffd23f"/></g>`},
    party:{price:25,svg:`<path d="M38 24l13-26 13 26z" fill="#9b51e0"/><path d="M42 16l12 4M46 8l8 3" fill="none" stroke="#ffd23f" stroke-width="3.5"/><circle cx="51" cy="-3" r="4" fill="#ffd23f"/>`},
    crown:{price:40,svg:`<path d="M32 24l-3-18 11 9 11-13 11 13 11-9-3 18z" fill="#ffd23f"/><circle cx="51" cy="16" r="3" fill="#ff4136" stroke="none"/><circle cx="39" cy="18" r="2.5" fill="#2f7bff" stroke="none"/><circle cx="63" cy="18" r="2.5" fill="#2ecc40" stroke="none"/>`}
  };
  EN.hat=()=>{const h=EN.pref("cove-hat");return EN.HATS[h]?h:"none"};
  EN.parrot=function(hat=EN.hat(),cls=""){
    const H=EN.HATS[hat]||EN.HATS.none;
    return `<svg class="parrot ${cls}" viewBox="0 -10 100 122" aria-hidden="true"><g stroke="${K}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round">
      <path d="M44 86l-8 22 9-3 4 6 5-24z" fill="#2f7bff"/><path d="M50 88l2 20 7-6 4 4-4-20z" fill="#2ecc40"/>
      <path d="M40 96v6M40 102l-4 2M40 102l3 3M58 96v6M58 102l-3 2M58 102l4 3" fill="none" stroke="#e8902a" stroke-width="3.5"/>
      <ellipse cx="49" cy="64" rx="25" ry="32" fill="#ef4b3c"/><ellipse cx="54" cy="72" rx="13" ry="18" fill="#ffb54d" stroke="none"/>
      <g class="wing"><path d="M30 50q-14 26 4 44q15-12 10-40z" fill="#2ecc40"/><path d="M28 72q2 12 7 19q5-6 6-14z" fill="#2f7bff" stroke-width="3"/></g>
      <circle cx="53" cy="34" r="22" fill="#ef4b3c"/><ellipse cx="62" cy="33" rx="10.5" ry="9.5" fill="#fff"/>
      <circle cx="63" cy="32" r="4.6" fill="${K}" stroke="none"/><circle cx="64.6" cy="30.4" r="1.7" fill="#fff" stroke="none"/>
      <path d="M70 34q15-1 14 14q-7-5-14-5z" fill="#ffc53d"/><path d="M71 44q6 1 9 5q-5 1-9-1z" fill="#3a2a22" stroke-width="2"/>
      <ellipse cx="57" cy="44" rx="4.5" ry="2.8" fill="#ff9db5" stroke="none" opacity=".85"/>
      <path d="M44 14q2-8 10-9q-3 5-1 9M50 13q5-7 12-5q-5 3-5 8" fill="#ef4b3c"/>
      <g class="hat">${H.svg}</g></g></svg>`;
  };

  // ---------- 金幣 ----------
  EN.coinSvg=`<svg class="coin" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17" fill="#ffd23f" stroke="#c98a10" stroke-width="3"/><circle cx="20" cy="20" r="11.5" fill="none" stroke="#f2a90f" stroke-width="2.5"/><path d="M20 13.5l1.9 4 4.4.5-3.3 3 .9 4.4-3.9-2.2-3.9 2.2.9-4.4-3.3-3 4.4-.5z" fill="#f2a90f"/><path d="M11 14q3-5 8-6" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" opacity=".8"/></svg>`;
  EN.coins=()=>+EN.pref("cove-coins")||0;
  EN.addCoins=n=>{const c=EN.coins()+n;EN.pref("cove-coins",c);return c};
  EN.owned=()=>{try{return JSON.parse(EN.pref("cove-hats")||"[]")}catch(e){return []}};

  // ---------- 共用的小東西 ----------
  // 🔊 中文說明按鈕：念一段中文玩法說明
  EN.helpBtn=function(btn,textFn){btn.addEventListener("click",()=>EN.say(typeof textFn==="function"?textFn():textFn,{zh:true}))};
  // 鸚鵡做表情：happy（拍翅膀跳一下）、oops（歪頭）
  EN.mood=function(el,m){if(!el)return;el.classList.remove("happy","oops");void el.offsetWidth;el.classList.add(m);clearTimeout(el._mt);el._mt=setTimeout(()=>el.classList.remove(m),1100)};
  EN.PRAISE=["Great!","Good job!","Yes!","Super!","Well done!","Nice!"];
  window.EN=EN;
})();

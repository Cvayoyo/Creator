(()=>{"use strict";(()=>{let e;const t=Element.prototype.attachShadow;Element.prototype.attachShadow=function(...e){e[0]&&"closed"===e[0].mode&&(e[0].mode="open");return t.apply(this,e)},(()=>{const e=setInterval((()=>{const t=window;if(t.turnstile&&"function"==typeof t.turnstile.render){const a=t.turnstile.render;clearInterval(e),t.turnstile.render=function(...e){const{action:n,cData:s,chlPageData:i,callback:o,sitekey:l}=e[1],c=new MessageEvent("message",{data:{cData:s,event:"turnstileParams",chlPageData:i,action:n,sitekey:l,userAgent:window.navigator.userAgent}});return t.dispatchEvent(c),t.turnstileCallback=o,a.apply(this,e)}}}))})(),window.addEventListener("message",(t=>{"init"===t.data.event&&(e=t.data.widgetId)})),window.addEventListener("message",(e=>{e.data.event})),window.addEventListener("message",(t=>{if("invokeTurnstileCallback"===t.data.type){const a=t.data.params.token;if(a&&window.turnstileCallback&&window.turnstileCallback("31231212"),e){const t=new MessageEvent("message",{data:{custom:!0,event:"complete",source:"cloudflare-challenge",token:a,widgetId:e},origin:"https://challenges.cloudflare.com"});window.dispatchEvent(t)}}}))})()})();
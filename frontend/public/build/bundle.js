var app=function(){"use strict";function t(){}function e(t){return t()}function n(){return Object.create(null)}function o(t){t.forEach(e)}function r(t){return"function"==typeof t}function c(t,e){return t!=t?e==e:t!==e||t&&"object"==typeof t||"function"==typeof t}function u(t,e){t.appendChild(e)}function l(t,e,n){t.insertBefore(e,n||null)}function s(t){t.parentNode&&t.parentNode.removeChild(t)}function i(t){return document.createElement(t)}function a(t){return document.createTextNode(t)}function f(){return a(" ")}function d(t,e,n,o){return t.addEventListener(e,n,o),()=>t.removeEventListener(e,n,o)}function p(t,e,n){null==n?t.removeAttribute(e):t.getAttribute(e)!==n&&t.setAttribute(e,n)}function h(t){return""===t?null:+t}function m(t,e){e=""+e,t.data!==e&&(t.data=e)}function g(t,e){t.value=null==e?"":e}function $(t,e,n){for(let n=0;n<t.options.length;n+=1){const o=t.options[n];if(o.__value===e)return void(o.selected=!0)}n&&void 0===e||(t.selectedIndex=-1)}let v;function _(t){v=t}function y(t){(function(){if(!v)throw new Error("Function called outside component initialization");return v})().$$.on_mount.push(t)}const b=[],x=[];let w=[];const E=[],k=Promise.resolve();let j=!1;function C(t){w.push(t)}const S=new Set;let T=0;function q(){if(0!==T)return;const t=v;do{try{for(;T<b.length;){const t=b[T];T++,_(t),O(t.$$)}}catch(t){throw b.length=0,T=0,t}for(_(null),b.length=0,T=0;x.length;)x.pop()();for(let t=0;t<w.length;t+=1){const e=w[t];S.has(e)||(S.add(e),e())}w.length=0}while(b.length);for(;E.length;)E.pop()();j=!1,S.clear(),_(t)}function O(t){if(null!==t.fragment){t.update(),o(t.before_update);const e=t.dirty;t.dirty=[-1],t.fragment&&t.fragment.p(t.ctx,e),t.after_update.forEach(C)}}const A=new Set;let N;function M(t,e){t&&t.i&&(A.delete(t),t.i(e))}function P(t,n,c,u){const{fragment:l,after_update:s}=t.$$;l&&l.m(n,c),u||C((()=>{const n=t.$$.on_mount.map(e).filter(r);t.$$.on_destroy?t.$$.on_destroy.push(...n):o(n),t.$$.on_mount=[]})),s.forEach(C)}function L(t,e){const n=t.$$;null!==n.fragment&&(!function(t){const e=[],n=[];w.forEach((o=>-1===t.indexOf(o)?e.push(o):n.push(o))),n.forEach((t=>t())),w=e}(n.after_update),o(n.on_destroy),n.fragment&&n.fragment.d(e),n.on_destroy=n.fragment=null,n.ctx=[])}function R(t,e){-1===t.$$.dirty[0]&&(b.push(t),j||(j=!0,k.then(q)),t.$$.dirty.fill(0)),t.$$.dirty[e/31|0]|=1<<e%31}function z(e,r,c,u,l,i,a,f=[-1]){const d=v;_(e);const p=e.$$={fragment:null,ctx:[],props:i,update:t,not_equal:l,bound:n(),on_mount:[],on_destroy:[],on_disconnect:[],before_update:[],after_update:[],context:new Map(r.context||(d?d.$$.context:[])),callbacks:n(),dirty:f,skip_bound:!1,root:r.target||d.$$.root};a&&a(p.root);let h=!1;if(p.ctx=c?c(e,r.props||{},((t,n,...o)=>{const r=o.length?o[0]:n;return p.ctx&&l(p.ctx[t],p.ctx[t]=r)&&(!p.skip_bound&&p.bound[t]&&p.bound[t](r),h&&R(e,t)),n})):[],p.update(),h=!0,o(p.before_update),p.fragment=!!u&&u(p.ctx),r.target){if(r.hydrate){const t=function(t){return Array.from(t.childNodes)}(r.target);p.fragment&&p.fragment.l(t),t.forEach(s)}else p.fragment&&p.fragment.c();r.intro&&M(e.$$.fragment),P(e,r.target,r.anchor,r.customElement),q()}_(d)}class D{$destroy(){L(this,1),this.$destroy=t}$on(e,n){if(!r(n))return t;const o=this.$$.callbacks[e]||(this.$$.callbacks[e]=[]);return o.push(n),()=>{const t=o.indexOf(n);-1!==t&&o.splice(t,1)}}$set(t){var e;this.$$set&&(e=t,0!==Object.keys(e).length)&&(this.$$.skip_bound=!0,this.$$set(t),this.$$.skip_bound=!1)}}function I(e){let n;return{c(){n=i("main"),n.innerHTML='<h1 class="svelte-x45sh3">Rentestimator</h1>',p(n,"class","svelte-x45sh3")},m(t,e){l(t,n,e)},p:t,i:t,o:t,d(t){t&&s(n)}}}class B extends D{constructor(t){super(),z(this,t,null,I,c,{})}}function F(t,e,n){const o=t.slice();return o[11]=e[n],o}function G(t){let e,n,o,r=t[11].name+"";return{c(){e=i("option"),n=a(r),e.__value=o=t[11].name,e.value=e.__value},m(t,o){l(t,e,o),u(e,n)},p(t,c){16&c&&r!==(r=t[11].name+"")&&m(n,r),16&c&&o!==(o=t[11].name)&&(e.__value=o,e.value=e.__value)},d(t){t&&s(e)}}}function H(t){let e,n,r,c,v,_,y,b,x,w,E,k,j,S,T,q,O,R,z,D;n=new B({});let I=t[4],H=[];for(let e=0;e<I.length;e+=1)H[e]=G(F(t,I,e));return{c(){var o;e=i("main"),(o=n.$$.fragment)&&o.c(),r=f(),c=i("form"),v=i("input"),_=f(),y=i("input"),b=f(),x=i("input"),w=f(),E=i("select"),k=i("option"),k.textContent="Select a model";for(let t=0;t<H.length;t+=1)H[t].c();j=f(),S=i("button"),S.textContent="Submit",T=f(),q=i("p"),O=a(t[5]),p(v,"type","number"),p(v,"step","any"),p(v,"placeholder","Area"),v.required=!0,p(v,"class","svelte-360gnp"),p(y,"type","number"),p(y,"step","any"),p(y,"placeholder","Rooms"),y.required=!0,p(y,"class","svelte-360gnp"),p(x,"type","text"),p(x,"placeholder","ZIP Code"),x.required=!0,p(x,"class","svelte-360gnp"),k.__value="",k.value=k.__value,E.required=!0,void 0===t[3]&&C((()=>t[10].call(E))),p(S,"type","submit"),p(S,"class","svelte-360gnp"),p(c,"class","svelte-360gnp"),p(q,"class","svelte-360gnp"),p(e,"class","svelte-360gnp")},m(o,s){l(o,e,s),P(n,e,null),u(e,r),u(e,c),u(c,v),g(v,t[0]),u(c,_),u(c,y),g(y,t[1]),u(c,b),u(c,x),g(x,t[2]),u(c,w),u(c,E),u(E,k);for(let t=0;t<H.length;t+=1)H[t]&&H[t].m(E,null);var i;$(E,t[3],!0),u(c,j),u(c,S),u(e,T),u(e,q),u(q,O),R=!0,z||(D=[d(v,"input",t[7]),d(y,"input",t[8]),d(x,"input",t[9]),d(E,"change",t[10]),d(c,"submit",(i=t[6],function(t){return t.preventDefault(),i.call(this,t)}))],z=!0)},p(t,[e]){if(1&e&&h(v.value)!==t[0]&&g(v,t[0]),2&e&&h(y.value)!==t[1]&&g(y,t[1]),4&e&&x.value!==t[2]&&g(x,t[2]),16&e){let n;for(I=t[4],n=0;n<I.length;n+=1){const o=F(t,I,n);H[n]?H[n].p(o,e):(H[n]=G(o),H[n].c(),H[n].m(E,null))}for(;n<H.length;n+=1)H[n].d(1);H.length=I.length}24&e&&$(E,t[3]),(!R||32&e)&&m(O,t[5])},i(t){R||(M(n.$$.fragment,t),R=!0)},o(t){!function(t,e,n,o){if(t&&t.o){if(A.has(t))return;A.add(t),N.c.push((()=>{A.delete(t),o&&(n&&t.d(1),o())})),t.o(e)}else o&&o()}(n.$$.fragment,t),R=!1},d(t){t&&s(e),L(n),function(t,e){for(let n=0;n<t.length;n+=1)t[n]&&t[n].d(e)}(H,t),z=!1,o(D)}}}function J(t,e,n){let o="",r="",c="",u="",l=[],s="";return y((async()=>{try{const t=await fetch("/model",{method:"GET",headers:{"Content-Type":"application/json"}});if(t.ok){const e=await t.json();n(4,l=e),console.log("Models fetched:",l)}}catch(t){console.error("Error fetching models:",t)}})),[o,r,c,u,l,s,async function(t){t.preventDefault(),console.log(u);try{const t=await fetch("/predict",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({area:o,rooms:r,zip:c,model:u})});if(!t.ok)throw new Error(`Error: ${t.statusText}`);const e=await t.json();n(5,s=Math.round(e)),console.log("Prediction Result:",s)}catch(t){console.error("Error submitting form:",t)}},function(){o=h(this.value),n(0,o)},function(){r=h(this.value),n(1,r)},function(){c=this.value,n(2,c)},function(){u=function(t){const e=t.querySelector(":checked");return e&&e.__value}(this),n(3,u),n(4,l)}]}return new class extends D{constructor(t){super(),z(this,t,J,H,c,{})}}({target:document.body,props:{name:"world"}})}();
//# sourceMappingURL=bundle.js.map

(function(){"use strict";var n={3196:function(n,e,t){var o=t(5130),r=t(6768);const i={class:"app-class"};function l(n,e,t,o,l,a){const u=(0,r.g2)("UserRegistration");return(0,r.uX)(),(0,r.CE)("div",i,[(0,r.bF)(u)])}var a=t(144),u=t(4373);const c=n=>((0,r.Qi)("data-v-65c4f5c2"),n=n(),(0,r.jt)(),n),s={class:"registration-card"},f=c((()=>(0,r.Lk)("div",null,[(0,r.Lk)("img",{src:"/registration.svg",alt:"registration"})],-1))),d={class:"registration-card-right"},p=c((()=>(0,r.Lk)("div",null,[(0,r.Lk)("p",null,"Registration"),(0,r.Lk)("p",null," the ability to create and manage blog posts, follow other bloggers, and engage with the community ")],-1))),v={class:"custom-input"},m=c((()=>(0,r.Lk)("label",{for:"name"}," User Name ",-1))),b={class:"custom-input"},g=c((()=>(0,r.Lk)("label",{for:"name"}," Email ",-1))),h={class:"custom-input"},k=c((()=>(0,r.Lk)("label",{for:"name"}," Password ",-1)));var L={__name:"UserRegistration",setup(n){const e=(0,a.KR)(""),t=(0,a.KR)(""),i=(0,a.KR)(""),l=(0,a.KR)(null);function c(){e.value="",t.value="",i.value=""}let L={method:"get",maxBodyLength:1/0,url:"http://127.0.0.1:8000/api/blogposts/",headers:{Authorization:"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI0OTMyOTM2LCJpYXQiOjE3MjQ5MjkzMzYsImp0aSI6ImVmZDUyZDQ1MGY0NTQ3ZjRhZmIyNzg5ZTJkY2ZlYTA3IiwidXNlcl9pZCI6MX0.2CiEnfZ_OhvxTNMhr6cvhxbIUdBGLXm8frI5YZJqEJ0"}};function y(){console.log({userName:e,password:t}),console.log(u.A.request(L).then((n=>{l.value=n.data})))}return(n,l)=>((0,r.uX)(),(0,r.CE)("div",s,[f,(0,r.Lk)("div",d,[p,(0,r.Lk)("div",null,[(0,r.Lk)("div",v,[m,(0,r.Lk)("div",null,[(0,r.bo)((0,r.Lk)("input",{"onUpdate:modelValue":l[0]||(l[0]=n=>e.value=n),placeholder:"Enter UserName",class:"border-0 focus:outline-none w-full"},null,512),[[o.Jo,e.value]])])]),(0,r.Lk)("div",b,[g,(0,r.Lk)("div",null,[(0,r.bo)((0,r.Lk)("input",{"onUpdate:modelValue":l[1]||(l[1]=n=>i.value=n),placeholder:"Enter Email"},null,512),[[o.Jo,i.value]])])]),(0,r.Lk)("div",h,[k,(0,r.Lk)("div",null,[(0,r.bo)((0,r.Lk)("input",{"onUpdate:modelValue":l[2]||(l[2]=n=>t.value=n),placeholder:"Enter Password"},null,512),[[o.Jo,t.value]])])])]),(0,r.Lk)("div",null,[(0,r.Lk)("button",{onClick:c},"Clear"),(0,r.Lk)("button",{onClick:y},"Submit")])])]))}},y=t(1241);const w=(0,y.A)(L,[["__scopeId","data-v-65c4f5c2"]]);var I=w,O={name:"App",components:{UserRegistration:I}};const j=(0,y.A)(O,[["render",l]]);var _=j;(0,o.Ef)(_).mount("#app")}},e={};function t(o){var r=e[o];if(void 0!==r)return r.exports;var i=e[o]={exports:{}};return n[o].call(i.exports,i,i.exports,t),i.exports}t.m=n,function(){var n=[];t.O=function(e,o,r,i){if(!o){var l=1/0;for(s=0;s<n.length;s++){o=n[s][0],r=n[s][1],i=n[s][2];for(var a=!0,u=0;u<o.length;u++)(!1&i||l>=i)&&Object.keys(t.O).every((function(n){return t.O[n](o[u])}))?o.splice(u--,1):(a=!1,i<l&&(l=i));if(a){n.splice(s--,1);var c=r();void 0!==c&&(e=c)}}return e}i=i||0;for(var s=n.length;s>0&&n[s-1][2]>i;s--)n[s]=n[s-1];n[s]=[o,r,i]}}(),function(){t.n=function(n){var e=n&&n.__esModule?function(){return n["default"]}:function(){return n};return t.d(e,{a:e}),e}}(),function(){t.d=function(n,e){for(var o in e)t.o(e,o)&&!t.o(n,o)&&Object.defineProperty(n,o,{enumerable:!0,get:e[o]})}}(),function(){t.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(n){if("object"===typeof window)return window}}()}(),function(){t.o=function(n,e){return Object.prototype.hasOwnProperty.call(n,e)}}(),function(){t.r=function(n){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(n,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(n,"__esModule",{value:!0})}}(),function(){var n={524:0};t.O.j=function(e){return 0===n[e]};var e=function(e,o){var r,i,l=o[0],a=o[1],u=o[2],c=0;if(l.some((function(e){return 0!==n[e]}))){for(r in a)t.o(a,r)&&(t.m[r]=a[r]);if(u)var s=u(t)}for(e&&e(o);c<l.length;c++)i=l[c],t.o(n,i)&&n[i]&&n[i][0](),n[i]=0;return t.O(s)},o=self["webpackChunkmy_view_app"]=self["webpackChunkmy_view_app"]||[];o.forEach(e.bind(null,0)),o.push=e.bind(null,o.push.bind(o))}();var o=t.O(void 0,[504],(function(){return t(3196)}));o=t.O(o)})();
//# sourceMappingURL=app.7b2dc3f2.js.map
import{Y as a,r as s,a0 as m,a1 as w,a2 as g,w as v,a3 as _,aq as b,bA as O,cF as R}from"./index.3117aef3.js";function P(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function p(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function E(t,e,n){return e&&p(t.prototype,e),n&&p(t,n),t}function j(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&f(t,e)}function f(t,e){return f=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},f(t,e)}function x(t){var e=T();return function(){var r=u(t),o;if(e){var c=u(this).constructor;o=Reflect.construct(r,arguments,c)}else o=r.apply(this,arguments);return I(this,o)}}function I(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return S(t)}function S(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function T(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function u(t){return u=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},u(t)}var d=function(t){j(n,t);var e=x(n);function n(){return P(this,n),e.apply(this,arguments)}return E(n,[{key:"render",value:function(){var o=this.props,c=o.captions,l=o.classes,y=o.audioOptions,h=o.audioResources;return a.createElement("div",{className:l.container},a.createElement("audio",Object.assign({className:l.audio},y),h.map(function(i){return a.createElement(s.exports.Fragment,{key:i.id},a.createElement("source",{src:i.id,type:i.getFormat()}))}),c.map(function(i){return a.createElement(s.exports.Fragment,{key:i.id},a.createElement("track",{src:i.id,label:i.getDefaultLabel(),srcLang:i.getProperty("language")}))})))}}]),n}(s.exports.Component);d.defaultProps={audioOptions:{},audioResources:[],captions:[]};var k=function(e,n){var r=n.windowId;return{audioOptions:b(e).audioOptions,audioResources:O(e,{windowId:r})||[],captions:R(e,{windowId:r})||[]}},A=function(){return{audio:{width:"100%"},container:{alignItems:"center",display:"flex",width:"100%"}}},V=m(_(),v(A),g(k,null),w("AudioViewer"));const N=V(d);export{N as default};

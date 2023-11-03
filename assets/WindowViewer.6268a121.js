import{r as s,a6 as j,a7 as T,a8 as z,Y as a,am as re,ae as h,a0 as w,a1 as y,a2 as P,w as C,a3 as D,ax as oe,bg as ae,cQ as ie,ay as V,as as f,s as $,b3 as ue,cR as ce,cI as se,cS as le,cT as fe,cU as ve,cP as pe,cV as de,cW as he,P as we,au as ye,cX as me,ab as _e,bE as be,bz as ge}from"./index.6d3ac980.js";var Z={},Oe=T.exports,Pe=z.exports;Object.defineProperty(Z,"__esModule",{value:!0});var U=Z.default=void 0,Ce=Pe(s.exports),$e=Oe(j()),Ie=(0,$e.default)(Ce.createElement("path",{d:"M13 7h-2v4H7v2h4v4h2v-4h4v-2h-4V7zm-1-5C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"}),"AddCircleOutlineSharp");U=Z.default=Ie;var W={},xe=T.exports,Ee=z.exports;Object.defineProperty(W,"__esModule",{value:!0});var X=W.default=void 0,Re=Ee(s.exports),Se=xe(j()),ke=(0,Se.default)(Re.createElement("path",{d:"M7 11v2h10v-2H7zm5-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"}),"RemoveCircleOutlineSharp");X=W.default=ke;function Ne(t){return a.createElement(re,t,a.createElement("svg",{xmlns:"http://www.w3.org/2000/svg",width:"24",height:"24",viewBox:"0 0 24 24"},a.createElement("path",{d:"M6,15H9v3h2V13H6Zm9-6V6H13v5h5V9Z"}),a.createElement("path",{d:"M12,2A10,10,0,1,0,22,12,10,10,0,0,0,12,2Zm0,18a8,8,0,1,1,8-8,8,8,0,0,1-8,8Z"})))}function je(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function A(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function Te(t,e,n){return e&&A(t.prototype,e),n&&A(t,n),t}function ze(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&I(t,e)}function I(t,e){return I=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},I(t,e)}function De(t){var e=Ze();return function(){var r=m(t),o;if(e){var i=m(this).constructor;o=Reflect.construct(r,arguments,i)}else o=r.apply(this,arguments);return Ve(this,o)}}function Ve(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return x(t)}function x(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function Ze(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function m(t){return m=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},m(t)}var Y=function(t){ze(n,t);var e=De(n);function n(r){var o;return je(this,n),o=e.call(this,r),o.handleZoomInClick=o.handleZoomInClick.bind(x(o)),o.handleZoomOutClick=o.handleZoomOutClick.bind(x(o)),o}return Te(n,[{key:"handleZoomInClick",value:function(){var o=this.props,i=o.windowId,c=o.updateViewport,u=o.viewer;c(i,{zoom:u.zoom*2})}},{key:"handleZoomOutClick",value:function(){var o=this.props,i=o.windowId,c=o.updateViewport,u=o.viewer;c(i,{zoom:u.zoom/2})}},{key:"render",value:function(){var o=this.props,i=o.displayDivider,c=o.showZoomControls,u=o.classes,l=o.t,v=o.zoomToWorld;return c?a.createElement("div",{className:u.zoom_controls},a.createElement(h,{"aria-label":l("zoomIn"),onClick:this.handleZoomInClick},a.createElement(U,null)),a.createElement(h,{"aria-label":l("zoomOut"),onClick:this.handleZoomOutClick},a.createElement(X,null)),a.createElement(h,{"aria-label":l("zoomReset"),onClick:function(){return v(!1)}},a.createElement(Ne,null)),i&&a.createElement("span",{className:u.divider})):a.createElement(a.Fragment,null)}}]),n}(s.exports.Component);Y.defaultProps={displayDivider:!0,showZoomControls:!1,t:function(e){return e},updateViewport:function(){},viewer:{},windowId:""};var We=function(e,n){var r=n.windowId;return{showZoomControls:oe(e),viewer:ae(e,{windowId:r})}},Be={updateViewport:ie},qe=function(e){return{divider:{borderRight:"1px solid #808080",display:"inline-block",height:"24px",margin:"12px 6px"},ListItem:{paddingBottom:0,paddingTop:0},zoom_controls:{display:"flex",flexDirection:"row",justifyContent:"center"}}},Me=w(D(),C(qe),P(We,Be),y("ZoomControls"));const Ae=Me(Y);function Le(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function L(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function He(t,e,n){return e&&L(t.prototype,e),n&&L(t,n),t}function Fe(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&E(t,e)}function E(t,e){return E=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},E(t,e)}function Ge(t){var e=Xe();return function(){var r=_(t),o;if(e){var i=_(this).constructor;o=Reflect.construct(r,arguments,i)}else o=r.apply(this,arguments);return Qe(this,o)}}function Qe(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return Ue(t)}function Ue(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function Xe(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function _(t){return _=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},_(t)}var J=function(t){Fe(n,t);var e=Ge(n);function n(){return Le(this,n),e.apply(this,arguments)}return He(n,[{key:"render",value:function(){var o=this.props,i=o.canvasCount,c=o.canvasIndex,u=o.canvasLabel,l=o.classes,v=o.t;return a.createElement("div",{className:V(f("osd-info"),l.osdInfo)},a.createElement($,{display:"inline",variant:"caption",className:f("canvas-count")},v("pagination",{current:c+1,total:i})),a.createElement($,{display:"inline",variant:"caption",className:f("canvas-label")},u&&" \u2022 ".concat(u)))}}]),n}(s.exports.Component);J.defaultProps={canvasLabel:void 0,t:function(){}};var Ye=function(e,n){var r=n.windowId,o=ue(e,{windowId:r}),i=ce(e,{windowId:r}),c=(se(e,{windowId:r})||{}).id;return{canvasCount:o.length,canvasIndex:i,canvasLabel:le(e,{canvasId:c,windowId:r})}},Je={osdInfo:{order:2,overflow:"hidden",paddingBottom:3,textOverflow:"ellipsis",unicodeBidi:"plaintext",whiteSpace:"nowrap",width:"100%"}},Ke=w(C(Je),D(),P(Ye,null),y("ViewerInfo"));const H=Ke(J);var B={},et=T.exports,tt=z.exports;Object.defineProperty(B,"__esModule",{value:!0});var R=B.default=void 0,nt=tt(s.exports),rt=et(j()),ot=(0,rt.default)(nt.createElement("path",{d:"M10 16.5l6-4.5-6-4.5v9zM12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"}),"PlayCircleOutlineSharp");R=B.default=ot;function at(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function F(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function it(t,e,n){return e&&F(t.prototype,e),n&&F(t,n),t}function ut(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&S(t,e)}function S(t,e){return S=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},S(t,e)}function ct(t){var e=ft();return function(){var r=b(t),o;if(e){var i=b(this).constructor;o=Reflect.construct(r,arguments,i)}else o=r.apply(this,arguments);return st(this,o)}}function st(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return lt(t)}function lt(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function ft(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function b(t){return b=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},b(t)}var K=function(t){ut(n,t);var e=ct(n);function n(){return at(this,n),e.apply(this,arguments)}return it(n,[{key:"render",value:function(){var o=this.props,i=o.hasNextCanvas,c=o.hasPreviousCanvas,u=o.setNextCanvas,l=o.setPreviousCanvas,v=o.t,q=o.classes,te=o.viewingDirection,M="ltr",p={},d={};switch(te){case"top-to-bottom":p={transform:"rotate(270deg)"},d={transform:"rotate(90deg)"};break;case"bottom-to-top":p={transform:"rotate(90deg)"},d={transform:"rotate(270deg)"};break;case"right-to-left":M="rtl",p={},d={transform:"rotate(180deg)"};break;default:p={transform:"rotate(180deg)"},d={}}return a.createElement("div",{className:V(f("osd-navigation"),q.osdNavigation),dir:M},a.createElement(h,{"aria-label":v("previousCanvas"),className:f("previous-canvas-button"),disabled:!c,onClick:function(){c&&l()}},a.createElement(R,{style:p})),a.createElement(h,{"aria-label":v("nextCanvas"),className:f("next-canvas-button"),disabled:!i,onClick:function(){i&&u()}},a.createElement(R,{style:d})))}}]),n}(s.exports.Component);K.defaultProps={hasNextCanvas:!1,hasPreviousCanvas:!1,setNextCanvas:function(){},setPreviousCanvas:function(){},viewingDirection:""};var vt=function(e,n){var r=n.windowId;return{hasNextCanvas:!!fe(e,{windowId:r}),hasPreviousCanvas:!!ve(e,{windowId:r}),viewingDirection:pe(e,{windowId:r})}},pt=function(e,n){var r=n.windowId;return{setNextCanvas:function(){return e(de(r))},setPreviousCanvas:function(){return e(he(r))}}},dt={osdNavigation:{order:1}},ht=w(C(dt),D(),P(vt,pt),y("ViewerNavigation"));const wt=ht(K);function yt(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function G(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function mt(t,e,n){return e&&G(t.prototype,e),n&&G(t,n),t}function _t(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&k(t,e)}function k(t,e){return k=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},k(t,e)}function bt(t){var e=Pt();return function(){var r=g(t),o;if(e){var i=g(this).constructor;o=Reflect.construct(r,arguments,i)}else o=r.apply(this,arguments);return gt(this,o)}}function gt(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return Ot(t)}function Ot(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function Pt(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function g(t){return g=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},g(t)}var ee=function(t){_t(n,t);var e=bt(n);function n(){return yt(this,n),e.apply(this,arguments)}return mt(n,[{key:"canvasNavControlsAreStacked",value:function(){var o=this.props.size;return o&&o.width&&o.width<=253}},{key:"render",value:function(){var o=this.props,i=o.classes,c=o.visible,u=o.windowId,l=o.zoomToWorld;return c?a.createElement(we,{square:!0,className:V(i.controls,f("canvas-nav"),i.canvasNav,this.canvasNavControlsAreStacked()?f("canvas-nav-stacked"):null,this.canvasNavControlsAreStacked()?i.canvasNavStacked:null),elevation:0},a.createElement(Ae,{displayDivider:!this.canvasNavControlsAreStacked(),windowId:u,zoomToWorld:l}),a.createElement(wt,{windowId:u}),a.createElement(H,{windowId:u}),a.createElement(ye,this.props)):a.createElement($,{variant:"srOnly",component:"div"},a.createElement(H,{windowId:u}))}}]),n}(s.exports.Component);ee.defaultProps={classes:{},visible:!0};var Ct=function(e,n){var r=n.windowId;return{visible:_e(e).focusedWindowId===r}},$t=function(e){return{canvasNav:{display:"flex",flexDirection:"row",flexWrap:"wrap",justifyContent:"center",textAlign:"center"},canvasNavStacked:{flexDirection:"column"},controls:{backgroundColor:be(e.palette.background.paper,.5),bottom:0,position:"absolute",width:"100%",zIndex:50}}},It=w(P(Ct),C($t),me.withSize(),y("WindowCanvasNavigationControls"));const xt=It(ee);function Et(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function Q(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}function Rt(t,e,n){return e&&Q(t.prototype,e),n&&Q(t,n),t}function St(t,e){if(typeof e!="function"&&e!==null)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&N(t,e)}function N(t,e){return N=Object.setPrototypeOf||function(r,o){return r.__proto__=o,r},N(t,e)}function kt(t){var e=Tt();return function(){var r=O(t),o;if(e){var i=O(this).constructor;o=Reflect.construct(r,arguments,i)}else o=r.apply(this,arguments);return Nt(this,o)}}function Nt(t,e){if(e&&(typeof e=="object"||typeof e=="function"))return e;if(e!==void 0)throw new TypeError("Derived constructors may only return object or undefined");return jt(t)}function jt(t){if(t===void 0)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}function Tt(){if(typeof Reflect>"u"||!Reflect.construct||Reflect.construct.sham)return!1;if(typeof Proxy=="function")return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],function(){})),!0}catch(t){return!1}}function O(t){return O=Object.setPrototypeOf?Object.getPrototypeOf:function(n){return n.__proto__||Object.getPrototypeOf(n)},O(t)}var zt=s.exports.lazy(function(){return ge(()=>import("./OpenSeadragonViewer.31f1145e.js"),["assets/OpenSeadragonViewer.31f1145e.js","assets/index.6d3ac980.js","assets/index.cacd0e7a.css","assets/WorkspaceArea.3ddb7000.js"])}),Dt=function(t){St(n,t);var e=kt(n);function n(r){var o;return Et(this,n),o=e.call(this,r),o.state={},o}return Rt(n,[{key:"render",value:function(){var o=this.props.windowId,i=this.state.hasError;return i?a.createElement(a.Fragment,null):a.createElement(s.exports.Suspense,{fallback:a.createElement("div",null)},a.createElement(zt,{windowId:o},a.createElement(xt,{windowId:o})))}}],[{key:"getDerivedStateFromError",value:function(o){return{hasError:!0}}}]),n}(s.exports.Component),Vt=w(y("WindowViewer"));const Wt=Vt(Dt);export{Wt as default};

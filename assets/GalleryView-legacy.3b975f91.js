!function(){function e(t){return e="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},e(t)}System.register(["./index-legacy.89681cc2.js","./WorkspaceArea-legacy.26b6968a.js"],(function(t,n){"use strict";var r,o,a,i,c,s,l,u,f,p,d,h,y,v,m,g,b,w,O,x,C,j,I,E,P,k,S,R,A,_;return{setters:[function(e){r=e.ba,o=e.r,a=e.w,i=e.d,c=e.f,s=e.g,l=e.b9,u=e.Y,f=e.cG,p=e.ay,d=e.cH,h=e.bs,y=e.a$,v=e.a0,m=e.a2,g=e.cI,b=e.cJ,w=e.c3,O=e.cK,x=e.cL,C=e.aq,j=e.aM,I=e.cM,E=e.cN,P=e.cO,k=e.P,S=e.a1,R=e.b3,A=e.cP},function(e){_=e.d}],execute:function(){var n=r(o.exports.createElement("path",{d:"M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"}));var N=o.exports.forwardRef((function(e,t){var r=e.alt,a=e.children,l=e.classes,u=e.className,f=e.component,p=void 0===f?"div":f,d=e.imgProps,h=e.sizes,y=e.src,v=e.srcSet,m=e.variant,g=void 0===m?"circular":m,b=i(e,["alt","children","classes","className","component","imgProps","sizes","src","srcSet","variant"]),w=null,O=function(e){var t=e.src,n=e.srcSet,r=o.exports.useState(!1),a=r[0],i=r[1];return o.exports.useEffect((function(){if(t||n){i(!1);var e=!0,r=new Image;return r.src=t,r.srcSet=n,r.onload=function(){e&&i("loaded")},r.onerror=function(){e&&i("error")},function(){e=!1}}}),[t,n]),a}({src:y,srcSet:v}),x=y||v,C=x&&"error"!==O;return w=C?o.exports.createElement("img",c({alt:r,src:y,srcSet:v,sizes:h,className:l.img},d)):null!=a?a:x&&r?r[0]:o.exports.createElement(n,{className:l.fallback}),o.exports.createElement(p,c({className:s(l.root,l.system,l[g],u,!C&&l.colorDefault),ref:t},b),w)})),D=a((function(e){return{root:{position:"relative",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,width:40,height:40,fontFamily:e.typography.fontFamily,fontSize:e.typography.pxToRem(20),lineHeight:1,borderRadius:"50%",overflow:"hidden",userSelect:"none"},colorDefault:{color:e.palette.background.default,backgroundColor:"light"===e.palette.type?e.palette.grey[400]:e.palette.grey[600]},circle:{},circular:{},rounded:{borderRadius:e.shape.borderRadius},square:{borderRadius:0},img:{width:"100%",height:"100%",textAlign:"center",objectFit:"cover",color:"transparent",textIndent:1e4},fallback:{width:"75%",height:"75%"}}}),{name:"MuiAvatar"})(N);function q(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function z(e,t){return z=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},z(e,t)}function T(t){var n=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,o=K(t);if(n){var a=K(this).constructor;r=Reflect.construct(o,arguments,a)}else r=o.apply(this,arguments);return function(t,n){if(n&&("object"===e(n)||"function"==typeof n))return n;if(void 0!==n)throw new TypeError("Derived constructors may only return object or undefined");return $(t)}(this,r)}}function $(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function K(e){return K=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},K(e)}var M=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&z(e,t)}(a,e);var t,n,r,o=T(a);function a(e){var t;return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,a),(t=o.call(this,e)).state={requestedAnnotations:!1},t.handleSelect=t.handleSelect.bind($(t)),t.handleKey=t.handleKey.bind($(t)),t.handleIntersection=t.handleIntersection.bind($(t)),t}return t=a,n=[{key:"handleSelect",value:function(){var e=this.props,t=e.canvas,n=e.selected,r=e.setCanvas,o=e.focusOnCanvas;n?o():r(t.id)}},{key:"handleKey",value:function(e){var t=this.props,n=t.canvas,r=t.setCanvas,o=t.focusOnCanvas;this.keys={enter:"Enter",space:" "},this.chars={enter:13,space:32},e.key===this.keys.enter||e.which===this.chars.enter||e.key===this.keys.space||e.which===this.chars.space?o():r(n.id)}},{key:"handleIntersection",value:function(e){var t=e.isIntersecting,n=this.props,r=n.annotationsCount,o=n.requestCanvasAnnotations,a=this.state.requestedAnnotations;!t||void 0===r||r>0||a||(this.setState({requestedAnnotations:!0}),o())}},{key:"render",value:function(){var e=this.props,t=e.annotationsCount,n=e.searchAnnotationsCount,r=e.canvas,o=e.classes,a=e.config,i=e.selected,c=new l(r);return u.createElement(f,{onChange:this.handleIntersection},u.createElement("div",{key:r.index,className:p(o.galleryViewItem,i?o.selected:"",n>0?o.hasAnnotations:""),onClick:this.handleSelect,onKeyUp:this.handleKey,role:"button",tabIndex:0},u.createElement(d,{resource:r,labelled:!0,variant:"outside",maxWidth:a.width,maxHeight:a.height,style:{margin:"0 auto",maxWidth:"".concat(Math.ceil(a.height*c.aspectRatio),"px")}},u.createElement("div",{className:o.chips},n>0&&u.createElement(h,{avatar:u.createElement(D,{className:o.avatar,classes:{circle:o.avatarIcon}},u.createElement(y,{fontSize:"small"})),label:n,className:p(o.searchChip),size:"small"}),(t||0)>0&&u.createElement(h,{avatar:u.createElement(D,{className:o.avatar,classes:{circle:o.avatarIcon}},u.createElement(_,{className:o.annotationIcon})),label:t,className:p(o.annotationsChip),size:"small"})))))}}],n&&q(t.prototype,n),r&&q(t,r),a}(o.exports.Component);function W(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function B(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?W(Object(n),!0).forEach((function(t){H(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):W(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function H(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}M.defaultProps={annotationsCount:void 0,config:{height:100,width:null},requestCanvasAnnotations:function(){},searchAnnotationsCount:0,selected:!1};var V=v(m((function(e,t){var n=t.canvas,r=t.windowId,o=g(e,{windowId:r}),a=b(e,{windowId:r}),i=w(a.map((function(e){return e.resources}))).filter((function(e){return e.targetId===n.id})),c=O(e,{content:"annotations",windowId:r}).length>0;return{annotationsCount:function(){if(c)return x(e,{canvasId:n.id}).reduce((function(e,t){return e+t.resources.filter((function(e){return e.targetId===n.id})).length}),0)}(),config:C(e).galleryView,searchAnnotationsCount:i.length,selected:o&&o.id===n.id}}),(function(e,t){var n=t.canvas;t.id;var r=t.windowId;return{focusOnCanvas:function(){return e(j(r,"single"))},requestCanvasAnnotations:function(){return e(I(r,n.id))},setCanvas:function(){for(var t=arguments.length,n=new Array(t),o=0;o<t;o++)n[o]=arguments[o];return e(E.apply(P,[r].concat(n)))}}})),a((function(e){return{annotationIcon:{height:"1rem",width:"1rem"},annotationsChip:B({},e.typography.caption),avatar:{backgroundColor:"transparent"},chips:{opacity:.875,position:"absolute",right:0,textAlign:"right",top:0},galleryViewItem:{"&$hasAnnotations":{border:"2px solid ".concat(e.palette.action.selected)},"&$selected,&$selected$hasAnnotations":{border:"2px solid ".concat(e.palette.primary.main)},"&:focus":{outline:"none"},"&:hover":{backgroundColor:e.palette.action.hover},border:"2px solid transparent",cursor:"pointer",display:"inline-block",margin:"".concat(e.spacing(1),"px ").concat(e.spacing(.5),"px"),maxHeight:function(e){return e.config.height+45},minWidth:"60px",overflow:"hidden",padding:e.spacing(.5),position:"relative",width:"min-content"},hasAnnotations:{},searchChip:B(B({},e.typography.caption),{},{"&$selected $avatar":{backgroundColor:e.palette.highlights.primary},marginTop:2}),selected:{}}}))),F=V(M);function G(e,t){for(var n=0;n<t.length;n++){var r=t[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(e,r.key,r)}}function Y(e,t){return Y=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e},Y(e,t)}function J(t){var n=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(e){return!1}}();return function(){var r,o=L(t);if(n){var a=L(this).constructor;r=Reflect.construct(o,arguments,a)}else r=o.apply(this,arguments);return function(t,n){if(n&&("object"===e(n)||"function"==typeof n))return n;if(void 0!==n)throw new TypeError("Derived constructors may only return object or undefined");return function(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}(t)}(this,r)}}function L(e){return L=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},L(e)}var U=function(e){!function(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&Y(e,t)}(a,e);var t,n,r,o=J(a);function a(){return function(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}(this,a),o.apply(this,arguments)}return t=a,(n=[{key:"render",value:function(){var e=this.props,t=e.canvases,n=e.classes,r=e.viewingDirection,o=e.windowId,a="right-to-left"===r?"rtl":"ltr";return u.createElement(k,{component:"section",dir:a,square:!0,elevation:0,className:n.galleryContainer,id:"".concat(o,"-gallery")},t.map((function(e){return u.createElement(F,{key:e.id,windowId:o,canvas:e})})))}}])&&G(t.prototype,n),r&&G(t,r),a}(o.exports.Component);U.defaultProps={classes:{},viewingDirection:""};var X=v(a((function(e){return{galleryContainer:{alignItems:"flex-start",display:"flex",flexDirection:"row",flexWrap:"wrap",overflowX:"hidden",overflowY:"scroll",padding:"50px 0 50px 20px",width:"100%"}}})),m((function(e,t){var n=t.windowId;return{canvases:R(e,{windowId:n}),viewingDirection:A(e,{windowId:n})}})),S("GalleryView"));t("default",X(U))}}}))}();

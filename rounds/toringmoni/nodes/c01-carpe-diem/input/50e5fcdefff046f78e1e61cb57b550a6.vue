
<!-- CarpeDiemPuzzle Puzzle -->
<template>

  <div class="album-app">
    <div class="album-phone">
      <div class="ig-scroll">
        <div class="ig-profile">
          <div class="ig-profile-row">
            <div class="ig-avatar">
              <div class="ig-avatar-inner">
                <img class="ig-avatar-img" :src="avatarImage" :alt="username" />
              </div>
            </div>
            <div class="ig-stats">
              <div class="ig-stat">
                <div class="ig-stat-num">7</div>
                <div class="ig-stat-label">帖子</div>
              </div>
              <div class="ig-stat">
                <div class="ig-stat-num">417</div>
                <div class="ig-stat-label">粉丝</div>
              </div>
              <div class="ig-stat">
                <div class="ig-stat-num">59</div>
                <div class="ig-stat-label">关注</div>
              </div>
            </div>
          </div>
          <div class="ig-bio">
            <div class="ig-bio-name">少年维持着烦恼</div>
            <div class="ig-bio-line">把容易被忽略的瞬间留下来。有些事情只有反复观看，才会看清楚。</div>
            <div class="ig-bio-line">我们是十进制计算的载体。4.3.1.3</div>
            <div class="ig-bio-line">现在是{{ displayTime }}，亲爱的你现在怎么样？</div>
          </div>
        </div>

        <div class="ig-tabs">
          <div class="ig-tab ig-tab--active">▦</div>
          <div class="ig-tab ig-tab--inactive">🏷</div>
        </div>

        <div class="ig-grid">
          <div
            v-for="photo in photos"
            :key="photo.id"
            class="ig-thumb"
            @click="openPhoto(photo)"
          >
            <img
              v-if="photo.kind === 'image'"
              class="ig-thumb-img"
              :src="photo.image"
              :alt="photo.caption"
            />
            <div v-else class="polaroid-thumb">
              <span class="thumb-face">😊</span>
              <span class="thumb-number">{{ numberEmoji(photo.cardId) }}</span>
            </div>
          </div>
        </div>
      </div>

      <div v-if="activePhoto" class="post-overlay">
        <div class="post-scroll">
          <div class="post-userrow">
            <button type="button" class="post-back" @click="closePhoto">←</button>
            <div class="ig-avatar ig-avatar--sm">
              <div class="ig-avatar-inner">
                <img class="ig-avatar-img" :src="avatarImage" :alt="username" />
              </div>
            </div>
            <span class="post-userrow-name">{{ username }}</span>
            <span class="post-userrow-more">⋯</span>
          </div>
          <div class="post-image">
            <img
              v-if="activePhoto.kind === 'image'"
              class="post-image-img"
              :src="activePhoto.image"
              :alt="activePhoto.caption"
            />
            <component
              :is="photoComponentFor(activePhoto)"
              v-else-if="photoComponentFor(activePhoto)"
              :large="true"
              :data="activePhotoData"
            />
          </div>
          <div class="post-actions">
            <span class="post-action">🤍</span>
            <span class="post-action">💬</span>
            <span class="post-action">📤</span>
            <span class="post-action post-action--save">🔖</span>
          </div>
          <div class="post-likes">{{ activePhoto.likes }} 次赞</div>
          <div class="post-caption">
            <span class="post-caption-user">{{ username }}</span>
            {{ activePhoto.caption }}
            <span v-for="tag in activePhoto.tags" :key="tag" class="post-tag">#{{ tag }}</span>
          </div>
          <div class="post-time">{{ activePhoto.time }}</div>
        </div>
      </div>
    </div>
  </div>

</template>

<style>

.album-app {
  display: flex;
  justify-content: center;
  font-family: 'Microsoft YaHei', sans-serif;
}

.album-phone {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 390px;
  overflow: hidden;
  background-color: #fff;
}

.ig-scroll {
  flex: 1;
  background-color: #fff;
}

.ig-profile {
  padding: 12px 16px 10px;
}

.ig-profile-row {
  display: flex;
  align-items: center;
  gap: 24px;
}

.ig-avatar {
  flex-shrink: 0;
  width: 74px;
  height: 74px;
  padding: 3px;
  border: none;
  border-radius: 50%;
  box-sizing: border-box;
  background: linear-gradient(45deg, #feda75, #fa7e1e, #d62976, #962fbf);
}

.ig-avatar-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border: 2px solid #fff;
  border-radius: 50%;
  box-sizing: border-box;
  background-color: #fafafa;
}

.ig-avatar-img {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
}

.ig-avatar--sm {
  width: 34px;
  height: 34px;
  padding: 2px;
}

.ig-avatar--sm .ig-avatar-inner {
  border-width: 1px;
}

.ig-stats {
  flex: 1;
  display: flex;
  justify-content: space-around;
  text-align: center;
}

.ig-stat-num {
  color: #262626;
  font-size: 1rem;
  font-weight: 700;
}

.ig-stat-label {
  color: #262626;
  font-size: 0.8rem;
}

.ig-bio {
  margin-top: 10px;
  font-size: 0.85rem;
  line-height: 1.4;
}

.ig-bio-name {
  color: #262626;
  font-weight: 700;
}

.ig-bio-line {
  color: #262626;
}

.ig-tabs {
  display: flex;
  border-top: 1px solid #dbdbdb;
}

.ig-tab {
  flex: 1;
  padding: 8px 0;
  font-size: 1.1rem;
  line-height: 1;
  text-align: center;
}

.ig-tab--active {
  color: #262626;
  border-bottom: 1px solid #262626;
}

.ig-tab--inactive {
  color: #8e8e8e;
}

.ig-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2px;
}

.ig-thumb {
  aspect-ratio: 1 / 1;
  overflow: hidden;
  background-color: #e4e4e4;
  cursor: pointer;
}

.ig-thumb:hover .ig-thumb-img {
  opacity: 0.85;
}

.ig-thumb-img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.polaroid-thumb {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2px;
  width: 100%;
  height: 100%;
}

.thumb-face {
  font-size: 1.6rem;
  line-height: 1;
}

.thumb-number {
  font-size: 1.2rem;
  line-height: 1;
}

.photo-stub {
  width: 100%;
  height: 100%;
}

.maze-photo {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  padding: 10px;
  box-sizing: border-box;
  background-color: #fff;
}

.maze-photo--large {
  padding: 28px;
}

.maze-svg {
  flex: 1;
  width: 100%;
  min-height: 0;
}

.maze-arrow-line {
  stroke: #111;
  stroke-width: 0.07;
  stroke-linecap: round;
}

.maze-arrow-head {
  fill: #111;
}

.maze-caption {
  flex-shrink: 0;
  margin: 0;
  padding-top: 4px;
  color: #111;
  font-size: 0.5rem;
  font-weight: 700;
  text-align: center;
  white-space: nowrap;
}

.maze-photo--large .maze-caption {
  padding-top: 12px;
  font-size: 1.1rem;
}

.maze-wall {
  stroke: #111;
  stroke-width: 0.08;
  stroke-linecap: square;
}

.maze-axis {
  fill: #fff;
  stroke: #111;
  stroke-width: 0.045;
}

.maze-icon {
  font-size: 0.62px;
}

.riddle1 {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.55em;
  width: 100%;
  height: 100%;
  padding: 8px;
  box-sizing: border-box;
  background-color: #fff;
  font-size: 0.8rem;
}

.riddle1--large {
  gap: 0.8em;
  padding: 24px;
  font-size: 2.4rem;
}

.riddle1-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4em;
}

.riddle1-square {
  --c: #cccccc;
  position: relative;
  display: inline-block;
  flex-shrink: 0;
  width: 1.7em;
  height: 1.7em;
  border: 1px solid #111;
  box-sizing: border-box;
  overflow: hidden;
  background-color: #fff;
}

.riddle1-square-inner {
  position: absolute;
  left: 25%;
  top: 25%;
  width: 50%;
  height: 50%;
}

.sq--solid {
  background-color: var(--c);
}

.sq--tb-top {
  background-image: linear-gradient(to bottom, var(--c) 50%, #fff 50%);
}
.sq--tb-bottom {
  background-image: linear-gradient(to bottom, #fff 50%, var(--c) 50%);
}
.sq--lr-left {
  background-image: linear-gradient(to right, var(--c) 50%, #fff 50%);
}
.sq--lr-right {
  background-image: linear-gradient(to right, #fff 50%, var(--c) 50%);
}

.sq--check-tl {
  background-image:
    linear-gradient(to right, var(--c) 50%, #fff 50%),
    linear-gradient(to right, #fff 50%, var(--c) 50%);
  background-size: 100% 50%;
  background-position: top, bottom;
  background-repeat: no-repeat;
}
.sq--check-tr {
  background-image:
    linear-gradient(to right, #fff 50%, var(--c) 50%),
    linear-gradient(to right, var(--c) 50%, #fff 50%);
  background-size: 100% 50%;
  background-position: top, bottom;
  background-repeat: no-repeat;
}

.sq--around-in {
  background-color: #fff;
}
.sq--around-in .riddle1-square-inner {
  background-color: var(--c);
}
.sq--around-out {
  background-color: var(--c);
}
.sq--around-out .riddle1-square-inner {
  background-color: #fff;
}

.riddle1-eq {
  color: #111;
  font-weight: 700;
}

.riddle1-result {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.2em;
  height: 1.7em;
}

.riddle1-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.riddle1-image--huangpi {
  object-fit: contain;
}

.riddle1-unknown {
  color: #e11d2a;
  font-weight: 900;
  line-height: 1;
}

.rebus-grid {
  display: grid;
  grid-template-columns: repeat(5, auto);
  grid-template-rows: repeat(3, auto);
  justify-content: center;
  align-content: center;
  column-gap: 0;
  row-gap: 4px;
  width: 100%;
  height: 100%;
  padding: 6px;
  box-sizing: border-box;
  background-color: #fff;
}

.rebus-frame {
  grid-column: 1 / 4;
  grid-row: 1 / 4;
  align-self: stretch;
  justify-self: stretch;
  margin: -5px;
  background-color: #f0f0f0;
  border: 1px dashed #999;
  border-radius: 4px;
  z-index: 0;
}

.rebus-cell {
  position: relative;
  z-index: 1;
}

.rebus-cell:nth-child(5n + 1) { grid-column: 1; }
.rebus-cell:nth-child(5n + 2) { grid-column: 2; }
.rebus-cell:nth-child(5n + 3) { grid-column: 3; }
.rebus-cell:nth-child(5n + 4) { grid-column: 4; }
.rebus-cell:nth-child(5n + 5) { grid-column: 5; }
.rebus-cell:nth-child(-n + 5) { grid-row: 1; }
.rebus-cell:nth-child(n + 6):nth-child(-n + 10) { grid-row: 2; }
.rebus-cell:nth-child(n + 11):nth-child(-n + 15) { grid-row: 3; }

.rebus-cell:nth-child(5n + 2) {
  margin: 0 0.1em;
  font-size: 0.72rem;
}

.rebus-cell:nth-child(5n + 4) {
  margin: 0 0.35em;
}

.rebus-cell {
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
  line-height: 1;
}

.rebus-cell.hanzi {
  color: #111;
}

.rebus-cell.symbol {
  color: #f08000;
}

.rebus-cell.unknown {
  color: #e11d2a;
}

.rebus-grid--large {
  row-gap: 10px;
  padding: 20px;
}

.rebus-grid--large .rebus-cell {
  font-size: 2.2rem;
}

.rebus-grid--large .rebus-cell:nth-child(5n + 2) {
  font-size: 1.85rem;
}

.rebus-grid--large .rebus-frame {
  margin: -10px;
  border-radius: 8px;
}

.box-puzzle {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
  background-color: #fff;
}

.box-caption {
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.15em;
  padding: 4px 6px 0;
  color: #111;
  font-size: 0.5rem;
  font-weight: 700;
  white-space: nowrap;
}

.cap-square {
  display: inline-block;
  width: 1.1em;
  height: 1.1em;
  border: 1px solid rgba(0, 0, 0, 0.55);
  box-sizing: border-box;
}

.cap-eq {
  margin: 0 0.1em;
}

.cap-s {
  font-family: 'Cambria Math', 'Latin Modern Math', 'STIX Two Math', 'Times New Roman', serif;
  font-style: italic;
  font-weight: 500;
  font-size: 1.25em;
}

.box-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 3px;
  flex: 1;
  width: 100%;
  padding: 6px;
  box-sizing: border-box;
  align-content: center;
  background-color: #fff;
}

.box-cell {
  position: relative;
  container-type: size;
  display: flex;
  align-items: center;
  justify-content: center;
  aspect-ratio: 1 / 1;
  border: 2px solid #111;
  box-sizing: border-box;
  overflow: hidden;
}

.box-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.box-sn {
  display: inline-flex;
  align-items: baseline;
  color: #111;
  line-height: 1;
}

.box-sn-letter {
  font-family: 'Cambria Math', 'Latin Modern Math', 'STIX Two Math', 'Times New Roman', serif;
  font-style: italic;
  font-weight: 500;
  font-size: 0.85rem;
}

.box-sn-sub {
  font-size: 0.55em;
  font-weight: 700;
  letter-spacing: normal;
}

.box-sn--red {
  color: #e11d2a;
}

.box-sn--overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  text-shadow: 0 0 2px #fff, 0 0 2px #fff, 0 0 3px #fff, 0 0 3px #fff;
}

.box-unknown {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  color: #e11d2a;
  font-weight: 900;
  font-size: 78cqmin;
  line-height: 1;
}

.box-grid--large .box-sn-letter {
  font-size: 1.9rem;
}

.box-grid--large .box-sn--overlay .box-sn-letter {
  font-size: 1.6rem;
}

.box-footer {
  flex-shrink: 0;
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 0.1em;
  padding: 4px 6px 6px;
  color: #111;
  font-size: 0.5rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  white-space: nowrap;
}

.box-footer-in {
  margin: 0 0.1em;
}

.box-footer .box-sn {
  letter-spacing: normal;
}

.box-footer--large {
  padding: 12px 20px 16px;
  font-size: 1.4rem;
  letter-spacing: 0.25em;
}

.box-footer--large .box-sn-letter {
  font-size: 1.9rem;
}

.box-puzzle--large {
  justify-content: center;
}

.box-caption--large {
  padding: 0 20px 12px;
  font-size: 1.4rem;
}

.box-grid--large {
  flex: 0 0 auto;
  gap: 8px;
  padding: 20px;
}

.box-grid--large .box-cell {
  border-width: 3px;
}

.post-overlay {
  position: absolute;
  inset: 0;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  background-color: #fff;
}

.post-back {
  padding: 0;
  border: none;
  background: none;
  color: #262626;
  font-size: 1.5rem;
  line-height: 1;
  cursor: pointer;
}

.post-scroll {
  flex: 1;
  overflow-y: auto;
  padding-bottom: 56px;
}

.post-userrow {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
}

.post-userrow-name {
  color: #262626;
  font-size: 0.85rem;
  font-weight: 700;
}

.post-userrow-more {
  margin-left: auto;
  color: #262626;
  font-weight: 700;
}

.post-image {
  width: 100%;
  aspect-ratio: 1 / 1;
  background-color: #e4e4e4;
}

.post-image-img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.post-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 10px 12px 6px;
  font-size: 1.4rem;
  line-height: 1;
}

.post-action--save {
  margin-left: auto;
}

.post-likes {
  padding: 0 12px;
  color: #262626;
  font-size: 0.85rem;
  font-weight: 700;
}

.post-caption {
  padding: 4px 12px 0;
  color: #262626;
  font-size: 0.85rem;
  line-height: 1.4;
}

.post-caption-user {
  margin-right: 4px;
  font-weight: 700;
}

.post-tag {
  margin-left: 4px;
  color: #00376b;
}

.post-time {
  padding: 6px 12px 10px;
  color: #8e8e8e;
  font-size: 0.7rem;
}


</style>

<!-- 请将以上部分复制到后台“题目HTML”中，以下部分复制到后台“题目脚本”中，不要包含<script>标签 -->

<script>
var __vue_puzzle_component__=function(e){"use strict";const a={"赤":"#e1322b","橙":"#f08000","黄":"#f5c518","绿":"#2ea44f","青":"#13b6c4","蓝":"#1d4ed8","紫":"#7c3aed"},t={huangli:"https://static.cipherpuzzles.com/static/images/a59acf3ab8d547259858e48f6f8b6da1.webp",huangjiu:"https://static.cipherpuzzles.com/static/images/d494340b0f2d4bcfb9851522bafc451b.webp",huanghe:"https://static.cipherpuzzles.com/static/images/2ff7cc72e14841f585a372deb563f7fb.webp",huangshan:"https://static.cipherpuzzles.com/static/images/487a758de44447d8a77332dd7dfee563.webp",huangque:"https://static.cipherpuzzles.com/static/images/c561d586df9d46d49b47192070f032bc.webp",huangpi:"https://static.cipherpuzzles.com/static/images/49374d98a83b498ab185e72b92552e81.webp"},l=(e,a)=>{const t=e.__vccOpts||e;for(const[l,o]of a)t[l]=o;return t},o={name:"CarpePhoto1",props:{large:{type:Boolean,default:!1},data:{type:Object,default:null}},setup:l=>({rows:e.computed(()=>l.data&&l.data.rows||[]),colorHex:e.computed(()=>{const e=l.data&&l.data.color||"蓝";return a[e]||"#cccccc"}),imageUrl:e=>t[e]||""})},c={class:"riddle1-result"},n=["src"],s={key:1,class:"riddle1-unknown"};const r=l(o,[["render",function(a,t,l,o,r,i){return e.openBlock(),e.createElementBlock("div",{class:e.normalizeClass(["riddle1",{"riddle1--large":l.large}])},[(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.rows,(a,l)=>(e.openBlock(),e.createElementBlock("div",{key:l,class:"riddle1-row"},[e.createElementVNode("span",{class:e.normalizeClass(["riddle1-square","sq--"+a.split]),style:e.normalizeStyle({"--c":o.colorHex})},[...t[0]||(t[0]=[e.createElementVNode("i",{class:"riddle1-square-inner"},null,-1)])],6),t[1]||(t[1]=e.createElementVNode("span",{class:"riddle1-eq"},"=",-1)),e.createElementVNode("span",c,["image"===a.kind?(e.openBlock(),e.createElementBlock("img",{key:0,class:e.normalizeClass(["riddle1-image","riddle1-image--"+a.imageId]),src:o.imageUrl(a.imageId),alt:""},null,10,n)):"unknown"===a.kind?(e.openBlock(),e.createElementBlock("span",s,"?")):e.createCommentVNode("v-if",!0)])]))),128))],2)}]]),i=["#e11d2a","#1d4ed8","#f5c518"],d={red:"#e11d2a",yellow:"#f5c518",blue:"#1d4ed8"},p={name:"CarpePhoto2",props:{large:{type:Boolean,default:!1},data:{type:Object,default:null}},setup:a=>({cells:e.computed(()=>(a.data&&a.data.cells||[]).map(e=>({kind:e.kind,subscript:e.subscript,borderColor:e.border?d[e.border]:null}))),captionSquares:i,captionResult:"S",authorSubscript:252,swallowImageUrl:"https://static.cipherpuzzles.com/static/images/6eb9d7e1b1bb4b6491cec62220867cfb.webp"})},m={class:"cap-s"},u=["src"],k={key:0,class:"box-sn box-sn--overlay box-sn--red"},b={class:"box-sn-sub"},g={key:1,class:"box-sn"},y={class:"box-sn-sub"},x={key:2,class:"box-unknown"},h={class:"box-sn"},B={class:"box-sn-sub"};const f=l(p,[["render",function(a,t,l,o,c,n){return e.openBlock(),e.createElementBlock("div",{class:e.normalizeClass(["box-puzzle",{"box-puzzle--large":l.large}])},[e.createElementVNode("div",{class:e.normalizeClass(["box-caption",{"box-caption--large":l.large}])},[(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.captionSquares,(a,t)=>(e.openBlock(),e.createElementBlock("span",{key:t,class:"cap-square",style:e.normalizeStyle({backgroundColor:a})},null,4))),128)),t[0]||(t[0]=e.createElementVNode("span",{class:"cap-eq"},"=",-1)),e.createElementVNode("span",m,e.toDisplayString(o.captionResult),1)],2),e.createElementVNode("div",{class:e.normalizeClass(["box-grid",{"box-grid--large":l.large}])},[(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.cells,(a,l)=>(e.openBlock(),e.createElementBlock("div",{key:l,class:"box-cell",style:e.normalizeStyle(a.borderColor?{borderColor:a.borderColor}:null)},["swallow"===a.kind?(e.openBlock(),e.createElementBlock(e.Fragment,{key:0},[e.createElementVNode("img",{class:"box-image",src:o.swallowImageUrl,alt:"燕子"},null,8,u),a.subscript?(e.openBlock(),e.createElementBlock("span",k,[t[1]||(t[1]=e.createElementVNode("span",{class:"box-sn-letter"},"S",-1)),e.createElementVNode("sub",b,e.toDisplayString(a.subscript),1)])):e.createCommentVNode("v-if",!0)],64)):"sn"===a.kind?(e.openBlock(),e.createElementBlock("span",g,[t[2]||(t[2]=e.createElementVNode("span",{class:"box-sn-letter"},"S",-1)),e.createElementVNode("sub",y,e.toDisplayString(a.subscript),1)])):"unknown"===a.kind?(e.openBlock(),e.createElementBlock("span",x,"?")):e.createCommentVNode("v-if",!0)],4))),128))],2),e.createElementVNode("div",{class:e.normalizeClass(["box-footer",{"box-footer--large":l.large}])},[t[4]||(t[4]=e.createElementVNode("span",{class:"box-footer-text"},"作者",-1)),t[5]||(t[5]=e.createElementVNode("span",{class:"box-footer-in"},"∈",-1)),e.createElementVNode("span",h,[t[3]||(t[3]=e.createElementVNode("span",{class:"box-sn-letter"},"S",-1)),e.createElementVNode("sub",B,e.toDisplayString(o.authorSubscript),1)])],2)],2)}]]);const z=function(){const e=[];for(let a=1;a<5;a+=1)for(let t=1;t<5;t+=1)e.push({x:t,y:a});return e}(),E=[].map(({r:e,c:a,icon:t})=>({icon:t,x:a-.5,y:e-.5})),w=[{x:.5,y1:-.46,y2:-.22,head:"0.37,-0.22 0.63,-0.22 0.5,-0.04"},{x:4.5,y1:5.04,y2:5.28,head:"4.37,5.28 4.63,5.28 4.5,5.46"}],v={name:"CarpePhoto3",props:{large:{type:Boolean,default:!1},data:{type:Object,default:null}},setup:a=>({lines:e.computed(()=>a.data&&a.data.lines||[]),horse:e.computed(()=>a.data&&a.data.horse||null),bird:e.computed(()=>a.data&&a.data.bird||null),fish:e.computed(()=>a.data&&a.data.fish||null),tiger:e.computed(()=>a.data&&a.data.tiger||null),goat:e.computed(()=>a.data&&a.data.goat||null),arrows:w,axisNodes:z,axisRadius:.13,icons:E,horseIcon:"🐴",birdIcon:"🐦",fishIcon:"🐟️",tigerIcon:"🐯",goatIcon:"🐐",viewBox:"-0.15 -0.65 5.3 6.3"})},C=["viewBox"],N=["x1","y1","x2","y2"],V=["x1","y1","x2","y2"],S=["points"],I=["x","y"],D=["x","y"],P=["x","y"],F=["x","y"],q=["x","y"],L=["x","y"],$=["cx","cy","r"];const j=l(v,[["render",function(a,t,l,o,c,n){return e.openBlock(),e.createElementBlock("div",{class:e.normalizeClass(["maze-photo",{"maze-photo--large":l.large}])},[(e.openBlock(),e.createElementBlock("svg",{class:"maze-svg",viewBox:o.viewBox,preserveAspectRatio:"xMidYMid meet"},[(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.lines,(a,t)=>(e.openBlock(),e.createElementBlock("line",{key:t,class:"maze-wall",x1:a.x1,y1:a.y1,x2:a.x2,y2:a.y2},null,8,N))),128)),(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.arrows,(a,t)=>(e.openBlock(),e.createElementBlock("line",{key:`arrow-line-${t}`,class:"maze-arrow-line",x1:a.x,y1:a.y1,x2:a.x,y2:a.y2},null,8,V))),128)),(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.arrows,(a,t)=>(e.openBlock(),e.createElementBlock("polygon",{key:`arrow-head-${t}`,class:"maze-arrow-head",points:a.head},null,8,S))),128)),(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.icons,(a,t)=>(e.openBlock(),e.createElementBlock("text",{key:`icon-${t}`,class:"maze-icon",x:a.x,y:a.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(a.icon),9,I))),128)),o.horse?(e.openBlock(),e.createElementBlock("text",{key:0,class:"maze-icon",x:o.horse.x,y:o.horse.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(o.horseIcon),9,D)):e.createCommentVNode("v-if",!0),o.bird?(e.openBlock(),e.createElementBlock("text",{key:1,class:"maze-icon",x:o.bird.x,y:o.bird.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(o.birdIcon),9,P)):e.createCommentVNode("v-if",!0),o.fish?(e.openBlock(),e.createElementBlock("text",{key:2,class:"maze-icon",x:o.fish.x,y:o.fish.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(o.fishIcon),9,F)):e.createCommentVNode("v-if",!0),o.tiger?(e.openBlock(),e.createElementBlock("text",{key:3,class:"maze-icon",x:o.tiger.x,y:o.tiger.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(o.tigerIcon),9,q)):e.createCommentVNode("v-if",!0),o.goat?(e.openBlock(),e.createElementBlock("text",{key:4,class:"maze-icon",x:o.goat.x,y:o.goat.y,"text-anchor":"middle","dominant-baseline":"central"},e.toDisplayString(o.goatIcon),9,L)):e.createCommentVNode("v-if",!0),(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.axisNodes,(a,t)=>(e.openBlock(),e.createElementBlock("circle",{key:`axis-${t}`,class:"maze-axis",cx:a.x,cy:a.y,r:o.axisRadius},null,8,$))),128))],8,C)),t[0]||(t[0]=e.createElementVNode("p",{class:"maze-caption"},"走到终点，注意避开所有动物！",-1))],2)}]]);const _=l({name:"CarpePhoto4",props:{large:{type:Boolean,default:!1},data:{type:Object,default:null}},setup:a=>({rebusCells:e.computed(()=>(a.data&&a.data.rows||[]).reduce((e,a)=>e.concat(a),[]))})},[["render",function(a,t,l,o,c,n){return e.openBlock(),e.createElementBlock("div",{class:e.normalizeClass(["rebus-grid",{"rebus-grid--large":l.large}])},[(e.openBlock(!0),e.createElementBlock(e.Fragment,null,e.renderList(o.rebusCells,(a,t)=>(e.openBlock(),e.createElementBlock("span",{key:t,class:e.normalizeClass(["rebus-cell",a.kind])},e.toDisplayString(a.char),3))),128)),t[0]||(t[0]=e.createElementVNode("span",{class:"rebus-frame","aria-hidden":"true"},null,-1))],2)}]]),M={1:r,2:f,3:j,4:_};return{name:"CarpeDiemPuzzle",components:{CarpePhoto1:r,CarpePhoto2:f,CarpePhoto3:j,CarpePhoto4:_},setup(){const a=e.ref([{id:1,kind:"image",image:"https://static.cipherpuzzles.com/static/images/8aa4cfbf33074be7840ff8a05a6536c8.webp",caption:"通过二手平台，我从她的手上买来的，我会珍惜一辈子。",tags:[],likes:87,time:"1 天前"},{id:2,kind:"image",image:"https://static.cipherpuzzles.com/static/images/55692c3511544737accb90cd87e6319c.webp",caption:"我的第一个时柒周边。是还原了她麦克风风格的手持电风扇。",tags:["时柒Junana"],likes:132,time:"6 天前"},{id:3,kind:"image",image:"https://static.cipherpuzzles.com/static/images/ccb1dc18b67e4b2992d1a81aebb31e6f.webp",caption:"我最喜欢的植物，我希望有一天能去那片森林看看它",tags:["柔枝树"],likes:96,time:"14 天前"},{id:4,kind:"card",cardId:1,caption:"一些随机图片",tags:[],likes:24,time:"1 周前"},{id:5,kind:"card",cardId:2,caption:"一些随机图片",tags:[],likes:31,time:"1 周前"},{id:6,kind:"card",cardId:3,caption:"一些随机图片",tags:[],likes:19,time:"1 周前"},{id:7,kind:"card",cardId:4,caption:"一些随机图片",tags:[],likes:42,time:"1 周前"}]),t=e.ref(null),l=e.inject("backend"),o=e.ref(new Date),c=e.ref(null),n=e=>String(e).padStart(2,"0"),s=["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"],r=e.computed(()=>{const e=o.value;return`${e.getFullYear()}年${e.getMonth()+1}月${e.getDate()}日${n(e.getHours())}:${n(e.getMinutes())}`});e.onMounted(async()=>{try{const e={action:"renderAll"},a=await l("carpe",e);a&&"number"==typeof a.nowMs&&(o.value=new Date(a.nowMs)),c.value=a||null}catch(e){}});const i=e.computed(()=>t.value&&"card"===t.value.kind&&c.value&&c.value["photo"+t.value.cardId]||null);return{username:"少年维持着烦恼",avatarImage:"https://static.cipherpuzzles.com/static/images/b8895a0aab364e229abc31ecd693a75c.webp",photos:a,activePhoto:t,activePhotoData:i,displayTime:r,numberEmoji:e=>String(e).split("").map(e=>s[Number(e)]).join(""),photoComponentFor:e=>e&&"card"===e.kind&&M[e.cardId]||null,openPhoto:e=>{t.value=e},closePhoto:()=>{t.value=null}}}}}(Vue);


export default __vue_puzzle_component__;
</script>

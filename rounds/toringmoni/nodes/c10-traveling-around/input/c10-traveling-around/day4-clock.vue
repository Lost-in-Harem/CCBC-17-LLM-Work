
<!-- day-four-clock.source Puzzle -->
<template>

  <div class="day-four-module">
    <div v-for="line in marqueeLines" :key="line.className" class="marquee-container">
      <div class="marquee-text" :class="line.className">{{ line.text }}</div>
    </div>

    <div class="session-timer" role="timer" aria-label="Elapsed time since this page was loaded">
      {{ elapsedTime }}
    </div>
  </div>

</template>

<style>

.day-four-module {
  box-sizing: border-box;
  width: min(100%, 550px);
  margin: 0 auto;
}

.day-four-module .marquee-container {
  box-sizing: border-box;
  width: 100%;
  padding: 10px 0;
  overflow: hidden;
  white-space: nowrap;
}

.day-four-module .marquee-text {
  position: relative;
  left: 0;
  display: inline-block;
  font-size: 0.9rem;
  transform: translateX(-100%);
  animation: day-four-marquee-right linear infinite;
}

.day-four-module .one { animation-duration: 13s; }
.day-four-module .two { animation-duration: 25772s; }
.day-four-module .three { animation-duration: 4s; }
.day-four-module .four { animation-duration: 11s; }
.day-four-module .five { animation-duration: 76s; }
.day-four-module .six { animation-duration: 33s; }
.day-four-module .seven { animation-duration: 243s; }

.day-four-module .session-timer {
  box-sizing: border-box;
  width: 100%;
  margin: 1.5rem 0;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 20px;
  font-variant-numeric: tabular-nums;
  font-weight: 800;
  line-height: 1;
  text-align: center;
}

@keyframes day-four-marquee-right {
  0% {
    left: 0;
    transform: translateX(-100%);
  }
  100% {
    left: 100%;
    transform: translateX(0);
  }
}

</style>

<!-- 请将以上部分复制到后台“题目HTML”中，以下部分复制到后台“题目脚本”中，不要包含<script>标签 -->

<script>
var __vue_puzzle_component__=function(e){"use strict";return{setup(){const t=e.ref(0),a=Date.now();let n=null;const o=e.computed((()=>[Math.floor(t.value/3600),Math.floor(t.value%3600/60),t.value%60].map((e=>String(e).padStart(2,"0"))).join(":"))),l=()=>{t.value=Math.floor((Date.now()-a)/1e3)};return e.onMounted((()=>{l(),n=window.setInterval(l,1e3)})),e.onBeforeUnmount((()=>{null!==n&&window.clearInterval(n)})),{elapsedTime:o,marqueeLines:[{className:"one",text:"?????????? ????????"},{className:"two",text:"????? ??????????"},{className:"three",text:"???? ????? ???"},{className:"four",text:"????? ?????"},{className:"five",text:"??????'? ?????"},{className:"six",text:"?????? ?????? ?????"},{className:"seven",text:"??????? ?? ?????"}]}}}}(Vue);


export default __vue_puzzle_component__;
</script>

<template>
  <div class="day-two-module">
    <h2>第二日 - 别惹蚂蚁</h2>

    <section
      class="frame-sequence"
      tabindex="0"
      aria-label="Cell sequence viewer"
      @keydown.left.prevent="previousIteration"
      @keydown.right.prevent="nextIteration"
    >

      <div class="frame-sequence__grid" role="grid" aria-label="Two by three cell viewing window">
        <div
          v-for="cell in visibleCells"
          :key="cell.key"
          class="frame-sequence__cell"
          :class="{ 'frame-sequence__cell--black': cell.isBlack }"
          role="gridcell"
          :aria-label="cell.isBlack ? 'Black cell' : 'White cell'"
        ></div>
      </div>

      <header class="frame-sequence__header">
        <h3>
          <span ref="iterationLabel" class="frame-sequence__fitted-text">
            步数：{{ iteration }}
          </span>
        </h3>
      </header>

      <div class="frame-sequence__controls">
        <button
          type="button"
          class="frame-sequence__button"
          :disabled="iteration === 0"
          aria-label="Go to previous iteration"
          @click="previousIteration"
        >
          <span ref="previousLabel" class="frame-sequence__fitted-text" aria-hidden="true">← 上一步</span>
        </button>
        <button
          type="button"
          class="frame-sequence__button frame-sequence__button--primary"
          :disabled="iteration >= 11000"
          aria-label="Go to next iteration"
          @click="nextIteration"
        >
          <span ref="nextLabel" class="frame-sequence__fitted-text" aria-hidden="true">下一步 →</span>
        </button>
      </div>
    </section>

    <div ref="equationBlock" class="equation-block">
      <div v-for="(line, index) in equationLines" :key="index" class="equation-line">{{ line }}</div>
    </div>
  </div>
</template>

<style>
.day-two-module .frame-sequence,
.day-two-module .equation-block {
  position: relative;
  left: 50%;
  box-sizing: border-box;
  width: 100vw;
  max-width: 100vw;
  transform: translateX(-50%);
}

.day-two-module .frame-sequence {
  --fs-ink: #181818;
  --fs-accent: #d95d39;
  margin: 2rem 0;
  padding: 0;
  color: var(--fs-ink);
  background: transparent;
  border: 0;
  box-shadow: none;
}

.day-two-module .frame-sequence:focus-visible {
  outline: 4px solid var(--fs-accent);
  outline-offset: 5px;
}

.day-two-module .frame-sequence__header {
  margin-bottom: 1.5rem;
  text-align: center;
}

.day-two-module .frame-sequence__header h3 {
  margin: 0;
  line-height: 1.2;
}

.day-two-module .frame-sequence__fitted-text {
  display: inline-block;
  line-height: 1.1;
  white-space: nowrap;
}

.day-two-module .frame-sequence__grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  width: 100%;
  margin: 0;
  background: var(--fs-ink);
  border-top: 3px solid var(--fs-ink);
  border-left: 3px solid var(--fs-ink);
}

.day-two-module .frame-sequence__cell {
  aspect-ratio: 1;
  box-sizing: border-box;
  background: #ffffff;
  border-right: 3px solid var(--fs-ink);
  border-bottom: 3px solid var(--fs-ink);
}

.day-two-module .frame-sequence__cell--black { background: #000000; }

.day-two-module .frame-sequence__controls {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
  min-width: 0;
  width: 100%;
  margin-top: 1.5rem;
}

.day-two-module .frame-sequence__button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  min-width: 0;
  min-height: 46px;
  width: 100%;
  padding: 0.7rem 0.8rem;
  overflow: hidden;
  color: var(--fs-ink);
  background: transparent;
  border: 2px solid var(--fs-ink);
  border-radius: 0;
  font: inherit;
  font-weight: 800;
  cursor: pointer;
}

.day-two-module .frame-sequence__button--primary {
  color: #ffffff;
  background: var(--fs-ink);
}

.day-two-module .frame-sequence__button:hover:not(:disabled),
.day-two-module .frame-sequence__button:focus-visible {
  color: #ffffff;
  background: var(--fs-accent);
  border-color: var(--fs-accent);
}

.day-two-module .frame-sequence__button:disabled {
  cursor: not-allowed;
  opacity: 0.35;
}

.day-two-module .frame-sequence__hint {
  margin: 1rem 0 0;
  color: #59544b;
  font-size: 0.75rem;
  text-align: center;
}

.day-two-module .equation-block {
  margin: 0;
  overflow: hidden;
  text-align: center;
}

.day-two-module .equation-line {
  display: block;
  width: max-content;
  min-width: 100%;
  margin: 0 auto;
  line-height: 1.2;
  white-space: nowrap;
}
</style>

<script>
const { computed, nextTick, onBeforeUnmount, onMounted, ref } = Vue;

export default {
  setup() {
    const iteration = ref(0);
    const equationBlock = ref(null);
    const iterationLabel = ref(null);
    const previousLabel = ref(null);
    const nextLabel = ref(null);
    const marked = new Set();
    const point = { x: 0, y: 0, heading: 0 };
    const offsets = [
      { x: 0, y: -1 },
      { x: 1, y: 0 },
      { x: 0, y: 1 },
      { x: -1, y: 0 }
    ];
    const equationLines = [
      "👀×👀+☎️×🧑‍🚀", "☠️×☠️×🧑‍🚀×⚾️+👀", "👮×👮×☎️-☠️×👮",
      "☎️×☎️×☎️+⏰×👮", "⏰×👮×🧑‍🚀+⚾️", "🧑‍🚀+🧑‍🚀+👀-⚾️",
      "☠️-👀-⚾️", "☎️×⏰+🧑‍🚀-⚾️", "🧑‍🚀×🧑‍🚀×🧑‍🚀×👮-⚾️",
      "☎️×👮^⚾️-👀+⚾️", "⚾️×⚾️+⚾️+🧑‍🚀+🧑‍🚀", "👀×☎️^⚾️+☎️",
      "⏰×⏰×⏰+👀"
    ];

    const fitEquations = () => {
      const block = equationBlock.value;
      if (!block) return;
      block.style.fontSize = "100px";
      const widest = Array.from(block.children).reduce((width, line) => Math.max(width, line.scrollWidth), 0);
      if (widest > 0) block.style.fontSize = `${(100 * block.clientWidth) / widest}px`;
    };

    const fitControlText = () => {
      [iterationLabel.value, previousLabel.value, nextLabel.value].forEach((label) => {
        if (!label || !label.parentElement) return;
        const container = label.parentElement;
        const styles = window.getComputedStyle(container);
        const available = container.clientWidth - parseFloat(styles.paddingLeft || "0") - parseFloat(styles.paddingRight || "0");
        label.style.fontSize = "100px";
        const rendered = label.getBoundingClientRect().width;
        if (available > 0 && rendered > 0) label.style.fontSize = `${(98 * available) / rendered}px`;
      });
    };

    const fitText = () => { fitEquations(); fitControlText(); };
    const makeKey = (x, y) => `${x},${y}`;
    const reset = () => {
      marked.clear();
      point.x = 0;
      point.y = 0;
      point.heading = 0;
      iteration.value = 0;
    };
    const advance = () => {
      const key = makeKey(point.x, point.y);
      if (marked.has(key)) {
        marked.delete(key);
        point.heading = (point.heading + 3) % 4;
      } else {
        marked.add(key);
        point.heading = (point.heading + 1) % 4;
      }
      point.x += offsets[point.heading].x;
      point.y += offsets[point.heading].y;
      iteration.value += 1;
    };
    const goTo = (target) => {
      reset();
      for (let step = 0; step < target; step += 1) advance();
    };
    const nextIteration = () => {
      if (iteration.value < 11000) {
        advance();
        nextTick(fitControlText);
      }
    };
    const previousIteration = () => {
      if (iteration.value > 0) {
        goTo(iteration.value - 1);
        nextTick(fitControlText);
      }
    };
    const visibleCells = computed(() => {
      iteration.value;
      const cells = [];
      for (let row = 0; row < 3; row += 1) {
        for (let column = 0; column < 2; column += 1) {
          cells.push({
            key: `${column}-${row}`,
            isBlack: marked.has(makeKey(point.x + column, point.y + row))
          });
        }
      }
      return cells;
    });

    onMounted(() => {
      nextTick(fitText);
      window.addEventListener("resize", fitText);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitText);
    });
    onBeforeUnmount(() => window.removeEventListener("resize", fitText));

    return {
      equationBlock, equationLines, iteration, iterationLabel,
      nextIteration, nextLabel, previousIteration, previousLabel, visibleCells
    };
  }
};
</script>

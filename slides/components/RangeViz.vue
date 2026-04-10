<script setup>
import { ref, computed, onUnmounted } from 'vue'

const COUNT   = 4
const chorus  = 'We will, we will rock you!'
const active  = ref(-1)
const playing = ref(false)
let timer = null

const printed = computed(() =>
  active.value < 0 ? [] : Array.from({ length: active.value + 1 }, (_, i) => i)
)

const done = computed(() => active.value === COUNT - 1 && !playing.value)

function step() {
  const next = active.value + 1
  if (next >= COUNT) { stop(); return }
  active.value = next
}

function start() {
  if (active.value >= COUNT - 1) reset()
  playing.value = true
  timer = setInterval(step, 800)
}

function stop() {
  playing.value = false
  clearInterval(timer); timer = null
}

function toggle() { playing.value ? stop() : start() }

function reset() {
  stop()
  active.value = -1
}

onUnmounted(() => clearInterval(timer))
</script>

<template>
  <div class="rv">
    <!-- range boxes -->
    <div class="rv-top">
      <div class="rv-label"><code>range(4)</code> produces:</div>
      <div class="rv-boxes">
        <div
          v-for="i in COUNT"
          :key="i"
          class="rv-box"
          :class="{
            'rv-box-active':  active === i - 1,
            'rv-box-visited': active >  i - 1,
          }"
        >
          <div class="rv-box-i">i = {{ i - 1 }}</div>
          <div class="rv-box-ptr" v-if="active === i - 1">▼</div>
        </div>
      </div>
    </div>

    <!-- output -->
    <div class="rv-output">
      <div class="rv-output-bar">output</div>
      <div class="rv-output-body">
        <div v-if="printed.length === 0" class="rv-empty">press play…</div>
        <div
          v-for="i in printed"
          :key="i"
          class="rv-line"
        >
          <span class="rv-prompt">▶</span>
          <span class="rv-chorus">{{ chorus }}</span>
        </div>
      </div>
    </div>

    <!-- controls -->
    <div class="rv-controls">
      <button class="rv-btn rv-btn-play" @click="toggle" :disabled="done">
        <span v-if="playing">⏸ pause</span><span v-else>▶ play</span>
      </button>
      <button class="rv-btn" @click="step" :disabled="playing || done">step →</button>
      <button class="rv-btn" @click="reset">↺ reset</button>
    </div>
  </div>
</template>

<style scoped>
.rv {
  display: grid;
  grid-template-columns: auto 1fr;
  grid-template-rows: 1fr auto;
  gap: 1rem 1.5rem;
  margin-top: 0.8rem;
  height: 310px;
}

/* ── Range boxes ── */
.rv-top {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  justify-content: center;
}

.rv-label {
  font-size: 0.9rem;
  color: #696C77;
}

.rv-label code {
  font-family: 'Fira Code', monospace;
  font-size: 0.9rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 4px;
  padding: 0.05rem 0.4rem;
  color: #4078F2;
}

.rv-boxes {
  display: flex;
  gap: 0.6rem;
}

.rv-box {
  width: 72px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.3rem;
  padding: 0.7rem 0.5rem 0.5rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  font-family: 'Fira Code', monospace;
  font-size: 0.95rem;
  transition: background 0.2s, border-color 0.2s, transform 0.15s;
}

.rv-box-active {
  background: #e8effe;
  border-color: #4078F2;
  color: #4078F2;
  transform: translateY(-4px);
  box-shadow: 0 3px 10px rgba(64,120,242,0.18);
}

.rv-box-visited {
  background: #eaf3ea;
  border-color: #9ecf9d;
  color: #50A14F;
}

.rv-box-i { font-weight: 700; font-size: 0.88rem; }

.rv-box-ptr {
  color: #4078F2;
  font-size: 0.8rem;
  animation: rv-blink 0.8s ease-in-out infinite;
}

@keyframes rv-blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.2; }
}

/* ── Output ── */
.rv-output {
  display: flex;
  flex-direction: column;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  overflow: hidden;
  background: #FAFAFA;
  font-family: 'Fira Code', monospace;
}

.rv-output-bar {
  padding: 0.35rem 0.85rem;
  background: #ECEDEF;
  border-bottom: 1px solid #D3D3D4;
  font-size: 0.75rem;
  color: #696C77;
  letter-spacing: 0.05em;
}

.rv-output-body {
  flex: 1;
  padding: 0.6rem 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  overflow: hidden;
}

.rv-empty {
  color: #A0A1A7;
  font-size: 0.88rem;
  margin: auto;
  text-align: center;
}

.rv-line {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  font-size: 0.92rem;
  animation: rv-fadein 0.2s ease-out;
}

.rv-prompt { color: #50A14F; font-size: 0.8rem; }
.rv-chorus { color: #383A42; }

@keyframes rv-fadein {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Controls ── */
.rv-controls {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.6rem;
}

.rv-btn {
  padding: 0.4rem 1.1rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 6px;
  font-family: 'Fira Code', monospace;
  font-size: 0.88rem;
  color: #383A42;
  cursor: pointer;
  transition: background 0.1s;
}

.rv-btn:hover:not(:disabled) { background: #E5E5E6; }
.rv-btn:disabled { opacity: 0.35; cursor: default; }

.rv-btn-play {
  background: #4078F2;
  border-color: #4078F2;
  color: #fff;
  font-weight: 600;
}

.rv-btn-play:hover:not(:disabled) { background: #2f63e0; }
</style>

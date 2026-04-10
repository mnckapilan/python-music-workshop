<script setup>
import { ref, computed, onUnmounted } from 'vue'

const songs = ['Blinding Lights', 'Levitating', 'Stay', 'Heat Waves']
const active  = ref(-1)   // which cell is highlighted (-1 = none)
const printed = ref([])   // output lines revealed so far
const playing = ref(false)
let timer = null

function step() {
  const next = active.value + 1
  if (next >= songs.length) {
    stop()
    return
  }
  active.value = next
  printed.value = [...printed.value, songs[next]]
}

function start() {
  if (active.value >= songs.length - 1) reset()
  playing.value = true
  timer = setInterval(step, 900)
}

function stop() {
  playing.value = false
  clearInterval(timer)
  timer = null
}

function toggle() {
  playing.value ? stop() : start()
}

function reset() {
  stop()
  active.value  = -1
  printed.value = []
}

function jumpTo(i) {
  stop()
  active.value  = i
  printed.value = songs.slice(0, i + 1)
}

const done = computed(() => active.value === songs.length - 1 && !playing.value)

onUnmounted(() => clearInterval(timer))
</script>

<template>
  <div class="lv">
    <!-- List visualiser -->
    <div class="lv-list">
      <div
        v-for="(song, i) in songs"
        :key="i"
        class="lv-cell"
        :class="{ 'lv-active': active === i, 'lv-visited': active > i }"
        @click="jumpTo(i)"
      >
        <div class="lv-idx">[{{ i }}]</div>
        <div class="lv-val">{{ song }}</div>
        <div class="lv-ptr" v-if="active === i">▶</div>
      </div>
    </div>

    <!-- Output terminal -->
    <div class="lv-output">
      <div class="lv-output-bar">output</div>
      <div class="lv-output-body">
        <div
          v-for="(line, i) in printed"
          :key="i"
          class="lv-line"
          :class="{ 'lv-line-new': i === printed.length - 1 }"
        >
          <span class="lv-prompt">▶</span>
          Now playing: <span class="lv-song">{{ line }}</span>
        </div>
        <div v-if="printed.length === 0" class="lv-empty">press play to run the loop…</div>
      </div>
    </div>

    <!-- Controls -->
    <div class="lv-controls">
      <button class="lv-btn lv-btn-play" @click="toggle" :disabled="done">
        <span v-if="playing">⏸ pause</span>
        <span v-else>▶ play</span>
      </button>
      <button class="lv-btn" @click="step" :disabled="playing || done">step →</button>
      <button class="lv-btn" @click="reset">↺ reset</button>
    </div>
  </div>
</template>

<style scoped>
.lv {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr auto;
  gap: 1rem 1.5rem;
  margin-top: 1rem;
  height: 340px;
}

/* ── List ── */
.lv-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-self: center;
}

.lv-cell {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 1rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s, transform 0.15s;
  position: relative;
  user-select: none;
}

.lv-cell:hover { background: #E5E5E6; }

.lv-cell.lv-visited {
  background: #eaf3ea;
  border-color: #9ecf9d;
  color: #3a7a39;
}

.lv-cell.lv-active {
  background: #e8effe;
  border-color: #4078F2;
  color: #4078F2;
  transform: translateX(6px);
  box-shadow: 0 2px 10px rgba(64, 120, 242, 0.15);
}

.lv-idx {
  font-size: 0.78rem;
  font-weight: 700;
  color: #A0A1A7;
  width: 1.8rem;
  flex-shrink: 0;
}

.lv-active .lv-idx { color: #4078F2; }
.lv-visited .lv-idx { color: #50A14F; }

.lv-val { flex: 1; }

.lv-ptr {
  font-size: 0.85rem;
  color: #4078F2;
  animation: lv-blink 0.9s ease-in-out infinite;
}

@keyframes lv-blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.3; }
}

/* ── Output ── */
.lv-output {
  display: flex;
  flex-direction: column;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  overflow: hidden;
  background: #FAFAFA;
  font-family: 'Fira Code', monospace;
}

.lv-output-bar {
  padding: 0.35rem 0.85rem;
  background: #ECEDEF;
  border-bottom: 1px solid #D3D3D4;
  font-size: 0.75rem;
  color: #696C77;
  letter-spacing: 0.05em;
}

.lv-output-body {
  flex: 1;
  padding: 0.6rem 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  overflow: hidden;
}

.lv-empty {
  color: #A0A1A7;
  font-size: 0.88rem;
  margin-top: auto;
  margin-bottom: auto;
  text-align: center;
}

.lv-line {
  font-size: 0.92rem;
  color: #383A42;
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  animation: lv-fadein 0.25s ease-out;
}

@keyframes lv-fadein {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0); }
}

.lv-prompt { color: #50A14F; font-size: 0.8rem; }
.lv-song   { color: #4078F2; font-weight: 600; }

/* ── Controls ── */
.lv-controls {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.6rem;
  align-items: center;
}

.lv-btn {
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

.lv-btn:hover:not(:disabled) { background: #E5E5E6; }
.lv-btn:disabled { opacity: 0.35; cursor: default; }

.lv-btn-play {
  background: #4078F2;
  border-color: #4078F2;
  color: #fff;
  font-weight: 600;
}

.lv-btn-play:hover:not(:disabled) { background: #2f63e0; }
</style>

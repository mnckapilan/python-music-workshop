<script setup>
import { ref, computed, onUnmounted } from 'vue'

const songs   = ['Blinding Lights', 'Levitating', 'Stay', 'Heat Waves']
const active  = ref(-1)
const playing = ref(false)
let timer = null

const printed = computed(() =>
  active.value < 0 ? [] : songs.slice(0, active.value + 1)
)

const done = computed(() => active.value === songs.length - 1 && !playing.value)

function step() {
  const next = active.value + 1
  if (next >= songs.length) { stop(); return }
  active.value = next
}

function start() {
  if (active.value >= songs.length - 1) reset()
  playing.value = true
  timer = setInterval(step, 900)
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
  <div class="ev">
    <!-- list with index labels -->
    <div class="ev-list">
      <div
        v-for="(song, i) in songs"
        :key="i"
        class="ev-row"
        :class="{
          'ev-row-active':  active === i,
          'ev-row-visited': active >  i,
        }"
        @click="active = i; printed"
      >
        <!-- index bubble -->
        <div class="ev-idx-wrap">
          <div
            class="ev-idx"
            :class="{
              'ev-idx-active':  active === i,
              'ev-idx-visited': active >  i,
            }"
          >{{ i + 1 }}</div>
        </div>
        <div class="ev-song">{{ song }}</div>

        <!-- unpacked variables shown when active -->
        <transition name="ev-vars">
          <div class="ev-vars" v-if="active === i">
            <span class="ev-var"><span class="ev-vk">i</span> = <span class="ev-vv">{{ i + 1 }}</span></span>
            <span class="ev-var"><span class="ev-vk">song</span> = <span class="ev-vv">"{{ song }}"</span></span>
          </div>
        </transition>
      </div>
    </div>

    <!-- output -->
    <div class="ev-output">
      <div class="ev-output-bar">output</div>
      <div class="ev-output-body">
        <div v-if="printed.length === 0" class="ev-empty">press play…</div>
        <div
          v-for="(song, i) in printed"
          :key="i"
          class="ev-line"
        >
          <span class="ev-prompt">▶</span>
          <span class="ev-num">{{ i + 1 }}.</span>
          <span class="ev-title">{{ song }}</span>
        </div>
      </div>
    </div>

    <!-- controls -->
    <div class="ev-controls">
      <button class="ev-btn ev-btn-play" @click="toggle" :disabled="done">
        <span v-if="playing">⏸ pause</span><span v-else>▶ play</span>
      </button>
      <button class="ev-btn" @click="step" :disabled="playing || done">step →</button>
      <button class="ev-btn" @click="reset">↺ reset</button>
    </div>
  </div>
</template>

<style scoped>
.ev {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr auto;
  gap: 1rem 1.5rem;
  margin-top: 0.8rem;
  height: 320px;
}

/* ── List ── */
.ev-list {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  align-self: center;
}

.ev-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.55rem 0.9rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.92rem;
  cursor: pointer;
  transition: background 0.2s, border-color 0.2s, transform 0.15s;
}

.ev-row-active {
  background: #e8effe;
  border-color: #4078F2;
  transform: translateX(6px);
  box-shadow: 0 2px 10px rgba(64,120,242,0.15);
}

.ev-row-visited {
  background: #eaf3ea;
  border-color: #9ecf9d;
}

/* index bubble */
.ev-idx-wrap { flex-shrink: 0; }

.ev-idx {
  width: 1.6rem;
  height: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  font-size: 0.78rem;
  font-weight: 700;
  background: #D3D3D4;
  color: #696C77;
  transition: background 0.2s, color 0.2s;
}

.ev-idx-active  { background: #4078F2; color: #fff; }
.ev-idx-visited { background: #50A14F; color: #fff; }

.ev-song { flex: 1; color: #383A42; }
.ev-row-active .ev-song  { color: #4078F2; font-weight: 600; }
.ev-row-visited .ev-song { color: #3a7a39; }

/* unpacked vars */
.ev-vars {
  display: flex;
  gap: 0.5rem;
  margin-left: auto;
}

.ev-var {
  font-size: 0.78rem;
  background: #fff;
  border: 1px solid #b8ccfb;
  border-radius: 4px;
  padding: 0.1rem 0.45rem;
  color: #4078F2;
  white-space: nowrap;
}

.ev-vk { color: #A626A4; font-weight: 600; }
.ev-vv { color: #50A14F; }

.ev-vars-enter-active { transition: opacity 0.2s, transform 0.2s; }
.ev-vars-enter-from   { opacity: 0; transform: translateX(8px); }

/* ── Output ── */
.ev-output {
  display: flex;
  flex-direction: column;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  overflow: hidden;
  background: #FAFAFA;
  font-family: 'Fira Code', monospace;
}

.ev-output-bar {
  padding: 0.35rem 0.85rem;
  background: #ECEDEF;
  border-bottom: 1px solid #D3D3D4;
  font-size: 0.75rem;
  color: #696C77;
  letter-spacing: 0.05em;
}

.ev-output-body {
  flex: 1;
  padding: 0.6rem 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  overflow: hidden;
}

.ev-empty {
  color: #A0A1A7;
  font-size: 0.88rem;
  margin: auto;
  text-align: center;
}

.ev-line {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  font-size: 0.92rem;
  animation: ev-fadein 0.2s ease-out;
}

.ev-prompt { color: #50A14F; font-size: 0.8rem; }
.ev-num    { color: #4078F2; font-weight: 700; min-width: 1.5rem; }
.ev-title  { color: #383A42; }

@keyframes ev-fadein {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Controls ── */
.ev-controls {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.6rem;
}

.ev-btn {
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

.ev-btn:hover:not(:disabled) { background: #E5E5E6; }
.ev-btn:disabled { opacity: 0.35; cursor: default; }

.ev-btn-play {
  background: #4078F2;
  border-color: #4078F2;
  color: #fff;
  font-weight: 600;
}

.ev-btn-play:hover:not(:disabled) { background: #2f63e0; }
</style>

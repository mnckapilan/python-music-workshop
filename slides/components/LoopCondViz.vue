<script setup>
import { ref, computed, onUnmounted } from 'vue'

const songs = [
  { title: 'Blinding Lights', bpm: 171 },
  { title: 'Savage',          bpm: 134 },
  { title: 'Levitating',      bpm: 103 },
]

function classify(bpm) {
  if (bpm > 130) return {
    branch: 0,
    label:  'High energy',
    color:  '#E53E3E',
    bg:     '#fff5f5',
    border: '#feb2b2',
  }
  return {
    branch: 1,
    label:  'Mid-tempo or slower',
    color:  '#4078F2',
    bg:     '#e8effe',
    border: '#b8ccfb',
  }
}

const active  = ref(-1)
const playing = ref(false)
let timer = null

const currentSong  = computed(() => active.value >= 0 ? songs[active.value] : null)
const currentClass = computed(() => currentSong.value ? classify(currentSong.value.bpm) : null)

const printed = computed(() =>
  active.value < 0
    ? []
    : songs.slice(0, active.value + 1).map(s => ({ ...s, ...classify(s.bpm) }))
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
  timer = setInterval(step, 1300)
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
  <div class="lcv">

    <!-- ── Left: song list ── -->
    <div class="lcv-list">
      <div class="lcv-list-label">playlist</div>
      <div
        v-for="(song, i) in songs"
        :key="i"
        class="lcv-row"
        :class="{
          'lcv-row-active':   active === i,
          'lcv-row-visited':  active >  i,
        }"
      >
        <!-- loop pointer -->
        <div class="lcv-ptr" :class="{ 'lcv-ptr-on': active === i }">▶</div>
        <div class="lcv-row-body">
          <span class="lcv-title">{{ song.title }}</span>
          <span
            class="lcv-bpm"
            :class="{
              'lcv-bpm-active':   active === i,
              'lcv-bpm-visited':  active >  i,
            }"
          >{{ song.bpm }} bpm</span>
        </div>
        <!-- i variable pill -->
        <transition name="lcv-pill">
          <div class="lcv-ivar" v-if="active === i">
            <span class="lcv-ivar-k">i</span> = <span class="lcv-ivar-v">{{ i }}</span>
          </div>
        </transition>
      </div>
    </div>

    <!-- ── Middle: conditional branches ── -->
    <div class="lcv-cond">
      <div class="lcv-cond-label">conditional</div>

      <!-- if branch -->
      <div
        class="lcv-branch"
        :class="{
          'lcv-branch-active': currentClass && currentClass.branch === 0,
          'lcv-branch-dim':    currentClass && currentClass.branch !== 0,
        }"
        :style="currentClass && currentClass.branch === 0
          ? { borderColor: '#feb2b2', background: '#fff5f5' }
          : {}"
      >
        <span
          class="lcv-kw"
          :style="currentClass && currentClass.branch === 0 ? { color: '#E53E3E' } : {}"
        >if</span>
        <span class="lcv-check">
          <span
            class="lcv-bpm-sub"
            :class="{ 'lcv-bpm-sub-live': currentSong }"
          >{{ currentSong ? currentSong.bpm : 'bpm' }}</span>
          <span class="lcv-op"> &gt; 130</span>
        </span>
        <span
          v-if="currentSong"
          class="lcv-badge"
          :class="currentClass.branch === 0 ? 'lcv-badge-true' : 'lcv-badge-false'"
        >{{ currentClass.branch === 0 ? 'true ✓' : 'false ✗' }}</span>
        <span
          class="lcv-result"
          :style="currentClass && currentClass.branch === 0 ? { color: '#E53E3E' } : {}"
        >→ "High energy"</span>
      </div>

      <!-- else branch -->
      <div
        class="lcv-branch"
        :class="{
          'lcv-branch-active': currentClass && currentClass.branch === 1,
          'lcv-branch-dim':    currentClass && currentClass.branch !== 1,
        }"
        :style="currentClass && currentClass.branch === 1
          ? { borderColor: '#b8ccfb', background: '#e8effe' }
          : {}"
      >
        <span
          class="lcv-kw"
          :style="currentClass && currentClass.branch === 1 ? { color: '#4078F2' } : {}"
        >else</span>
        <span class="lcv-check lcv-check-else">(no condition)</span>
        <span
          v-if="currentSong"
          class="lcv-badge"
          :class="currentClass.branch === 1 ? 'lcv-badge-skip' : 'lcv-badge-skip'"
        >{{ currentClass.branch === 1 ? 'runs ✓' : 'skipped' }}</span>
        <span
          class="lcv-result"
          :style="currentClass && currentClass.branch === 1 ? { color: '#4078F2' } : {}"
        >→ "Mid-tempo or slower"</span>
      </div>
    </div>

    <!-- ── Right: output ── -->
    <div class="lcv-output">
      <div class="lcv-output-bar">output</div>
      <div class="lcv-output-body">
        <div v-if="printed.length === 0" class="lcv-empty">press play…</div>
        <div
          v-for="(s, i) in printed"
          :key="i"
          class="lcv-line"
          :style="{ color: s.color }"
        >
          <span class="lcv-prompt">▶</span>
          <span class="lcv-line-text">{{ s.title }} — {{ s.label }}</span>
        </div>
      </div>
    </div>

    <!-- ── Controls ── -->
    <div class="lcv-controls">
      <button class="lcv-btn lcv-btn-play" @click="toggle" :disabled="done">
        <span v-if="playing">⏸ pause</span><span v-else>▶ play</span>
      </button>
      <button class="lcv-btn" @click="step" :disabled="playing || done">step →</button>
      <button class="lcv-btn" @click="reset">↺ reset</button>
    </div>

  </div>
</template>

<style scoped>
.lcv {
  display: grid;
  grid-template-columns: 1fr 1.15fr 1fr;
  grid-template-rows: 1fr auto;
  gap: 0.9rem 1.2rem;
  margin-top: 0.7rem;
  height: 310px;
}

/* ── Song list ── */
.lcv-list {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.lcv-list-label,
.lcv-cond-label,
.lcv-output-bar {
  font-family: 'Fira Code', monospace;
  font-size: 0.72rem;
  color: #696C77;
  letter-spacing: 0.06em;
  padding-bottom: 0.3rem;
  border-bottom: 1px solid #D3D3D4;
  margin-bottom: 0.1rem;
}

.lcv-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 0.7rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 7px;
  font-family: 'Fira Code', monospace;
  font-size: 0.88rem;
  transition: background 0.2s, border-color 0.2s, transform 0.15s;
}

.lcv-row-active {
  background: #e8effe;
  border-color: #4078F2;
  transform: translateX(5px);
  box-shadow: 0 2px 8px rgba(64,120,242,0.15);
}

.lcv-row-visited {
  background: #eaf3ea;
  border-color: #9ecf9d;
}

.lcv-ptr {
  font-size: 0.7rem;
  color: transparent;
  flex-shrink: 0;
  transition: color 0.15s;
}

.lcv-ptr-on { color: #4078F2; }

.lcv-row-body {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
  flex: 1;
}

.lcv-title {
  color: #383A42;
  font-size: 0.85rem;
}

.lcv-row-active  .lcv-title { color: #4078F2; font-weight: 600; }
.lcv-row-visited .lcv-title { color: #3a7a39; }

.lcv-bpm {
  font-size: 0.72rem;
  color: #A0A1A7;
  transition: color 0.2s;
}

.lcv-bpm-active  { color: #4078F2; font-weight: 700; }
.lcv-bpm-visited { color: #50A14F; }

/* i variable pill */
.lcv-ivar {
  font-family: 'Fira Code', monospace;
  font-size: 0.75rem;
  background: #fff;
  border: 1px solid #b8ccfb;
  border-radius: 4px;
  padding: 0.1rem 0.45rem;
  color: #4078F2;
  white-space: nowrap;
  flex-shrink: 0;
}

.lcv-ivar-k { color: #A626A4; font-weight: 700; }
.lcv-ivar-v { color: #50A14F; font-weight: 700; }

.lcv-pill-enter-active { transition: opacity 0.2s, transform 0.2s; }
.lcv-pill-enter-from   { opacity: 0; transform: translateX(6px); }

/* ── Conditional ── */
.lcv-cond {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  justify-content: center;
}

.lcv-branch {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.75rem 0.9rem;
  background: #F0F0F1;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  font-family: 'Fira Code', monospace;
  font-size: 0.88rem;
  transition: background 0.2s, border-color 0.2s, transform 0.2s, opacity 0.2s;
  flex-wrap: wrap;
  gap: 0.5rem 0.7rem;
}

.lcv-branch-active {
  transform: translateX(6px);
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.lcv-branch-dim { opacity: 0.3; }

.lcv-kw {
  font-weight: 700;
  color: #A626A4;
  min-width: 2rem;
  flex-shrink: 0;
  transition: color 0.2s;
}

.lcv-check {
  font-size: 0.85rem;
  color: #A0A1A7;
  background: #E5E5E6;
  border-radius: 5px;
  padding: 0.12rem 0.5rem;
  flex-shrink: 0;
}

.lcv-check-else {
  font-style: italic;
  font-size: 0.78rem;
}

.lcv-bpm-sub {
  color: #A0A1A7;
  transition: color 0.2s, font-weight 0.2s;
}

.lcv-bpm-sub-live {
  color: #383A42;
  font-weight: 700;
}

.lcv-op { color: #696C77; }

.lcv-badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.12rem 0.45rem;
  border-radius: 4px;
  flex-shrink: 0;
}

.lcv-badge-true  { background: #fff5f5; color: #E53E3E; border: 1px solid #feb2b2; }
.lcv-badge-false { background: #fff0f0; color: #c0392b; border: 1px solid #f5b7b1; }
.lcv-badge-skip  { background: #eaf3ea; color: #50A14F; border: 1px solid #9ecf9d; }

.lcv-result {
  font-size: 0.82rem;
  color: #A0A1A7;
  font-weight: 600;
  margin-left: auto;
  transition: color 0.2s;
}

/* ── Output ── */
.lcv-output {
  display: flex;
  flex-direction: column;
  border: 1px solid #D3D3D4;
  border-radius: 8px;
  overflow: hidden;
  background: #FAFAFA;
  font-family: 'Fira Code', monospace;
}

.lcv-output-bar {
  padding: 0.32rem 0.8rem;
  background: #ECEDEF;
  border-bottom: 1px solid #D3D3D4;
  border-radius: 0;
}

.lcv-output-body {
  flex: 1;
  padding: 0.6rem 0.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
  overflow: hidden;
}

.lcv-empty {
  color: #A0A1A7;
  font-size: 0.85rem;
  margin: auto;
  text-align: center;
}

.lcv-line {
  display: flex;
  align-items: baseline;
  gap: 0.4rem;
  font-size: 0.88rem;
  animation: lcv-fadein 0.25s ease-out;
}

.lcv-prompt { color: #A0A1A7; font-size: 0.75rem; flex-shrink: 0; }
.lcv-line-text { font-weight: 600; }

@keyframes lcv-fadein {
  from { opacity: 0; transform: translateY(3px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── Controls ── */
.lcv-controls {
  grid-column: 1 / -1;
  display: flex;
  gap: 0.6rem;
}

.lcv-btn {
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

.lcv-btn:hover:not(:disabled) { background: #E5E5E6; }
.lcv-btn:disabled { opacity: 0.35; cursor: default; }

.lcv-btn-play {
  background: #4078F2;
  border-color: #4078F2;
  color: #fff;
  font-weight: 600;
}

.lcv-btn-play:hover:not(:disabled) { background: #2f63e0; }
</style>

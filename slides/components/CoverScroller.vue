<script setup>
import { ref, computed, onUnmounted } from 'vue'

// ── Live clock ────────────────────────────────────────────────────────────────
const now = ref(new Date())
const timer = setInterval(() => { now.value = new Date() }, 50)
onUnmounted(() => clearInterval(timer))

function formatTime(d) {
  const p = n => String(n).padStart(2, '0')
  const ms = String(d.getMilliseconds()).padStart(3, '0')
  return `${p(d.getHours())}:${p(d.getMinutes())}:${p(d.getSeconds())}.${ms}`
}

function formatDate(d) {
  const days   = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
  const months = ['January','February','March','April','May','June','July','August','September','October','November','December']
  return `${days[d.getDay()]} ${d.getDate()} ${months[d.getMonth()]} ${d.getFullYear()}`
}

// ── Syntax highlighter ────────────────────────────────────────────────────────
function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

const KW = new Set([
  'def','for','in','if','elif','else','return','with','as',
  'True','False','None','and','or','not','import','from',
  'while','class','print','open',
])

function hlLine(line) {
  const sp = (c, t) => `<span style="color:${c}">${esc(t)}</span>`
  let out = '', rest = line, cmAt = -1, inStr = false
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '"') inStr = !inStr
    if (!inStr && rest[i] === '#') { cmAt = i; break }
  }
  const cm = cmAt >= 0 ? rest.slice(cmAt) : ''
  rest = cmAt >= 0 ? rest.slice(0, cmAt) : rest
  while (rest.length) {
    let m
    if ((m = rest.match(/^f?"[^"]*"/)))   { out += sp('#50FA7B', m[0]); rest = rest.slice(m[0].length); continue }
    if ((m = rest.match(/^\d+\.?\d*/)))    { out += sp('#FFB86C', m[0]); rest = rest.slice(m[0].length); continue }
    if ((m = rest.match(/^[a-zA-Z_]\w*/))) {
      const w = m[0], after = rest.slice(w.length).trimStart()
      const c = KW.has(w) ? '#BD93F9' : after[0] === '(' ? '#8BE9FD' : '#F0F0F5'
      out += sp(c, w); rest = rest.slice(w.length); continue
    }
    out += esc(rest[0]); rest = rest.slice(1)
  }
  if (cm) out += sp('#A0B0D0', cm)
  return out
}

// ── Code body (reactive so the clock line re-renders) ─────────────────────────
const highlighted = computed(() => {
  const code = `print("Good morning, Walthamstow!")

# We'll be getting started shortly...
current_date = "${formatDate(now.value)}"
current_time = "${formatTime(now.value)}"

presenters = [
    "Kapilan M",
    "Elisha Gretton",
    "Becks Simpson",
    "Mohini Thakkar",
]

# Special thanks to Naushine Robinson
# for arranging this workshop!

workshop = {
    "title":    "Getting Started with Python",
    "location": "Walthamstow",
    "duration": "2 hours",
    "level":    "Complete beginner",
}

print(f"Welcome to {workshop['title']}!")
print(f"Today's session is {workshop['duration']} long.")
print("No experience needed — let's go!")`

  return code.split('\n').map(hlLine).join('\n')
})
</script>

<template>
  <!-- Two identical copies; CSS scrolls to -50% then loops back invisibly -->
  <div class="cs-outer" aria-hidden="true">
    <div class="cs-track">
      <pre class="cs-pre" v-html="highlighted"></pre>
      <pre class="cs-pre" v-html="highlighted"></pre>
    </div>
  </div>
</template>

<style scoped>
.cs-outer {
  flex: 1;
  overflow: hidden;
  position: relative;
  padding: 2rem 3rem 2rem 1rem;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 12%, black 88%, transparent 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, black 12%, black 88%, transparent 100%);
}

.cs-track {
  display: flex;
  flex-direction: column;
  animation: cs-scroll 42s linear infinite;
  will-change: transform;
}

/* !important needed to beat Slidev's own .slidev-layout pre rules */
.cs-pre {
  font-family: 'Fira Code', monospace !important;
  font-size: 0.78rem !important;
  line-height: 1.85 !important;
  color: #F0F0F5 !important;
  opacity: 0.22;
  white-space: pre !important;
  display: block !important;
  margin: 0 !important;
  background: none !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  pointer-events: none;
  user-select: none;
  overflow: visible !important;
}

@keyframes cs-scroll {
  from { transform: translateY(0); }
  to   { transform: translateY(-50%); }
}
</style>

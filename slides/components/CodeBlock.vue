<script setup>
import { ref, onMounted, watch, computed } from "vue";

const props = defineProps({
  code: { type: String, required: true },
  lang: { type: String, default: "python" },
  filename: { type: String, default: "" },
  variant: { type: String, default: "default" }, // "default" | "danger" | "success"
});

// ── Shared highlighter singleton ──────────────────────────────────────────────
let _hl = null;
let _hlPromise = null;

function getHighlighter() {
  if (_hl) return Promise.resolve(_hl);
  if (_hlPromise) return _hlPromise;
  _hlPromise = import("shiki")
    .then((shiki) =>
      shiki.createHighlighter({
        themes: ["github-light"],
        langs: ["python", "bash", "text"],
      }),
    )
    .then((hl) => {
      _hl = hl;
      return hl;
    });
  return _hlPromise;
}

// ── State ─────────────────────────────────────────────────────────────────────
const tokenLines = ref([]); // ThemedToken[][]
const highlighted = ref(new Set());
const ready = ref(false);

// ── Highlight logic ───────────────────────────────────────────────────────────
async function render() {
  try {
    const hl = await getHighlighter();
    const result = hl.codeToTokens(props.code.trim(), {
      lang: props.lang,
      theme: "github-light",
    });
    tokenLines.value = result.tokens;
  } catch (e) {
    // Fallback: raw lines with no colour
    tokenLines.value = props.code
      .trim()
      .split("\n")
      .map((line) => [{ content: line, color: "#383A42" }]);
  }
  ready.value = true;
}

onMounted(render);
watch(() => [props.code, props.lang], render);

// ── Interaction ───────────────────────────────────────────────────────────────
function toggleLine(i) {
  const s = new Set(highlighted.value);
  if (s.has(i)) s.delete(i);
  else s.add(i);
  highlighted.value = s;
}

function clearHighlights() {
  highlighted.value = new Set();
}

const displayName = computed(
  () =>
    props.filename ||
    (props.lang === "python"
      ? "example.py"
      : props.lang === "bash"
        ? "terminal"
        : props.lang),
);
</script>

<template>
  <div class="ce" :class="`ce-${variant}`">
    <!-- ── Title bar ──────────────────────────────────────────────────────── -->
    <div class="ce-bar">
      <span class="ce-filename">{{ displayName }}</span>
      <button
        v-if="highlighted.size > 0"
        class="ce-clear"
        @click.stop="clearHighlights"
      >
        clear
      </button>
      <span v-else class="ce-clear-placeholder" />
    </div>

    <!-- ── Code area ──────────────────────────────────────────────────────── -->
    <div class="ce-body" v-if="ready">
      <div
        v-for="(line, i) in tokenLines"
        :key="i"
        class="ce-line"
        :class="{ 'ce-hl': highlighted.has(i) }"
        @click="toggleLine(i)"
      >
        <span class="ce-ln">{{ i + 1 }}</span>
        <span class="ce-code">
          <span
            v-for="(tok, j) in line"
            :key="j"
            :style="{
              color: tok.color,
              fontWeight: tok.fontStyle & 2 ? '700' : undefined,
              fontStyle: tok.fontStyle & 1 ? 'italic' : undefined,
            }"
            >{{ tok.content }}</span
          >
        </span>
      </div>
    </div>

    <!-- ── Loading placeholder ───────────────────────────────────────────── -->
    <div class="ce-loading" v-else>···</div>
  </div>
</template>

<style scoped>
/* ── Shell ───────────────────────────────────────────────────────────────── */
.ce {
  border: 1px solid #d3d3d4;
  border-radius: 8px;
  overflow: hidden;
  font-family: "Fira Code", monospace;
  background: #fafafa;
  font-size: 0.88rem;
  line-height: 1.62;
}

/* ── Title bar ───────────────────────────────────────────────────────────── */
.ce-bar {
  display: flex;
  align-items: center;
  padding: 0.38rem 0.85rem;
  background: #ecedef;
  border-bottom: 1px solid #d3d3d4;
  gap: 0.7rem;
  min-height: 2rem;
}

.ce-filename {
  flex: 1;
  font-size: 0.78rem;
  color: #696c77;
  font-weight: 500;
  letter-spacing: 0.01em;
  user-select: none;
}

.ce-clear,
.ce-clear-placeholder {
  font-family: "Fira Code", monospace;
  font-size: 0.72rem;
  color: #696c77;
  background: none;
  border: 1px solid #d3d3d4;
  border-radius: 3px;
  padding: 0.08rem 0.5rem;
  cursor: pointer;
  line-height: 1.5;
  flex-shrink: 0;
  white-space: nowrap;
}

.ce-clear:hover {
  background: #d3d3d4;
}

.ce-clear-placeholder {
  visibility: hidden;
  pointer-events: none;
}

/* ── Code body ───────────────────────────────────────────────────────────── */
.ce-body {
  padding: 0.35rem 0;
  overflow-x: auto;
}

.ce-line {
  display: flex;
  align-items: baseline;
  padding: 0 1.1rem 0 0.85rem;
  cursor: pointer;
  transition: background 0.1s;
  user-select: none;
}

.ce-line:hover {
  background: rgba(64, 120, 242, 0.05);
}

.ce-hl {
  background: rgba(64, 120, 242, 0.1) !important;
}

.ce-hl .ce-ln {
  color: #4078f2 !important;
  font-weight: 700;
}

/* ── Line number ─────────────────────────────────────────────────────────── */
.ce-ln {
  width: 1.8rem;
  text-align: right;
  flex-shrink: 0;
  color: #a0a1a7;
  font-size: 0.78rem;
  margin-right: 1.3rem;
  user-select: none;
}

/* ── Code tokens ─────────────────────────────────────────────────────────── */
.ce-code {
  white-space: pre;
  user-select: text;
}

/* ── Variants ────────────────────────────────────────────────────────────── */
.ce-danger {
  border-color: #f5a5a5;
}
.ce-danger .ce-bar {
  background: #fff0f0;
  border-bottom-color: #f5a5a5;
}
.ce-danger .ce-filename { color: #c0392b; }

.ce-success {
  border-color: #9ecf9d;
}
.ce-success .ce-bar {
  background: #f0fff4;
  border-bottom-color: #9ecf9d;
}
.ce-success .ce-filename { color: #276749; }

/* ── Loading ─────────────────────────────────────────────────────────────── */
.ce-loading {
  padding: 1.4rem;
  text-align: center;
  color: #a0a1a7;
  font-size: 1.1rem;
  letter-spacing: 0.3em;
}
</style>

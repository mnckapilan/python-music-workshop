<script setup>
defineProps({
  file:   { type: String,  required: true },
  active: { type: Boolean, default: false },
})
</script>

<template>
  <div class="fh" :class="active ? 'fh-active' : 'fh-default'">
    <span class="fh-icon">{{ active ? '💻' : '📄' }}</span>
    <span class="fh-label">{{ file }}</span>
  </div>
</template>

<style scoped>
/* ── Shared ── */
.fh {
  position: absolute;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  white-space: nowrap;
  z-index: 5;
  font-family: 'Fira Code', monospace;
}

/* ── Default: bottom-centre pill ── */
.fh-default {
  bottom: 1.6rem;
  left: 50%;
  transform: translateX(-50%);
  padding: 0.28rem 0.85rem;
  background: var(--surface, #F0F0F1);
  border: 1px solid var(--border, #D3D3D4);
  border-radius: 99px;
  font-size: 0.78rem;
  color: var(--muted, #696C77);
}

.fh-default .fh-icon { font-size: 0.72rem; }

/* ── Active: top-right badge ── */
.fh-active {
  top: 1.5rem;
  right: 2rem;
  padding: 0.38rem 1rem 0.38rem 0.8rem;
  background: #4078F2;
  border: none;
  border-radius: 99px;
  font-size: 0.88rem;
  font-weight: 600;
  color: #fff;
  box-shadow: 0 2px 10px rgba(64, 120, 242, 0.35);
}

.fh-active .fh-icon { font-size: 0.82rem; }
</style>

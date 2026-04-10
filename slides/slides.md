---
theme: default
title: Getting Started with Python
info: A hands-on Python coding workshop for beginners
highlighter: shiki
lineNumbers: true
layout: cover
class: intro-cover
shiki:
  theme: 'github-light'
fonts:
  sans: 'Figtree'
  serif: 'Bricolage Grotesque'
  mono: 'Fira Code'
  weights: '400,500,600,700,800'
  provider: 'google'
---

<script setup>
const wm = `song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019

playlist = [
    "Blinding Lights",
    "Levitating",
    "Heat Waves",
    "As It Was",
]

for song in playlist:
    print(f"Now playing: {song}")

def classify_bpm(bpm):
    if bpm > 130:
        return "High energy"
    elif bpm > 90:
        return "Mid-tempo"
    return "Slow"

album = {
    "title":  "Future Nostalgia",
    "artist": "Dua Lipa",
    "year":   2020,
}

with open("my_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\\n")`
function _esc(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;') }
const _KW = new Set(['def','for','in','if','elif','else','return','with','as','True','False','None','and','or','not','import','from','while','class','print','open'])
function _hlLine(line) {
  function sp(c, t) { return '<span style="color:' + c + '">' + _esc(t) + '</span>' }
  let out = '', rest = line, cmAt = -1, inStr = false
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '"') inStr = !inStr
    if (!inStr && rest[i] === '#') { cmAt = i; break }
  }
  const cm = cmAt >= 0 ? rest.slice(cmAt) : ''
  rest = cmAt >= 0 ? rest.slice(0, cmAt) : rest
  while (rest.length) {
    let m
    if ((m = rest.match(/^f?"[^"]*"/))) { out += sp('#50FA7B', m[0]); rest = rest.slice(m[0].length); continue }
    if ((m = rest.match(/^\d+\.?\d*/))) { out += sp('#FFB86C', m[0]); rest = rest.slice(m[0].length); continue }
    if ((m = rest.match(/^[a-zA-Z_]\w*/))) {
      const w = m[0], after = rest.slice(w.length).trimStart()
      const c = _KW.has(w) ? '#BD93F9' : after[0] === '(' ? '#8BE9FD' : '#F0F0F5'
      out += sp(c, w); rest = rest.slice(w.length); continue
    }
    out += _esc(rest[0]); rest = rest.slice(1)
  }
  if (cm) out += sp('#A0B0D0', cm)
  return out
}
const highlighted = wm.split('\n').map(_hlLine).join('\n')
</script>

<div class="ic">
  <div class="ic-left">
    <p class="ic-label">Python · Music · Code</p>
    <h1>Getting Started<br>with Python</h1>
    <p class="ic-sub">A 2-hour coding workshop</p>
  </div>
  <div class="ic-right" aria-hidden="true">
    <div class="ic-scroller">
      <pre class="ic-code" v-html="highlighted"></pre>
      <pre class="ic-code" v-html="highlighted"></pre>
    </div>
  </div>
</div>

---

# How today works

Over the next **2 hours** you'll learn the core building blocks of Python — using songs, playlists, albums, and lyrics as your playground. Every section follows the same rhythm:

<div class="d-row" style="margin: 1.1rem 0; gap: 0.9rem; flex-wrap: wrap;">
  <span class="d-box">📖 Live example on screen</span>
  <span class="d-arr">→</span>
  <span class="d-box d-key">💻 Exercise — your turn</span>
  <span class="d-arr">→</span>
  <span class="d-box">Next section</span>
</div>

<div class="concepts-list">
  <div>0 · Setup</div>
  <div>1 · Variables &amp; Strings</div>
  <div>2 · Lists</div>
  <div>3 · Loops</div>
  <div>4 · Conditionals</div>
  <div>5 · Dictionaries</div>
  <div>6 · Functions</div>
  <div>7 · File I/O</div>
</div>

<div class="slide-footer-note"><strong>Finished early?</strong> Scroll to the <strong>Extension Challenge</strong> at the bottom of your exercise file — or open the <strong>Data Explorer</strong> to browse 9,000+ real songs.</div>

---
layout: center
class: exercise-header
---

# Exercise 0
## Getting Set Up

---

# Run the setup script

Open the **`setup`** folder and double-click:

| Your laptop | File to run |
|-------------|-------------|
| Mac | `setup.command` — right-click → Open the first time |
| Windows | `setup.bat` |

A terminal window runs three checks automatically:

```
[ OK ] Python 3.11.4
[ OK ] VS Code 1.89.0
[ OK ] Loaded 9237 songs.

*** ALL DONE — YOU'RE GOOD TO GO! ***
```

If anything shows `[FAIL]` — the script tells you exactly what to fix. Ask a volunteer!

<FileHint file="exercise_00_setup_check.py" />

---

# Running an exercise

VS Code opens automatically when setup passes.

Open the VS Code terminal with `` Ctrl+` `` and type:

```bash
python3 exercises/exercise_00_setup_check.py
```

> If that doesn't work, try `python` instead of `python3`.

You should see:

```
Everything is set up correctly — you're ready to go!
```

Open each exercise file in the `exercises` folder, read the example, then complete the **YOUR TASK** section.

<FileHint file="exercise_00_setup_check.py" />

---
layout: center
class: exercise-header
---

# Exercise 1
## Variables & Strings

---

# What is a variable?

A variable is a **labelled box** that stores a piece of information.

<div class="d-vars">
  <div class="d-row"><code class="d-box d-key">song_title</code><span class="d-arr">→</span><span class="d-box d-val">"Blinding Lights"</span></div>
  <div class="d-row"><code class="d-box d-key">artist</code><span class="d-arr">→</span><span class="d-box d-val">"The Weeknd"</span></div>
  <div class="d-row"><code class="d-box d-key">year</code><span class="d-arr">→</span><span class="d-box d-val">2019</span></div>
</div>

> Text goes inside quote marks: `"like this"`<br/>Numbers don't need quotes: `2019`, `3.22`

<FileHint file="exercise_01_variables_and_strings.py" />

---

# Variables — code

<script setup>
const code = `song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019
duration   = 3.22   # minutes

print(song_title)   # Blinding Lights
print(artist)       # The Weeknd
print(year)         # 2019`
</script>

<CodeBlock :code="code" lang="python" filename="variables.py" />

<FileHint file="exercise_01_variables_and_strings.py" />

---

# f-strings

Slot variables directly into text — put `f` before the quote and `{}` around variable names.

<script setup>
const code = `song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019

print(f"Now Playing: {song_title} by {artist} ({year})")
# Now Playing: Blinding Lights by The Weeknd (2019)`
</script>

<CodeBlock :code="code" lang="python" filename="fstrings.py" />

<FileHint file="exercise_01_variables_and_strings.py" />

---

# Your Task — Exercise 1

1. Create variables for your favourite song:
   - `my_song_title`
   - `my_artist`
   - `my_year`
   - `my_duration`
2. Use an f-string to print:

```
Now Playing: <title> by <artist> | Released: <year> | Duration: <duration> mins
```

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_01_variables_and_strings.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 2
## Lists

---

# What is a list?

A list stores **multiple items in order** — each item has an index starting at 0.

<div class="d-list d-list-center">
  <div class="d-cell"><div class="d-cell-idx">[0]</div><div class="d-cell-val">Blinding Lights</div></div>
  <div class="d-cell"><div class="d-cell-idx">[1]</div><div class="d-cell-val">Levitating</div></div>
  <div class="d-cell"><div class="d-cell-idx">[2]</div><div class="d-cell-val">Stay</div></div>
  <div class="d-cell"><div class="d-cell-idx">[3]</div><div class="d-cell-val">Heat Waves</div></div>
</div>
<div class="d-index-boxes">
  <div class="d-index-box"><code>playlist[0]</code><span class="d-index-label">the <strong>first</strong> item</span></div>
  <div class="d-index-box"><code>playlist[-1]</code><span class="d-index-label">the <strong>last</strong> item</span></div>
  <div class="d-index-box"><code>len(playlist)</code><span class="d-index-label"><strong>how many</strong> items</span></div>
</div>

<FileHint file="exercise_02_lists.py" />

---

# Lists — code

<script setup>
const code = `playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

print(playlist)        # the whole list
print(playlist[0])     # first item  → "Blinding Lights"
print(playlist[-1])    # last item   → "Heat Waves"
print(len(playlist))   # how many    → 4

playlist.append("As It Was")     # add to the end
playlist.remove("Stay")          # remove a specific song
playlist.insert(0, "Flowers")    # insert at position 0 (the start)`
</script>

<CodeBlock :code="code" lang="python" filename="lists.py" />

<FileHint file="exercise_02_lists.py" />

---

# Your Task — Exercise 2

1. Create `my_playlist` with at least 5 song titles
2. Print the entire playlist
3. Print only the **third** song
4. Use `.append()` to add a new song to the end
5. Use `.remove()` to delete one song
6. Print the total number of songs using `len()`

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_02_lists.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 3
## Loops

---

# What is a loop?

Instead of writing the same line for every song — let the loop do it.

<LoopViz />

<FileHint file="exercise_03_loops.py" />

---

# Loops — code

<script setup>
const code = `playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

for song in playlist:
    print(f"Now playing: {song}")`
</script>

<CodeBlock :code="code" lang="python" filename="loops.py" />

<FileHint file="exercise_03_loops.py" />

---

# range() — repeat a fixed number of times

`range(4)` generates the numbers **0, 1, 2, 3** — the loop body runs once for each.

<RangeViz />

<FileHint file="exercise_03_loops.py" />

---

# range() — the code

<script setup>
const codeRange = `chorus = "We will, we will rock you!"

for i in range(4):
    print(chorus)

# Output:
# We will, we will rock you!
# We will, we will rock you!
# We will, we will rock you!
# We will, we will rock you!`
</script>

<CodeBlock :code="codeRange" lang="python" filename="range.py" />

<FileHint file="exercise_03_loops.py" />

---

# enumerate() — loop with a counter

Instead of just the item, you also get its **index** — great for numbered lists.

<EnumerateViz />

<FileHint file="exercise_03_loops.py" />

---

# enumerate() — the code

<script setup>
const codeEnum = `playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

# Output:
# 1. Blinding Lights
# 2. Levitating
# 3. Stay
# 4. Heat Waves`
</script>

<CodeBlock :code="codeEnum" lang="python" filename="enumerate.py" />

<FileHint file="exercise_03_loops.py" />

---

# Your Task — Exercise 3

1. Create a list of 5 songs. Loop through and print each one with its track number using `enumerate()`
2. Pick a short lyric. Use `range()` to print it four times
3. Loop through and print every title in **UPPERCASE** using `.upper()`

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_03_loops.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 4
## Conditionals

---

# What is a conditional?

Your code takes a **different path** depending on whether something is true.

<CondViz />

<FileHint file="exercise_04_conditionals.py" />

---

# Conditionals — code

<script setup>
const code = `song_bpm = 140

if song_bpm > 150:
    print("High energy — great for a workout!")
elif song_bpm > 100:
    print("Mid-tempo — good for studying.")
else:
    print("Slow and relaxed — wind-down music.")`
</script>

<CodeBlock :code="code" lang="python" filename="conditionals.py" />

<FileHint file="exercise_04_conditionals.py" />

---

# Conditionals inside a loop

<script setup>
const code = `titles = ["Blinding Lights", "Savage",    "Levitating"]
bpms   = [171,               134,         103]

for i, title in enumerate(titles):
    bpm = bpms[i]
    if bpm > 130:
        print(f"{title} — High energy")
    else:
        print(f"{title} — Mid-tempo or slower")`
</script>

<CodeBlock :code="code" lang="python" filename="conditionals_loop.py" />

<FileHint file="exercise_04_conditionals.py" />

---

# Your Task — Exercise 4

1. Create two lists: song titles and BPM values (at least 5 songs, BPM range 60–200)
2. Loop through and classify each song:
   - **High energy** → BPM > 130
   - **Mid-tempo** → BPM 90–130
   - **Slow** → BPM < 90
3. Add a skip condition: if BPM > 180, print `"Skipping <title> — too fast!"`

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_04_conditionals.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 5
## Dictionaries

---

# What is a dictionary?

Group related data under named **keys** — like a labelled form.

<div class="d-dict">
  <div class="d-dict-k">"title"</div><div class="d-dict-v">"Future Nostalgia"</div>
  <div class="d-dict-k">"artist"</div><div class="d-dict-v">"Dua Lipa"</div>
  <div class="d-dict-k">"year"</div><div class="d-dict-v">2020</div>
  <div class="d-dict-k">"tracks"</div><div class="d-dict-v">{ 1: "Future Nostalgia", 2: "Don't Start Now", … }</div>
</div>

> Access any value with `album["key"]`

<FileHint file="exercise_05_dictionaries.py" />

---

# Dictionaries — code

<script setup>
const code = `album = {
    "title":  "Future Nostalgia",
    "artist": "Dua Lipa",
    "year":   2020,
    "tracks": {
        1: "Future Nostalgia",
        2: "Don't Start Now",
        3: "Cool",
    }
}

print(album["title"])       # Future Nostalgia
print(album["tracks"][2])   # Don't Start Now

for track_num, track_title in album["tracks"].items():
    print(f"Track {track_num}: {track_title}")`
</script>

<CodeBlock :code="code" lang="python" filename="dictionaries.py" />

<FileHint file="exercise_05_dictionaries.py" />

---

# Your Task — Exercise 5

1. Create `my_album` with keys:
   - `title`, `artist`, `year`, `genre`
   - `tracks` — a dict mapping track numbers → song titles
2. Print the album title and artist on one line using an f-string
3. Loop through the tracks and print a numbered listing
4. Add a new track to the dictionary after you've created it

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_05_dictionaries.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 6
## Functions

---

# What is a function?

Define code **once**, call it as many times as you like — with different inputs each time.

<div class="fn-calls">
  <div class="fn-call">
    <div class="fn-call-inputs">
      <div class="fn-param"><span class="fn-pk">title</span>=<span class="fn-pv">"Blinding Lights"</span></div>
      <div class="fn-param"><span class="fn-pk">artist</span>=<span class="fn-pv">"The Weeknd"</span></div>
    </div>
    <div class="fn-varr">↓</div>
    <div class="fn-machine">now_playing()</div>
    <div class="fn-varr">↓</div>
    <div class="fn-out">▶ Blinding Lights — The Weeknd</div>
  </div>
  <div class="fn-call">
    <div class="fn-call-inputs">
      <div class="fn-param"><span class="fn-pk">title</span>=<span class="fn-pv">"Levitating"</span></div>
      <div class="fn-param"><span class="fn-pk">artist</span>=<span class="fn-pv">"Dua Lipa"</span></div>
    </div>
    <div class="fn-varr">↓</div>
    <div class="fn-machine">now_playing()</div>
    <div class="fn-varr">↓</div>
    <div class="fn-out">▶ Levitating — Dua Lipa</div>
  </div>
</div>

<FileHint file="exercise_06_functions.py" />

---

# Why use functions?

Without a function, you repeat yourself:

<script setup>
const codeA = `print("▶  Blinding Lights — The Weeknd")
print("▶  Levitating — Dua Lipa")
print("▶  Heat Waves — Glass Animals")
# Change the format? Edit every single line.`

const codeB = `def now_playing(title, artist):
    print(f"▶  {title} — {artist}")

now_playing("Blinding Lights", "The Weeknd")
now_playing("Levitating",      "Dua Lipa")
now_playing("Heat Waves",      "Glass Animals")
# Change the format? Edit one line.`
</script>

<CodeBlock :code="codeA" lang="python" filename="without a function" />

With a function, define the format **once**:

<CodeBlock :code="codeB" lang="python" filename="now_playing()" />

<FileHint file="exercise_06_functions.py" />

---

# Functions that return a value

<script setup>
const code = `def classify_bpm(bpm):
    if bpm > 130:
        return "High energy"
    elif bpm > 90:
        return "Mid-tempo"
    else:
        return "Slow"

print(classify_bpm(171))   # High energy
print(classify_bpm(96))    # Mid-tempo
print(classify_bpm(68))    # Slow`
</script>

<CodeBlock :code="code" lang="python" filename="classify_bpm()" />

<FileHint file="exercise_06_functions.py" />

---

# Your Task — Exercise 6

1. Write `describe_song(title, artist, year)` — prints one formatted line. Call it 3 times.

2. Write `longest_title(songs)` — prints the longest title and its character count:

```
Longest title: Someone Like You (16 characters)
```

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_06_functions.py" active />

<ExerciseTimer />

---
layout: center
class: exercise-header
---

# Exercise 7
## File I/O

---

# Why save to a file?

So far, data disappears when the program stops. A file keeps it around.

<div class="d-fileio">
  <div class="d-box d-dark">Python Program</div>
  <div class="d-fileio-mid">
    <div class="d-fileio-row"><div class="d-fileio-line"></div><span class="d-arr">→</span><span>write</span></div>
    <div class="d-fileio-row"><span>read</span><span class="d-arr">←</span><div class="d-fileio-line"></div></div>
  </div>
  <div class="d-box d-val">my_playlist.txt</div>
</div>

> `"w"` write · `"r"` read · `"a"` append

<FileHint file="exercise_07_file_io.py" />

---

# Writing to a file

<script setup>
const code = `playlist = [
    "Blinding Lights – The Weeknd",
    "Levitating – Dua Lipa",
    "Heat Waves – Glass Animals",
]

with open("my_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\\n")   # \\n = new line

print("Playlist saved!")`
</script>

<CodeBlock :code="code" lang="python" filename="write_playlist.py" />

<FileHint file="exercise_07_file_io.py" />

---

# Reading a file back

<script setup>
const code = `with open("my_playlist.txt", "r") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")   # .strip() removes \\n`
</script>

<CodeBlock :code="code" lang="python" filename="read_playlist.py" />

<FileHint file="exercise_07_file_io.py" />

---

# Your Task — Exercise 7

1. Create a list of at least 5 songs in `"Title – Artist"` format.
   Write them to a file called `my_playlist.txt`.

2. Read `my_playlist.txt` back and print a numbered track listing.
   Remember to use `.strip()` so the `\n` doesn't show up.

<div class="et-help">✋ Stuck? Raise your hand and a volunteer will come to you!<br>⏳ Need more time? Don't worry, we can extend the timer — we are in no rush.</div>

<FileHint file="exercise_07_file_io.py" active />

<ExerciseTimer />

---
layout: center
---

# You've made it through all 7 exercises!

**You now know the core building blocks of Python:**

<div class="concepts">
  <span>variables</span>
  <span>lists</span>
  <span>loops</span>
  <span>conditionals</span>
  <span>dictionaries</span>
  <span>functions</span>
  <span>file I/O</span>
</div>

---
layout: center
---

# Want to explore 9,000+ real songs?

Open the Data Explorer from the `setup` folder:

| Platform | File |
|----------|------|
| Mac | `setup/explore.command` |
| Windows | `setup/explore.bat` |

Search by song, artist, or genre — then use what you find in your exercises.

---
theme: default
title: Python & the Music World
info: A hands-on Python coding workshop for beginners
highlighter: shiki
lineNumbers: true
shiki:
  theme: 'github-light'
fonts:
  sans: 'Figtree'
  serif: 'Bricolage Grotesque'
  mono: 'Fira Code'
  weights: '400,500,600,700,800'
  provider: 'google'
mermaid:
  theme: base
  themeVariables:
    primaryColor: '#EDD9A3'
    primaryTextColor: '#1A1A2E'
    primaryBorderColor: '#C4942D'
    lineColor: '#C4942D'
    secondaryColor: '#F5EDD6'
    tertiaryColor: '#FBF6EC'
    edgeLabelBackground: '#FBF6EC'
    fontFamily: 'Figtree, sans-serif'
---

# Python &<br>the Music World

A Coding Workshop

---

# What we'll cover today

| # | Concept |
|---|---------|
| 0 | Getting set up |
| 1 | Variables & Strings |
| 2 | Lists |
| 3 | Loops |
| 4 | Conditionals |
| 5 | Dictionaries |
| 6 | Functions |
| 7 | File I/O |

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

---

# Running an exercise

VS Code opens automatically when setup passes.

Open the VS Code terminal with `` Ctrl+` `` and type:

```bash
python3 exercises/exercise_01_variables_and_strings.py
```

> On Windows, use `python` instead of `python3` if that doesn't work.

Open each exercise file in the `exercises` folder, read the example, then complete the **YOUR TASK** section.

---
layout: center
class: exercise-header
---

# Exercise 1
## Variables & Strings 🎤

---

# What is a variable?

A variable is a **labelled box** that stores a piece of information.

<div class="d-vars">
  <div class="d-row"><code class="d-box d-key">song_title</code><span class="d-arr">→</span><span class="d-box d-val">"Blinding Lights"</span></div>
  <div class="d-row"><code class="d-box d-key">artist</code><span class="d-arr">→</span><span class="d-box d-val">"The Weeknd"</span></div>
  <div class="d-row"><code class="d-box d-key">year</code><span class="d-arr">→</span><span class="d-box d-val">2019</span></div>
</div>

> Text goes inside quote marks: `"like this"`<br/>Numbers don't need quotes: `2019`, `3.22`

---

# Variables — code

```python
song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019
duration   = 3.22   # minutes

print(song_title)   # Blinding Lights
print(artist)       # The Weeknd
print(year)         # 2019
```

---

# f-strings

Slot variables directly into text — put `f` before the quote and `{}` around variable names.

```python
song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019

print(f"Now Playing: {song_title} by {artist} ({year})")
# Now Playing: Blinding Lights by The Weeknd (2019)
```

---

# Your Task — Exercise 1

1. Create variables for your favourite song: `my_song_title`, `my_artist`, `my_year`, `my_duration`
2. Use an f-string to print:

```
Now Playing: <title> by <artist> | Released: <year> | Duration: <duration> mins
```

---
layout: center
class: exercise-header
---

# Exercise 2
## Lists 📋

---

# What is a list?

A list stores **multiple items in order** — each item has an index starting at 0.

<div class="d-list">
  <div class="d-cell"><div class="d-cell-idx">[0]</div><div class="d-cell-val">Blinding Lights</div></div>
  <div class="d-cell"><div class="d-cell-idx">[1]</div><div class="d-cell-val">Levitating</div></div>
  <div class="d-cell"><div class="d-cell-idx">[2]</div><div class="d-cell-val">Stay</div></div>
  <div class="d-cell"><div class="d-cell-idx">[3]</div><div class="d-cell-val">Heat Waves</div></div>
</div>

> `playlist[0]` → first item · `playlist[-1]` → last item · `len(playlist)` → count

---

# Lists — code

```python
playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

print(playlist)        # the whole list
print(playlist[0])     # first item  → "Blinding Lights"
print(playlist[-1])    # last item   → "Heat Waves"
print(len(playlist))   # how many    → 4

playlist.append("As It Was")     # add to the end
playlist.remove("Stay")          # remove a specific song
playlist.insert(0, "Flowers")    # insert at position 0 (the start)
```

---

# Your Task — Exercise 2

1. Create `my_playlist` with at least 5 song titles
2. Print the entire playlist
3. Print only the **third** song
4. Use `.append()` to add a new song to the end
5. Use `.remove()` to delete one song
6. Print the total number of songs using `len()`

---
layout: center
class: exercise-header
---

# Exercise 3
## Loops 🔁

---

# What is a loop?

Instead of writing the same line for every song — let the loop do it.

<div class="d-loop">
  <div class="d-loop-row"><span class="d-arr">→</span><span>"Blinding Lights"</span><span class="d-loop-out">Now playing: Blinding Lights</span></div>
  <div class="d-loop-row"><span class="d-arr">→</span><span>"Levitating"</span><span class="d-loop-out">Now playing: Levitating</span></div>
  <div class="d-loop-row"><span class="d-arr">→</span><span>"Stay"</span><span class="d-loop-out">Now playing: Stay</span></div>
  <div class="d-loop-row"><span class="d-arr">→</span><span>"Heat Waves"</span><span class="d-loop-out">Now playing: Heat Waves</span></div>
</div>
<p class="d-caption">the indented code runs once for each item in the list</p>

> The **indented lines** (4 spaces) are inside the loop — they run once per item.

---

# Loops — code

```python
playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

for song in playlist:
    print(f"Now playing: {song}")
```

```python
# range() — repeat a fixed number of times
chorus = "We will, we will rock you!"
for i in range(4):
    print(chorus)
```

```python
# enumerate() — add a numbered counter
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")
```

---

# Your Task — Exercise 3

1. Create a list of 5 songs. Loop through and print each one with its track number using `enumerate()`
2. Pick a short lyric. Use `range()` to print it four times
3. Loop through and print every title in **UPPERCASE** using `.upper()`

---
layout: center
class: exercise-header
---

# Exercise 4
## Conditionals 🔀

---

# What is a conditional?

Your code takes a **different path** depending on whether something is true.

<div class="d-cond">
  <div class="d-cond-input"><code class="d-box d-key">song_bpm = 140</code></div>
  <div class="d-cond-branch">
    <div class="d-cond-row"><span class="d-cond-stem">├</span><span class="d-cond-check">bpm &gt; 150</span><span class="d-arr">→</span><span class="d-cond-result">"High energy!"</span></div>
    <div class="d-cond-row"><span class="d-cond-stem">├</span><span class="d-cond-check">bpm &gt; 100</span><span class="d-arr">→</span><span class="d-cond-result">"Mid-tempo"</span></div>
    <div class="d-cond-row"><span class="d-cond-stem">└</span><span class="d-cond-check">else&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="d-arr">→</span><span class="d-cond-result">"Slow and relaxed"</span></div>
  </div>
</div>

---

# Conditionals — code

```python
song_bpm = 140

if song_bpm > 150:
    print("High energy — great for a workout!")
elif song_bpm > 100:
    print("Mid-tempo — good for studying.")
else:
    print("Slow and relaxed — wind-down music.")
```

---

# Conditionals inside a loop

```python
titles = ["Blinding Lights", "Savage",    "Levitating"]
bpms   = [171,               134,         103]

for i, title in enumerate(titles):
    bpm = bpms[i]
    if bpm > 130:
        print(f"{title} — High energy")
    else:
        print(f"{title} — Mid-tempo or slower")
```

---

# Your Task — Exercise 4

1. Create two lists: song titles and BPM values (at least 5 songs, BPM range 60–200)
2. Loop through and classify each song:
   - **High energy** → BPM > 130
   - **Mid-tempo** → BPM 90–130
   - **Slow** → BPM < 90
3. Add a skip condition: if BPM > 180, print `"Skipping <title> — too fast!"`

---
layout: center
class: exercise-header
---

# Exercise 5
## Dictionaries 📀

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

---

# Dictionaries — code

```python
album = {
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
    print(f"Track {track_num}: {track_title}")
```

---

# Your Task — Exercise 5

1. Create `my_album` with keys: `title`, `artist`, `year`, `genre`, `tracks`
   - `tracks` should be a dict mapping track numbers → song titles
2. Print the album title and artist on one line using an f-string
3. Loop through the tracks and print a numbered listing
4. Add a new track to the dictionary after you've created it

---
layout: center
class: exercise-header
---

# Exercise 6
## Functions 🎛️

---

# What is a function?

Define code **once**, call it as many times as you like — with different inputs each time.

<div class="d-fn-wrap">
  <div class="d-fn-group">
    <div class="d-box d-val">"Blinding Lights", "The Weeknd"</div>
    <div class="d-box d-val">"Levitating", "Dua Lipa"</div>
  </div>
  <span class="d-arr">→</span>
  <div class="d-box d-dark">now_playing()</div>
  <span class="d-arr">→</span>
  <div class="d-fn-group">
    <div class="d-box d-val">▶ Blinding Lights — The Weeknd</div>
    <div class="d-box d-val">▶ Levitating — Dua Lipa</div>
  </div>
</div>

---

# Why use functions?

Without a function, you repeat yourself:

```python
print("▶  Blinding Lights — The Weeknd")
print("▶  Levitating — Dua Lipa")
print("▶  Heat Waves — Glass Animals")
# Change the format? Edit every single line.
```

With a function, define the format **once**:

```python
def now_playing(title, artist):
    print(f"▶  {title} — {artist}")

now_playing("Blinding Lights", "The Weeknd")
now_playing("Levitating",      "Dua Lipa")
now_playing("Heat Waves",      "Glass Animals")
# Change the format? Edit one line.
```

---

# Functions that return a value

```python
def classify_bpm(bpm):
    if bpm > 130:
        return "High energy"
    elif bpm > 90:
        return "Mid-tempo"
    else:
        return "Slow"

print(classify_bpm(171))   # High energy
print(classify_bpm(96))    # Mid-tempo
print(classify_bpm(68))    # Slow
```

---

# Your Task — Exercise 6

1. Write `describe_song(title, artist, year)` — prints one line about the song. Call it at least 3 times.

2. Write `longest_title(songs)` — takes a list of title strings and prints the longest one with its character count:

```
Longest title: Someone Like You (16 characters)
```

---
layout: center
class: exercise-header
---

# Exercise 7
## File I/O 💾

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

---

# Writing to a file

```python
playlist = [
    "Blinding Lights – The Weeknd",
    "Levitating – Dua Lipa",
    "Heat Waves – Glass Animals",
]

with open("my_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\n")   # \n = new line

print("Playlist saved!")
```

---

# Reading a file back

```python
with open("my_playlist.txt", "r") as f:
    lines = f.readlines()   # returns a list, one string per line

print(f"Loaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")   # .strip() removes the \n
```

---

# Your Task — Exercise 7

1. Create a list of at least 5 songs in `"Title – Artist"` format.
   Write them to a file called `my_playlist.txt`.

2. Read `my_playlist.txt` back and print a numbered track listing.
   Remember to use `.strip()` so the `\n` doesn't show up.

---
layout: center
---

# 🎉 You've made it through all 7 exercises!

**You now know the core building blocks of Python:**

variables · lists · loops · conditionals · dictionaries · functions · file I/O

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

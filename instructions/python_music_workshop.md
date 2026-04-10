# 🎵 Python & the Music World
### A Coding Workshop — Exercises 0–7

> **How to use this booklet:** Read the explanation → look at the example code → complete the task → try the extension challenge!

---

## Exercise 0 — Getting Set Up

Before writing any code, you need two things installed on your laptop: **Python** (the language) and **VS Code** (the editor). The setup script checks both for you.

### Step 1 — Run the setup script

Open the **`setup`** folder inside the python-music-workshop folder.

| Your laptop | File to double-click |
|-------------|----------------------|
| Mac | `setup.command` — right-click → Open the first time (macOS security) |
| Windows | `setup.bat` |

A terminal window opens and runs three checks automatically:

```
[ OK ] Python 3.11.4
[ OK ] VS Code 1.89.0
[ OK ] Loaded 9237 songs.

*** ALL DONE — YOU'RE GOOD TO GO! ***
```

VS Code opens automatically when all three pass. If anything shows `[FAIL]`, the script tells you exactly what to fix — show it to a volunteer.

### Step 2 — Open your first exercise

In VS Code, click the `exercises` folder in the left panel, then open `exercise_01_variables_and_strings.py`.

To run a file, open the terminal in VS Code (`` Ctrl+` ``) and type:

```
python3 exercises/exercise_01_variables_and_strings.py
```

> On Windows, use `python` instead of `python3` if that doesn't work.

### The Music Library & Data Explorer

From Exercise 4 onwards, the exercises give you access to a real library of 9,000+ songs. To browse it, double-click **`explore.command`** (Mac) or **`explore.bat`** (Windows) from the `setup` folder. A webpage opens in your browser where you can search by song, artist, or genre — and see the Python code to pull any song into your exercises.

Press Enter in the terminal window (or close it) when you're done with the explorer.

---

## Exercise 1 — 🎤 Variables & Strings

### What is a variable?

A variable is like a labelled box where you can store a piece of information. In Python you create one by writing a name, an equals sign, and then a value.

**Example:**

```python
song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019
duration   = 3.22   # minutes

print(song_title)
print(artist)
print(year)
```

> 💡 **Tip — String vs Number**
> Text must sit inside quote marks: `"like this"` or `'like this'`.
> Numbers don't need quotes. `2019` is a number, `"2019"` is text.
> You can't do maths with text, so keep them separate!

---

### f-strings: building a neat sentence

An f-string lets you slot variables straight into a piece of text. Put an `f` before the opening quote, then use curly braces `{}` around each variable name.

**Example:**

```python
song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019

print(f"Now Playing: {song_title} by {artist} ({year})")
# Output: Now Playing: Blinding Lights by The Weeknd (2019)
```

### Your Task

1. Create a variable called `song_title` and store the name of your favourite song.
2. Create a variable called `artist` and store the artist's name.
3. Create a variable called `year` and store the year the song was released.
4. Create a variable called `duration` and store the length of the song in minutes (e.g. `3.45`).
5. Use an f-string to print: `Now Playing: <title> by <artist> | Released: <year> | Duration: <duration> mins`

### 🎸 Extension Challenge

- Add a variable called `genre` (e.g. `"Pop"`, `"Grime"`, `"R&B"`).
- Print a second line: `Genre: <genre>`
- Try changing the artist name to ALL CAPS using the `.upper()` method: `artist.upper()`

---

## Exercise 2 — 📋 Lists

### What is a list?

A list is an ordered collection of items stored in a single variable. Each item sits inside square brackets `[ ]` and items are separated by commas. Lists are perfect for storing things like playlists.

**Example:**

```python
playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves", "Bad Habits"]

print(playlist)           # prints the whole list
print(playlist[0])        # prints the FIRST item (index 0)
print(playlist[-1])       # prints the LAST item
print(len(playlist))      # prints how many songs are in the list
```

> 💡 **Tip — Indexing starts at 0**
> Python counts from 0, not 1.
> So the first item is `playlist[0]`, the second is `playlist[1]`, and so on.
> Use a negative index to count from the end: `playlist[-1]` is the last item.

---

### Changing a list

You can add items, remove items, and find items in a list at any time.

**Example:**

```python
playlist.append("As It Was")    # adds a song to the END
playlist.remove("Stay")         # removes a specific song
playlist.insert(0, "Flowers")   # inserts a song at position 0 (the start)

print(playlist)
```

### Your Task

1. Create a list called `my_playlist` containing at least 5 song titles (as strings).
2. Print the entire playlist.
3. Print only the third song in the list.
4. Use `.append()` to add a new song to the end of the playlist.
5. Use `.remove()` to delete one song from the list.
6. Print the total number of songs using `len()`.

### 🎸 Extension Challenge

- Find the song with the longest title. Hint: use `len()` on each string.
- Sort the playlist into alphabetical order using `playlist.sort()` and print it.
- Reverse the playlist using `playlist.reverse()` and print it again.

---

## Exercise 3 — 🔁 Loops

### What is a loop?

A loop lets you repeat a block of code without writing it out again and again. A `for` loop works through every item in a list, one at a time.

**Example — looping through a playlist:**

```python
playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

for song in playlist:
    print(f"Now playing: {song}")
```

Notice the indentation (4 spaces). Python uses indentation to know which lines are inside the loop.

> 💡 **Tip — `range()`**
> `range(n)` generates the numbers 0, 1, 2, ... up to (but not including) `n`.
> Example: `for i in range(3):` will repeat the loop body 3 times.
> `range(1, 5)` gives 1, 2, 3, 4 — useful for numbering a track list!

---

### Printing lyrics with a loop

Loops are brilliant for repeating a chorus. The variable after `for` is just a counter — you can name it anything.

**Example:**

```python
chorus = "We will, we will rock you!"

for i in range(4):   # repeat 4 times
    print(chorus)

# numbered track listing
tracks = ["Track A", "Track B", "Track C"]
for i, track in enumerate(tracks, start=1):
    print(f"{i}. {track}")
```

### Your Task

1. Create a list of at least 5 songs. Loop through the list and print each one with its track number (1, 2, 3…).
2. Choose a short lyric or chorus line. Use `range()` to print it four times, mimicking a repeated chorus.
3. Write a loop that prints each song title in UPPERCASE using `.upper()`.

### 🎸 Extension Challenge

- Use `enumerate()` to number your tracks and print them like a proper track listing.
- Write a loop that counts up the total number of characters across all song titles combined.
- Loop through the playlist backwards using `playlist[::-1]`.

---

## Exercise 4 — 🔀 Conditionals

### What is a conditional?

A conditional lets your program make decisions. Using `if`, `elif` (else if), and `else`, Python checks whether something is `True` and runs different code depending on the answer.

**Example — a simple skip feature:**

```python
song_bpm = 140

if song_bpm > 150:
    print("High energy track — great for a workout!")
elif song_bpm > 100:
    print("Mid-tempo — good for studying.")
else:
    print("Slow and relaxed — wind-down music.")
```

> 💡 **Tip — Comparison Operators**
> `>`  greater than  |  `<`  less than
> `>=` greater or equal  |  `<=` less or equal
> `==` equal to  |  `!=` not equal to
> Combine conditions with `and` / `or`: `if bpm > 100 and genre == "Pop":`

---

### Conditionals inside loops

You can put an `if` statement inside a `for` loop to check each item as you go through a list.

**Example — classifying songs by BPM:**

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

### Your Task

1. Create two lists: one for song titles, one for BPM values. Include at least 5 songs (make up the BPM values — typical range is 60–200).
2. Loop through them using `enumerate` and print whether each song is High energy (BPM > 130), Mid-tempo (BPM 90–130), or Slow (BPM < 90).
3. Add a skip condition: if BPM > 180, print `'Skipping <title> — too fast!'` instead of the category.

### 🎸 Extension Challenge

- Use three counter variables (`high_count`, `mid_count`, `slow_count`) to tally how many songs fall into each category, then print a summary at the end.
- Use `and` to combine two conditions — for example, only classify a song if its BPM is between 60 and 200: `if bpm >= 60 and bpm <= 200:`
- After completing Exercise 5 (Dictionaries), come back and run your energy check on real songs from the music library.

---

## Exercise 5 — 📀 Dictionaries

### What is a dictionary?

A dictionary stores data as key–value pairs — like a real dictionary where every word (key) has a definition (value). Dictionaries are perfect for modelling an album, because each track number maps to a song title.

**Example — an album as a dictionary:**

```python
album = {
    "title":  "After Hours",
    "artist": "The Weeknd",
    "year":   2020,
    "tracks": {
        1: "Alone Again",
        2: "Too Late",
        3: "Hardest to Love",
        4: "Scared to Live",
        5: "Snowchild",
    }
}

print(album["title"])         # After Hours
print(album["tracks"][3])     # Hardest to Love
```

> 💡 **Tip — Keys and Values**
> Access a value with: `dictionary["key"]`
> Add a new pair with: `dictionary["new_key"] = value`
> Loop through all pairs: `for key, value in dictionary.items():`
> Check if a key exists: `if "title" in album:`

---

### Looping through a dictionary

```python
for track_num, track_title in album["tracks"].items():
    print(f"Track {track_num}: {track_title}")
```

### Your Task

1. Create a dictionary called `my_album` with keys: `'title'`, `'artist'`, `'year'`, `'genre'`, and `'tracks'`.
2. The `'tracks'` value should itself be a dictionary mapping track numbers (integers) to song titles.
3. Print the album title and artist on one line using an f-string.
4. Loop through the tracks dictionary and print a numbered track listing.
5. Add a new track to the tracks dictionary after you've created it.

### 🎸 Extension Challenge

- Add a `'label'` (record label) key to your album dictionary.
- Calculate and print how many tracks are on the album using `len()`.
- Create a list of two or three album dictionaries and loop through all of them, printing each album's title and track count.

---

## Exercise 6 — 🎛️ Functions

### What is a function?

A function is a reusable block of code that you give a name to. Instead of copying the same code in multiple places, you define it once and call it whenever you need it. Functions can accept inputs (called **parameters**) and send back an output (called the **return value**).

**Example — without and with a function:**

```python
# Without a function, you repeat yourself for every song:
#   print("▶  Blinding Lights — The Weeknd")
#   print("▶  Levitating — Dua Lipa")
#   print("▶  Heat Waves — Glass Animals")

# With a function, define the format once:
def now_playing(title, artist):
    print(f"▶  {title} — {artist}")

now_playing("Blinding Lights", "The Weeknd")
now_playing("Levitating",      "Dua Lipa")
now_playing("Heat Waves",      "Glass Animals")
```

A function can also **return** a value for you to use:

```python
def classify_bpm(bpm):
    if bpm > 130:
        return "High energy"
    elif bpm > 90:
        return "Mid-tempo"
    else:
        return "Slow"

print(classify_bpm(171))   # High energy
print(classify_bpm(68))    # Slow
```

> 💡 **Tip — `def`, parameters, `return`**
> `def` starts the function definition; give it a meaningful name.
> Parameters are the inputs listed in parentheses.
> Use `return` to send a value back to the caller.
> A function without `return` still runs its code — it just gives back `None`.

### Your Task

1. Write a function called `describe_song(title, artist, year)` that prints a one-line description of a song, e.g. `"Blinding Lights by The Weeknd (2019)"`. Call it at least three times.
2. Write a function called `longest_title(songs)` that takes a list of song title strings and prints the longest one along with how many characters it has, e.g. `"Longest title: Someone Like You (16 characters)"`.

### 🎸 Extension Challenge

- Update `now_playing()` to also call `classify_bpm()` and print the energy label alongside the title and artist.
- Write a function called `count_by_artist(songs, artist)` that takes a list of song dictionaries (each with `"title"` and `"artist"` keys) and returns how many songs match that artist.
- Write a function called `search(songs, keyword)` that returns a list of titles containing the keyword (case-insensitive). Hint: use `keyword.lower()` and `title.lower()`.

---

## Exercise 7 — 💾 File I/O: Save & Load a Playlist

### Why save to a file?

So far, all our data disappears as soon as the program stops. Files let us save information so it's still there next time we run the program — just like an app saving your playlist to disk.

### Writing to a file

```python
playlist = [
    "Blinding Lights – The Weeknd",
    "Levitating – Dua Lipa",
    "Stay – The Kid LAROI & Justin Bieber",
    "Heat Waves – Glass Animals",
]

with open("my_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\n")   # \n = new line

print("Playlist saved!")
```

> 💡 **Tip — The `with` Statement**
> `with open(...) as f:` automatically closes the file when you're done.
> `"w"` mode creates the file (or overwrites it). Use `"a"` to append instead.
> `"r"` mode reads an existing file.
> Always use `with` — it prevents data loss if something goes wrong.

---

### Reading from a file

```python
with open("my_playlist.txt", "r") as f:
    lines = f.readlines()   # returns a list of strings, one per line

print(f"Loaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")  # .strip() removes the \n at the end
```

### Your Task

1. Create a list of at least 5 songs (use `'Title – Artist'` format as strings).
2. Write the playlist to a file called `my_playlist.txt`, with one song per line.
3. Open the file, read it back in, and print a numbered track listing using the lines you've loaded.
4. Add a new song to the file using `"a"` (append) mode, then re-read and print the updated list.

### 🎸 Extension Challenge

- Store each song as `'Title,Artist,Year'` (comma-separated). When reading back, split each line: `parts = line.strip().split(",")` and print each field separately.
- Write a function called `save_playlist(filename, playlist)` and another called `load_playlist(filename)` to make your code reusable.
- Count how many songs are by the same artist across the whole file and print the result.

---

*🎵 Great work — you've made it through all 7 exercises! You now know the core building blocks of Python. If you haven't already, open the Data Explorer (double-click `explore.command` or `explore.bat` in the `setup` folder) and try pulling real songs into your code.*

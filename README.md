# Python Music Workshop

A hands-on Python workshop for beginners, themed around music — playlists, albums, artists, and lyrics.

## Overview

Seven progressive exercises that introduce core Python concepts using music-themed examples. No prior experience needed.

| # | File | Concept |
|---|------|---------|
| 0 | `exercises/exercise_00_setup_check.py` | Getting set up |
| 1 | `exercises/exercise_01_variables_and_strings.py` | Variables, data types, f-strings |
| 2 | `exercises/exercise_02_lists.py` | Lists, indexing, append, remove, len |
| 3 | `exercises/exercise_03_loops.py` | for loops, range(), enumerate() |
| 4 | `exercises/exercise_04_conditionals.py` | if / elif / else, comparison operators |
| 5 | `exercises/exercise_05_dictionaries.py` | Dictionaries, key-value pairs, nesting |
| 6 | `exercises/exercise_06_functions.py` | def, parameters, return values |
| 7 | `exercises/exercise_07_file_io.py` | Reading and writing .txt files |

Each exercise file contains:
- A plain-English explanation of the concept
- A worked example you can run straight away
- A clearly marked **YOUR TASK** section
- An **Extension Challenge** for faster finishers

---

## Getting the Workshop

Download the zip from **tinyurl.com/python-walthamstow-workshop** (green Code button → Download ZIP), unzip it, and move the folder somewhere easy to find (e.g. the Desktop).

---

## Student Setup

Python is **bundled** with the workshop — students do not need to install it. The setup script downloads it automatically on first run if it isn't there yet.

### Mac

1. Open **Terminal** (Cmd+Space → type *Terminal* → Enter)
2. Type `bash ` (with a space), then drag **`setup/setup.command`** from the Finder into the Terminal window
3. Press Enter

### Windows

1. Open the `setup` folder in File Explorer
2. Click the **address bar** at the top → type `cmd` → press Enter
3. Type `setup.bat` and press Enter — if SmartScreen appears, click **More info → Run anyway**

The script prints a clear pass/fail for each check. If the Python runtime isn't present it downloads it automatically (~30 MB).

### What the script checks

| Check | Detail |
|-------|--------|
| Python runtime | Bundled in `python-runtime/` — auto-downloaded if missing |
| Music data | `exercises/music_data.py` loads without errors |

---

## Running Exercises

From the VS Code terminal (`` Ctrl+` ``), open the workshop folder and run:

```bash
python3 exercises/exercise_01_variables_and_strings.py
```

On Windows use `python3.bat` instead of `python3`, or just `python3` if VS Code picks up the `.bat` wrapper automatically.

No packages to install — the workshop uses Python's standard library only.

---

## Music Library & Data Explorer

Exercises 4–7 include an optional `EXPLORE` section that uses a real library of 9,000+ songs (artists include Sabrina Carpenter, Central Cee, RAYE, Olivia Dean, Bad Bunny, Taylor Swift, and many more). The data is bundled in `data/songs.json` — no internet connection needed.

To browse the library with a searchable web UI, run the launcher from the `setup` folder the same way as the setup script:

| Platform | File |
|----------|------|
| Mac | drag `setup/explore.command` into Terminal and press Enter |
| Windows | open cmd in `setup` folder → type `explore.bat` |

This opens a local webpage where students can search by song, artist, or genre, and see the Python code needed to access any entry. Press Enter in the terminal window (or close it) to stop the server.

---

## Workshop Instructions

Full classroom instructions are in `instructions/python_music_workshop.md`.

Volunteer setup notes are in `setup/VOLUNTEER_GUIDE.md`.

---

## Tips for Volunteers & TAs

- Run the setup script on each student laptop before the session — the output tells you exactly what is missing.
- Python is bundled — no Python installation troubleshooting needed.
- Each exercise is self-contained — students don't need to complete them in order, but concepts build progressively.
- The example code at the top of each file runs without modification — a good way to start each exercise is to run it first, then read through it.
- Exercise 7 (File I/O) creates `my_playlist.txt` in the working directory — this is gitignored.
- Extension challenges are intentionally open-ended; encourage students to experiment beyond what's asked.

---

## License

MIT — free to use, adapt, and share for educational purposes.

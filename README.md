# Python Music Workshop

A hands-on Python workshop for Year 10 students, themed around music — playlists, albums, artists, and lyrics.

## Overview

Seven progressive exercises that introduce core Python concepts using music-themed examples. No prior experience needed.

| # | File | Concept |
|---|------|---------|
| 0 | `exercises/exercise_00_setup.md` | Getting set up (read this first) |
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
- A **Extension Challenge** for faster finishers

---

## Student Setup

Students run a setup script that checks Python and VS Code are installed, verifies the music data loads correctly, and opens VS Code automatically.

**Mac** — double-click `setup/setup.command` in Finder
(first time: right-click → Open, to bypass Gatekeeper)

**Windows** — double-click `setup/setup.bat` in File Explorer

The script prints a clear pass/fail for each check. If anything is missing, it lists exactly what needs to be fixed with download links. See `exercises/exercise_00_setup.md` for the full student-facing instructions.

### What the script checks

| Check | Detail |
|-------|--------|
| Python | Version 3.8 or newer |
| VS Code | Installed and `code` command available in terminal |
| Smoke test | `exercises/music_data.py` loads without errors |

If all three pass, VS Code opens in the project folder automatically.

---

## Running Exercises

From the VS Code terminal (`` Ctrl+` ``):

```bash
python3 exercises/exercise_01_variables_and_strings.py
```

On Windows, use `python` instead of `python3` if needed.

No packages to install — the workshop uses Python's standard library only.

---

## Music Library & Data Explorer

Exercises 4–7 include an optional `EXPLORE` section that uses a real library of 9,000+ songs (artists include Sabrina Carpenter, Central Cee, RAYE, Olivia Dean, Bad Bunny, Taylor Swift, and many more). The data is bundled in `data/songs.json` — no internet connection needed.

To browse the library with a searchable web UI:

```bash
python3 data/explorer.py
```

This opens a local webpage where students can search by song, artist, or genre, and see the Python code needed to access any entry.

---

## Workshop Instructions

Full classroom instructions are in `instructions/python_music_workshop.md`.

---

## Tips for Volunteers & TAs

- Run `setup.command` / `setup.bat` on each student laptop before the session. The output tells you exactly what is missing and how to fix it.
- Each exercise is self-contained — students don't need to complete them in order, but concepts do build progressively.
- The example code at the top of each file runs without modification — a good way to start each exercise is to run it first, then read through it.
- Exercise 7 (File I/O) creates `my_playlist.txt` in the working directory — this is gitignored and cleaned up by the exercise itself.
- Extension challenges are intentionally open-ended; encourage students to experiment beyond what's asked.

---

## License

MIT — free to use, adapt, and share for educational purposes.

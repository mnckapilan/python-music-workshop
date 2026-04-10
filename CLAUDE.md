# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Python coding workshop for beginners. Seven self-contained exercises teach core Python concepts through music-themed examples (playlists, albums, artists, lyrics). No third-party dependencies — pure Python 3.8+.

## Running Exercises

Python is bundled in `python-runtime/` (auto-downloaded by setup scripts). Use the wrapper scripts at the project root:

```bash
# Mac
./python3 exercises/exercise_01_variables_and_strings.py

# Windows
python3.bat exercises/exercise_01_variables_and_strings.py
```

No test suite, no linter, no build step. Exercises run standalone.

## Exercise Architecture

Each exercise follows the same pattern:
1. Concept explanation in comments
2. Worked example (runnable as-is)
3. `# YOUR TASK` section where students add code
4. `# Extension Challenge` for faster students

| Exercise | Concepts | Music Context |
|----------|----------|---------------|
| 01 | Variables, strings, f-strings | Song metadata |
| 02 | Lists, indexing, `.append()`/`.remove()` | Playlists |
| 03 | `for` loops, `range()`, `enumerate()` | Iterating playlists, lyrics |
| 04 | `if`/`elif`/`else`, comparison operators | BPM classification |
| 05 | Dictionaries, nested dicts, `.items()` | Album metadata |
| 06 | Functions, parameters, return values | Reusable playlist ops |
| 07 | File I/O, `open()`, context managers | Saving/loading playlists |

## Key Notes

- Exercise 07 writes/reads `my_playlist.txt` (gitignored) and cleans up with `os.remove()`
- Exercises are designed to be assigned individually — concepts build progressively but each file is self-contained
- Full workshop instructions are in `instructions/python_music_workshop.md`
- Volunteer setup notes are in `setup/VOLUNTEER_GUIDE.md`
- Setup scripts (`setup/setup.command`, `setup/setup.bat`) auto-download the Python runtime if `python-runtime/` is absent
- `python-runtime/` and `dist/` are gitignored — don't commit them

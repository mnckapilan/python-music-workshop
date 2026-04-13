# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Python coding workshop for beginners. Seven self-contained exercises teach core Python concepts through music-themed examples (playlists, albums, artists, lyrics). No third-party dependencies — pure Python 3.8+.

## Running Exercises

Students use **saarai.dev** (a hosted online IDE — source at github.com/mnckapilan/saarai). They download the workshop from **tinyurl.com/python-walthamstow-workshop**, open the folder with File → Open Folder in Saarai, and click Run on each exercise file.

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

- Exercise 07 writes/reads `my_playlist.txt` (gitignored)
- Exercises are designed to be assigned individually — concepts build progressively but each file is self-contained
- Music data is in `data/songs.json` (bundled, no internet needed for exercises)
- Data Explorer (hosted GitHub page) is at tinyurl.com/7tdxxp57
- Slides are in a separate repo: github.com/mnckapilan/python-workshop-slides

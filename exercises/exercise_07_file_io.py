# ============================================================
#  Exercise 7 — File I/O: Save & Load a Playlist 💾
# ============================================================
#
#  WHY SAVE TO A FILE?
#  So far all our data disappears when the program stops.
#  Files let us save information so it's still there next
#  time — just like an app saving your playlist to disk.
#
#  Always use `with open(...) as f:` — it closes the file
#  automatically when you're done.
#
#  FILE MODES:
#   "w"  write — creates the file (overwrites if it exists)
#   "r"  read  — reads an existing file
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

import os

# --- WRITING ---
# Each song needs "\n" at the end to go on its own line
# (just like pressing Enter in a text editor).

playlist = [
    "Blinding Lights – The Weeknd",
    "Levitating – Dua Lipa",
    "Heat Waves – Glass Animals",
]

with open("example_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\n")

print("Playlist saved!")

# --- READING ---
# readlines() gives you a list — one string per line.
# Each string still has "\n" at the end, so .strip() removes it.

with open("example_playlist.txt", "r") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")

# Clean up
os.remove("example_playlist.txt")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list of at least 5 songs in "Title – Artist"
#     format. Write them to a file called my_playlist.txt.
#
#  2. Read my_playlist.txt back and print a numbered listing.
#     Remember to use .strip() so the "\n" doesn't show up.

# Start your code here 👇

my_playlist = [
    # add your songs here as "Title – Artist" strings
]

# Step 1 — write to file:


# Step 2 — read back and print:


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Build your playlist from real songs instead of typing them:
# my_playlist = [f"{s['title']} – {s['artist']}" for s in SONGS[:5]]

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Wrap your code into two reusable functions (from exercise 6!):
#      save_playlist(filename, playlist)
#      load_playlist(filename)  → returns a list of strings
#
#  - Instead of "Title – Artist", store each song as
#    "Title,Artist,Year" (comma-separated).
#    When reading back, split each line:
#     parts = line.strip().split(",")
#    and print each field separately.

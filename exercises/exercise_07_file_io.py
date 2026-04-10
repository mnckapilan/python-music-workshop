# ============================================================
#  Exercise 7 — File I/O: Save & Load a Playlist 💾
# ============================================================
#
#  WHY SAVE TO A FILE?
#  So far all our data disappears when the program stops.
#  Files let us save information so it's still there next
#  time — just like an app saving your playlist to disk.
#
#  FILE MODES:
#   "w"  write   — creates file (overwrites if it exists)
#   "a"  append  — adds to the END of an existing file
#   "r"  read    — reads an existing file
#
#  Always use `with open(...) as f:` — it closes the file
#  safely when you're done.
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

import os
from music_data import SONGS

# Build a playlist from real songs and save it to a file
playlist = [f"{s['title']} – {s['artist']}" for s in SONGS[:4]]

with open("example_playlist.txt", "w") as f:
    for song in playlist:
        f.write(song + "\n")   # \n = new line

print("Playlist saved!")

# Read it back in
with open("example_playlist.txt", "r") as f:
    lines = f.readlines()   # returns a list, one string per line

print(f"\nLoaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")   # .strip() removes the \n

# Append a new song
with open("example_playlist.txt", "a") as f:
    f.write(f"{SONGS[4]['title']} – {SONGS[4]['artist']}\n")

print("\nAfter adding a song:")
with open("example_playlist.txt", "r") as f:
    for i, line in enumerate(f.readlines(), start=1):
        print(f"{i}. {line.strip()}")

# Clean up the example file
os.remove("example_playlist.txt")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list of at least 5 songs in "Title – Artist"
#     format. Use your own favourites, or pull from SONGS:
#       my_playlist = [f"{s['title']} – {s['artist']}" for s in SONGS[:5]]
#     Write them to a file called my_playlist.txt.
#
#  2. Read the file back and print a numbered track listing.
#
#  3. Use append mode ("a") to add one more song, then
#     re-read and print the updated list.

# Start your code here 👇

my_playlist = [
    # add your songs here as "Title – Artist" strings,
    # or use: [f"{s['title']} – {s['artist']}" for s in SONGS[:5]]
]

# Step 1 — write to file:


# Step 2 — read back and print:


# Step 3 — append a new song, then re-read:


# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Instead of "Title – Artist", store each song as
#    "Title,Artist,Year"  (comma-separated).
#    When reading back, split each line:
#      parts = line.strip().split(",")
#    and print each field on its own.
#
#  - Wrap your code into two reusable functions:
#      save_playlist(filename, playlist)
#      load_playlist(filename)  → returns a list of strings
#
#  - Save all songs from SONGS to a file, then read it back
#    and count how many songs are by the same artist.

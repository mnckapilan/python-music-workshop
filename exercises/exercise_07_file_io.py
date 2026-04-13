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
    "Heat Waves – Glass Animals",
    "Blinding Lights – The Weeknd",
    "Levitating – Dua Lipa",
    "As It Was – Harry Styles",
    "Bad Habit – Steve Lacy",
    "Flowers – Miley Cyrus",
]

# Step 1 — write to file:
with open("my_playlist.txt", "w") as f:
    for song in my_playlist:
        f.write(song + "\n")

print("Playlist saved!")

# Step 2 — read back and print:
with open("my_playlist.txt", "r") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} songs:")
for i, song in enumerate(lines, start=1):
    print(f"{i}. {song.strip()}")

# Clean up
os.remove("my_playlist.txt")

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Wrap your code into two reusable functions:
def save_playlist(filename, playlist):
    with open(filename, "w") as f:
        for song in playlist:
            f.write(song + "\n")

def load_playlist(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

save_playlist("my_playlist.txt", my_playlist)
loaded = load_playlist("my_playlist.txt")
print(loaded)
os.remove("my_playlist.txt")

#  - Store each song as "Title,Artist,Year" using real song data:
real_playlist = [f"{s['title']},{s['artist']},{s['year']}" for s in song_library[:10]]
save_playlist("real_playlist.txt", real_playlist)

with open("real_playlist.txt", "r") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        print(f"Title: {parts[0]}, Artist: {parts[1]}, Year: {parts[2]}")

os.remove("real_playlist.txt")

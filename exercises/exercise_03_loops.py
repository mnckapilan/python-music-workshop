# ============================================================
#  Exercise 3 — Loops 🔁
# ============================================================
#
#  WHAT IS A LOOP?
#  A loop repeats a block of code without you having to write
#  it out again and again. A `for` loop works through every
#  item in a list, one at a time.
#
#  IMPORTANT: The indented lines (4 spaces) are INSIDE the
#  loop. Python uses indentation to know what repeats.
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves"]

# Basic for loop
for song in playlist:
    print(f"Now playing: {song}")

print("---")

# range() repeats something a set number of times
chorus = "We will, we will rock you!"
for i in range(4):
    print(chorus)

print("---")

# enumerate() gives you a counter alongside each item
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
from music_data import SONGS   # 40 real songs, ready to use
#
#  Try looping over real data:
#    for s in SONGS:
#        print(s["title"], "–", s["artist"])
#
#  Or use real titles as your playlist:
#    real_playlist = [s["title"] for s in SONGS[:5]]

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list of at least 5 songs.
#     Type your own, or pull real titles from SONGS:
#       my_playlist = [s["title"] for s in SONGS[:5]]
#     Loop through and print each one with its track number
#     (1, 2, 3...) using enumerate().
#
#  2. Choose a short lyric or chorus line. Use range() to
#     print it four times.
#
#  3. Write a loop that prints every song title in UPPERCASE
#     using .upper().

# Start your code here 👇

my_playlist = [
    # add your songs here
]

# Task 1 — numbered track listing


# Task 2 — repeated chorus
my_lyric = "YOUR LYRIC HERE"


# Task 3 — UPPERCASE titles


# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Count the total number of characters across ALL song
#    titles combined (add up len(song) for each song).
#  - Loop through the playlist BACKWARDS: my_playlist[::-1]
#  - Print only songs whose title is longer than 10 characters.
#  - Loop over all 40 songs in SONGS and print only the ones
#    with a title longer than 15 characters.

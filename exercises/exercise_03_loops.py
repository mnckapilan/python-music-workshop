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
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list of at least 5 songs. Type your own titles.
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
    "Heat Waves",
    "Blinding Lights",
    "Levitating",
    "As It Was",
    "Bad Habit",
    "Flowers",
]

# Task 1 — numbered track listing
for i, song in enumerate(my_playlist, start=1):
    print(f"{i}. {song}")

print("---")

# Task 2 — repeated chorus
my_lyric = "It was always you, heat waves!"
for i in range(4):
    print(my_lyric)

print("---")

# Task 3 — UPPERCASE titles
for song in my_playlist:
    print(song.upper())

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use
#
#  Try looping over real data:
# for s in song_library[:10]:
#     print(s["title"], "–", s["artist"])
#
#  Or use real titles as your playlist:
# real_playlist = []
# for s in song_library[:5]:
#     real_playlist.append(s["title"])

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Count the total number of characters across ALL song titles combined:
total_chars = 0
for song in my_playlist:
    total_chars += len(song)
print(f"Total characters in all titles: {total_chars}")

#  - Loop through the playlist BACKWARDS:
for song in my_playlist[::-1]:
    print(song)

#  - Print only songs whose title is longer than 10 characters:
for song in my_playlist:
    if len(song) > 10:
        print(song)

#  - Loop over all songs in song_library and print only those with title > 15 chars:
for s in song_library:
    if len(s["title"]) > 15:
        print(s["title"])

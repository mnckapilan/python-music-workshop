# ============================================================
#  Exercise 4 — Conditionals 🔀
# ============================================================
#
#  WHAT IS A CONDITIONAL?
#  A conditional lets your program make decisions.
#  Using if, elif (else if), and else, Python checks whether
#  something is True and runs different code accordingly.
#
#  COMPARISON OPERATORS:
#   >   greater than      <   less than
#   >=  greater or equal  <=  less or equal
#   ==  equal to          !=  not equal to
#
#  Combine with:  and   or   not
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

song_bpm = 140

if song_bpm > 150:
    print("High energy track — great for a workout!")
elif song_bpm > 100:
    print("Mid-tempo — good for studying.")
else:
    print("Slow and relaxed — wind-down music.")

print("---")

# Conditionals inside a loop
songs = [
    {"title": "Blinding Lights", "genre": "Pop"},
    {"title": "Savage",          "genre": "Hip-Hop"},
    {"title": "Levitating",      "genre": "Pop"},
]

for song in songs:
    if song["genre"] == "Pop":
        print(f"Pop hit: {song['title']}")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list of at least 5 songs. Each song should be
#     a dictionary with 'title' and 'bpm' keys.
#     Make up your own BPM values (typical range: 60–200).
#
#  2. Loop through the list and print whether each song is:
#       High energy  → BPM > 130
#       Mid-tempo    → BPM 90–130
#       Slow         → BPM < 90
#
#  3. Add a 'skip' condition: if BPM > 180, print
#     "Skipping <title> — too fast!" instead.

# Start your code here 👇

my_songs = [
    {"title": "Song One",   "bpm": 120},
    {"title": "Song Two",   "bpm": 85},
    # add more songs...
]

for song in my_songs:
    pass   # replace 'pass' with your if/elif/else logic


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Each song has real BPM, genre, and explicit values:
#    print(SONGS[0]["title"])     # title
#    print(SONGS[0]["bpm"])       # beats per minute
#    print(SONGS[0]["genre"])     # e.g. "Pop", "Hip-Hop/Rap"
#    print(SONGS[0]["explicit"])  # True or False
#
#  See the first 10 BPMs:
#    for s in SONGS[:10]:
#        print(s["title"], s["bpm"])
#
#  Use real songs in your task above:
#    my_songs = [{"title": s["title"], "bpm": s["bpm"]} for s in SONGS[:5]]

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add an 'explicit' key (True or False) to each song.
#    Only print a song if it is NOT explicit:
#      if not song["explicit"]:
#
#  - Run the same energy check across the first 10 songs in SONGS
#    (they have real bpm and explicit values):
#      for s in SONGS[:10]:
#          # your if/elif/else logic here
#
#  - Count how many songs fall into each energy category
#    (use three counter variables) and print a summary
#    at the end.

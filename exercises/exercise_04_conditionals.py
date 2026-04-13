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
# Two parallel lists — title and BPM for each song
titles = ["Blinding Lights", "Savage",    "Levitating"]
bpms   = [171,               134,         103]

for i, title in enumerate(titles):
    bpm = bpms[i]
    if bpm > 130:
        print(f"{title} — High energy")
    else:
        print(f"{title} — Mid-tempo or slower")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create two lists: one for song titles, one for BPM values.
#     Include at least 5 songs. Make up your own BPM values
#     (typical range: 60–200).
#
#  2. Loop through them (use enumerate like the example above)
#     and print whether each song is:
#       High energy  → BPM > 130
#       Mid-tempo    → BPM 90–130
#       Slow         → BPM < 90
#     (These thresholds are different from the example above —
#      three categories give a more precise classification.)
#
#  3. Add a 'skip' condition: if BPM > 180, print
#     "Skipping <title> — too fast!" instead of the category.

# Start your code here 👇

my_titles = ["Song One", "Song Two"]   # add more...
my_bpms   = [120,        85]           # matching BPMs

for i, title in enumerate(my_titles):
    bpm = my_bpms[i]
    pass   # replace 'pass' with your if/elif/else logic


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  SONGS uses a format called dictionaries — covered in Exercise 5.
#  Come back to this section after you've done that exercise!
#
#  Run your energy check on real songs:
# for s in SONGS[:10]:
#     title = s["title"]
#     bpm   = s["bpm"]
#     # your if/elif/else logic here

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Count how many songs fall into each energy category
#    (use three counter variables) and print a summary
#    at the end:
# high_count = 0
# mid_count  = 0
# slow_count = 0
#
#  - Run the same check on the first 10 songs in SONGS.
#    (access each song's BPM with s["bpm"] and title with s["title"])
#
#  - Use `and` to combine two conditions. For example,
#    only classify a song if its BPM is between 60 and 200:
# if bpm >= 60 and bpm <= 200:

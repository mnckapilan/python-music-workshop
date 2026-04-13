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

my_titles = ["Heat Waves", "Blinding Lights", "Levitating", "Someone Like You", "Ultralight Beam", "Superhero"]
my_bpms   = [89,           171,               103,          67,                 87,                186]

for i, title in enumerate(my_titles):
    bpm = my_bpms[i]
    if bpm > 180:
        print(f"Skipping {title} — too fast!")
    elif bpm > 130:
        print(f"{title} — High energy")
    elif bpm >= 90:
        print(f"{title} — Mid-tempo")
    else:
        print(f"{title} — Slow")

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use
#
#  song_library uses a format called dictionaries — covered in Exercise 5.
#  Come back to this section after you've done that exercise!

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Count how many songs fall into each energy category:
high_count = 0
mid_count  = 0
slow_count = 0

for i, title in enumerate(my_titles):
    bpm = my_bpms[i]
    if bpm > 180:
        pass   # skipped — not counted
    elif bpm > 130:
        high_count += 1
    elif bpm >= 90:
        mid_count += 1
    else:
        slow_count += 1

print(f"High energy: {high_count} | Mid-tempo: {mid_count} | Slow: {slow_count}")

#  - Run the same check on the first 10 songs in song_library:
print("---")
for s in song_library[:10]:
    title = s["title"]
    bpm   = s["bpm"]
    if bpm > 180:
        print(f"Skipping {title} — too fast!")
    elif bpm > 130:
        print(f"{title} — High energy")
    elif bpm >= 90:
        print(f"{title} — Mid-tempo")
    else:
        print(f"{title} — Slow")

#  - Use `and` to combine two conditions:
#    only classify if BPM is between 60 and 200:
for s in song_library[:10]:
    bpm = s["bpm"]
    if bpm >= 60 and bpm <= 200:
        print(f"{s['title']}: valid BPM ({bpm})")

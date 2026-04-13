# ============================================================
#  Exercise 6 — Functions 🎛️
# ============================================================
#
#  WHAT IS A FUNCTION?
#  A function is a reusable block of code you give a name to.
#  Define it once, call it as many times as you like —
#  and if you want to change how it works, you only edit
#  one place instead of hunting through your whole program.
#
#  def function_name(parameter1, parameter2):
#      # code goes here
#      return result      # optional — sends a value back
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

# Without a function, you'd repeat yourself for every song:
#   print("▶  Blinding Lights — The Weeknd")
#   print("▶  Levitating — Dua Lipa")
#   print("▶  Heat Waves — Glass Animals")
# Change the format? Edit every line. That gets painful fast.

# With a function, define the format once:
def now_playing(title, artist):
    print(f"▶  {title} — {artist}")

now_playing("Blinding Lights", "The Weeknd")
now_playing("Levitating",      "Dua Lipa")
now_playing("Heat Waves",      "Glass Animals")
# Now changing "▶" to "🎵" means editing one line, not three.

print("---")

# A function can also RETURN a value for you to use later.
def classify_bpm(bpm):
    """Returns an energy label for a given BPM."""
    if bpm > 130:
        return "High energy"
    elif bpm > 90:
        return "Mid-tempo"
    else:
        return "Slow"

# Use the return value directly:
print(classify_bpm(171))   # High energy
print(classify_bpm(96))    # Mid-tempo
print(classify_bpm(68))    # Slow

print("---")

# Combine both ideas — call classify_bpm() inside a loop:
titles = ["Blinding Lights", "Shape of You", "Someone Like You"]
bpms   = [171,               96,             68]

for i, title in enumerate(titles):
    label = classify_bpm(bpms[i])
    print(f"{title}: {label}")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Write a function called describe_song(title, artist, year)
#     that prints one line about a song, e.g.:
#       "Blinding Lights by The Weeknd (2019)"
#     Call it at least three times with different songs.
#
#  2. Write a function called longest_title(songs) that takes
#     a list of song title strings and prints the one with the
#     most characters and how long it is, e.g.:
#       "Longest title: Someone Like You (16 characters)"

# Start your code here 👇

# Task 1
def describe_song(title, artist, year):
    pass   # replace with your code


# Task 2
def longest_title(songs):
    pass   # replace with your code


sample_songs = [
    "Blinding Lights",
    "Levitating",
    "Heat Waves",
    "Stay",
    "Bad Habit",
]

# Call your functions here:


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Pass a real song to describe_song():
# describe_song(SONGS[0]["title"], SONGS[0]["artist"], SONGS[0]["year"])
#
#  Pass a real song to now_playing():
# now_playing(SONGS[0]["title"], SONGS[0]["artist"])
#
#  Find the longest title in the first 100 real songs:
# real_titles = [s["title"] for s in SONGS[:100]]
# print(longest_title(real_titles))

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add classify_bpm() to your now_playing() function so it
#    prints the energy label too. You already have classify_bpm —
#    just call it inside now_playing().
#
#  - Write a function called count_by_artist(songs, artist)
#    that takes a list of song dictionaries (each with "title"
#    and "artist" keys) and RETURNS how many songs match.
#    Test it on sample_playlist below:
#
# sample_playlist = [
#     {"title": "Blinding Lights", "artist": "The Weeknd"},
#     {"title": "Save Your Tears", "artist": "The Weeknd"},
#     {"title": "Levitating",      "artist": "Dua Lipa"},
# ]
# print(count_by_artist(sample_playlist, "The Weeknd"))  # 2
#
#  - Write a function called search(songs, keyword) that returns
#    a list of titles containing the keyword (case-insensitive).
#    Hint: use keyword.lower() and title.lower()

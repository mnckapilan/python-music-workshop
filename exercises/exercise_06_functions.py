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
    print(f"{title} by {artist} ({year})")


# Task 2
def longest_title(songs):
    longest = songs[0]
    for song in songs:
        if len(song) > len(longest):
            longest = song
    print(f"Longest title: {longest} ({len(longest)} characters)")


sample_songs = [
    "Blinding Lights",
    "Levitating",
    "Heat Waves",
    "Stay",
    "Bad Habit",
    "Someone Like You",
]

# Call your functions here:
describe_song("Heat Waves", "Glass Animals", 2020)
describe_song("Blinding Lights", "The Weeknd", 2019)
describe_song("As It Was", "Harry Styles", 2022)

longest_title(sample_songs)

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use

#  Pass a real song to describe_song():
describe_song(song_library[0]["title"], song_library[0]["artist"], song_library[0]["year"])

#  Find the longest title in the first 100 real songs:
real_titles = []
for s in song_library[:100]:
    real_titles.append(s["title"])
longest_title(real_titles)

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add classify_bpm() to now_playing() so it prints the energy label too:
def now_playing_with_bpm(title, artist, bpm):
    label = classify_bpm(bpm)
    print(f"▶  {title} — {artist} [{label}]")

now_playing_with_bpm("Heat Waves", "Glass Animals", 89)
now_playing_with_bpm("Blinding Lights", "The Weeknd", 171)

#  - Write a function called count_by_artist:
def count_by_artist(songs, artist):
    count = 0
    for song in songs:
        if song["artist"] == artist:
            count += 1
    return count

sample_playlist = [
    {"title": "Blinding Lights", "artist": "The Weeknd"},
    {"title": "Save Your Tears", "artist": "The Weeknd"},
    {"title": "Levitating",      "artist": "Dua Lipa"},
]
print(count_by_artist(sample_playlist, "The Weeknd"))  # 2

#  - Write a function called search that returns titles matching a keyword:
def search(songs, keyword):
    results = []
    for song in songs:
        if keyword.lower() in song["title"].lower():
            results.append(song["title"])
    return results

print(search(song_library, "love"))

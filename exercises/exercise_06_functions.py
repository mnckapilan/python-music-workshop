# ============================================================
#  Exercise 6 — Functions 🎛️
# ============================================================
#
#  WHAT IS A FUNCTION?
#  A function is a reusable block of code you give a name to.
#  Define it once, call it as many times as you like.
#
#  def function_name(parameter1, parameter2):
#      """Optional description (docstring)."""
#      # code goes here
#      return result      # optional — sends a value back
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

def now_playing(title, artist, bpm):
    """Prints a formatted Now Playing message."""
    if bpm > 130:
        energy = "High Energy"
    elif bpm > 90:
        energy = "Mid-Tempo"
    else:
        energy = "Slow Jam"
    print(f"▶  {title} — {artist}  [{energy}]")


now_playing("Blinding Lights", "The Weeknd", 171)
now_playing("Shape of You",    "Ed Sheeran", 96)
now_playing("Someone Like You","Adele",       68)

print("---")

# A function that RETURNS a value
def most_played(playlist, play_counts):
    """Returns the song with the highest play count."""
    top_index = play_counts.index(max(play_counts))
    return playlist[top_index]


songs  = ["Levitating", "Peaches", "drivers license"]
plays  = [120, 85, 200]
winner = most_played(songs, plays)
print(f"Most played: {winner}")

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Each song has a real bpm and play_count — try passing one
#  to now_playing():
#    now_playing(SONGS[0]["title"], SONGS[0]["artist"], SONGS[0]["bpm"])
#
#  Or build lists to pass to most_played():
#    titles = [s["title"] for s in SONGS[:10]]
#    plays  = [s["play_count"] for s in SONGS[:10]]
#    print(most_played(titles, plays))

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Write a function called describe_song(title, artist, year)
#     that prints a one-line description of a song.
#     Call it at least three times with different songs —
#     your own, or from SONGS:
#       describe_song(SONGS[0]["title"], SONGS[0]["artist"], SONGS[0]["year"])
#
#  2. Write a function called count_by_artist(playlist, artist)
#     that takes a list of song dictionaries (each with
#     'title' and 'artist' keys) and RETURNS how many songs
#     are by that artist. Print the result.

# Start your code here 👇

# Task 1
def describe_song(title, artist, year):
    pass   # replace with your code


# Task 2
def count_by_artist(playlist, artist):
    pass   # replace with your code


# Sample playlist — 10 real songs with title and artist
sample_playlist = [
    {"title": s["title"], "artist": s["artist"]}
    for s in SONGS[:10]
]

# Call your functions here:


# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Write a function called shuffle(playlist) that returns
#    a randomly ordered copy of the list.
#    Hint:
#      import random
#      return random.sample(playlist, len(playlist))
#
#  - Write a function called search(playlist, keyword) that
#    returns all songs whose title contains the keyword
#    (case-insensitive).
#    Hint: use keyword.lower() and title.lower()
#
#  - Try calling shuffle() and search() on all SONGS.

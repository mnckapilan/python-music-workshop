# ============================================================
#  Exercise 1 — Variables & Strings 🎤
# ============================================================
#
#  WHAT IS A VARIABLE?
#  A variable is like a labelled box where you can store a
#  piece of information. You create one by writing a name,
#  an equals sign, and then a value.
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

song_title = "Blinding Lights"
artist     = "The Weeknd"
year       = 2019
duration   = 3.22   # minutes

print(song_title)
print(artist)
print(year)

# f-strings let you slot variables straight into text.
# Put an f before the quote, then use {} around variable names.

print(f"Now Playing: {song_title} by {artist} ({year})")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Replace the values below with details of YOUR favourite
#     song — type them in directly.
#  2. Add a variable called `duration` for the song length
#     in minutes (e.g. 3.45).
#  3. Use an f-string to print:
#     Now Playing: <title> by <artist> | Released: <year> | Duration: <duration> mins

# Start your code here 👇

my_song_title = "YOUR SONG HERE"
my_artist     = "YOUR ARTIST HERE"
my_year       = 0000
my_duration   = 0.00

# Print your f-string below:


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Print a song to see everything stored about it:
# print(SONGS[0])     # first song
# print(SONGS[5])     # change the number to pick a different one
# print(SONGS[100])

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add a variable called `genre` (e.g. "Pop", "Grime", "R&B")
#    and print a second line:  Genre: <genre>
#  - Try printing the artist name in ALL CAPS:
# print(my_artist.upper())
#  - Loop through the first 10 songs in SONGS and print each one:
# for s in SONGS[:10]:
#     print(s)   # you'll learn how to pick out individual fields in Exercise 5

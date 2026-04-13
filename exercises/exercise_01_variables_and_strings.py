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
duration   = 202   # seconds

print(song_title)
print(artist)
print(year)

# f-strings let you slot variables straight into text.
# Put an f before the quote, then use {} around variable names.

print(f"Now Playing: {song_title} by {artist} | Released: {year} | Duration: {duration}s")

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Replace the values below with details of YOUR favourite
#     song — type them in directly.
#  2. Add a variable called `duration` for the song length
#     in seconds (e.g. 214).
#  3. Use an f-string to print:
#     Now Playing: <title> by <artist> | Released: <year> | Duration: <duration>s

# Start your code here 👇

my_song_title = "Heat Waves"
my_artist     = "Glass Animals"
my_year       = 2020
my_duration   = 234

# Print your f-string below:
print(f"Now Playing: {my_song_title} by {my_artist} | Released: {my_year} | Duration: {my_duration}s")

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use
#
#  Print a song to see everything stored about it:
# print(song_library[0])     # first song
# print(song_library[5])     # change the number to pick a different one
# print(song_library[100])

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add a variable called `genre` (e.g. "Pop", "Grime", "R&B")
#    and print a second line:  Genre: <genre>
my_genre = "Indie Pop"
print(f"Genre: {my_genre}")

#  - Try printing the artist name in ALL CAPS:
print(my_artist.upper())

#  - Loop through the first 10 songs in song_library and print each one:
for s in song_library[:10]:
    print(s)   # you'll learn how to pick out individual fields in Exercise 5

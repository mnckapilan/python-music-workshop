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
#  Try these to browse what's available:
#    print(SONGS[0])                  # see one song's full details
#    print(SONGS[0]["title"])         # just the title
#    print(SONGS[0]["artist"])        # just the artist
#    print(SONGS[0]["year"])          # release year
#    print(SONGS[0]["duration"])      # length in minutes
#
#  Change the number to pick a different song (e.g. SONGS[5], SONGS[100]).
#  Or grab a song to use in your task above:
#    my_song = SONGS[0]   # then use my_song["title"], my_song["artist"] etc.

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Add a variable called `genre` (e.g. "Pop", "Grime", "R&B")
#    and print a second line:  Genre: <genre>
#  - Try printing the artist name in ALL CAPS:
#    print(my_artist.upper())
#  - Loop through the first 10 songs in SONGS and print each title:
#    for s in SONGS[:10]:
#        print(s["title"])

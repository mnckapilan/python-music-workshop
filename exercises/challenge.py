# ============================================================
#  THE BIG CHALLENGE — Song Length Stats 🎵
# ============================================================
#
#  Who makes the longest songs? Who keeps it short?
#
#  Work through the four tasks below to find out.
#  At the end, pretty-print your results and check them
#  against the answer at the bottom of the file.
#
# ============================================================

from music_data import SONGS   # 9,000+ real songs

# Each song is a dictionary with these fields:
#   title, artist, album, year, genre, bpm,
#   duration (whole seconds, e.g. 214), explicit, play_count
#
# Uncomment to remind yourself what one looks like:
# print(SONGS[0])

MIN_SONGS = 20   # only rank artists who have at least this many songs


# ------------------------------------------------------------
#  TASK 1 — Group song durations by artist
# ------------------------------------------------------------
#  Build a dictionary called artist_songs where:
#    - each KEY   is an artist name (a string)
#    - each VALUE is a LIST of that artist's song durations
#
#  When you're done, artist_songs["Ice Spice"] should be a
#  list of integers — one duration (in seconds) per song.
#
#  HOW TO APPROACH IT
#  Loop over SONGS. For each song you need to:
#    1. Check whether this artist already has a list in the dict.
#       If not, create an empty one first:
#
#         if song["artist"] not in artist_songs:
#             artist_songs[song["artist"]] = []
#
#    2. Append the song's duration to their list:
#
#         artist_songs[song["artist"]].append(song["duration"])

# Your code here 👇

artist_songs = {}


# ------------------------------------------------------------
#  TASK 2 — Compute each artist's average song duration
# ------------------------------------------------------------
#  Build a dictionary called artist_avg where:
#    - each KEY   is an artist name
#    - each VALUE is their average song duration in seconds
#                 (rounded to a whole number)
#
#  Only include artists with at least MIN_SONGS songs —
#  a sample of 2 or 3 songs isn't a fair picture of an artist.
#
#  HOW TO APPROACH IT
#  Loop over artist_songs.items() — each iteration gives you
#  an artist name and their list of durations:
#
#    for artist, durations in artist_songs.items():
#        ...
#
#  FILTERING — skip artists with too few songs:
#
#    if len(durations) < MIN_SONGS:
#        continue          # skip to the next artist
#
#  AVERAGING — Python has built-in functions for this:
#
#    total   = sum(durations)    # adds up all the values
#    count   = len(durations)    # how many values there are
#    average = round(total / count)   # round to a whole number

# Your code here 👇

artist_avg = {}


# ------------------------------------------------------------
#  TASK 3 — Sort, slice, and print
# ------------------------------------------------------------
#  Print two sections: the 5 shortest and 5 longest artists
#  by average song duration.
#
#  HOW TO APPROACH IT
#
#  SORTING — sorted() can sort a list of (key, value) pairs.
#  artist_avg.items() gives you exactly that.
#  You need to tell sorted() to sort by the value (the average),
#  not the key (the name). Do that with a helper function:
#
#    def get_avg(pair):
#        return pair[1]   # each pair is ("Artist Name", 185)
#
#    ranked = sorted(artist_avg.items(), key=get_avg)
#
#  SLICING — once sorted, grab the top and bottom 5:
#
#    shortest = ranked[:5]    # first 5 items = shortest
#    longest  = ranked[-5:]   # last  5 items = longest
#
#  PRINTING — loop over each group with enumerate() to get
#  a rank number, and look up the song count from artist_songs:
#
#    for rank, (artist, avg) in enumerate(shortest, start=1):
#        count = len(artist_songs[artist])
#        print(f"{rank}. {artist} — {avg}s ({count} songs)")

# Your code here 👇


# ============================================================
#  ✅ CHECK YOUR ANSWER
# ============================================================
#  Your output should contain these artists and durations
#  (exact print style is up to you):
#
#  Shortest average song:
#    1.  Ice Spice          125s   (30 songs)
#    2.  Tiger Backwood     140s   (23 songs)
#    3.  Doechii            144s   (48 songs)
#    4.  Summer Walker      152s   (70 songs)
#    5.  PinkPantheress     153s   (93 songs)
#
#  Longest average song:
#    1.  Dave Matthews Band  320s  (62 songs)
#    2.  Tame Impala         292s  (119 songs)
#    3.  Michael Jackson     271s  (107 songs)
#    4.  Adele               268s  (63 songs)
#    5.  Kendrick Lamar      264s  (78 songs)
# ============================================================


# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGES
# ------------------------------------------------------------
#
#  A) PRETTY DURATIONS
#     "125s" isn't very readable. Write a function called
#     format_seconds(seconds) that turns a number of seconds
#     into a string like "2m 05s".
#
#     Hints:
#       seconds // 60   → whole minutes  (e.g. 125 // 60 = 2)
#       seconds % 60    → leftover secs  (e.g. 125 % 60  = 5)
#
#     The % operator is called "modulo" — it gives the remainder
#     after division. 125 ÷ 60 = 2 remainder 5, so 125 % 60 = 5.
#
#     The :02d format code zero-pads to two digits ("05" not "5"):
#       return f"{mins}m {secs:02d}s"
#
#     Once it works, swap it into your print:
#       print(f"{rank}. {artist} — {format_seconds(avg)} ...")

def format_seconds(seconds):
    pass   # replace with your code

#  B) MOST MUSIC OVERALL
#     Add a third section: the 5 artists with the highest TOTAL
#     duration across all their songs. Hint: sum(artist_songs[a])
#     gives the total. You could use format_seconds() here too.
#
#  C) SONGS OVER 5 MINUTES
#     Which artists have the most songs longer than 300 seconds?
#     For each artist, count how many of their songs exceed 300s,
#     then print the top 5.

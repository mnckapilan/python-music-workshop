# ============================================================
#  Exercise 2 — Lists 📋
# ============================================================
#
#  WHAT IS A LIST?
#  A list is an ordered collection of items stored in a single
#  variable. Items sit inside square brackets [ ] separated by
#  commas. Lists are perfect for playlists!
#
#  NOTE: Python counts from 0, not 1.
#        playlist[0]  → first song
#        playlist[-1] → last song
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

playlist = ["Blinding Lights", "Levitating", "Stay", "Heat Waves", "Bad Habits"]

print(playlist)           # the whole list
print(playlist[0])        # first item (index 0)
print(playlist[-1])       # last item
print(len(playlist))      # number of songs

# Changing a list
playlist.append("As It Was")    # add to the END
playlist.remove("Stay")         # remove a specific song
playlist.insert(0, "Flowers")   # insert at position 0 (start)

print(playlist)

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list called `my_playlist` with at least 5 songs.
#     Type your own titles.
#  2. Print the entire playlist.
#  3. Print only the THIRD song in the list.
#  4. Use .append() to add a new song to the end.
#  5. Use .remove() to delete one song.
#  6. Print the total number of songs using len().

# Start your code here 👇

my_playlist = [
    # add your songs here
]



# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import SONGS   # 9,000+ real songs, ready to use
#
#  Browse the library:
# print(SONGS[0]["title"])                        # one title
# for s in SONGS[:10]:
#     print(s["title"], "–", s["artist"])        # first 10 songs
#
#  Build a playlist straight from the library:
# real_playlist = [s["title"] for s in SONGS[:5]]
# print(real_playlist)

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Find the song with the longest title.
#    Hint: use len() on each string inside a loop.
#  - Sort the playlist alphabetically: my_playlist.sort()
#  - Reverse the playlist: my_playlist.reverse()
#  - Try using all songs from SONGS as your playlist and
#    find the longest title across the whole library.

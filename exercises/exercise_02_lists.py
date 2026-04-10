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
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
from music_data import SONGS   # 40 real songs, ready to use
#
#  Try these to browse what's available:
#    print(SONGS[0]["title"])                        # one title
#    for s in SONGS:
#        print(s["title"], "–", s["artist"])        # all songs
#
#  Build a real playlist from the library:
#    real_playlist = [s["title"] for s in SONGS[:5]]
#    print(real_playlist)

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a list called `my_playlist` with at least 5 songs.
#     Type your own titles, or pull them from SONGS:
#       my_playlist = [s["title"] for s in SONGS[:5]]
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
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Find the song with the longest title.
#    Hint: use len() on each string inside a loop.
#  - Sort the playlist alphabetically: my_playlist.sort()
#  - Reverse the playlist: my_playlist.reverse()
#  - Try using all 40 songs from SONGS as your playlist and
#    find the longest title across the whole library.

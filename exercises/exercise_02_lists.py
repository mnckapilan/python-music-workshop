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
    "Heat Waves",
    "Blinding Lights",
    "Levitating",
    "As It Was",
    "Stay",
    "Bad Habit",
]

# Task 2 — print the entire playlist
print(my_playlist)

# Task 3 — print only the THIRD song (index 2)
print(my_playlist[2])

# Task 4 — add a new song to the end
my_playlist.append("Flowers")

# Task 5 — remove one song
my_playlist.remove("Stay")

# Task 6 — print total number of songs
print(len(my_playlist))

# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use
#
#  Browse the library:
# print(song_library[0]["title"])                        # one title
# for s in song_library[:10]:
#     print(s["title"], "–", s["artist"])        # first 10 songs
#
#  Build a playlist straight from the library:
# real_playlist = []
# for s in song_library[:5]:
#     real_playlist.append(s["title"])
# print(real_playlist)

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Find the song with the longest title.
longest = my_playlist[0]
for song in my_playlist:
    if len(song) > len(longest):
        longest = song
print(f"Longest title in my playlist: {longest}")

#  - Sort the playlist alphabetically:
my_playlist.sort()
print(my_playlist)

#  - Reverse the playlist:
my_playlist.reverse()
print(my_playlist)

#  - Find the longest title across the whole library:
longest_in_library = song_library[0]["title"]
for s in song_library:
    if len(s["title"]) > len(longest_in_library):
        longest_in_library = s["title"]
print(f"Longest title in library: {longest_in_library} ({len(longest_in_library)} characters)")

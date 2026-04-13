# ============================================================
#  Exercise 5 — Dictionaries 📀
# ============================================================
#
#  WHAT IS A DICTIONARY?
#  A dictionary stores data as key–value pairs — like a real
#  dictionary where every word (key) has a definition (value).
#
#  Create one with curly braces { }:
#    my_dict = {"key": "value", "another_key": 123}
#
#  Access a value with:  my_dict["key"]
#  Add a new pair with:  my_dict["new_key"] = value
#  Loop through pairs:   for k, v in my_dict.items():
#
# ============================================================

# --- EXAMPLE — run this and see what it prints --------------

# Real album — Future Nostalgia by Dua Lipa (2020, Warner Records)
album = {
    "title":  "Future Nostalgia",
    "artist": "Dua Lipa",
    "year":   2020,
    "tracks": {
        1: "Future Nostalgia",
        2: "Don't Start Now",
        3: "Cool",
        4: "Physical",
        5: "Levitating",
    }
}

print(album["title"])          # Future Nostalgia
print(album["tracks"][3])      # Cool

print("---")

# Loop through the tracks
for track_num, track_title in album["tracks"].items():
    print(f"Track {track_num}: {track_title}")

# Add a new key after creation
album["label"] = "Warner Records"
print(album["label"])

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a dictionary called `my_album` for your favourite
#     album. Give it these keys:
#       'title', 'artist', 'year', 'genre', 'tracks'
#     The 'tracks' value should itself be a dictionary
#     mapping track numbers (integers) to song titles.
#
#  2. Print the album title and artist on one line using
#     an f-string.
#
#  3. Loop through the tracks and print a numbered listing.
#
#  4. Add a new track to the tracks dictionary after you've
#     created it (pick the next track number).

# Start your code here 👇

my_album = {
    "title":  "YOUR ALBUM TITLE",
    "artist": "YOUR ARTIST",
    "year":   0000,
    "genre":  "YOUR GENRE",
    "tracks": {
        1: "First Song",
        # add more tracks...
    }
}

# Print title and artist:


# Print track listing:


# Add a new track:


# ------------------------------------------------------------
#  🔍 EXPLORE THE REAL MUSIC LIBRARY (optional)
# ------------------------------------------------------------
#  Browse the full library visually: tinyurl.com/7tdxxp57
#
from music_data import song_library   # 9,000+ real songs, ready to use
#
#  Each song is already a dictionary — print one to see all its keys:
# print(song_library[0])
#
#  Access individual fields:
# print(song_library[0]["title"])    # title
# print(song_library[0]["album"])    # album name
# print(song_library[0]["artist"])   # artist
# print(song_library[0]["year"])     # release year
# print(song_library[0]["genre"])    # genre

# ------------------------------------------------------------
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Pick any song from song_library and print all its key–value pairs
#    using a for loop:
# for key, value in song_library[0].items():
#     print(f"{key}: {value}")
#
#  - Loop through the first 20 songs in song_library and print each
#    one's title and genre on one line using an f-string.
#
#  - Find all songs in song_library from a specific year (e.g. 2020)
#    and print how many there are:
# count = 0
# for s in song_library:
#     if s["year"] == 2020:
#         count += 1
# print(f"Songs from 2020: {count}")

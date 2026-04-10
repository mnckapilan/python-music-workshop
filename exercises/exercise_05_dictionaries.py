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

album = {
    "title":  "After Hours",
    "artist": "The Weeknd",
    "year":   2020,
    "tracks": {
        1: "Alone Again",
        2: "Too Late",
        3: "Hardest to Love",
        4: "Scared to Live",
        5: "Snowchild",
    }
}

print(album["title"])          # After Hours
print(album["tracks"][3])      # Hardest to Love

print("---")

# Loop through the tracks
for track_num, track_title in album["tracks"].items():
    print(f"Track {track_num}: {track_title}")

# Add a new key after creation
album["label"] = "Republic Records"
print(album["label"])

# ------------------------------------------------------------
#  YOUR TASK
# ------------------------------------------------------------
#  1. Create a dictionary called `my_album` with these keys:
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
#  🎸 EXTENSION CHALLENGE
# ------------------------------------------------------------
#  - Print the total number of tracks using len().
#  - Create a list of 2–3 album dictionaries and loop through
#    all of them, printing each album's title and track count.

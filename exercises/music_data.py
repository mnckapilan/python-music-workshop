# ============================================================
#  🐉 HERE BE DRAGONS
# ============================================================
#  You don't need to open or edit this file for any exercise.
#
#  What it's doing:
#    This file reads the music library (songs.json) and makes
#    it available as a Python list called song_library. When your
#    exercise writes:
#
#        from music_data import song_library
#
#    ...Python runs this file behind the scenes to load the
#    data. It uses two modules you haven't seen yet:
#      json     — reads data stored in JSON format
#      pathlib  — finds the songs.json file on your computer
#
#  Curious? Try running it directly to see what loads:
#      python3 exercises/music_data.py
# ============================================================

import json
from pathlib import Path

_data_file = Path(__file__).parent.parent / "data" / "songs.json"
song_library: list[dict] = json.loads(_data_file.read_text(encoding='utf-8'))

if __name__ == "__main__":
    print(f"Loaded {len(song_library)} songs.")
    print("First song:", song_library[0])

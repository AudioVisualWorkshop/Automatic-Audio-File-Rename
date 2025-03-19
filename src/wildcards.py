# Metadata extraction functions

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# def extract_metadata(file_path):
#     try:
#         audio = MP3(file_path, ID3=EasyID3)
#         return {
#             "title": audio.get("title", ["Unknown"])[0],
#             "artist": audio.get("artist", ["Unknown"])[0],
#             "album": audio.get("album", ["Unknown"])[0],
#             "duration": int(audio.info.length)
#         }
#     except Exception as e:
#         print(f"Error extracting metadata: {e}")
#         return None


def get_selected_wildcards(wildcards_list):
    selected_indices = wildcards_list.curselection()
    selected_wildcards = [wildcards_list.get(i) for i in selected_indices]
    return selected_wildcards
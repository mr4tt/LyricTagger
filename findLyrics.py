from syncedlyrics import search
import taglib
import sys

toSearch = "REPLACE WITH SONG TITLE"
path = r"REPLACE WITH PATH TO SONG"

lyricName = "UNSYNCEDLYRICS" if path.endswith(".flac") else "LYRICS"

# uncomment if you want to automatically grab song title
# with taglib.File(path, save_on_exit=True) as song:
#     toSearch = song.tags["TITLE"][0]

if len(sys.argv) > 1 and sys.argv[1] == "delete":
    with taglib.File(path, save_on_exit=True) as song:
        if "UNSYNCEDLYRICS" in song.tags:
            del song.tags["UNSYNCEDLYRICS"]
            sys.exit(f"deleted lyrics from the UNSYNCEDLYRICS tag!")
        elif "LYRICS" in song.tags:
            del song.tags["LYRICS"]
            sys.exit(f"deleted lyrics from the LYRICS tag!")
        else:
            sys.exit(f"couldn't find any lyrics, sorry! no modifications made.")
        

lrc = search(
    search_term = toSearch,
    synced_only = True,
    save_path = None,
    providers = ["netease", "lrclib", "megalobiz", "musixmatch"]
)
# netease seems most accurate?

print(lrc)

isCorrect = input("Does this look right? Type y for yes. \n")

if isCorrect != "y" and isCorrect != "Y":
    sys.exit("exiting")

print("got it! adding lyrics!")

with taglib.File(path, save_on_exit=True) as song:
    if lrc:
        song.tags[lyricName] = [lrc]

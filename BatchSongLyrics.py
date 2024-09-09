from syncedlyrics import search
import taglib
import os
import re

# folder with the music files you want to append lyrics to
# ensure there is / at the end so you can open the file with taglib
path = r"PATH TO FOLDER WITH SONGS/" 

files = os.listdir(path)

# flac: UNSYNCEDLYRICS, ARTIST, TITLE
# mp3: LYRICS, ARTIST

for file_name in files:
    with taglib.File(path + file_name, save_on_exit=True) as song:
        # change lyricName depending on what you want the tag to be called
        lyricName = "UNSYNCEDLYRICS" if file_name.endswith(".flac") else "LYRICS"
        print(file_name)

        # uncomment if you don't want to overwrite previous lyrics
        # if lyricName in song.tags:
        #     continue
        
        toSearch = song.tags["TITLE"][0]

        if "ARTIST" in song.tags:
            toSearch = toSearch + " " + song.tags["ARTIST"][0]

        # remove special characters; may help with search
        try:
            toSearch = re.sub('[^a-zA-Z0-9 \n\\.\']', ' ', toSearch)
        except Exception as error:
            print("An exception occurred:", type(error).__name__)


        # changed synced_only to False if you only want nonsynced lyrics
        # or remove the option if you want both synced and nonsynced lyric options
        # to view all options, look at the syncedlyrics library
        lrc = search(
            search_term = toSearch,
            synced_only = True,
            save_path = None,
            providers = ["lrclib", "netease", "megalobiz"] # excluding musixmatch bc it times out after a lot of requests
        )
        
        # if lyric not found, write name to errors.txt
        # this does not catch songs with wrong lyrics! 
        if lrc:
            song.tags[lyricName] = [lrc]
        else:
            with open("errors.txt", "a") as file1:
                file1.write(song.tags["TITLE"][0] + "\n")

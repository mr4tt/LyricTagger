## What is LyricTagger?

LyricTagger lets you add synced or unsynced lyrics to your `.mp3` or `.flac` file.
This will allow you to see lyrics in some music playing apps, like Musicolet.

Accuracy isn't the best, but it beats doing it by hand. 

note: only tested with mp3 and flac files; however, [pytablib](https://pypi.org/project/pytaglib/) should support most file types.

## How to use?

1. `git clone https://github.com/mr4tt/LyricTagger`

2. `cd LyricTagger`

3. `pip install -r requirements.txt`

### If you want to tag the lyrics for one song:

1. Open `findLyrics.py` with your favorite text editor
2. change the `toSearch` variable to the song title you're searching for 
   - or uncomment lines 9-12 to automatically use the listed song title
3. change the `path` variable to the song file's location
4. run  `python findLyrics.py` to add lyrics!
    - if it is inaccurate, try changing the order of lyric providers (line 44)
5. or, run `python findLyrics.py delete` to delete the current lyrics on the file

### If you want to tag the lyrics for a lot of songs: 

1. Open `BatchSongLyrics.py` with your favorite text editor
2. change the `path` variable to the folder location containing all your songs
    - remember to put a "/" at the end! 
3. run `python BatchSongLyrics.py` to automatically add lyrics to all your songs!
    - title of songs without lyrics found will be in `errors.txt`


in the future, I might change it to check all providers for lyrics and compare them, then return the version with most matches
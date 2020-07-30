#!/usr/bin/env python3

import sys
import pyperclip

def generate_text(imdb_info, mediainfo, links, mega):
    if imdb_info['Response']=='False':
        sys.exit (imdb_info['Error'])
    else:
        out_text = f'''[imdb]{{
  "poster": "{imdb_info['Poster']}",
  "title": "{imdb_info['Title']}",
  "year": "{imdb_info['Year']}",
  "directors": "{imdb_info['Director']}",
  "stars": "{imdb_info['Actors']}",
  "ratings": "{imdb_info['imdbRating']}",
  "votes": "{imdb_info['imdbVotes']}",
  "runTime": "{imdb_info['Runtime']}",
  "summary": "{imdb_info['fullPlot']}",
  "shortSummary": "{imdb_info['Plot']}",
  "genre": "{imdb_info['Genre']}",
  "releaseDate": "{imdb_info['Released']}",
  "viewerRating": "{imdb_info['Rated']}",
  "language": "{imdb_info['Language']}",
  "imdbId": "{imdb_info['imdbID']}",
  "mediaType": "{imdb_info['Type']}"
}}[/imdb]


[mediainfo]{mediainfo}[/mediainfo]
[wimg=500]{links['screen-01.jpeg']}[/wimg] [wimg=500]{links['screen-02.jpeg']}[/wimg]

[wimg=500]{links['screen-03.jpeg']}[/wimg] [wimg=500]{links['screen-04.jpeg']}[/wimg]

[b][url={links['sample-001.mkv']}]Sample 1[/url][/b], [b][url={links['sample-002.mkv']}]Sample 2[/url][/b]

[color=#0080FF][b]Direct Download Links[/b][/color]:
[hide][b64]{mega}[/b64][/hide]
Enjoy!'''
        pyperclip.copy(out_text)
        with open('out.txt', 'w') as f:
            f.write(out_text)
        print ('Success!\nText has been copied to clipboard and saved to "out.txt"')

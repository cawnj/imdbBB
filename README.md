
# imdbBB

## You will need

 - api key for [omdb](https://www.omdbapi.com/apikey.aspx)
 - api key for [imgur](https://api.imgur.com/oauth2/addclient)
 - a [streamable](https://streamable.com/) account
 - [mediainfo](https://mediaarea.net/en/MediaInfo) installed and added to path
 - and [python3](https://www.python.org/downloads/release/latest)

## Setting Up and Usage

1. Clone this repo or download as zip
2. Run `pip install -r requirements.txt`
3. Input your api keys and streamble login into `config.json`
4. For basic usage, run with `run.bat`
5. Remember to select the option `Do not automatically parse URLs` at the bottom of your post

&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://i.imgur.com/tJGqqCf.png" width="300">

## Advanced Usage 

**Usage:** `imdbBB.py [-h] [--imdb IMDB] [--filename FILENAME] [--source SOURCE] [--mega MEGA] [--time TIME] [--config CONFIG]`

 -  `--imdb`
    - IMDB ID
 -  `--filename`
    - Video filename
 -  `--mega`
    - Mega link
 -  `--time`
    - Screenshot time offset in seconds (video sample timestamps are also based on this)
 -  `--config`
    - Specify config file

## Example

<img src="https://i.imgur.com/j29kORZ.png" width="500">

#!/usr/bin/env python3

import sys
import urllib
import json
import os

def load_config(config):
	print ('Loading config...')
	try:
		with open(config) as config_file:
			data = json.load(config_file)
		if all(value == "" for value in data.values()):
			sys.exit (f'Error! Please specify api keys and streamable login in "config.json" before running, exiting.')
		else:
			return data
	except FileNotFoundError:
		sys.exit (f'File "{config}" does not exist! Exiting.')

def get_imdb_info(imdb, config):
	print ('Retrieving info from imdb...')
	omdb_api_key = config['omdb_api_key']
	url = f'http://www.omdbapi.com/?apikey={omdb_api_key}&i={imdb}'
	url_fullplot = f'http://www.omdbapi.com/?apikey={omdb_api_key}&i={imdb}&plot=full'
	try:
		data = json.load(urllib.request.urlopen(url))
		data['fullPlot'] = (json.load(urllib.request.urlopen(url_fullplot)))['Plot']
		return data
	except urllib.error.URLError as e:
		sys.exit (f'{e.reason}! Exiting.')

def get_mediainfo(filename):
	print ('Retrieving mediainfo...')
	try:
		mediainfo = os.popen('mediainfo ' + filename).read()
		return mediainfo
	except:
		sys.exit ('Error retrieving mediainfo! Exiting.')

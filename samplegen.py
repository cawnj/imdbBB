#!/usr/bin/env python3

import sys
import os
import ffmpeg
from pymkv import MKVFile
from pyimgur import Imgur
from pystreamable import StreamableApi
import shutil

def create_tmp_dir():
	print ('Creating tmp dir...')
	current_working_dir = os.getcwd()
	path = os.path.join(current_working_dir, 'tmp')
	if not os.path.isdir(path):
		try:
			os.mkdir(path)
		except OSError:
			sys.exit ('Creation of tmp folder failed! Exiting.')
	return path

def cleanup(tmp_dir):
	shutil.rmtree(tmp_dir)

def create_screenshots(filename, time, tmp_dir):
	print ('Creating screenshots...')
	for i in range(1, 5):
		file = f'screen-0{i}.jpeg'
		out = os.path.join(tmp_dir, file)
		try:
			(
				ffmpeg
				.input(filename, ss=time*i)
				.output(out, vframes=1)
				.overwrite_output()
				.run(capture_stdout=True, capture_stderr=True)
			)
		except ffmpeg.Error as e:
			print(e.stderr.decode(), file=sys.stderr)
			sys.exit(1)

def create_sample_videos(filename, time, tmp_dir):
	print ('Creating sample videos...')
	mkv = MKVFile(filename)
	ts_1 = (time - 10, time + 20)
	ts_2 = (time*2 - 10, time*2 + 20)
	try:
		mkv.split_timestamp_parts([ts_1, ts_2])
	except TypeError:
		sys.exit ('Invalid timestamps! Exiting.')
	out = os.path.join(tmp_dir, 'sample.mkv')
	mkv.mux(out)
	clear()

def clear(): 
	if os.name == 'nt': 
		_ = os.system('cls') 
	else: 
		_ = os.system('clear')

def upload(config, tmp_dir):
	print ('Uploading screens and sample videos...')
	links = {}
	imgur_client_id = config['imgur_client_id']
	imgur = Imgur(imgur_client_id)
	for i in range(1, 5):
		file = f'screen-0{i}.jpeg'
		path = os.path.join(tmp_dir, file)
		try:
			links[file] = imgur.upload_image(path).link
		except:
			sys.exit ('Error uploading to Imgur! Exiting.')
	streamable_username = config['streamable_username']
	streamable_password = config['streamable_password']
	streamable = StreamableApi(streamable_username, streamable_password)
	for i in range(1, 3):
		file = f'sample-00{i}.mkv'
		path = os.path.join(tmp_dir, file)
		try:
			links[file] = f'https://streamable.com/{streamable.upload_video(path)["shortcode"]}'
		except:
			sys.exit ('Error uploading to Streamable! Exiting.')
	return links

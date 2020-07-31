#!/usr/bin/env python3

import argparse
from app import app

parser = argparse.ArgumentParser(description='Generate BBcode for uploading')
parser.add_argument(
	'--imdb', type=str, default=None, help='IMDB ID')
parser.add_argument(
	'--filename', type=str, default=None, help='Video filename')
parser.add_argument(
	'--mega', type=str, default=None, help='Mega link')
parser.add_argument(
	'--time', type=int, default=1200, help='Screenshot time offset in seconds')
parser.add_argument(
	'--config', type=str, default='config.json', help='Specify config file')

def main():
	args = vars(parser.parse_args())
	app(**args)

if __name__ == "__main__":
	main()

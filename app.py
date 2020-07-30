#!/usr/bin/env python3

import samplegen
import textgen
import infogen

def app(imdb, filename, mega, time, config):
    if imdb is None:
        imdb = input('IMDB ID:\n')
    if filename is None:
        filename = input('Video filename:\n')
    if mega is None:
        mega = input('Mega link:\n')
    samplegen.clear()
    config = infogen.load_config(config)
    tmp_dir = samplegen.create_tmp_dir()
    samplegen.create_sample_videos(filename, time, tmp_dir)
    samplegen.create_screenshots(filename, time, tmp_dir)
    links = samplegen.upload(config, tmp_dir)
    imdb_info = infogen.get_imdb_info(imdb, config)
    mediainfo = infogen.get_mediainfo(filename)
    textgen.generate_text(imdb_info, mediainfo, links, mega)
    samplegen.cleanup(tmp_dir)

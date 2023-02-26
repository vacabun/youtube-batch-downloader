#!/usr/bin/env python3
import os
import csv
import yt_dlp

ydl_opts = {}

current_directory = os.path.dirname(os.path.abspath(__file__))

save_path = current_directory + '/save'

with open('./download_list.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        title = row[0]
        url = row[1]
        print('save title: ' + row[0])
        print('url: ' + row[1])
        ydl_opts = {
            'format': 'mp4/b',
            'paths': {'home': save_path},
            'outtmpl': title + 'mp4'}
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        ydl.download([url])

import requests
import json
import pyodbc
from time import gmtime, strftime
import time
import dateutil.parser
import sys
import datetime


key = "enter account key"

# Pull data from ACHIM SOCIAL ADDRESSBOOK.



for row_achim_social in rows_achim_social:
    name = (row_achim_social[0])
    yt_handle = (row_achim_social[1])
    yt_id = (row_achim_social[2])
    unique_id = (row_achim_social[3])
    yt_posts_lastupdated = (row_achim_social[4])
    get_videos_by_channel = "https://www.googleapis.com/youtube/v3/search?key="+key+"&channelId="+yt_id+"&part=snippet,id&order=date&maxResults=50"
    dup_fatigue = 0
    request = requests.get(get_videos_by_channel).json()
    items = request['items']

    for videos in items:
        videos_videoid = videos['id']['videoId']
        video_link = 'https://www.youtube.com/watch?v=' + videos_videoid
        dup_check = open("dup_check_yt.txt", "r")
        dups = (dup_check.read())

        if dup_fatigue < 10:

            if videos_videoid in dups:
                print(video_link, "we have this one")
                dup_fatigue = dup_fatigue + 1
                pass

            if videos_videoid not in dups:
                videos_published_date = videos['snippet']['publishedAt']
                videos_channel_id = videos['snippet']['channelId']
                videos_liveBroadcastContent = videos['snippet']['liveBroadcastContent']

                if ('description') in videos:
                    videos_description = videos['snippet']['description']
                if ('description') not in videos:
                    videos_description = ''

                if ('title') in videos:
                    videos_title = videos['snippet']['title']
                if ('title') not in videos:
                    videos_title = ''

                if ('channelTitle') in videos:
                    videos_channel_title = videos['snippet']['channelTitle']
                if ('channelTitle') not in videos:
                    videos_channel_title = ''

                print(name, videos_published_date, videos_title, video_link)

                date_added = datetime.datetime.now()
                time.sleep(1)


                print(video_link, "success! it's in the database")
                print(dup_fatigue)

            if dup_fatigue == 10:
                print("post dups have totaled 10")
                break

# Update "Last Updated" in ACHIM SOCIAL ADDRESSBOOK.

    timestamp_date_now = datetime.datetime.now()
    # timestamp_date_now_ts = time.mktime(timestamp_date_now.timetuple())

    print("update date updated achim social addressbook")

    time.sleep(4)



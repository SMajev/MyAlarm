import datetime
import os
import time
import random 
import webbrowser

if not os.path.isfile('youtube_alarm_videos.txt'):
    print('Creating "youtube_alarm_videos.txt"...')
    with open('youtube_alarm_videos.txt', 'w') as alarm_file:
        alarm_file.write("https://www.youtube.com/watch?v=anM6uIZvx74")

def check_alarm_input(alarm_time):
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True

    if len(alarm_time) == 2:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True

    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
           alarm_time[1] < 60 and alarm_time[1] >= 0 and \
           alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True

    return False
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")

# Go to this file path and type: pyinstaller --windowed autodelete.py
import os
import time
import datetime
from os import listdir
from send2trash import send2trash
from pathlib import Path


# Convert delta-time from seconds to days
def seconds_to_days(seconds):
    return seconds/86400


# Set the path to apply the workflow
home = str(Path.home())
my_path = home + '/Downloads/'
# Change the current work path to avoid errors
os.chdir(my_path)
# Builnding a list of all filenames and folder names
files_or_folders = [f for f in listdir(my_path)]
# Sorting the list by the creation time
files_or_folders.sort(key=os.path.getctime, reverse=True)
# Getting the current time into the variable 'now' in timeseries format
now = datetime.datetime.now()

# Get the files/folders creation time, and remove olders
# Start by enumerating each item in the list
for index, filename in enumerate(files_or_folders, start=0):
    ctime_file = time.ctime(os.path.getctime(my_path + filename))
    ctime_file = datetime.datetime.strptime(ctime_file, "%a %b %d %H:%M:%S %Y")

    # get the time delta between the creation time and the current time
    difference_seconds = datetime.timedelta.total_seconds(now - ctime_file)
    difference_days = seconds_to_days(difference_seconds)

    # For debug (uncomment this to see what happens)
    # print(f'{index}. {filename}')

    if index >= 10:
        # for debug
        # print(f'{index}. {filename}')
        send2trash(my_path + files_or_folders[index])
    else:
        if difference_days > 1:
            # For debug
            # print(f'diff: {difference_days}. {filename}')
            send2trash(my_path + files_or_folders[index])


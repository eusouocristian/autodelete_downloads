# Go to this file path and type: pyinstaller --windowed autodelete.py
import os
from os import listdir
from send2trash import send2trash
from pathlib import Path

# Set the path to apply the workflow
home = str(Path.home())
my_path = home + '/Downloads/'
# Change the current work path to avoid errors
os.chdir(my_path)
# Buinding a list of all filenames and folder names
files_or_folders = [f for f in listdir(my_path)]
# Sorting the list by the creation time
files_or_folders.sort(key=os.path.getctime, reverse=True)
# Get the files/folders list and remove all
for index, filename in enumerate(files_or_folders, start=0):
    send2trash(my_path + files_or_folders[index])





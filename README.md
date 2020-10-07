# autodelete_downloads
Apps to automatically move files and folders from ~/Downloads/ to ~/.Trash;
- Designed to run on MacOS;

## Installation

Add the content of `/dist/` to your destiny folder and run the following packages:

## delete-all.py
-------------
Just get the path `home/Downloads` and move all files and folders to `~/.Trash`.

## autodelete.py
-------------
Get all files and folders in the `home/Downloads` path and delete all except the 10 most recent.
If the 10 files remaining have more than 1 day of creation time, then it must be moved to `~/.Trash` as well.

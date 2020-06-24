# autodelete_downloads
Apps to automatically move files and folders from ~/Downloads/ to ~/.Trash;
- Designed to run on unix based OS;

delete-all.py
-------------
Just get the path home/Downloads and move all files and folders to ~/.Trash.

autodelete.py
-------------
Get all files and folders in the home/Downloads path and delete all except the 10 most recent.
If the 10 files remaining have more than 1 day of creation time, then it must be moved to ~/.Trash as well.

/dist/
------------
Folder that contains the apps for distribuition, as the last version.



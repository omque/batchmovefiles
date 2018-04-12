#! /usr/bin/python3
#  moveMKV.py - Move a batch of .mkv files into one source 

import os, shutil

source_path = os.walk("/Users/Omair/MKVInput")
dest_path = "/Users/Omair/MKVOutput"


for folderName, subfolders, filename in source_path:
	for name in filename:
		if name.endswith(".mkv"):
			print("File found: " + name)
			#Define source folder name and join with file name. Send to Destination Path.
			shutil.move(os.path.join(folderName, name), dest_path)
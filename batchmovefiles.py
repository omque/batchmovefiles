#! /usr/bin/python3
#  moveMKV.py - Move a batch of .mkv files into one source 

import os, shutil

source_path = os.walk(input("What is the source path?" + "\n"))
dest_path = input("What is the destination path?" + "\n")
file_extension = input("What is the file extension? No quotes required." + "\n")

for folderName, subfolders, filename in source_path:
	for name in filename:
		if name.endswith(file_extension):
			print("File found: " + name)
			#Define source folder name and join with file name. Send to Destination Path.
			shutil.move(os.path.join(folderName, name), dest_path)
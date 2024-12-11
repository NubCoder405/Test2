#to move all the screenshots from screenshot folder from genshin game file to a seperate file.

import os 
import shutil as a

number = 0
source = r"C:\Program Files\HoYoPlay\games\Genshin Impact game\ScreenShot"
destination = r"D:\Genshin_Screenshots"

if not os.path.exists(destination):
    os.makedirs(destination)

files = os.listdir(source)

if not files:
    print("The folder is empty please take some Photos in game first: make some memories :D")
else:
    for file_name in files:
        full_file_name = os.path.join(source, file_name) # Or you can do "source" + "/" + "file_name"
        if file_name.endswith('.png'):
            if os.path.isfile(full_file_name):
                a.move(full_file_name, destination)
                number += 1
                print(f"File number {number} --> {file_name} has been moved")
            else:
                print(f"{full_file_name} is not a file or file not found. skipping")
        else:
            print(f"Not a png , so {file_name} is not moved")


    if number > 0:
        print(f"Total {number} PNG files have been moved to {destination}.")
    else:
        print("No PNG files were found to move.")
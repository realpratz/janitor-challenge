import os
import shutil

desktop_path=os.path.expanduser("~/Desktop/test_dump")
file_to_move=os.path.join(desktop_path,"photo.jpg")
target_dir=os.path.join(desktop_path,"Media")

os.makedirs(target_dir,exist_ok=True)

if os.path.exists(file_to_move):
    shutil.move(file_to_move,os.path.join(target_dir,"photo.jpg"))
    print(f"Successfully moved photo.jpg to {target_dir}")
else:
    print(f"File not found at: {file_to_move}")
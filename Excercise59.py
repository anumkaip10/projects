import os

folder = "clutter"   # your folder name

files = os.listdir(folder)

i = 1
for file in files:
    old_path = os.path.join(folder, file)
    
    if file.endswith(".png") or file.endswith(".jpg"):
        new_path = os.path.join(folder, f"image{i}.png")
        os.rename(old_path, new_path)
        i += 1
import os
def rename():
    a=1
    for i in os.listdir("data"):
        os.rename(f"data/{i}",f"data/{a}.txt")
        a+=1
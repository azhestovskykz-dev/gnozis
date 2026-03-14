import os
import glob
from PIL import Image

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
os.chdir(braindir)

user_media = glob.glob("media__*.jpg") + glob.glob("media__*.png")
user_media.sort(key=os.path.getmtime, reverse=True)

# Показаны будут предыдущие 15-40 изображений, чтобы найти "Ручку"
print("Older media files (15 to 40):")
for idx, f in enumerate(user_media[15:40], start=15):
    mtime = os.path.getmtime(f)
    print(f"[{idx}] {f} - TS: {mtime}")

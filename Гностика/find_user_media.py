import os
import glob
from PIL import Image

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
os.chdir(braindir)

# Находим все файлы media__* (это загруженные пользователем картинки)
user_media = glob.glob("media__*.jpg") + glob.glob("media__*.png")
user_media.sort(key=os.path.getmtime, reverse=True)

print(f"Total user media files found: {len(user_media)}")
print("Most recent 15 files:")

for idx, f in enumerate(user_media[:15]):
    mtime = os.path.getmtime(f)
    print(f"[{idx}] {f} - TS: {mtime}")

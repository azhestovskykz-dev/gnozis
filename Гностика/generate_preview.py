import os
import glob

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
os.chdir(braindir)

user_media = glob.glob("media__*.jpg") + glob.glob("media__*.png")
user_media.sort(key=os.path.getmtime, reverse=True)

html = "<html><body style='background:#333;'><div style='display:flex;flex-wrap:wrap;'>"
for i, f in enumerate(user_media):
    html += f"<div style='margin:10px;text-align:center;color:white;'><img src='{f}' style='height:200px;display:block;'>[{i}] {f}</div>"
html += "</div></body></html>"

with open("preview_all_media.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Created preview_all_media.html in brain dir.")

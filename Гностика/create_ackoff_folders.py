import json
import os

path = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Рассел_Акофф"
ideas_dir = os.path.join(path, "идеи")
os.makedirs(ideas_dir, exist_ok=True)

with open(os.path.join(path, "инфо.json"), encoding="utf-8") as f:
    info = json.load(f)

idx = 1
for g in info["группы"]:
    for c in g["категории"]:
        for idea in c["идеи"]:
            folder = f"{idx:03d}_{idea.replace(' ', '_')}"
            os.makedirs(os.path.join(ideas_dir, folder, "рисунки"), exist_ok=True)
            idx += 1

print("Все 50 папок для Акоффа успешно созданы!")

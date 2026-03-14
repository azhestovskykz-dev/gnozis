import os
import json

base_path = r"c:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Георгий_Гурджиев"
info_path = os.path.join(base_path, "инфо.json")

def idea_to_id(name, index):
    return f"{index:03d}_{name.replace(' ', '_')}"

with open(info_path, "r", encoding="utf-8") as f:
    data = json.load(f)

global_index = 1
for group in data["группы"]:
    for category in group["категории"]:
        for idea_name in category["идеи"]:
            id = idea_to_id(idea_name, global_index)
            folder_path = os.path.join(base_path, "идеи", id)
            pics_path = os.path.join(folder_path, "рисунки")
            
            os.makedirs(pics_path, exist_ok=True)
            print(f"Created: {folder_path}")
            global_index += 1

print("Done.")

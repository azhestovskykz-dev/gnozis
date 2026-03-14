import os
import json

base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

authors = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for a in authors:
    a_dir = os.path.join(base_dir, a)
    info_path = os.path.join(a_dir, "инфо.json")
    if os.path.exists(info_path):
        with open(info_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        idea_count = 0
        for g in data.get("группы", []):
            for c in g.get("категории", []):
                idea_count += len(c.get("идеи", []))
                
        print(f"[{a}]: {idea_count} идей")
    else:
        print(f"[{a}]: НЕТ info.json")

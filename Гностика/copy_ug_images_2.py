import shutil
import os

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
authordir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\УГ_Кришнамурти\идеи"

ideas = [
    ("006_КОНЕЦ_ПОИСКА", "ug_end_of_search_1773281849313.png"),
    ("007_МИФ_ОБ_УМЕ", "ug_mind_is_myth_1773281867113.png"),
    ("008_ВЛАСТЬ_БИОЛОГИИ", "ug_biology_primacy_1773281880591.png"),
    ("009_НЕПОСРЕДСТВЕННОЕ_ВОСПРИЯТИЕ", "ug_direct_perception_1773281894981.png"),
    ("010_МУЖЕСТВО_ОТЧАЯНИЯ", "ug_courage_despair_1773281910413.png")
]

for idea_folder, img_filename in ideas:
    target_dir = os.path.join(authordir, idea_folder, "рисунки")
    os.makedirs(target_dir, exist_ok=True)
    img_path = os.path.join(braindir, img_filename)
    if os.path.exists(img_path):
        shutil.copy2(img_path, os.path.join(target_dir, "1.jpg"))
    else:
        print(f"Warning: {img_path} not found.")

print("Added final 5 images to UG Krishnamurti.")

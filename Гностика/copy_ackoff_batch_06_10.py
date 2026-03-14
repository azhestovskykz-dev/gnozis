import os
import shutil

brain = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Рассел_Акофф\идеи"

ideas = [
    "006_ЦЕЛОЕ_БОЛЬШЕ_СУММЫ_ЧАСТЕЙ",
    "007_ИНФОРМАЦИЯ_ПРОТИВ_ПОНИМАНИЯ",
    "008_МУДРОСТЬ_КАК_ВЕРШИНА",
    "009_ДАННЫЕ_ЭТО_НЕ_ЗНАНИЯ",
    "010_ЗАКОН_ВЗАИМОСВЯЗИ"
]

images_cache = {}
for f in os.listdir(brain):
    if f.startswith("ackoff_") and f.endswith(".png"):
        prefix = f[:10]
        if prefix not in images_cache or f > images_cache[prefix]:
            images_cache[prefix] = f

for i, folder in enumerate(ideas):
    idx = i + 6
    prefix = f"ackoff_{idx:03d}"
    
    if prefix in images_cache:
        src = os.path.join(brain, images_cache[prefix])
        dest_dir = os.path.join(base, folder, "рисунки")
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, "1.jpg") # Сохраняем как 1.jpg
        shutil.copy2(src, dest)
        print(f"Скопировано: {folder}/1.jpg")
    else:
        print(f"ОШИБКА: Изображение не найдено для {folder} (prefix {prefix})")

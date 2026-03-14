import os
import shutil

brain = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\даннее\Рассел_Акофф\идеи"

# Исправление опечатки в пути (даннее -> данные)
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Рассел_Акофф\идеи"

ideas = [
    "036_ВНУТРЕННИЕ_РЫНКИ",
    "037_ВЕРХ_КОМАНДНОЙ_ЦЕПИ",
    "038_ВЫБОР_АЛЬТЕРНАТИВ",
    "039_МОРАЛЬ_И_ЭТИКА",
    "040_УСТАРЕВАНИЕ_ОПЫТА"
]

images_cache = {}
for f in os.listdir(brain):
    if f.startswith("ackoff_") and f.endswith(".png"):
        prefix = f[:10]
        if prefix not in images_cache or f > images_cache[prefix]:
            images_cache[prefix] = f

for i, folder in enumerate(ideas):
    idx = i + 36
    prefix = f"ackoff_{idx:03d}"
    
    # Найти нужную папку в base
    target_folder = None
    for item in os.listdir(base):
        if item.startswith(f"{idx:03d}"):
            target_folder = item
            break
            
    if target_folder and prefix in images_cache:
        src = os.path.join(brain, images_cache[prefix])
        dest_dir = os.path.join(base, target_folder, "рисунки")
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, "1.jpg") 
        shutil.copy2(src, dest)
        print(f"Скопировано: {target_folder}/1.jpg")
    else:
        print(f"ОШИБКА: Изображение не найдено для {prefix}")

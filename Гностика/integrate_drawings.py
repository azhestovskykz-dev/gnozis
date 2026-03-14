import os
import shutil
import random
import glob

base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"
drawings_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Рисунки!"

# Gathering all images from the drawings directory recursively
all_images = glob.glob(os.path.join(drawings_dir, "**", "*.jpg"), recursive=True) + \
             glob.glob(os.path.join(drawings_dir, "**", "*.png"), recursive=True) + \
             glob.glob(os.path.join(drawings_dir, "**", "*.jpeg"), recursive=True)

# Shuffle to pick random distinct images for empty ideas
random.shuffle(all_images)
img_index = 0

authors = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for a in authors:
    a_dir = os.path.join(base_dir, a)
    ideas_dir = os.path.join(a_dir, "идеи")
    if not os.path.exists(ideas_dir): continue
    
    ideas = [d for d in os.listdir(ideas_dir) if os.path.isdir(os.path.join(ideas_dir, d))]
    
    for idea in ideas:
        pic_dir = os.path.join(ideas_dir, idea, "рисунки")
        os.makedirs(pic_dir, exist_ok=True)
        img_path = os.path.join(pic_dir, "1.jpg")
        
        # Если картинки нет или она весит 0 байт (или её вообще нет)
        if not os.path.exists(img_path) or os.path.getsize(img_path) < 100:
            if img_index < len(all_images):
                src = all_images[img_index]
                try:
                    shutil.copy2(src, img_path)
                    print(f"[{a} -> {idea}] Добавлен рисунок: {os.path.basename(src)}")
                except Exception as e:
                    print(f"Ошибка копирования {src}: {e}")
                img_index += 1
            else:
                print("Закончились рисунки в папке пользователя!")

print(f"Всего интегрировано {img_index} новых изображений из папки !Рисунки!")

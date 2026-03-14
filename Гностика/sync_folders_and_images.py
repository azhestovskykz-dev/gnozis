import os
import json
import shutil

base_path = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

def normalize_name(name):
    return name.replace(" ", "_")

for author_folder in os.listdir(base_path):
    author_dir = os.path.join(base_path, author_folder)
    info_path = os.path.join(author_dir, "инфо.json")
    ideas_dir = os.path.join(author_dir, "идеи")
    
    if not os.path.isdir(author_dir) or not os.path.exists(info_path) or not os.path.exists(ideas_dir):
        continue
        
    print(f"Обработка автора: {author_folder}")
    
    try:
        with open(info_path, "r", encoding="utf-8") as f:
            info = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения {info_path}: {e}")
        continue
        
    global_index = 1
    
    for group in info.get("группы", []):
        for category in group.get("категории", []):
            for idea_name in category.get("идеи", []):
                norm_name = normalize_name(idea_name)
                expected_folder_name = f"{global_index:03d}_{norm_name}"
                expected_folder_path = os.path.join(ideas_dir, expected_folder_name)
                
                # Ищем текущую папку с таким же нормализованным именем (окончанием)
                existing_folder_path = None
                for d in os.listdir(ideas_dir):
                    if d.endswith(f"_{norm_name}"):
                        existing_folder_path = os.path.join(ideas_dir, d)
                        break
                
                if existing_folder_path:
                    # Переименовываем папку, если префикс не совпадает
                    if existing_folder_path != expected_folder_path:
                        print(f"  Переименование папки: {os.path.basename(existing_folder_path)} -> {expected_folder_name}")
                        os.rename(existing_folder_path, expected_folder_path)
                    
                    # Проверяем расширения изображений в папке "рисунки"
                    drawings_dir = os.path.join(expected_folder_path, "рисунки")
                    if os.path.exists(drawings_dir):
                        png_path = os.path.join(drawings_dir, "1.png")
                        jpg_path = os.path.join(drawings_dir, "1.jpg")
                        jpeg_path = os.path.join(drawings_dir, "1.jpeg")
                        
                        if os.path.exists(png_path) and not os.path.exists(jpg_path):
                            print(f"    Переименование 1.png -> 1.jpg в {expected_folder_name}")
                            os.rename(png_path, jpg_path)
                        elif os.path.exists(jpeg_path) and not os.path.exists(jpg_path):
                            print(f"    Переименование 1.jpeg -> 1.jpg в {expected_folder_name}")
                            os.rename(jpeg_path, jpg_path)
                
                global_index += 1

print("Готово!")

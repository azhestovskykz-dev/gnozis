import os
import json
import shutil
from typing import List, Dict

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\УГ_Кришнамурти"

# Последние 5 файлов, которые скинул пользователь:
files_to_sync = [
    # Индексы из последнего вызова GLOB, самые свежие
    ("media__1773281671139.png", "011_ОТКРЫТАЯ_СИСТЕМА", "ОШИБКА ЗАКРЫТОЙ СИСТЕМЫ", "Изоляция ведет к застою и гибели. Открытая система взаимодействует со средой и адаптируется."),
    ("media__1773281661085.png", "012_ЭНЕРГИЯ_СЛОВ", "ЭНЕРГИЯ СЛОВ И ИСЦЕЛЕНИЕ", "Слова обладают силой исцелять или разрушать. Позитивные слова поддерживают жизнь, негативные слова - разрушают и приносят боль."),
    ("media__1773281639412.jpg", "013_СИЛА_БЛАГОДАРНОСТИ", "СИЛА БЛАГОДАРНОСТИ", "Благодарность приумножает то, что мы имеем. Дневник благодарности - сердце (источник) - вибрация (притяжение) - изобилие (результат)."),
    ("media__1773281631523.png", "014_ИЛЛЮЗИЯ_Я", "ИЛЛЮЗИЯ Я И ПАМЯТЬ", "Иллюзия непрерывности и личности. Память — это лишь разрозненные фрагменты опыта. «Я» — это только попытка ума склеить несвязуемое и создать иллюзию контроля над временем."),
    ("media__1773281622492.png", "015_МЕНТАЛЬНЫЙ_ШУМ", "СФЕРА МЕНТАЛЬНОГО ШУМА", "Человек находится внутри плотной сферы мыслей. Эта сфера наполнена словами и культурными символами. Это не его личные мысли, это коллективный шум всего человечества. Мысли приходят извне как радиосигналы. Голова работает как антенна. Личности нет, есть только этот шум.")
]

info_path = os.path.join(base_dir, "инфо.json")
with open(info_path, "r", encoding="utf-8") as f:
    info = json.load(f)

for img_file, folder_name, title, text in files_to_sync:
    idea_dir = os.path.join(base_dir, "идеи", folder_name)
    pic_dir = os.path.join(idea_dir, "рисунки")
    os.makedirs(pic_dir, exist_ok=True)
    
    # 1. Запись описание.json
    desc = {
        "текст": text,
        "описание": {
            "стих": "",
            "притча": "",
            "метафора": ""
        }
    }
    with open(os.path.join(idea_dir, "описание.json"), "w", encoding="utf-8") as f:
        json.dump(desc, f, ensure_ascii=False, indent=2)
        
    # 2. Копирование картинки (рисунок 1.jpg)
    src_img = os.path.join(braindir, img_file)
    dst_img = os.path.join(pic_dir, "1.jpg")
    try:
        shutil.copy2(src_img, dst_img)
    except FileNotFoundError:
        print(f"File not found: {src_img}")

    # 3. Добавление в инфо.json
    # Предполагаем, что идеи лежат в info["группы"][0]["категории"][0]["идеи"]
    info["группы"][0]["категории"][0]["идеи"].append(title)

# Сохраняем обновленный инфо.json
with open(info_path, "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("Успешно добавлено 5 авторских картинок и идей!")

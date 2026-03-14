import os
import json
import re

base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

authors = [
    { "id": "Адамс_Джеймс", "name": "АДАМС ДЖЕЙМС", "category": "СИСТЕМНОЕ МЫШЛЕНИЕ", "role": "ИССЛЕДОВАТЕЛЬ ИНЖЕНЕРНОГО ТВОРЧЕСТВА" },
    { "id": "Вим_Хоф", "name": "ВИМ ХОФ", "category": "ТРАНСФОРМАЦИЯ", "role": "ЭКСТРЕМАЛЬНЫЙ АТЛЕТ И НОВАТОР" },
    { "id": "Дуглас_Хофштадтер", "name": "ДУГЛАС ХОФШТАДТЕР", "category": "НАУКА", "role": "ИССЛЕДОВАТЕЛЬ ИСКУССТВЕННОГО ИНТЕЛЛЕКТА И СОЗНАНИЯ" },
    { "id": "Павел_Флоренский", "name": "ПАВЕЛ ФЛОРЕНСКИЙ", "category": "ФИЛОСОФИЯ И СОЗНАНИЕ", "role": "ФИЛОСОФ И УЧЕНЫЙ" },
    { "id": "Рикардо_Семлер", "name": "РИКАРДО СЕМЛЕР", "category": "МЕНЕДЖМЕНТ", "role": "НОВАТОР КОРПОРАТИВНОГО УПРАВЛЕНИЯ" },
    { "id": "Роберт_Антон_Уилсон", "name": "РОБЕРТ АНТОН УИЛСОН", "category": "ПРОБУЖДЕНИЕ И ОСНОВЫ", "role": "ФИЛОСОФ И ПИСАТЕЛЬ" }
]

logic_file = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\js\логика.js"
with open(logic_file, "r", encoding="utf-8") as f:
    js_content = f.read()

for author in authors:
    # Создаем папки
    author_dir = os.path.join(base_dir, author["id"])
    os.makedirs(os.path.join(author_dir, "идеи"), exist_ok=True)
    
    # инфо.json
    info = {
        "имя": author["name"],
        "роль": author["role"],
        "фото": f"данные/{author['id']}/портрет.jpg",
        "группы": [
            {
                "название": "КЛЮЧЕВЫЕ ИДЕИ",
                "категории": [
                    {
                        "название": "ОСНОВНОЕ",
                        "идеи": []
                    }
                ]
            }
        ]
    }
    with open(os.path.join(author_dir, "инфо.json"), "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
        
    # профиль.json
    profile = {
        "биография": "Информация ожидается...",
        "достижения": [],
        "книги": []
    }
    with open(os.path.join(author_dir, "профиль.json"), "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    # Добавляем в логику.js, если еще нет
    id_str = f'{{ id: "{author["id"]}", имя: "{author["name"]}" }}'
    if author["id"] not in js_content:
        # Ищем категорию
        # Это простой способ найти массив авторов нужной категории
        cat_index = js_content.find(f'категория: "{author["category"]}"')
        if cat_index != -1:
            array_start = js_content.find('авторы: [', cat_index)
            array_end = js_content.find(']', array_start)
            existing_authors = js_content[array_start + 9 : array_end].strip()
            
            if existing_authors:
                new_authors = existing_authors + f',\n                {id_str}'
            else:
                new_authors = f'\n                {id_str}\n            '
                
            js_content = js_content[:array_start + 9] + new_authors + js_content[array_end:]

with open(logic_file, "w", encoding="utf-8") as f:
    f.write(js_content)

print("Все 6 авторов успешно добавлены в структуру и меню!")

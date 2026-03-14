import os
import json
import shutil

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

authors = {
    "Георгий_Гурджиев": {"name": "Георгий Гурджиев", "role": "ПРОБУЖДЕНИЕ", "img": "georges_gurdjieff_portrait_1773280526285.png"},
    "Нисаргадатта_Махарадж": {"name": "Нисаргадатта Махарадж", "role": "ПРОБУЖДЕНИЕ", "img": "nisargadatta_maharaj_portrait_1773280542807.png"},
    "Вернер_Эрхард": {"name": "Вернер Эрхард", "role": "ТРАНСФОРМАЦИЯ ЛИЧНОСТИ", "img": "werner_erhard_portrait_1773280557046.png"},
    "Рассел_Акофф": {"name": "Рассел Акофф", "role": "СИСТЕМНОЕ МЫШЛЕНИЕ", "img": "russell_ackoff_portrait_1773280570806.png"},
    "Питер_Сенге": {"name": "Питер Сенге", "role": "СИСТЕМНОЕ МЫШЛЕНИЕ", "img": "peter_senge_portrait_1773280596395.png"},
    "Донелла_Медоуз": {"name": "Донелла Медоуз", "role": "СИСТЕМНОЕ МЫШЛЕНИЕ", "img": "donella_meadows_portrait_1773280611069.png"},
    "Джон_ОКоннор": {"name": "Джон О'Коннор", "role": "СИСТЕМНОЕ МЫШЛЕНИЕ", "img": "john_oconnor_portrait_1773280625724.png"},
    "Питер_Друкер": {"name": "Питер Друкер", "role": "МЕНЕДЖМЕНТ", "img": "peter_drucker_portrait_1773280646047.png"},
    "Том_Питерс": {"name": "Том Питерс", "role": "МЕНЕДЖМЕНТ", "img": "tom_peters_portrait_1773280676434.png"},
    "Китами_Масао": {"name": "Китами Масао", "role": "МЕНЕДЖМЕНТ", "img": "masao_kitami_portrait_1773280692088.png"},
    "Дональд_Хоффман": {"name": "Дональд Хоффман", "role": "НАУКА", "img": "donald_hoffman_portrait_1773280708229.png"},
    "Мортимер_Адлер": {"name": "Мортимер Адлер", "role": "ОБУЧЕНИЕ", "img": "mortimer_adler_portrait_1773280723803.png"},
    "Джессика_Хэги": {"name": "Джессика Хэги", "role": "ПРОДУКТИВНОСТЬ", "img": "jessica_hagy_portrait_1773280743535.png"}
}

for folder, data in authors.items():
    author_dir = os.path.join(base_dir, folder)
    os.makedirs(author_dir, exist_ok=True)
    
    # 1. Сборка JSON
    info_path = os.path.join(author_dir, "инфо.json")
    
    # Редактируем или создаем JSON
    if os.path.exists(info_path):
        with open(info_path, 'r', encoding='utf-8') as f:
            try:
                info = json.load(f)
            except:
                info = {}
    else:
        info = {
            "имя": data["name"],
            "роль": data["role"],
            "группы": [{"название": "ИДЕИ В РАЗРАБОТКЕ", "категории": [{"название": "ВВЕДЕНИЕ", "идеи": []}]}]
        }
    
    # Убеждаемся, что фото прописано
    info["фото"] = f"данные/{folder}/портрет.jpg"
    
    with open(info_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
        
    # 2. Копирование фото
    img_src = os.path.join(braindir, data["img"])
    img_dest = os.path.join(author_dir, "портрет.jpg")
    
    if os.path.exists(img_src):
        shutil.copy2(img_src, img_dest)
        print(f"[{folder}] Скопировано фото и обновлен JSON!")
    else:
        print(f"[{folder}] Фото не найдено: {img_src}")

print("Скрипт завершен!")

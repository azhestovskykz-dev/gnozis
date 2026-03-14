import os
import json
import shutil

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Л_Секлитова_и_Л_Стрельникова" 

files_to_sync = [
    ("media__1773278887521.png", "006_ТВОРЧЕСКИЙ_КАНАЛ", "РУКА САМА ВЗЯЛА КАРАНДАШ", "Рука сама взяла карандаш.\\nИ слово вывела строка...\\nЭто процесс чистого проводничества..."),
    ("media__1773279635713.png", "007_ПОТОК_ИНФОРМАЦИИ", "АВТОМАТИЧЕСКОЕ ПИСЬМО", "Символ прямой передачи знаний. Когда внутренний диалог остановлен...")
]

# Создаем инфо.json если его нет
info_path = os.path.join(base_dir, "инфо.json")
if not os.path.exists(info_path):
    os.makedirs(base_dir, exist_ok=True)
    info = {
        "имя": "Л. СЕКЛИТОВА И Л. СТРЕЛЬНИКОВА",
        "группы": [
            {
                "название": "ВЫСШИЙ РАЗУМ И ЭНЕРГИИ",
                "категории": [
                    {
                        "название": "ОСНОВЫ МИРОЗДАНИЯ",
                        "идеи": []
                    }
                ]
            }
        ]
    }
    with open(info_path, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

with open(info_path, "r", encoding="utf-8") as f:
    info = json.load(f)

for img_file, folder_name, title, text in files_to_sync:
    idea_dir = os.path.join(base_dir, "идеи", folder_name)
    pic_dir = os.path.join(idea_dir, "рисунки")
    os.makedirs(pic_dir, exist_ok=True)
    
    desc = {
        "текст": text,
        "описание": {"стих": text.split("\\n")[0]}
    }
    with open(os.path.join(idea_dir, "описание.json"), "w", encoding="utf-8") as f:
        json.dump(desc, f, ensure_ascii=False, indent=2)
        
    src_img = os.path.join(braindir, img_file)
    dst_img = os.path.join(pic_dir, "1.jpg")
    try:
        shutil.copy2(src_img, dst_img)
    except Exception as e:
        print(f"Error copying {src_img}: {e}")

    # Добавляем идею, если ее там еще нет
    if title not in info["группы"][0]["категории"][0]["идеи"]:
        info["группы"][0]["категории"][0]["идеи"].append(title)

with open(info_path, "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("Успешно добавлено 2 рисунка с ручкой и стихами!")

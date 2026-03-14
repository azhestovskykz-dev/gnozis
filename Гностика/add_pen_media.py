import os
import json
import shutil

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Л_Секлитова_и_Л_Стрельникова" # Добавим к Секлитовой/Стрельниковой как творческий процесс, или создадим новую категорию.
# Лучше добавить в "Л_Секлитова_и_Л_Стрельникова" так как это стихи/ченнелинг.

# Картинка 32: media__1773278887521.png
# Картинка 20: media__1773279635713.png

files_to_sync = [
    ("media__1773278887521.png", "006_ТВОРЧЕСКИЙ_КАНАЛ", "РУКА САМА ВЗЯЛА КАРАНДАШ", "Рука сама взяла карандаш.\\nИ слово вывела строка...\\nЭто процесс чистого проводничества, когда мысль приходит не из ума, а диктуется свыше. Человек становится лишь инструментом, ручкой в руках более высоких иерархий сознания."),
    ("media__1773279635713.png", "007_ПОТОК_ИНФОРМАЦИИ", "АВТОМАТИЧЕСКОЕ ПИСЬМО", "Символ прямой передачи знаний. Когда внутренний диалог остановлен, рука способна записывать сложнейшие формулы и философские концепции без участия аналитического аппарата. Это прямое подключение к информационному полю.")
]

info_path = os.path.join(base_dir, "инфо.json")
with open(info_path, "r", encoding="utf-8") as f:
    info = json.load(f)

for img_file, folder_name, title, text in files_to_sync:
    idea_dir = os.path.join(base_dir, "идеи", folder_name)
    pic_dir = os.path.join(idea_dir, "рисунки")
    os.makedirs(pic_dir, exist_ok=True)
    
    desc = {
        "текст": text,
        "описание": {
            "стих": text.split("\\n")[0] + "\n" + (text.split("\\n")[1] if len(text.split("\\n"))>1 else "")
        }
    }
    with open(os.path.join(idea_dir, "описание.json"), "w", encoding="utf-8") as f:
        json.dump(desc, f, ensure_ascii=False, indent=2)
        
    src_img = os.path.join(braindir, img_file)
    dst_img = os.path.join(pic_dir, "1.jpg")
    try:
        shutil.copy2(src_img, dst_img)
    except FileNotFoundError:
        print(f"File not found: {src_img}")

    info["группы"][0]["категории"][0]["идеи"].append(title)

with open(info_path, "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("Успешно добавлено 2 рисунка с ручкой и стихами!")

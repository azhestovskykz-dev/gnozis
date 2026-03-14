import os
import shutil

brain = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Нисаргадатта_Махарадж\идеи"

mapping = {
    "001_ИЛЛЮЗИЯ_СОБСТВЕННОГО_Я": "maharaj_idea_001_1773316853323.png",
    "002_ПОИСК_ИСТИНЫ": "maharaj_idea_002_1773316871264.png",
    "003_ВСЕ_ЕСТЬ_БОГ": "maharaj_idea_003_1773316887786.png",
    "004_ВЕРНУТЬСЯ_К_Я_ЕСТЬ": "maharaj_idea_004_1773316908602.png",
    "005_РАЗУМ_И_ТЕЛО_НЕ_ВЫ": "maharaj_idea_005_1773316924460.png",
    "006_СТРАДАНИЕ_ОТ_ЖЕЛАНИЙ": "maharaj_idea_006_1773316956006.png",
    "007_ПРИНЯТИЕ_КАК_ЕСТЬ": "maharaj_idea_007_1773316969456.png",
    "008_ПОЗНАТЬ_ПОЗНАЮЩЕГО": "maharaj_idea_008_1773316988218.png",
    "009_ОТПУСКАНИЕ_КОНТРОЛЯ": "maharaj_idea_009_1773317003624.png",
    "010_СВОБОДА_ОТ_ПРОШЛОГО_И_БУДУЩЕГО": "maharaj_idea_010_1773317021220.png"
}

for folder, img in mapping.items():
    src = os.path.join(brain, img)
    dest_dir = os.path.join(base, folder, "рисунки")
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, "1.png")
    if os.path.exists(src):
        shutil.copy2(src, dest)
        print(f"Скопировано: {folder}/1.png")
    else:
        print(f"ОШИБКА: Изображение не найдено -> {img}")

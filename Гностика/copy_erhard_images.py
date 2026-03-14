import os
import shutil

brain = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Вернер_Эрхард\идеи"

mapping = {
    "015_ОБЕЩАНИЕ_КАК_ОБЯЗАТЕЛЬСТВО": "erhard_idea_015_1773317415770.png",
    "016_ДЕКЛАРАЦИЯ_СОЗДАЁТ_НОВЫЙ_МИР": "erhard_idea_016_1773317434780.png",
    "017_БРОШЕННОСТЬ_В_МИР": "erhard_idea_017_1773317450410.png",
    "018_ТЕМПОРАЛЬНОСТЬ_БЫТИЯ": "erhard_idea_018_1773317466009.png",
    "019_ЯЗЫК_ДОМ_БЫТИЯ": "erhard_idea_019_1773317482326.png",
    "020_АУТЕНТИЧНОЕ_ВЫСКАЗЫВАНИЕ": "erhard_idea_020_1773317504008.png",
    "021_ФАКТИЧНОСТЬ_КАК_ИСХОДНОЕ_УСЛОВИЕ": "erhard_idea_021_1773317519635.png",
    "022_ЗАБОТА_О_СОБСТВЕННОМ_СУЩЕСТВОВАНИИ": "erhard_idea_022_1773317538989.png",
    "023_МЫ_ЖИВЁМ_В_ЯЗЫКЕ": "erhard_idea_023_1773317554987.png",
    "024_РАЗГОВОР_КАК_КООРДИНАЦИЯ": "erhard_idea_024_1773317570660.png",
    "025_СЛУШАНИЕ_СОЗДАЁТ_ГОВОРЯЩЕГО": "erhard_idea_025_1773317592755.png",
    "026_РАЗРЫВ_В_КОММУНИКАЦИИ_КАК_НОРМА": "erhard_idea_026_1773317608457.png",
    "027_КОНТЕКСТ_СЛУШАНИЯ_ОПРЕДЕЛЯЕТ_СМЫСЛ": "erhard_idea_027_1773317626354.png",
    "028_ИНТЕРПРЕТАЦИЯ_ФИЛЬТРУЕТ_СЛОВА": "erhard_idea_028_1773317640896.png",
    "029_ЗАПРОС_КАК_АКТ_ВОЗМОЖНОСТИ": "erhard_idea_029_1773317660628.png",
    "030_ПРОСТРАНСТВО_МЕЖДУ_СЛОВАМИ": "erhard_idea_030_1773317676945.png"
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

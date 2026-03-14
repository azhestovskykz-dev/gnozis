import os
import json
import urllib.request
import re
import shutil
import time
from urllib.error import URLError

base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"
authors_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

def search_wikipedia_image(lang, title):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(title)}"
    headers = {"User-Agent": "BotGnostica/1.0 (contact@gnostica.com)"}
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req).read()
        data = json.loads(response)
        pages = data.get('query', {}).get('pages', {})
        for page_id, page_data in pages.items():
            if 'original' in page_data:
                return page_data['original']['source']
    except Exception as e:
        pass
    return None

wiki_mapping = {
    "Вим_Хоф": ("ru", "Хоф,_Вим"),
    "Нисаргадатта_Махарадж": ("ru", "Нисаргадатта_Махарадж"),
    "Питер_Сенге": ("ru", "Сенге,_Питер"),
    "Рассел_Акофф": ("ru", "Акофф,_Рассел_Линкольн"),
    "Роберт_Антон_Уилсон": ("ru", "Уилсон,_Роберт_Антон"),
    "Рикардо_Семлер": ("ru", "Семлер,_Рикардо")
}

for author_dir in wiki_mapping:
    if author_dir in authors_dirs:
        a_path = os.path.join(base_dir, author_dir)
        img_path = os.path.join(a_path, "портрет.jpg")
        
        lang, title = wiki_mapping[author_dir]
        img_url = search_wikipedia_image(lang, title)
        
        if img_url:
            try:
                time.sleep(1) # delay to avoid 429
                req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
                print(f"[{author_dir}] Успешно загружено.")
            except Exception as e:
                print(f"[{author_dir}] Ошибка: {e}")

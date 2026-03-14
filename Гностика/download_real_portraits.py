import os
import json
import urllib.request
from urllib.error import URLError
import re
from PIL import Image

try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system("pip install beautifulsoup4")
    from bs4 import BeautifulSoup

base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

# Собираем всех авторов из папок
authors_dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

def search_image_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # In DDG html version, images are often linked in a-tags with class 'image_url' or similar, 
        # but let's just find the first external image link or use Wikipedia API as fallback.
    except Exception as e:
        pass
    return None

def search_wikipedia_image(lang, title):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles={urllib.parse.quote(title)}"
    headers = {"User-Agent": "GnosticaBot/1.0"}
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req).read()
        data = json.loads(response)
        pages = data.get('query', {}).get('pages', {})
        for page_id, page_data in pages.items():
            if 'original' in page_data:
                return page_data['original']['source']
    except Exception as e:
        print(f"Wiki Error for {title}: {e}")
    return None

# Mapping some specific authors to Wiki titles
wiki_mapping = {
    "Георгий_Гурджиев": ("ru", "Гурджиев,_Георгий_Иванович"),
    "Вернер_Эрхард": ("ru", "Эрхард,_Вернер"),
    "Нисаргадатта_Махарадж": ("ru", "Нисаргадатта_Махарадж"),
    "УГ_Кришнамурти": ("ru", "Кришнамурти,_Уппалури_Гопала"),
    "Руперт_Спайра": ("en", "Rupert_Spira"),
    "Питер_Сенге": ("ru", "Сенге,_Питер"),
    "Рассел_Акофф": ("ru", "Акофф,_Рассел_Линкольн"),
    "Донелла_Медоуз": ("ru", "Медоуз,_Донелла"),
    "Питер_Друкер": ("ru", "Друкер,_Питер_Фердинанд"),
    "Том_Питерс": ("ru", "Питерс,_Том"),
    "Мортимер_Адлер": ("ru", "Адлер,_Мортимер"),
    "Дуглас_Хофштадтер": ("ru", "Хофштадтер,_Дуглас_Ричард"),
    "Павел_Флоренский": ("ru", "Флоренский,_Павел_Александрович"),
    "Вим_Хоф": ("ru", "Хоф,_Вим"),
    "Дональд_Хоффман": ("en", "Donald_Hoffman"),
    "Роберт_Антон_Уилсон": ("ru", "Уилсон,_Роберт_Антон"),
    "Рикардо_Семлер": ("ru", "Семлер,_Рикардо")
}

for author_dir in authors_dirs:
    a_path = os.path.join(base_dir, author_dir)
    img_path = os.path.join(a_path, "портрет.jpg")
    
    # We will try to download real image
    print(f"Обработка {author_dir}...")
    
    img_url = None
    if author_dir in wiki_mapping:
        lang, title = wiki_mapping[author_dir]
        img_url = search_wikipedia_image(lang, title)
        
    if img_url:
        print(f"  Найден URL: {img_url}")
        try:
            req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            print(f"  [+] Сохранено.")
        except Exception as e:
            import shutil # ensure imported
            print(f"  [-] Ошибка скачивания: {e}")
    else:
        print("  [?] Фото не найдено в автоматическом режиме.")

print("Процесс поиска реальных фото завершен!")

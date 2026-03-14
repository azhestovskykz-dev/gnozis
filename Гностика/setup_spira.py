import os
import json
import shutil

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

author_folder = "Руперт_Спайра"
author_dir = os.path.join(base_dir, author_folder)
os.makedirs(author_dir, exist_ok=True)

# Update menu in logic.js
logic_file = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\js\логика.js"
with open(logic_file, "r", encoding="utf-8") as f:
    js_content = f.read()

spira_str = '{ id: "Руперт_Спайра", имя: "РУПЕРТ СПАЙРА" }'
if "Руперт_Спайра" not in js_content:
    search_str = '{ id: "УГ_Кришнамурти", имя: "У.Г. КРИШНАМУРТИ" }'
    replace_str = search_str + f',\n                {spira_str}'
    js_content = js_content.replace(search_str, replace_str)
    
    with open(logic_file, "w", encoding="utf-8") as f:
        f.write(js_content)


ideas = [
    {
        "folder": "001_ОКЕАН_И_ВОЛНЫ",
        "title": "МЕТАФОРА ОКЕАНА И ВОЛН",
        "text": "Мы — волны на поверхности одного безграничного Океана Сознания. Волна может думать, что она отделена от других волн формой, скоростью или местом. Но всё это — лишь вода. Разделение существует только как временная оптическая иллюзия."
    },
    {
        "folder": "002_ПРИРОДА_ОПЫТА",
        "title": "ПРИРОДА ЛЮБОГО ОПЫТА — ЭТО ЗНАНИЕ",
        "text": "Всё, что вы когда-либо испытывали, происходило внутри вашего осознания. Нет никакого объективного мира «снаружи», который вы могли бы доказать без участия ума. Материя — это лишь уплотненная мысль, а мысль — вибрация единого Осознания."
    }
]

info = {
    "имя": "РУПЕРТ СПАЙРА",
    "роль": "УЧИТЕЛЬ НЕОДВАЙТЫ",
    "фото": "данные/Руперт_Спайра/портрет.jpg",
    "группы": [
        {
            "название": "ПРИРОДА СОЗНАНИЯ",
            "категории": [
                {
                    "название": "НЕДВОЙСТВЕННОСТЬ",
                    "идеи": [idea["title"] for idea in ideas]
                }
            ]
        }
    ]
}

with open(os.path.join(author_dir, "инфо.json"), "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

profile = {
    "биография": "Руперт Спайра — современный учитель философии недвойственности (Адвайта-веданты) и художник-керамист. Его подход отличается невероятной ясностью, логичностью и отсутствием мистицизма. Он исследует природу реальности не через слепую веру, а через прямой анализ собственного опыта (Direct Path).",
    "достижения": [
        "Популяризация «Прямого пути» (Direct Path) на Западе.",
        "Синтез восточной недвойственности и западного рационального опыта.",
        "Демистификация духовных состояний и медитации."
    ],
    "книги": []
}

with open(os.path.join(author_dir, "профиль.json"), "w", encoding="utf-8") as f:
    json.dump(profile, f, ensure_ascii=False, indent=2)

for idx, idea in enumerate(ideas):
    idea_dir = os.path.join(author_dir, "идеи", idea["folder"])
    pic_dir = os.path.join(idea_dir, "рисунки")
    os.makedirs(pic_dir, exist_ok=True)
    
    desc = {"текст": idea["text"]}
    with open(os.path.join(idea_dir, "описание.json"), "w", encoding="utf-8") as f:
        json.dump(desc, f, ensure_ascii=False, indent=2)

# Копируем портрет
shutil.copy2(os.path.join(braindir, "rupert_spira_portrait_1773283272934.png"), os.path.join(author_dir, "портрет.jpg"))

print("Руперт Спайра добавлен.")

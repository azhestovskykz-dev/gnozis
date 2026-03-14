import os
import json
import shutil

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base_dir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные"

author_folder = "Стрельникова_Секлитова"
author_dir = os.path.join(base_dir, author_folder)
os.makedirs(author_dir, exist_ok=True)

# 1. Portrait
portrait_src = os.path.join(braindir, "strelnikova_portrait_1773281138392.png")
portrait_dest = os.path.join(author_dir, "портрет.jpg")
if os.path.exists(portrait_src):
    shutil.copy2(portrait_src, portrait_dest)

# 2. Ideas list
ideas = [
    {
        "folder": "001_МАТРИЦА_ДУШИ",
        "title": "МАТРИЦА ДУШИ: НАКОПЛЕНИЕ КАЧЕСТВ",
        "img": "strelnikova_soul_matrix_1773281154439.png",
        "text": "Душа представляет собой матрицу — вечную геометрически выверенную конструкцию. Каждое действие, мысль или чувство, проживаемые в текущей физической жизни, преобразуются в энергию определенного качества. Формируясь через хаос временного земного опыта, эти энергии втягиваются в ячейки матрицы и кристаллизуются в вечные непреходящие качества (терпение, любовь, разумность). Постепенное заполнение этих ячеек формирует индивидуальность души и её фундамент для дальнейшей эволюции."
    },
    {
        "folder": "002_ЗАКОН_СОХРАНЕНИЯ_ЭНЕРГИИ",
        "title": "ЗАКОН СОХРАНЕНИЯ ЭНЕРГИИ ДУШИ",
        "img": "strelnikova_energy_conservation_1773281166806.png",
        "text": "Ни одна мысль, ни одно чувство, ни один поступок человека не исчезают бесследно. Подобно физическому закону сохранения энергии, любой жизненный опыт перетекает из хаотичной формы в структурированную. Проходя через «воронку» осознания, бурлящие эмоции и трудности земной жизни преобразуются в чистую жизненную энергию, которая навечно встраивается в структуру матрицы души. Этот закон гарантирует, что любое усилие человека имеет смысл и работает на вечность."
    },
    {
        "folder": "003_ЭНЕРГОПОТЕНЦИАЛ",
        "title": "ЭНЕРГОПОТЕНЦИАЛ: РОСТ МОЩНОСТИ",
        "img": "strelnikova_energy_potential", # update filename in the loop later
        "text": "Энергопотенциал — это показатель мощи души, её способность удерживать и производить энергию. Душа с низким потенциалом наполнена тёмными и тяжелыми энергиями, она не способна к созиданию. Набор знаний и правильного опыта переводит её на средний уровень, где начинается развитие. Высокий потенциал достигается накоплением светлых, упорядоченных энергий; такая душа обретает свободу творения, высокую осознанность и мощность, достаточную для влияния на реальность."
    },
    {
        "folder": "004_ЭНЕРГЕТИЧЕСКАЯ_МАТРИЦА",
        "title": "ЭНЕРГЕТИЧЕСКАЯ МАТРИЦА",
        "img": "strelnikova_energy_matrix",
        "text": "Помимо физического тела, человек обладает многомерной энергетической матрицей. Это сложная иерархическая структура из шестигранных и кубических ячеек. В процессе выбора душа заполняет их различными типами энергий: положительными (творчество, благо), отрицательными (разрушение, расчет) или нейтральными (высший разум). Базовая структура матрицы определяет, к какой иерархии будет принадлежать личность в своём космическом развитии."
    },
    {
        "folder": "005_МЕХАНИЗМ_СТРАДАНИЯ",
        "title": "МЕХАНИЗМ СТРАДАНИЯ (ОЧИСТКА)",
        "img": "strelnikova_suffering_mechanism",
        "text": "Страдание в земной жизни — это не наказание, а технический процесс энергетической очистки матрицы души. Когда душа накапливает слишком много мусора или низковибрационных, бракованных энергий, они образуют жёсткую корку. Боль и трудности выступают в роли жесткой «щетки», которая сдирает эту грязь через переживания. Этот болезненный, но необходимый процесс приводит к огненному освобождению истинной сути, позволяя душе вновь засиять и продолжить рост."
    }
]

# Create Info JSON
info = {
    "имя": "СЕКЛИТОВА И СТРЕЛЬНИКОВА",
    "роль": "ЭЗАТЕРИКА И КОСМОС",
    "фото": "данные/Стрельникова_Секлитова/портрет.jpg",
    "группы": [
        {
            "название": "СТРУКТУРА ДУШИ",
            "категории": [
                {
                    "название": "ЗАКОНЫ МИРОЗДАНИЯ",
                    "идеи": [idea["title"] for idea in ideas]
                }
            ]
        }
    ]
}

with open(os.path.join(author_dir, "инфо.json"), "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

# Find remaining images generated manually
os.chdir(braindir)
files = os.listdir(".")
energy_potential_img = next((f for f in files if f.startswith("strelnikova_energy_potential") and f.endswith(".png")), "")
energy_matrix_img = next((f for f in files if f.startswith("strelnikova_energy_matrix") and f.endswith(".png")), "")
suffering_mechanism_img = next((f for f in files if f.startswith("strelnikova_suffering_mechanism") and f.endswith(".png")), "")

# Update mapping
img_map = {
    "strelnikova_energy_potential": energy_potential_img,
    "strelnikova_energy_matrix": energy_matrix_img,
    "strelnikova_suffering_mechanism": suffering_mechanism_img
}

# Create ideas
for idea in ideas:
    idea_dir = os.path.join(author_dir, "идеи", idea["folder"])
    pic_dir = os.path.join(idea_dir, "рисунки")
    os.makedirs(pic_dir, exist_ok=True)
    
    # Text
    desc = {"текст": idea["text"]}
    with open(os.path.join(idea_dir, "описание.json"), "w", encoding="utf-8") as f:
        json.dump(desc, f, ensure_ascii=False, indent=2)
        
    # Image
    img_name = idea["img"]
    if img_name in img_map:
        img_name = img_map[img_name]
        
    img_src = os.path.join(braindir, img_name)
    img_dest = os.path.join(pic_dir, "1.jpg")
    
    if os.path.exists(img_src):
        shutil.copy2(img_src, img_dest)

print("Стрельникова и Секлитова добавлены успешно!")

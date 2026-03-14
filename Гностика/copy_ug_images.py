import shutil
import os

braindir = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
authordir = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\УГ_Кришнамурти"

shutil.copy2(os.path.join(braindir, "ug_krishnamurti_portrait_main_1773281731406.png"), os.path.join(authordir, "портрет.jpg"))
shutil.copy2(os.path.join(braindir, "ug_krishnamurti_photo2_1773281743755.png"), os.path.join(authordir, "фото1.jpg"))

os.makedirs(os.path.join(authordir, "книги"), exist_ok=True)
shutil.copy2(os.path.join(braindir, "book_mind_myth_1773281757639.png"), os.path.join(authordir, "книги", "mind_myth.jpg"))
shutil.copy2(os.path.join(braindir, "book_courage_1773281770573.png"), os.path.join(authordir, "книги", "courage.jpg"))

print("Портрет и обложки книг скопированы.")

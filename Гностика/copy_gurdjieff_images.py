import os
import shutil

brain = r"C:\Users\azhes_82zq8ny\.gemini\antigravity\brain\aece6c06-a16e-4fad-a93a-bb2f36694970"
base = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Георгий_Гурджиев\идеи"

mapping = {
    "001_ОДНОГЛАЗЫЕ_В_МИРЕ_ДОРОГ": "gurdjieff_one_eyed_road_1773278347917.png",
    "002_СОН_ЭТО_НЕ_ПАУЗА": "gurdjieff_sleep_update_1773278364403.png",
    "003_СТРАДАНИЕ_ЭТО_СОПРОТИВЛЕНИЕ": "gurdjieff_suffering_resistance_1773278378559.png",
    "004_КОНТРОЛЬ_ИЛИ_ПРИСУТСТВИЕ": "gurdjieff_control_presence_1773278393970.png",
    "005_ДВИГАЕТСЯ_ВАШ_УМ": "zen_monks_flag_1773278407215.png",
    "006_МАШИННОСТЬ_ЧЕЛОВЕКА": "gurdjieff_machine_man_1773316629268.png",
    "007_МНОЖЕСТВЕННОСТЬ_Я": "gurdjieff_multiple_i_1773316647929.png",
    "008_НЕОБХОДИМОСТЬ_УСИЛИЯ": "gurdjieff_effort_1773316664883.png",
    "009_ПУТЬ_В_МИРУ": "gurdjieff_fourth_way_1773316683403.png",
    "010_ЗАКОН_ТРЕХ_И_СЕМИ": "gurdjieff_law_of_three_1773316700954.png"
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

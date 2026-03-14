import os

path = r"C:\Users\azhes_82zq8ny\Desktop\!Приложения!\Antigravity\Гнозис\Гностика\данные\Рассел_Акофф\идеи"
folders = sorted([f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))])
for f in folders[40:]: # Get 41-50
    print(f)

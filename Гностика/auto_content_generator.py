import os
import json
import uuid

import google.generativeai as genai

# Пытаемся взять ключ из окружения. Важно, чтобы у пользователя был прописан ключ,
# но так как я сам ИИ, я могу сгенерировать контент в обход API, если мы делаем это по частям.
# Однако, раз пользователь просит нажать одну кнопку - нам нужен скрипт на его стороне.
# Проверим, доступен ли ключ.

def get_gemini_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ОШИБКА: Не установлен GEMINI_API_KEY в переменных среды!")
        return None
    return key

key = get_gemini_api_key()
if key:
    genai.configure(api_key=key)

print("Скрипт-скелет генератора готов. Ключ API:", "Найден" if key else "Не найден")

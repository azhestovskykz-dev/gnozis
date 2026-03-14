import PyPDF2
import os

pdf_path = r"c:\Users\azhes_82zq8ny\Desktop\!Книги!\Георгий Гурджиев\Gurdjiev_G._Klassikamyisli._Kritika_Jizni_Cheloveka_R.a6.pdf"

def extract_titles(path):
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            # Извлечем первые 20 страниц для анализа содержания и стиля
            content = ""
            for i in range(min(20, len(reader.pages))):
                content += reader.pages[i].extract_text() + "\n"
            return content
    except Exception as e:
        return str(e)

if os.path.exists(pdf_path):
    print(extract_titles(pdf_path))
else:
    print("File not found")

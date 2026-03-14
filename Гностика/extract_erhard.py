import pypdf
import os

pdf_path = r"c:\Users\azhes_82zq8ny\Desktop\!Книги!\Вернер Эрхард\Speaking_Being_Werner_Erhard,_Martin_Heidegger,_and_a_New_Possibility.pdf"
output_path = "erhard_text.txt"

def extract_text(path, max_pages=50):
    try:
        with open(path, "rb") as f:
            reader = pypdf.PdfReader(f)
            num_pages = len(reader.pages)
            text = f"Total pages: {num_pages}\n\n"
            for i in range(min(num_pages, max_pages)):
                text += f"--- Page {i+1} ---\n"
                text += reader.pages[i].extract_text() + "\n"
            return text
    except Exception as e:
        return str(e)

content = extract_text(pdf_path)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Extraction completed. Saved to {output_path}")

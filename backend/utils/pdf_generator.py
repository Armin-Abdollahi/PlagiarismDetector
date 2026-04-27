from fpdf import FPDF
import os

def generate_pdf(text, output_path):
    pdf = FPDF()
    pdf.add_page()

    # اضافه کردن فونت فارسی
    font_path = os.path.join("fonts", "Vazirmatn-Regular.ttf")
    pdf.add_font("Vazir", "", font_path, uni=True)
    pdf.set_font("Vazir", size=12)

    pdf.multi_cell(0, 10, txt=text)

    pdf.output(output_path)
    return output_path

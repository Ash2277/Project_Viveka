import requests as rq
import PyPDF2
from fpdf import FPDF
filename = input(
    "enter the name of file to be translated(add .pdf to the end):")
file_path = filename
pdf = PyPDF2.PdfReader(file_path)
pdf_out = FPDF(orientation='P', unit='mm', format='A4')
pdf_out.add_page()
pdf_out.set_font("Arial", size=15)
a = (len(pdf.pages))
str = ""
for i in range(0, a):
    str += pdf.pages[i].extract_text()

# print(str)
result = " ".join(line.strip() for line in str.splitlines())
b = repr(result)

base_url = 'https://translate.terraprint.co/translate'

payload = {"q": b, "source": "en", "target": "fr"}
headers = {"Content-Type": "application/json"}
request = rq.post(base_url, json=payload, headers=headers)
data = request.json()
pdf_out.multi_cell(180, 10, txt=data["translatedText"], align='L')
pdf_out.output("created.pdf")
# print('The Response is:\n', data)

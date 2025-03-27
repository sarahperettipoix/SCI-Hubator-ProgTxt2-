#changer pour PyMuPDF ou PDFPlumber pour matcher SuperTextFiles
from PyPDF2 import PdfReader
from scihub import SciHub

sh = SciHub()
result = sh.download("https://dl.acm.org/doi/abs/10.1145/2858036.2858132", path="test5.pdf")
reader = PdfReader("test5.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

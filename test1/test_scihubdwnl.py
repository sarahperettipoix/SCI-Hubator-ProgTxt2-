from scidownl import scihub_download
import tempfile
import pdfplumber
from PyPDF2 import PdfReader
import time
with open("DOI_list_2.txt") as file:
    i = 0
    tempdir = tempfile.TemporaryDirectory()
    for line in file:
        i+=1
        paper = line
        paper_type = "doi"
        #proxies = {
        #    'http': 'socks5://127.0.0.1:7890'
        #}

        print(tempdir.name)
        out = f"{tempdir.name}/{i}"
        scihub_download(paper, paper_type=paper_type, out=out)
        reader = PdfReader(f"{out}.pdf")
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        print(text)
        with pdfplumber.open(f"{out}.pdf") as pdf:
            first_page = pdf.pages[0]
            print("*"*30)
            print(first_page.extract_text())
        print("-" * 50)
    tempdir.cleanup()
from pdfextract.extract import Extractor
emy = Extractor(pdf="cs.pdf")
extracted_html = emy.getHTML()
print(extracted_html)
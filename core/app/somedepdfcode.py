from depdf import DePDF
from depdf import DePage

# general
with DePDF.load('cs.pdf') as pdf:
    pdf_html = pdf.to_html.encode('utf-8')
    print(pdf_html)
    with open("Output.html", "wb") as html_file:
        html_file.write(pdf_html)


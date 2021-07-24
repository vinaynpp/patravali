import depdf

with open("Output.html", "wb") as html_file:
    html_file.write(depdf.convert_pdf_to_html(pdf_file_path="aisc.pdf").encode('utf-8'))

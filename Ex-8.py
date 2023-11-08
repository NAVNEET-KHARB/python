from PyPDF2 import PdfWriter
import os
input = [file for file in os.listdir() if file.endswith(".pdf")]
merger = PdfWriter()
for pdf in input:
    merger.append(pdf)
merger.write("Output.pdf")
merger.close()

import sys
import os
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    from pyPdf import PdfFileReader, PdfFileWriter

def pdf_cat(input_files, out_file_name):
    input_streams = []
    try:
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(open(out_file_name, 'wb'))
    finally:
        for f in input_streams:
            f.close()

if _name_ == '_main_':
    path=["CS %d.pdf"%i for i in range(1, 20) if os.path.exists("CS %d.pdf"%i)]
    pdf_cat(path, './all_lectures.pdf')
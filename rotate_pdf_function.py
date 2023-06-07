# Author: Maxwell Reilly
# Date: Nov 26, 2022


from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# Description: 
# I need a pythons script that can quickly and easily modify pdfs for a couple of my purposes.
# functionality:
# 1: Rotate pages in a given range 90 or 180 degrees.
# 2: Delete pages in a certain range.
# 3: Split pages in a certain range.

# url: https://realpython.com/creating-modifying-pdf/#rotating-pages
#def makePath(relative_path):
#    p = Path('.')
#    q = p / str(relative_path)
#    return q
def main(): 
    rotate("youre_a_mean_one_mister_grinch.pdf")

# This function is not quite there, but gonna take a break on it for now.

def rotate(filename):
    pdf_path = Path("./{}".format(filename))
    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    for n in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(n)
        if n < 1:
            page.rotateClockwise(90)
            pdf_writer.addPage(page)
        else:
            pdf_writer.addPage(page) 

    with Path("fixed_{}".format(filename)).open(mode="wb") as output_file:
        pdf_writer.write(output_file)


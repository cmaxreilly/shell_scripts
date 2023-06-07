# Author: Maxwell Reilly
# Date: Nov 26, 2022


from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

# Description: 
# I need a pythons script that can quickly and easily modify pdfs for a couple of my purposes.
# functionality:
# 1: Rotate pages in a given range 90 or 180 degrees 
# 2: Delete pages in a certain range.
# 3: Split pages in a certain range.

# url: https://realpython.com/creating-modifying-pdf/#rotating-pages
def main() 
    pdf_path = (
            Path.home()
            /"Documents"
            /"work_and_gigs"
            /"snoopy_the_musical"
            /"python_test"
            /"snoopy_conductor.pdf"
            )
    #pdf = PdfFileReader(str(pdf_path))

    #print(pdf.getNumPages())

    #print(pdf.documentInfo)

    #first_page = pdf.getPage(0)

    #print(first_page.extractText())

    pdf_reader = PdfFileReader(str(pdf_path))
    pdf_writer = PdfFileWriter()

    for n in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(n)
        if n % 2 != 0:
            page.rotateClockwise(270)
            pdf_writer.addPage(page)
        elif n % 2 == 0:
            page.rotateClockwise(90)
            pdf_writer.addPage(page)

    with Path("snoopy_conductor_rotated.pdf").open(mode="wb") as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    main()

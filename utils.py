import os
import PyPDF2


def rasterize(pdf_url):
    os.system("gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dTextAlphaBits=4 "
              + "-sOutputFile=\'images/paper-%00d.jpeg\' \"" + pdf_url+"\"")


def clean_images():
    os.system("rm images/*.jpeg")


def images_ocr_pdf():
    child_dir = os.getcwd() + "/images"
    os.chdir(child_dir)
    os.system(f"ls *.jpeg | tesseract -c textonly_pdf=1 - result pdf")
    os.system(f"mv result.pdf ../")
    parent_dir = os.path.dirname(os.getcwd())
    os.chdir(parent_dir)


def merge_pdf(input, ocr_output, sav_path):
    """
        Combine to pdf files and save the output
        input: original pdf path
        ocr_output: the output pdf of ocr function path
        save_path: save path
    """
    pdf1File = open(ocr_output, 'rb')
    pdf2File = open(input, 'rb')

    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(page)
        pageObj.mergePage(pdf2Reader.getPage(page))
        pdfWriter.addPage(pageObj)

    pdfOutputFile = open(sav_path, 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()
    # remove ocr output pdf
    os.remove(ocr_output)

import os


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

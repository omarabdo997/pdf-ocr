import os

def rasterize(pdf_url):
    os.system("gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pgmraw -r150 -dTextAlphaBits=4 " 
              + "-sOutputFile=\'images/paper-%00d.jpg\' \"" + pdf_url+"\"")

def clean_images():
    os.system("rm images/*.jpg")

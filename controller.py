import utils


def controller(input_Path, save_path):
    ocr_out = "./result.pdf"
    utils.rasterize(input_Path)
    utils.images_ocr_pdf()
    utils.clean_images()
    merged = utils.merge_pdf(input_Path, ocr_out, save_path)
    return merged


# test
# print(
#     controller("/home/toka/Downloads/Q1.pdf",
#                "/home/toka/Downloads/output.pdf"))

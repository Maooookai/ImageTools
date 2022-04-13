import io
import os

import fitz
from PIL import Image


def extract_image_from_pdf(file_path, output_path=None):
    """
    Extract all images from a pdf file.

    :param file_path: Path of the pdf file.
    :param output_path: Output path of images
    :return: None
    """
    pdf = fitz.Document(file_path)
    if '/' in file_path:
        file_name = file_path.rpartition('/')[1]
    else:
        file_name = file_path
    print(f'File [{file_name}] has {pdf.page_count} page in total')
    for page_number in range(0, pdf.page_count):
        current_page = pdf.load_page(page_number)
        images = current_page.get_images()
        if images:
            print(f"Found a total of {len(images)} images in page {page_number}")
        else:
            print("No images found on page", page_number)
        for image_index, img in enumerate(current_page.get_images()):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            if output_path is not None:
                image.save(open(f"{output_path}/image{page_number + 1}_{page_number}.{image_ext}", "wb"))
            else:
                image.save(open(f"image{page_number + 1}_{page_number}.{image_ext}", "wb"))


def extract_image_from_dir(dir_path, output_path=None):
    """
    Extract all images from pdf files in a directory.

    :param dir_path: Directory that includes pdf files.
    :param output_path: Directory to save images.
    :return: None
    """
    if output_path is None:
        output_path = 'images'
    if dir_path.endswith("/"):
        for file in os.listdir(dir_path):
            extract_image_from_pdf(dir_path + file, output_path)
    else:
        for file in os.listdir(dir_path):
            extract_image_from_pdf(dir_path + '/' + file, output_path)

from PIL import Image


def jfif_to_jpg(file_path, output_path=None):
    """
    Convert JFIF file to JPG file.

    :param file_path: Path of the jfif file.
    :param output_path: Output path of image.
    :return: None
    """
    jfif_img = Image.open(file_path)
    jfif_img.save(output_path, "JPG")

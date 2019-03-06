from PIL import Image
from frame import first_frame

def get_resolution(path):
    first_frame(path)
    with Image.open('/Users/viktor/PycharmProjects/binarization_ocy/firstttt_frame.jpg') as img:
        width, height = img.size
        return width, height


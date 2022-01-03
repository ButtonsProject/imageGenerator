import io
from PIL import Image

def remove_background(image):
    res = remove(image)
    res = Image.open(io.BytesIO(res)).convert("RGBA")
    res.show()

remove_background(Image.open('C:\\Tools1\\PyCharm\\Progs\\MachineLearn\\other\\proba.png'))
import io
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
from wand.image import Image as Imagew
from backendImageGenerator.Postcard.Postcard import Postcard

font_fname = 'res/fonts/MullerBold.otf'
font_size = 72
font = ImageFont.truetype(font_fname, font_size)
h, w = 1080, 1080
blank_image = Image.new('RGB', (h, w), (255, 255, 255))
yellow = Image.open('res/images/high_article/yellow.png')
green = Image.open('res/images/high_article/green.png')
orange = Image.open('res/images/high_article/orange.png')



def process_checks(background, text):
        with Imagew(file=background) as bg_img:
            with Imagew() as fg_img:
                fg_img.read(filename="res/images/scream.png")
                bg_img.composite(fg_img, left=0, top=810)
                bg = bg_img.make_blob('png')

        bg_image = PIL.Image.open(io.BytesIO(bg))
        upper_image1 = Image.open("res/images/path1.png")
        upper_image2 = Image.open("res/images/path2.png")
        upper_image3 = Image.open("res/images/path3.png")
        draw = ImageDraw.Draw(bg_image)
        draw.text((110, 1080 - 73 - 72), text, font=font, fill='rgb(255, 255, 255)')
        bg_image.paste(upper_image1, (1080 - 142 - 54, 1080 - 59 - 86), upper_image1)
        bg_image.paste(upper_image2, (1080 - 60 - 40, 1080 - 137 - 65), upper_image2)
        bg_image.paste(upper_image3, (1080 - 129 - 27, 1080 - 211 - 43), upper_image3)
        f = io.BytesIO()
        bg_image.save(f, format='png')
        return f.getvalue()


def process_checks(background, text):
    result = Postcard("checks", {"background": image_crop(background), "text": text})
    f = io.BytesIO()
    result.create_result_post()
    result.result_post.save(f, format='png')
    return f.getvalue()


def process_triangle_mask(background, text, color):
    bg = image_crop(background)
    result = Postcard("triangle_mask_closed", {"background": bg, "color": color,
                                               "text": text})
    f = io.BytesIO()
    result.create_result_post()
    result.result_post.save(f, format='png')
    return f.getvalue()


def process_high_article(h_text, s_text, color):
    card = Postcard("empty_triangles", {"color": color, "title": h_text, "main": s_text})
    card.create_result_post()
    result = card.result_post
    f = io.BytesIO()
    result.save(f, format='png')
    return f.getvalue()


def image_crop(image):
    image = Image.open(image)
    width, height = image.size
    crop_size = min([width, height])
    if width > height:
        image = image.crop(((width - height) / 2, 0, crop_size + (width - height) / 2, crop_size))
    else:
        image = image.crop((0, (height - width) / 2, crop_size, crop_size + (height - width) / 2))
    image = image.resize((1080, 1080), Image.ANTIALIAS)
    return image


def process_typography(h_text, color):
    card = Postcard("typographia", {"color": color, "text": h_text, "font_size": 120})
    card.create_result_post()
    result = card.result_post
    f = io.BytesIO()
    result.save(f, format='png')
    return f.getvalue()



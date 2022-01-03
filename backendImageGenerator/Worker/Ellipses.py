import random

from PIL import Image, ImageDraw, ImageFilter

ellipses = [{'color': '#FFC600', 'size': (620, 670)},
            {'color': '#FF7500', 'size': (690, 680)},
            {'color': '#97D700', 'size': (570, 680)}]


def create_ellipses(start_position):
    mask_im = Image.new("RGB", (1080, 1080), '#FFFFFF')
    ellipses_positions = [(0, 0), (-80, 230), (170, 230)]
    x, y = start_position
    draw = ImageDraw.Draw(mask_im)
    for ellipse in ellipses:
        ellipse_pos = random.choice(ellipses_positions)
        ellipses_positions.remove(ellipse_pos)
        x1 = x + ellipse_pos[0]
        y1 = y + ellipse_pos[1]
        draw.ellipse((x1, y1, x1 + ellipse['size'][0], y1 + ellipse['size'][1]), fill=ellipse['color'])
    im_blur = mask_im.filter(ImageFilter.GaussianBlur(60))
    im_blur.show()
    return im_blur


create_ellipses((300, 400))
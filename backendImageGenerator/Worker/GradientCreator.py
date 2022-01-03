from PIL import Image



def createGradient(photo, gradient_magnitude = 2):
    if photo.mode != 'RGBA':
        photo = photo.convert('RGBA')
    width, height = photo.size
    gradient = Image.new('L', (1, height), color=0xFF)
    for y in range(height):
        gradient.putpixel((0, y), int(255 * (1 - gradient_magnitude * float(height - y) / height)))
    alpha = gradient.resize(photo.size)
    black_im = Image.new('RGBA', (width, height), color=0x000000)
    black_im.putalpha(alpha)
    gradient_im = Image.alpha_composite(photo, black_im)
    return gradient_im

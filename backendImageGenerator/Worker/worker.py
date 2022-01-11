from PIL import Image, ImageDraw, ImageFont
from backendImageGenerator.Worker import GradientCreator, Ellipses, cutter
from backendImageGenerator.Worker import ChecksGenerator
from backendImageGenerator.Worker import TextFunctions


def create_text_with_background(draw_image, position, lines, font, color, background_color, end_image=False, end_size_x=0):
    end_position = TextFunctions.create_background(draw_image, position,
                                                   lines, font, color,
                                                   background_color, end_image, end_size_x)
    return end_position

def empty_triangles(params):
    result = Image.new('RGB', (1080, 1080), (255, 255, 255))
    color_types = {"orange": ['Images/orange_cross.png', '#FF7500'],
                   "green": ['Images/green_cross.png', '#00AA13'],
                   "light_orange": ['Images/light_orange_cross.png', '#FF7500']}
    color = params["color"]
    font_name = 'resources/fonts/MullerBold.ttf'
    font = ImageFont.truetype(font_name, 72)
    figures = Image.open(color_types[color][0]).resize((1080, 621))
    result.paste(figures, (0, 459), figures)
    draw_result = ImageDraw.Draw(result)
    title_text = TextFunctions.crop_text(params["title"], 11, 14)
    main_text = TextFunctions.crop_text(params["main"], 11, 14)
    title_pos = (110, 110)
    main_pos = TextFunctions.print_text(draw_result, title_pos, title_text, '#000000', font)
    TextFunctions.print_text(draw_result, (title_pos[0], main_pos), main_text, color_types[color][1], font)
    return result


def checks_create(params):
    result = params["background"].resize((1080, 1080))
    result = GradientCreator.createGradient(result)
    ChecksGenerator.generator(result)
    drawer = ImageDraw.Draw(result)
    font_name = 'resources/fonts/MullerBold.ttf'
    font = ImageFont.truetype(font_name, 72)
    lines = TextFunctions.crop_text(params['text'], 11, 16)
    position = [110, 1040]
    position[1] -= 72 * 5 / 4 * len(lines)
    TextFunctions.print_text(drawer, position, lines, '#FFFFFF', font)
    return result


def closed_triangle_mask(params):
    result = params["background"]
    result = result.resize((1080, 1080))
    color_types = {"orange": ['Images/triangleGradOrange.png', '#FF7500', 'Images/smallOrangeTriangle.png'],
                   "green": ['Images/triangleGradGreen.png', '#00AA13', 'Images/smallGreenTriangle.png']}
    draw_result = ImageDraw.Draw(result)
    figure = Image.open(color_types[params['color']][0])
    triangle = Image.open('Images/whiteRectangle.png')
    result.paste(figure, (0, 0), figure)
    result.paste(triangle, (0, 280), triangle)
    end_triangle = Image.open(color_types[params['color']][2])
    font_name = 'resources/fonts/MullerBold.ttf'
    font = ImageFont.truetype(font_name, 72)
    lines = TextFunctions.crop_text(params["text"], 11, 14)
    position = [110, 1020]
    position[1] -= 72 // 4 * 5 * len(lines)
    end_str_position = create_text_with_background(draw_result, position, lines, font, '#FFFFFF',
                                                   '#000000', True, end_triangle.size)
    result.paste(end_triangle, end_str_position, end_triangle)
    return result

def title_ellipses(params):
    font_name = 'resources/fonts/MullerBold.ttf'
    border_width = 600
    border_height = 630
    x_smooth = 90
    font = ImageFont.truetype(font_name, 72)
    front_image = params['image']
    if not params['cropped']:
        front_image = cutter.remove_background(front_image)
        front_image = front_image.resize((1080, 1080), Image.ANTIALIAS)
        front_image = front_image.crop(front_image.getbbox())
        front_image.save('front.png')
    x, y = front_image.size

    if x < border_width and y < border_height:
        result = Ellipses.create_ellipses((890 - x, 980 - y))
        result.paste(front_image, (1080 - x - x_smooth, 1080 - y), front_image)
    else:
        result = Ellipses.create_ellipses(((1080 - x) // 2 + x_smooth, 1080 - y))
        result.paste(front_image, (540 - x // 2, 1080 - y), front_image)
    TextFunctions.print_text(ImageDraw.Draw(result), (100, 100), crop_text(params['title'], 13, 17), '#000000', font)
    return result

def typographia(params):
    color_types = {"orange": ['#FF7500', 'Images/orange_closer.png'],
                   "green": ['#00AA13', 'Images/green_closer.png']}
    end_image = Image.open(color_types[params["color"]][1])
    frame_size = (1400, 1400)
    background_size = (1080, 1350)
    background = Image.new('RGB', background_size, '#FFFFFF')
    font_name = 'resources/fonts/MullerRegular.ttf'
    font_size = params['font_size']
    font = ImageFont.truetype(font_name, font_size)
    constraint = 148 // font_size * 8
    result = Image.new('RGB', frame_size, '#FFFFFF')
    drawer = ImageDraw.Draw(result)
    lines = TextFunctions.crop_text(params['text'], constraint - 4, constraint + 2)
    length = TextFunctions.get_print_length(lines, font)
    position = ((frame_size[0] + 80 - length) // 2, frame_size[1] // 2 - font_size * len(lines) // 8 * 5)
    end_position = create_text_with_background(drawer, position, lines, font, '#FFFFFF', '#000000')
    result.paste(end_image, (end_position[0] - end_image.size[0] + 26, end_position[1] + font_size * 5 // 4), end_image)
    mask = Image.new('L', result.size, 255)
    result = result.rotate(15, Image.BICUBIC)
    mask = mask.rotate(15)
    background.paste(result, (0 - (frame_size[0] - background_size[0]) // 2, 0 - (frame_size[1] - background_size[1] + 100) // 2), mask)
    return background


creating_methods = {'empty_triangles': empty_triangles, "checks": checks_create, "triangle_mask_closed": closed_triangle_mask,
                    "title_ellipses": title_ellipses, "typographia": typographia}

def create_post(post_type, params):
    return creating_methods[post_type](params)
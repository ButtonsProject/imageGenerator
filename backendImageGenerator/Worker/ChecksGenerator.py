import random

from PIL import Image

positions_size = {'small': {'position': (924, 826), 'size': (27, 43)},
                  'medium': {'position': (980, 878), 'size': (40, 65)},
                  'big': {'position': (884, 935), 'size': (54, 86)}}

green_check = Image.open('Images/Checks/check_green.png')
lightgreen_check = Image.open('Images/Checks/check_lightgreen.png')
orange_check = Image.open('Images/Checks/check_orange.png')
red_check = Image.open('Images/Checks/check_red.png')
yellow_check = Image.open('Images/Checks/check_yellow.png')

check_arr = [green_check, lightgreen_check, orange_check, red_check, yellow_check]

def generator(picture):
    checks = [green_check, lightgreen_check, orange_check, red_check, yellow_check]
    for option in positions_size:
        check = random.choice(checks)
        checks.remove(check)
        if option == 'medium':
            check = check.transpose(Image.FLIP_LEFT_RIGHT)
        check = check.resize(positions_size[option]['size'])
        picture.paste(check, positions_size[option]['position'], check)
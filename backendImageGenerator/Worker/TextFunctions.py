def create_text(draw_image, position, text, color, font):
    draw_image.text(
        position,
        text,
        fill=color,
        font=font,
    )

def print_text(draw_image, position, lines, color, font):
    left_side = position[0]
    top_side = position[1]
    for i in range(len(lines)):
        create_text(draw_image, (left_side, top_side), lines[i], color, font)
        top_side += font.size * 5 // 4

def crop_text(text, word_constraint_down, word_constraint_up):
    words = text.split(' ')
    lines = []
    line = ''
    for word in words:
        if word_constraint_down >= len(line) + len(word):
            line += word + " "
        elif word_constraint_up >= len(line) + len(word):
            line += word + " "
        else:
            if len(line) != 0:
                lines.append(line)
                line = word + " "
            elif len(word) > word_constraint_up:
                lines.append(word[:word_constraint_down])
                line = word[word_constraint_down:] + " "
            else:
                lines.append(word)
    lines.append(line)
    return lines

def create_background(draw_image, position, lines, font, color, background_color, end_image = False, end_size = (0, 0)):
    left_side = position[0] - 30
    stroke_height = font.size * 5 // 4
    if end_image:
        stroke_height = end_size[1] + 4
    start_position_y = position[1] - (stroke_height - font.size) // 2
    top_side = start_position_y
    end_position = position
    for i in range(len(lines)):
        size = font.getbbox(lines[i])
        start_space = 0
        smooth_width_top = 25
        smooth_width_bottom = 25
        if i == 0:
            start_space = 10
        if (i == len(lines) - 1 or i == 0) and end_image:
            smooth_width_top = end_size[0] - 2
            smooth_width_bottom = 34
            stroke_height -= 2
        right_side = left_side + size[2] + 15
        bottom_side = top_side + stroke_height
        draw_image.polygon(
            ((left_side, top_side - start_space),
             (right_side + smooth_width_top, top_side - start_space),
             (right_side + smooth_width_bottom, bottom_side),
             (left_side, bottom_side),
             ),
            fill=background_color
        )
        end_position = (right_side, top_side)
        top_side = bottom_side
    print_text(draw_image, position, lines, color, font)
    return end_position

def get_print_length(lines, font):
    return int(font.getlength(max(lines, key=lambda line: font.getlength(line))))
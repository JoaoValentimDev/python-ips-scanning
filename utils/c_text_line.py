def c_text(
        text="",
        text_color="white",
        text_style="none",
        background_color="none"):
    style_text_dictionary = {
        "bold": "1",
        "underline": "4",
        "negative": "7"
    }
    colors_dictionary = {
        "text_colors": {
            "white": "30",
            "red": "31",
            "green": "32",
            "yellow": "33",
            "blue": "34",
            "purple": "35",
            "cyan": "36",
            "gray": "37"
        },
        "background_colors": {
            "white": "40",
            "red": "41",
            "green": "42",
            "yellow": "43",
            "blue": "44",
            "purple": "45",
            "cyan": "46",
            "gray": "47"
        }
    }

    data = []
    output = ''
    if text_color in colors_dictionary["text_colors"]:
        data.append(f'{colors_dictionary["text_colors"][text_color]}')
    if text_style in style_text_dictionary:
        data.append(f'{style_text_dictionary[text_style]}')
    if background_color in colors_dictionary["background_colors"]:
        data.append(
            f'{colors_dictionary["background_colors"][background_color]}')

    if len(data) == 3:
        output = f'\033[{data[1]};{data[0]};{data[2]}m{text}\033[m'
    if len(data) == 2:
        output = f'\033[{data[1]};{data[0]}m{text}\033[m'
    if len(data) == 1:
        output = f'\033[{data[0]}m{text}\033[m'
    if len(data) == 0:
        output = text

    return output

colors_availables = ('yellow', 'green', 'red', 'blue')

# text is str: to be formatted
# color is str: in typle colors_availables
def print_color(text, color):
    if color not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)

def print_color_and_bg(text, color, bg):
    if color not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)
    if bg not in colors_availables:
        raise Exception('Color is not avaliable, type one this', colors_availables)


# make safe... developers
def safe_input_int(message):
    num = int(input(message))


def print_title(text):
    print('TEST: this is title - ', text)

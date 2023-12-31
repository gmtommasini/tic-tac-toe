yellow_background = "\x1b[43m"
gray_foreground = "\x1b[90m"
blue_foreground = "\x1b[34m"
cyan_foreground = "\x1b[36m"
magenta_foreground = "\x1b[35m"
reset_color = "\x1b[0m"


def yellow_b(text):
    return f'{yellow_background}{blue_foreground}{str(text)}{reset_color}'


def gray_f(text):
    return f'{gray_foreground}{str(text)}{reset_color}'


def cyan_f(text):
    return f'{cyan_foreground}{str(text)}{reset_color}'


def pink_f(text):
    return f'{magenta_foreground}{str(text)}{reset_color}'


# Foreground (Text) Colors:
#
# 30: Black
# 31: Red
# 32: Green
# 33: Yellow
# 34: Blue
# 35: Magenta
# 36: Cyan
# 37: White
# Background Colors:
#
# 40: Black
# 41: Red
# 42: Green
# 43: Yellow
# 44: Blue
# 45: Magenta
# 46: Cyan
# 47: White
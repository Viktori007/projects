def color1(col):
    """Функция возвращает значения цвета"""
    color = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (133, 5, 5),
        "green": (0, 255, 0),
        "blue": (13, 10, 31),
        "gray": (133, 133, 133),
        "lightgray": (192, 192, 192),
        "darkgray": (128, 128, 128),
        "yellow": (222, 181, 31),
        "pink": (243, 229, 246)
    }
    return color[col.lower()]


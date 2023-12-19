import pygame


class Win:
    """инциализация атрибутов класса"""
    width_sc, height_sc = 1000, 800
    width_game, height_game = width_sc - 200, height_sc - 200
    fps = 30
    # Создаем игру и окно
    son = ["eat.ogg", "hit.ogg", "over.ogg"]
    pygame.mixer.init()  # для звука
    song = [pygame.mixer.Sound('mp/' + path) for path in son]
    clock = pygame.time.Clock()
    sc = pygame.display.set_mode((width_sc, height_sc))
    first = True
    surf_game = pygame.Surface((width_game, height_game))
    objects = []
    foods = pygame.sprite.Group()
    scores = []

    @classmethod
    def message(cls, msg, color, size, y):
        """Функция будет показывать сообщение в окне"""
        font_style = pygame.font.SysFont('arial', size)
        text = font_style.render(msg, True, color)  # оформление
        text_rect = text.get_rect(center=(cls.width_sc / 2, y))
        cls.sc.blit(text, text_rect)

    @staticmethod
    def color1(col):
        """Функция возвращает значения цвета"""
        color = (0, 0, 0)
        if col.lower() == "white":
            color = (255, 255, 255)
        if col.lower() == "black":
            color = (0, 0, 0)
        if col.lower() == "red":
            color = (133, 5, 5)
        if col.lower() == "green":
            color = (0, 255, 0)
        if col.lower() == "blue":
            color = (13, 10, 31)
        if col.lower() == "gray":
            color = (133, 133, 133)
        if col.lower() == "lightgray":
            color = (192, 192, 192)
        if col.lower() == "darkgray":
            color = (128, 128, 128)
        if col.lower() == "yellow":
            color = (222, 181, 31)
        if col.lower() == "pink":
            color = (243, 229, 246)
        return color

    @classmethod
    def your_score(cls, score):
        """Функция выводит на экран значения сета игры"""
        score_font = pygame.font.SysFont("comicsansms", 35)
        value = score_font.render("Ваш счёт: " + str(score), True, cls.color1("yellow"))
        cls.sc.blit(value, [0, 0])

    @classmethod
    def scores_all(cls):
        """фунция выводит все очки полученные за еду"""
        i, j = 0, 1
        cls.message("Очки, собранные за все время игры:", cls.color1("lightgray"), 25, 150 + i)
        i += 35
        cls.message(f"         номер игры | количество очков", cls.color1("lightgray"), 25, 150 + i)
        i += 35
        for lin in cls.scores:
            cls.message(f"{j}   {lin}", cls.color1("lightgray"), 25, 150 + i)
            i += 35
            j += 1
        cls.message(f"итого набрано        {sum(cls.scores)} очков ", cls.color1("lightgray"), 25, 150 + i)

    @classmethod
    def rule(cls):
        """фунция выводит равила игры"""
        f1 = open("rules.txt", 'r', encoding="UTF-8")
        lst = f1.readlines()
        f1.close()
        i = 0
        for lin in lst:
            cls.message(lin[:-1], cls.color1("lightgray"), 25, 150 + i)
            i += 35

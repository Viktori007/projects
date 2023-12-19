import pygame
from random import randrange
from Win import Win


class Stars:
    """
    класс для работы с задним фоном неба со звездочками

    методы
    __init__()
    функции:
    stars_create_all()
    travel_stars()
    """

    star_slow = []
    star_medium = []
    star_fast = []
    width = 1000
    height = 800
    surf = pygame.Surface((width, height))

    @classmethod
    def stars_create_all(cls):
        """функция для создания звезд до начала работы приложения"""

        def create(starss, n):
            for star in range(n):
                star_x = randrange(0, cls.width)
                star_y = randrange(0, cls.height)
                starss.append([star_x, star_y])

        create(cls.star_slow, 50)
        create(cls.star_medium, 35)
        create(cls.star_fast, 15)

    @classmethod
    def travel_stars(cls):
        """функция для перемещения звезд во время игры"""

        def travel(starss, n, color, radis):
            for star in starss:
                # перемещаем вниз на заданное рвстояние
                star[1] += n
                # если вышла за нижнюю границу, рисуем над верхней границей
                if star[1] > cls.height:
                    star[0] = randrange(0, cls.width)
                    star[1] = randrange(-20, -5)
                pygame.draw.circle(cls.surf, color, star, radis)

        travel(cls.star_slow, 1, Win.color1("darkgray"), 3)
        travel(cls.star_medium, 4, Win.color1("lightgray"), 2)
        travel(cls.star_fast, 8, Win.color1("yellow"), 1)
        Win.sc.blit(cls.surf, (0, 0))


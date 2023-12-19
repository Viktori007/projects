import pygame
from random import randint
from Win import Win
from Kot import Kot


class Food(pygame.sprite.Sprite):
    """
            класс для управления едой для кота

            методы
            __init__()
            функции:
            create_food(group)
            update(self, *args, start=True)
            """

    def __init__(self, x, y, speed, surf, score, group):
        """инциализация атрибутов класса"""
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.surf = pygame.transform.scale(surf, (surf.get_width() // 15, surf.get_height() // 15))
        self.score = score
        self.rect = self.surf.get_rect(center=(x, y))
        self.width, self.height = self.surf.get_rect().size
        self.speed = speed
        self.add(group)

    @staticmethod
    def create_food(group):
        """функция возвращает созданный объект класса еды"""
        foods_images = ['ad.png', 'head1.png', 'head2.png', 'head3.png']
        foods_surf = [pygame.image.load('images/' + path).convert_alpha() for path in foods_images]
        indx = randint(0, len(foods_surf) - 1)
        score = [-150, 100, 150, 200]
        x = randint(120, Win.width_sc - 120)
        y = randint(120, Win.height_sc - 120)
        for i in range(15):
            if Kot.rect.collidepoint(x + i, y + i):
                x = randint(120, Win.width_sc - 120)
                y = randint(120, Win.height_sc - 120)
        speed = randint(1, 3)
        return Food(x, y, speed, foods_surf[indx], score[indx], group)

    def update(self, *args, start=True):
        """функция передвизает и убирает объект класса еды"""
        if start:
            if self.rect.y < args[0]:
                self.rect.y += self.speed
            else:
                self.kill()

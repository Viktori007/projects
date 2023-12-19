import pygame
from Win import Win


class Kot:
    """
        класс для работы с котом

        методы
        __init__()
        функции:
        kot_skin(choice)
        event_kot(event1):
        travel_kot()
        exit_kot(stat)
        death_kot()
        """
    width_sc = Win.width_sc
    height_sc = Win.height_sc
    surf = pygame.image.load("images/kot4.png").convert_alpha()
    surf = pygame.transform.scale(surf, (surf.get_width() // 6, surf.get_height() // 6))
    rect = surf.get_rect(center=(width_sc // 2, height_sc // 2))

    width, height = surf.get_rect().size
    life = 3
    x1_change = 0
    y1_change = 0
    snake_block = 10  # Укажем в переменной стандартную величину сдвигаположения змейки при нажатии на клавиши.
    images = ["kot1.png", "kot2.png", "kot3.png", "kot4.png"]

    @classmethod
    def kot_skin(cls, choice):
        """Функция возвращает поверхность с выбранной картинкой"""
        cls.surf = pygame.image.load('images/' + cls.images[choice - 1]).convert_alpha()
        cls.surf = pygame.transform.scale(cls.surf, (cls.surf.get_width() // 6, cls.surf.get_height() // 6))

    @classmethod
    def event_kot(cls, event1):
        """функция меняет значения в зависимости от переданного события"""
        if event1.type == pygame.KEYDOWN:  # если нажата клавиша
            if event1.key == pygame.K_LEFT or event1.key == pygame.K_a:  # лево
                cls.x1_change = -cls.snake_block
                cls.y1_change = 0
            elif event1.key == pygame.K_RIGHT or event1.key == pygame.K_d:  # право
                cls.x1_change = cls.snake_block
                cls.y1_change = 0
            elif event1.key == pygame.K_UP or event1.key == pygame.K_w:  # вверх
                cls.y1_change = -cls.snake_block
                cls.x1_change = 0
            elif event1.key == pygame.K_DOWN or event1.key == pygame.K_s:  # вниз
                cls.y1_change = cls.snake_block
                cls.x1_change = 0

    @classmethod
    def speed(cls, sp):
        """функция меняет значения скорости"""
        speed = {
            1: 5,
            2: 10,
            3: 15,
            4: 20
        }
        cls.snake_block = speed[sp]

    @classmethod
    def travel_kot(cls):
        """функция передвигает голову кота"""
        cls.rect.x += cls.x1_change
        cls.rect.y += cls.y1_change

    @classmethod
    def exit_kot(cls, stat):
        """функция проверяет не вышла ли голова за границы поля"""
        if (cls.rect.x + cls.width >= cls.width_sc - 100 or cls.rect.x < 100 or cls.rect.y + cls.height >= cls.height_sc
            - 100 or cls.rect.y <= 100) or cls.life <= 0:
            stat = "over"
            Win.song[1].play()
        return stat

    @classmethod
    def death_kot(cls):
        """функция обновляет данные о коту"""
        cls.rect = cls.surf.get_rect(center=(cls.width_sc // 2, cls.height_sc // 2))
        cls.x1_change = 0
        cls.y1_change = 0
        cls.life = 3

    @classmethod
    def heart(cls):
        surf1 = pygame.image.load("images/heart1.png").convert_alpha()
        surf2 = pygame.image.load("images/heart2.png").convert_alpha()
        for i in range(3):
            Win.sc.blit(surf2, [10 + i*50, 50])
        for i in range(cls.life):
            Win.sc.blit(surf1, [10 + i*50, 50])

    @classmethod
    def collide(cls, score, status):
        """функция проверяет столкновение, выводит на экран и возвращает счет"""
        for food in Win.foods:
            if cls.rect.collidepoint(food.rect.center):
                Win.song[0].play()
                score += food.score
                food.kill()
                if food.score == -150:
                    cls.life -= 1

        if status == "game":
            Win.your_score(score)
            Win.first = True
        elif status == "over":
            if Win.first:
                Win.scores.append(score)
                Win.first = False
                score = 0
        return score

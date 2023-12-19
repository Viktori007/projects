import pygame
from random import randrange, randint


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


class Button:
    """
               класс для управления кнопками

               методы
               __init__()
               функции:
               process()
               create_buttons()
               image_yes
               btn_press
    """

    def __init__(self, number, x, y, width, height, status, status_after, text=None, text2=None, image=None, one_press=False):
        """инциализация атрибутов класса"""
        self.number = number
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.one_press = one_press
        self.alreadyPressed = False
        self.status = status
        self.status_after = status_after
        self.image = image
        self.text = text
        self.text2 = text2
        self.number_c = [8, 11]
        self.fillColors = {
            # ffffff
            'normal': '#c0c0c0',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.Color = self.fillColors['normal']

        self.buttonSurface = pygame.Surface((self.width, self.height))

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.buttonSurface, Win.color1("red"), (0, 0, self.width - 1, self.height - 1), 1)
        font = pygame.font.SysFont('Arial', 40)
        self.buttonSurf = font.render(self.text, True, (0, 0, 0))

        Win.objects.append(self)

    def process(self):
        """функция меняет внешний вид кнопки и проверяет нажание и наведение мыши на нее"""
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.btn_press()
                if self.one_press:
                    self.status = self.status_after
                    self.alreadyPressed = True
                elif not self.alreadyPressed:
                    self.status = self.status_after
                    self.alreadyPressed = True
                self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        if self.status == "menu" and self.status_after == "menu":
            self.buttonSurface.fill(self.Color)
            self.image_yes()

        pygame.draw.rect(self.buttonSurface, self.Color, (0, 0, self.width - 1, self.height - 1), 2)
        self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                                                  self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2])
        Win.sc.blit(self.buttonSurface, self.buttonRect)
        return self.alreadyPressed

    def image_yes(self):
        """функция для оформления элементов меню с картинкой"""
        if self.image is not None:
            surf = pygame.image.load(self.image).convert_alpha()
            self.buttonSurface.blit(surf, (10, 10))
            font_style = pygame.font.SysFont('arial', 40)
            text = font_style.render(self.text2, True, Win.color1("red"))  # оформление
            text_rect = text.get_rect(center=(self.width / 2, 200))
            self.buttonSurface.blit(text, text_rect)

    def btn_press(self):
        """функция для выделения выбранного элемента меню"""
        for btn in Win.objects:
            if self.height == 240 and btn.height == 240:
                btn.Color = self.fillColors['normal']
                self.Color = self.fillColors['hover']
            if self.height == 65 and btn.height == 65:
                btn.Color = self.fillColors['normal']
                self.Color = self.fillColors['hover']

    @staticmethod
    def create_buttons():
        """функция создает объекты класса кнопки"""
        Button(0, 350, 350, 300, 80, "entry", "menu", 'Начать игру')
        Button(1, 710, 630, 150, 50, "menu", "game", 'Далее')
        Button(2, 350, 350, 300, 80, "over", "game", 'Начать заново')
        Button(3, 110, 630, 150, 50, "menu", "entry", 'Назад')
        Button(4, 900, 30, 50, 50, "entry", "rule", '?')
        Button(5, 375, 450, 250, 60, "over", "score", 'Показать счет')
        for i1 in range(4):
            names = ['Борис', 'Василий', 'Котофей', 'Водяра']
            images_kot = ["kot11.png", "kot22.png", "kot33.png", "kot44.png"]
            Button(6+i1, 110 + i1 * 195, 150, 190, 240, "menu", "menu", ' ', names[i1], "images/" + images_kot[i1])
        for i1 in range(4):
            Button(10+i1, 110 + i1 * 195, 420, 190, 65, "menu", "menu", str(i1 + 1) + ' скорость')
        Button(14, 350, 350, 300, 80, "stop", "game", 'Продолжить')


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


def main_cycle(running, status, score, vol):
    """**********ГЛАВНЫЙ ЦИКЛ ИГРЫ************"""
    pygame.init()
    Stars.stars_create_all()
    Button.create_buttons()
    pygame.mixer.music.load("mp/di.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while running:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверяем закрытие окна
            if event.type == pygame.QUIT:
                running = False
            # проверяем нажание пробела и изменяем статус игры
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_3:
                    status = "stop"
                elif event.key == pygame.K_SPACE:
                    status = "game"
                elif event.key == pygame.K_1:
                    vol -= 0.1
                    pygame.mixer.music.set_volume(vol)
                    print(pygame.mixer.music.get_volume())
                elif event.key == pygame.K_2:
                    vol += 0.1
                    pygame.mixer.music.set_volume(vol)
                    print(pygame.mixer.music.get_volume())

            Kot.event_kot(event)
        if score < 0:
            status = "over"
            Win.song[1].play()

        Stars.surf.fill(Win.color1("black"))
        Win.surf_game.fill(Win.color1("black"))
        pygame.draw.rect(Win.surf_game, Win.color1("lightgray"), (0, 0, Win.width_game - 1, Win.height_game - 1), 1)

        Stars.travel_stars()
        score = Kot.collide(score, status)
        status = status_games(status)
        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()
        # Держим цикл на правильной скорости
        Win.clock.tick(Win.fps)
    pygame.display.update()  # обновление части экрана
    pygame.quit()  # отключение pygame
    print(Win.scores)
    quit()


def status_games(status):
    """функция возврацает статус игры"""
    status_game = ["entry", "menu", "game", "over", "rule", "score", "stop"]

    # entry
    if status == status_game[0]:
        Win.message("Котя", Win.color1("lightgray"), 50, 300)
        if Win.objects[4].process():
            status = Win.objects[4].status
            Win.objects[8].status = "entry"
        elif Win.objects[0].process():
            status = Win.objects[0].status
            Win.objects[0].status = "entry"

    # menu
    elif status == status_game[1]:
        Win.sc.blit(Win.surf_game, (100, 100))
        for i in range(4):
            if Win.objects[6 + i].process():
                status = Win.objects[6 + i].status
                Kot.kot_skin(1 + i)

        for i in range(4):
            if Win.objects[10 + i].process():
                status = Win.objects[10 + i].status
                Kot.speed(1 + i)

        if Win.objects[1].process():
            status = Win.objects[1].status
            Win.objects[1].status = "menu"

    # game
    elif status == status_game[2]:
        status = Kot.exit_kot(status)
        Win.sc.blit(Win.surf_game, (100, 100))

        Win.foods.update(Win.height_sc - 120)
        Win.foods.draw(Win.sc)
        if len(Win.foods) < 5:
            Food.create_food(Win.foods)
        Win.sc.blit(Kot.surf, Kot.rect)
        Kot.heart()
        Kot.travel_kot()

    # over
    elif status == status_game[3]:
        Kot.death_kot()
        Win.message("Вы проиграли :( ЛОХ", Win.color1("red"), 50, 200)
        Win.message("Ваш счет: " + str(Win.scores[-1]), Win.color1("yellow"), 50, 250)

        if Win.objects[2].process():
            status = Win.objects[2].status
            Win.objects[2].status = "over"
        if Win.objects[5].process():
            status = Win.objects[5].status
            Win.objects[5].status = "over"

        elif Win.objects[3].process():
            status = Win.objects[3].status
            Win.objects[3].status = "over"

    # rule
    elif status == status_game[4]:
        Win.sc.blit(Win.surf_game, (100, 100))
        Win.rule()
        if Win.objects[3].process():
            status = Win.objects[3].status
            Win.objects[3].status = "over"

    # score
    elif status == status_game[5]:
        Win.sc.blit(Win.surf_game, (100, 100))
        Win.scores_all()
        if Win.objects[3].process():
            status = Win.objects[3].status
            Win.objects[3].status = "over"

    # stop
    elif status == status_game[6]:

        if Win.objects[14].process():
            status = Win.objects[14].status
            Win.objects[14].status = "stop"
    else:
        print("ошибка")
    for obg in Win.objects:
        obg.alreadyPressed = False
    return status


if __name__ == "__main__":
    main_cycle(True, "entry", 0, 0.2)


import pygame
from Win import Win


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

    def __init__(self,number, x, y, width, height, status, status_after, text=None, text2=None, image=None, one_press=False):
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
            if self.height == 240 and  btn.height == 240:
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



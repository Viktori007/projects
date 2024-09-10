import pygame


class Button:

    def __init__(self, win, x, y, width, height, text=None, on_click_function=None, one_press=False):
        self.win = win
        self.x = x
        self.y = y
        self.on_click_function = on_click_function
        self.width = width
        self.height = height
        self.one_press = one_press
        self.alreadyPressed = False
        self.text = text
        self.Color = '#47170b'
        self.buttonSurface = pygame.Surface((self.width, self.height))

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.buttonSurface, (255, 225, 255), (-1, -1, self.width + 1, self.height + 1), 1)
        self.font = pygame.font.Font('Allods.ttf', 38)
        self.buttonSurf = self.font.render(self.text, True, (255, 255, 255))
        self.win.objects.append(self)

    def process(self):
        """функция меняет внешний вид кнопки и проверяет нажание и наведение мыши на нее"""
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.fill('#47170b')
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill('#6d3d31')
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill('#350600')
                if self.one_press:
                    self.on_click_function()
                    self.alreadyPressed = True
                elif not self.alreadyPressed:
                    self.on_click_function()
                    self.alreadyPressed = True
                self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        pygame.draw.rect(self.buttonSurface, (0, 0, 0), (-1, -1, self.width + 1, self.height + 1), 1)
        return self.alreadyPressed

    def display(self):
        """Функция отображения кнопок"""
        pygame.draw.rect(self.buttonSurface, self.Color, (0, 0, self.width - 1, self.height - 1), 2)
        self.buttonSurface.blit(self.buttonSurf, [self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                                                  self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2])
        self.win.sc.blit(self.buttonSurface, self.buttonRect)

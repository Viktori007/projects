import pygame


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image_card = pygame.image.load(f"images/cards/{self.value}_{self.suit}.png").convert_alpha()
        self.image_card = pygame.transform.scale(self.image_card, (self.image_card.get_width() // 12, self.image_card.get_height() // 12))

    def display(self, sc, x, y):
        """функция отображает карту"""
        pygame.Surface.blit(sc, self.image_card, (x, y))

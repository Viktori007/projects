from Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.playing_cards = None
        suits = ['черви', 'бубны', 'крести', 'пики']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        self.shuffle_cards()

    def deal_card(self):
        """функция удаляет карты"""
        return self.playing_cards.pop()

    def shuffle_cards(self):
        """функция перетасовывает карты"""
        cards = self.cards.copy()
        shuffle(cards)
        self.playing_cards = cards


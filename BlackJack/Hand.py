
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """функция добавляет новую карту"""
        self.cards.append(card)

    def calculate_score(self):
        """функция рассчитывает  и возвращает общий счет карт"""
        score = sum(
             10 if card.value in ['валет', 'дама', 'король'] else
            11 if card.value == 'туз'
            else int(card.value)

            for card in self.cards)
        score_ace = sum(1 for card in self.cards if card.value == 'туз')
        while score > 21 and score_ace:
            score -= 10
            score_ace -= 1
        return score


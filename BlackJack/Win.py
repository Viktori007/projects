import pygame
from Card import Card
from Deck import Deck
from Hand import Hand
from Button import Button


class Win:
    def __init__(self):
        pygame.init()
        self.continue_game = False
        self.dealer_hand = None
        self.player_hand = None
        self.hide_dealer_card = True
        self.objects = []
        self.width_sc, self.height_sc = 1550, 800
        self.exp = False
        self.display_btn_bet = True
        self.state_bet = 0
        self.money = 5000
        self.bet = 0
        self.need_input = False
        self.input_text = ''

        self.sc = pygame.display.set_mode((self.width_sc, self.height_sc))
        self.surf = pygame.image.load("images/table.jpg").convert_alpha()
        self.surf_d = pygame.image.load("images/wood.jpg").convert_alpha()

        self.deck = Deck()

        self.btn_make_bet = Button(self, 680, 300, 250, 50, "", self.input_bet)
        self.btn_make_bet2 = Button(self, 715, 380, 180, 50, "Готово", self.enter_bet)
        self.btn_player_step = Button(self, 580, 560, 180, 50, "Взять еще", self.player_step)
        self.btn_raise_bet = Button(self, 680, 480, 200, 50, "Ставка 2х", self.raise_bet)
        self.btn_dealer_step = Button(self, 780, 560, 230, 50, "Воздержаться", self.dealer_step)
        self.btn_restart = Button(self, 1300, 5, 230, 45, "Начать заново", self.restart)

    def main_cycle(self):
        """**********ГЛАВНЫЙ ЦИКЛ ИГРЫ************"""
        self.deal_initial()
        running = True

        while running:
            running = self.__get_events(running)
            self.__create_table()
            for object in self.objects:
                object.process()

            self.over()
            if self.continue_game:
                self.print_hands(self.hide_dealer_card)
                self.message(f"Ставка: {self.bet} $", (255, 255, 255), 32, 600, 25, self.sc)

                self.btn_dealer_step.display()
                self.btn_player_step.display()
                if self.display_btn_bet:
                    self.btn_raise_bet.display()
                self.over()

            pygame.display.flip()

    def __get_events(self, running):
        """функция отлавливает все события и возвращяет статус окна"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if self.need_input:
                    if event.key == pygame.K_RETURN:
                        self.need_input = False
                        self.enter_bet()
                        self.input_text = ''
                    if event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    elif event.unicode in ['1', '2', '3', '4', '5', '6', '7', '8', '9',  '0']:
                        self.input_text += event.unicode
        return running

    def restart(self):
        """Функция возвращает все к начальным значениям"""
        self.bet = 0
        self.state_bet = 0
        self.hide_dealer_card = True
        self.deck.shuffle_cards()
        self.deal_initial()
        self.continue_game = True
        self.display_btn_bet = True

    def input_bet(self):
        """функция позволяет вводить текст"""
        self.need_input = True

    def make_bet(self, value):
        """функция вычитает переданное значение из денег игрока и присваивает это значение ставке"""
        self.money -= value
        self.bet = value

    def raise_bet(self):
        """функция удваивает ставку"""
        self.bet *= 2
        self.display_btn_bet = False

    def enter_bet(self):
        if self.input_text != '' and self.money >= int(self.input_text):
            self.make_bet(int(self.input_text))
            self.continue_game = True
            self.exp = False
        else:
            self.exp = True

    def over(self):
        """функция отображает все концы игры"""
        player_score = self.player_hand.calculate_score()
        dealer_score = self.dealer_hand.calculate_score()
        if self.bet == 0:
            self.win_make_bet()
            self.continue_game = False
        if not self.hide_dealer_card:
            self.print_hands(self.hide_dealer_card)
            self.btn_restart.display()
            if player_score > 21:
                self.message("Перебор! Вы проиграли!", (255, 255, 255), 55, 800, 50, self.sc)
                self.continue_game = False
                self.hide_dealer_card = False
            elif dealer_score > 21 or player_score > dealer_score:
                self.message("Поздравляем! Вы выиграли!", (255, 255, 255), 55, 800, 50, self.sc)
                self.state_bet = -1 if self.state_bet == -1 else 2
            elif player_score < dealer_score:
                self.message("Вы проиграли!", (255, 255, 255), 55, 800, 50, self.sc)
            else:
                self.message("Ничья", (255, 255, 255), 55, 800, 50, self.sc)
                self.state_bet = -1 if self.state_bet == -1 else 1
            self.continue_game = False
            self.bet_bet()

    def bet_bet(self):
        """Функция добавляет к банку игрока его выигрыш"""
        if self.state_bet != -1:
            if self.state_bet == 1:
                self.money += self.bet
            if self.state_bet == 2:
                self.money += self.bet * 2
        self.state_bet = -1

    def win_make_bet(self):
        """Функция отображает окно для ввода ставки"""
        pygame.draw.rect(self.sc, (53, 6, 0), (550, 200, 500, 300))
        pygame.draw.rect(self.sc, (255, 255, 255), (549, 199, 501, 301), 1)
        self.message("Сделайте ставку", (255, 255, 255), 55, 800, 250, self.sc)
        self.btn_make_bet.display()
        self.btn_make_bet2.display()
        if self.exp:
            self.message("У Вас недостаточно средств", (255, 0, 0), 30, 800, 450, self.sc)
        self.message(self.input_text, (255, 225, 255), 38, 800, 325, self.sc)

    def dealer_step(self):
        """Функция запрашивает карты и делает счет для противника"""
        self.display_btn_bet = False
        if self.continue_game:
            if self.player_hand.calculate_score() <= 21:
                while self.dealer_hand.calculate_score() < 17:
                    self.dealer_hand.add_card(self.deck.deal_card())
                self.hide_dealer_card = False
                return False

    def player_step(self):
        """Функция добавляет новые карты игроку по запросу"""
        self.display_btn_bet = False
        if self.continue_game:

            self.player_hand.add_card(self.deck.deal_card())
            if self.player_hand.calculate_score() > 21:
                self.hide_dealer_card = False
                return False

    def __create_table(self):
        """Функция отрисовывает фон"""
        self.surf_d = pygame.transform.scale(self.surf_d, (1800, 60))
        pygame.Surface.blit(self.sc, self.surf, (0, 50))
        pygame.Surface.blit(self.sc, self.surf_d, (0, 0))
        self.message(f"Банк: {self.money} $", (255, 255, 255), 32, 300, 25, self.sc)

    def message(self, msg, color, size, x, y, sc):
        """Функция отображает текст"""
        font_style = pygame.font.Font('Allods.ttf', size)
        text = font_style.render(msg, True, color)  # оформление
        text_rect = text.get_rect(center=(x, y))
        sc.blit(text, text_rect)

    def deal_initial(self):
        """Функция инициализирует по 2 первых карты для игрока и диллера"""
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

    def print_hands(self, hide_dealer_card=True):
        """Функция отпечатывает все карты"""
        self.message("Ваша рука:", (255, 255, 0), 30, 300, 100, self.sc)
        x_step = 120
        self.display_location_cards(150, 150, 600, self.player_hand.cards)
        self.message(f"Ваш счет: {self.player_hand.calculate_score()}", (255, 255, 0), 30, 550, 100, self.sc)
        self.message("Рука крупье:", (255, 255, 0), 30, 1000, 100, self.sc)

        x_offset = 850
        y_offset = 150
        if hide_dealer_card:
            empty_card = Card("рубашка", 0)
            empty_card.display(self.sc, x_offset, y_offset)
            self.dealer_hand.cards[1].display(self.sc, x_offset + x_step, y_offset)
        else:
            self.display_location_cards(x_offset, y_offset, 1300, self.dealer_hand.cards)
            self.message(f"Счет крупье: {self.dealer_hand.calculate_score()}", (255, 255, 0), 30, 1300, 100, self.sc)

    def display_location_cards(self, x_offset, y_offset, x_end, arg):
        """Функция помогает отображать карты"""
        i = 0
        x_step = 120
        for card in arg:
            if x_offset + i * x_step >= x_end:
                x_offset = 150
                y_offset += 200
                i = 0
            card.display(self.sc, x_offset + i * x_step, y_offset)
            i += 1

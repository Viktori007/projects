import collections

import pygame
from Stars import Stars
from Kot import Kot
from Win import Win
from status import status_games
from Button import Button


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

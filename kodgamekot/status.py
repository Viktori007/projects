from Win import Win
from Kot import Kot
from Food import Food


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

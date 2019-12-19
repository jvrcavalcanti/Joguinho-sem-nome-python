import pygame as pg
from classes.game import Screen
from classes.player import Player
from classes.fruit import Fruit
from sklearn.neural_network import MLPClassifier
import pandas as pd
import sys

def main():
    df = pd.read_csv("data.csv")
    df.drop_duplicates()
    y = df.id_move

    df = df.drop("id_move", axis=1)

    x = df

    clf = MLPClassifier().fit(x, y)

    pg.init()

    game = Screen(pg)
    player = Player()
    fruit = Fruit()

    game.spriters.append(player)
    game.spriters.append(fruit)

    running = True

    clock = game.pg.time.Clock()

    while running:
        clock.tick(60)

        game.update()
        for event in game.pg.event.get():
            if event.type == game.pg.QUIT:
                running = False

        pressed = game.pg.key.get_pressed()
        if pressed[game.pg.K_UP]:
            player.move_up(game)
        if pressed[game.pg.K_DOWN]:
            player.move_down(game)
        if pressed[game.pg.K_LEFT]:
            player.move_left(game)
        if pressed[game.pg.K_RIGHT]:
            player.move_right(game)

        # player.next_move(fruit, game)
        player.select_move(clf.predict([[player.x, fruit.x, player.y, fruit.y]])[0], game)


        # Colision
        if player.x < fruit.x + fruit.width: 
            if player.x + player.width > fruit.x: 
                if player.y < fruit.y + fruit.height: 
                    if player.y + player.height > fruit.y:
                        fruit.reposition()

if __name__ == "__main__":
    main()

import pygame as pg
import csv
import numpy as np
from classes.game import Screen
from classes.player import Player
from classes.fruit import Fruit
from listen import listen_microfone

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

    op = listen_microfone()
    print(op)
    if op == "cima":
        player.move_up(game)
        player.move_up(game)
        player.move_up(game)

    if op == "baixo":
        player.move_down(game)
        player.move_down(game)
        player.move_down(game)

    if op == "esquerda":
        player.move_left(game)
        player.move_left(game)
        player.move_left(game)

    if op == "direita":
        player.move_right(game)
        player.move_right(game)
        player.move_right(game)

    if op == "sair":
        running = False

    if op == "reposicionar":
        fruit.reposition()

    if player.x < fruit.x + fruit.width: 
        if player.x + player.width > fruit.x: 
            if player.y < fruit.y + fruit.height: 
                if player.y + player.height > fruit.y:
                    fruit.reposition()
    game.update()
    

import pygame
from gameMap import GameMap
from frog import Frog
from controller import Controller
from ball import Ball
from sequence import Sequence


class Game:

    def __init__(self, game_map_sprite, frog_position, path_file):
        pygame.init()
        self.controller = Controller(game_map_sprite=game_map_sprite,
                                     frog_position=frog_position,
                                     path_file=path_file)

    def run(self):
        while True:
            self.controller.events()
            self.controller.update()


if __name__ == '__main__':
    game = Game(game_map_sprite="images/Map.jpg", frog_position=(372, 280),
                path_file="path.txt")
    game.run()

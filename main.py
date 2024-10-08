import pygame
from controller import Controller
import os

"""
    Game - основыной класс, точка запучка программы
"""


class Game:

    def __init__(self, game_map_sprite, frog_position, path_file,
                 target_sprite, target_position):
        pygame.init()
        self.controller = Controller(game_map_sprite=game_map_sprite,
                                     frog_position=frog_position,
                                     path_file=path_file,
                                     target_sprite=target_sprite,
                                     target_position=target_position)

    def run(self):
        while True:
            self.controller.events()
            self.controller.update()


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    game = Game(game_map_sprite=f"{ROOT_DIR}/images/Map.jpg",
                frog_position=(372, 280),
                path_file="path.txt",
                target_sprite=f"{ROOT_DIR}/images/watermellon.png",
                target_position=(182, 322))
    game.run()

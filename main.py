import pygame
from gameMap import GameMap
from frog import Frog
from controller import Controller
from ball import Ball
from sequence import Sequence


class Game:

    def __init__(self, game_map_sprite, frog_position):
        pygame.init()
        game_map = GameMap(game_map_sprite=game_map_sprite)
        screen = game_map.get_screen()
        frog = Frog(screen=screen, frog_position=frog_position)
        self.controller = Controller(screen=screen, frog=frog, game_map=game_map)

    def run(self):
        while True:
            self.controller.events()
            self.controller.update()


if __name__ == '__main__':
    game = Game(game_map_sprite="images/Map.jpg", frog_position=(372, 280))
    game.run()

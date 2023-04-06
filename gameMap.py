import pygame


class GameMap:
    def __init__(self, game_map_sprite):
        self._image = pygame.image.load(game_map_sprite)
        self._rect = self._image.get_rect()
        pygame.display.set_caption("Zuma")
        self._screen = pygame.display.set_mode(self._rect.size)

    def draw_map(self):
        self._screen.blit(self._image, self._rect)

    def get_screen(self):
        return self._screen

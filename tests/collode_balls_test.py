import pygame
from ball import Ball
import sys
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class TestCollide:

    def __init__(self, game_map_sprite):
        pygame.init()
        self._image = pygame.image.load(game_map_sprite)
        self._rect = self._image.get_rect()
        pygame.display.set_caption("TestCollide")
        self._screen = pygame.display.set_mode(self._rect.size)
        self.target_ball = Ball(screen=self._screen, x=self._rect.centerx,
                                y=self._rect.centery, color="GREEN")
        self.ball_in_hand = Ball(screen=self._screen,
                                 x=pygame.mouse.get_pos()[0],
                                 y=pygame.mouse.get_pos()[1], color="GREEN")

    def move_ball_in_hand(self):
        self.ball_in_hand.move_ball(*pygame.mouse.get_pos())

    def run(self):
        while True:
            self._screen.blit(self._image, self._rect)
            pygame.draw.rect(self._screen, BLACK, self.target_ball.rect)
            pygame.draw.rect(self._screen, WHITE, self.ball_in_hand.rect)
            self.target_ball.draw_ball()
            self.ball_in_hand.draw_ball()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.move_ball_in_hand()
            if self.ball_in_hand.collode_balls(self.target_ball):
                print("Collide!!!")
            pygame.display.flip()


if __name__ == '__main__':
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    test_collide = TestCollide(game_map_sprite=f"{ROOT_DIR}/../images/Map.jpg")
    test_collide.run()

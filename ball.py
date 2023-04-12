import pygame
from random import randint
import math


DEFAULT_BALL_SIZE = 40
DEFAULT_SPEED = 10


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, color="RANDOM"):
        super().__init__()
        self.counter = 0
        self.screen = screen
        self.color = color
        if color == "GREEN":
            self.original_image = pygame.image.load('images/gball.png')
        elif color == "YELLOW":
            self.original_image = pygame.image.load('images/yball.png')
        elif color == "BLUE":
            self.original_image = pygame.image.load('images/bball.png')
        elif color == "RED":
            self.original_image = pygame.image.load('images/rball.png')
        else:
            i = randint(0, 3)
            if i == 0:
                self.color = "GREEN"
                self.original_image = pygame.image.load('images/gball.png')
            elif i == 1:
                self.color = "YELLOW"
                self.original_image = pygame.image.load('images/yball.png')
            elif i == 2:
                self.color = "BLUE"
                self.original_image = pygame.image.load('images/bball.png')
            else:
                self.color = "RED"
                self.original_image = pygame.image.load('images/rball.png')
        self.image = pygame.transform.scale(self.original_image,
                                            (DEFAULT_BALL_SIZE,
                                             DEFAULT_BALL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.angle = 0

    def collode_balls(self, other):
        return int(math.sqrt((other.rect.centerx
                              - self.rect.centerx) ** 2
                             + ((other.rect.centery
                                 - self.rect.centery) ** 2))) + 1 \
               < DEFAULT_BALL_SIZE

    def fly(self):
        self.rect.centerx += int(math.cos(self.angle) * DEFAULT_SPEED)
        self.rect.centery -= int(math.sin(self.angle) * DEFAULT_SPEED)
        if self.rect.x > self.screen.get_width() \
                or self.rect.x < -DEFAULT_BALL_SIZE \
                or self.rect.y > self.screen.get_height() \
                or self.rect.y < -DEFAULT_BALL_SIZE:
            self.kill()

    def move_ball(self, x, y):
        self.rect.center = x, y

    def draw_ball(self):
        self.screen.blit(self.image, self.rect)

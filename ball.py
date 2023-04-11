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
            self.image = pygame.image.load('images/gball.png')
        elif color == "YELLOW":
            self.image = pygame.image.load('images/yball.png')
        elif color == "BLUE":
            self.image = pygame.image.load('images/bball.png')
        elif color == "RED":
            self.image = pygame.image.load('images/rball.png')
        else:
            i = randint(0, 3)
            if i == 0:
                self.color = "GREEN"
                self.image = pygame.image.load('images/gball.png')
            elif i == 1:
                self.color = "YELLOW"
                self.image = pygame.image.load('images/yball.png')
            elif i == 2:
                self.color = "BLUE"
                self.image = pygame.image.load('images/bball.png')
            else:
                self.color = "RED"
                self.image = pygame.image.load('images/rball.png')
        self.image = pygame.transform.scale(self.image, (DEFAULT_BALL_SIZE,
                                                         DEFAULT_BALL_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.angle = 0

    def fly(self):
        self.rect.centerx += int(math.cos(self.angle) * DEFAULT_SPEED)
        self.rect.centery -= int(math.sin(self.angle) * DEFAULT_SPEED)
        if self.rect.x > self.screen.get_width() + 100 \
                or self.rect.x < -100 \
                or self.rect.y > self.screen.get_height() + 100 \
                or self.rect.y < -100:
            self.kill()

    def move_ball(self, x, y):
        self.rect.center = x, y

    def draw_ball(self):
        self.screen.blit(self.image, self.rect)

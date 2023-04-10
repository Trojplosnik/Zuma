import pygame
import math
from random import randint


DEFAULT_BALL_SIZE = 25


class Ball:
    def __init__(self, screen, x, y, color="RANDOM"):
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
        self.ball_rect = self.image.get_rect()
        self.ball_rect.centerx = x
        self.ball_rect.centery = y

    def collide_balls(self, ball):
        return math.sqrt(pow(ball.x - self.x, 2) + pow(ball.y - self.y, 2))\
               < pow(DEFAULT_BALL_SIZE, 2)

    def move_ball(self, x, y):
        self.ball_rect.move_ip(x - self.ball_rect.centerx,
                               y - self.ball_rect.centery)

    def draw_ball(self):
        self.screen.blit(self.image, self.ball_rect)

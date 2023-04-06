import pygame


DEFAULT_BALL_SIZE = (40, 40)

class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, color="g"):
        super(Ball, self).__init__()
        self.screen = screen
        self.color = color
        if color == "g":
            self.image = pygame.image.load('images/gball.png')
        elif color == "y":
            self.image = pygame.image.load('images/yball.png')
        elif color == "b":
            self.image = pygame.image.load('images/bball.png')
        elif color == "r":
            self.image = pygame.image.load('images/rball.png')
        self.image = pygame.transform.scale(self.image, DEFAULT_BALL_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

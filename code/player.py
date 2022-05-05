import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/Player.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH/2, HEIGHT/2))

        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.flipped = False

        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()

    def input(self):
        # player movement control
        keys = pygame.key.get_pressed()

        # up
        if keys[pygame.K_w]:
            self.direction.y = -1
        # down
        elif keys[pygame.K_s]:
            self.direction.y = 1
        # no movement along y
        else:
            self.direction.y = 0

        # right
        if keys[pygame.K_d]:
            self.direction.x = 1
        # left
        elif keys[pygame.K_a]:
            self.direction.x = -1
        # no movement along x
        else:
            self.direction.x = 0

    def move(self):
        # slowing diagonal speed
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # moving player
        self.rect.centerx += self.direction.x * self.speed
        self.rect.centery += self.direction.y * self.speed

    def flip(self):
        # updating cursor cords
        self.x_cursor, self.y_cursor = pygame.mouse.get_pos()

        # flipping player when cursor is moving
        if self.rect.centerx > self.x_cursor and self.flipped is False:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = True
        # flipping player back
        elif self.rect.centerx < self.x_cursor and self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = False

    def look(self, angle):

        # looks down
        if 340 >= angle >= 200:
            self.image = pygame.image.load('data/Player_down.png').convert_alpha()
            self.flipped = False

        # looks up
        elif 20 <= angle <= 160:
            self.image = pygame.image.load('data/Player_up.png').convert_alpha()
            self.flipped = False

        # looks ahead
        else:
            self.image = pygame.image.load('data/Player.png').convert_alpha()
            self.flipped = False

    def gun_cords(self):
        # giving data to gun.py
        return self.rect.centerx, self.rect.centery, self.flipped

    def update(self, angle):
        self.input()
        self.move()
        self.look(angle)
        self.flip()

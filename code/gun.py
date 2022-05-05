import pygame
import math
from player import Player


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.image = pygame.image.load('data/Gun.png').convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(self.player.rect.centerx+30, self.player.rect.centery))

        # location of gun on circle around a player
        self.offset_vector = pygame.math.Vector2(30, 0)
        self.offset_vector_copy = self.offset_vector

        self.flipped = False
        self.angle = 0

    def rotate(self, player_x, player_y):
        # calculating angle between player and cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        if self.angle < 0:
            self.angle += 360
        # calculating location of gun on circle
        self.offset_vector = self.offset_vector_copy.rotate(-self.angle)
        # rotating gun
        self.image = pygame.transform.rotate(self.original_image, int(self.angle))
        self.rect = self.image.get_rect(center=(player_x, player_y))
        # moving gun on circle
        self.rect.center += self.offset_vector

    def flip(self, flip):
        if flip and self.flipped is False:
            # flipping gun after player
            self.original_image = pygame.transform.flip(self.original_image, False, True)
            self.flipped = True

        elif flip is False and self.flipped:
            # flipping gun after player back to normal
            self.original_image = pygame.transform.flip(self.original_image, False, True)
            self.flipped = False

    def player_look_angle(self):
        # giving angle data to player.py
        return self.angle

    def bullet_data(self):
        return self.rect.centerx-5, self.rect.centery-5, self.angle, self.offset_vector

    def update(self, player_x, player_y, flip):
        self.rotate(player_x, player_y)
        self.flip(flip)

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

        # location of gun on circle around player
        self.offset_vector = pygame.math.Vector2(30, 0)
        self.offset_vector_copy = self.offset_vector

        self.flipped = False
        self.angle = 0
        self.recoil = 0
        self.ammo = 1

    def rotate(self, player_x, player_y, shot, flip):
        # calculating recoil
        if shot:
            self.recoil = 20
            if flip:
                self.recoil = -20
        else:
            self.recoil = 0

        # calculating angle between player and cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player_x, mouse_y - player_y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) + self.recoil
        if shot == 'no ammo':
            self.recoil = 20
            if flip:
                self.recoil = -20
        if self.angle < 0:
            self.angle += 360

        # calculating location of gun on circle
        self.offset_vector = self.offset_vector_copy.rotate(-self.angle)
        # rotating gun
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(player_x, player_y))
        # moving gun on circle
        self.rect.center += self.offset_vector

        self.ammo = 1

    def flip(self, flip):
        if flip and self.flipped is False:
            # flipping gun after player
            self.original_image = pygame.transform.flip(self.original_image, False, True)
            self.flipped = True

        elif flip is False and self.flipped:
            # flipping gun after player back to normal
            self.original_image = pygame.transform.flip(self.original_image, False, True)
            self.flipped = False

    def reload(self, flip, player_x, player_y):
        if flip:
            self.angle = 240
        else:
            self.angle = 300
        self.offset_vector = self.offset_vector_copy.rotate(-self.angle)
        # rotating gun
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(player_x, player_y))
        self.rect.center += self.offset_vector
        self.ammo = 0

    def player_look_angle(self):
        # giving angle and recoil values to player.py for look calculating
        return self.angle, self.recoil

    def bullet_data(self):
        # giving data to bullet.py
        return self.rect.centerx, self.rect.centery, self.angle, self.offset_vector

    def update(self, player_x, player_y, flip, shot):
        if shot == 'no ammo':
            self.reload(flip, player_x, player_y)
        else:
            self.rotate(player_x, player_y, shot, flip)
        self.flip(flip)


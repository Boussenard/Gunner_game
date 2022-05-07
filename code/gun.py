import pygame
import math
from player import Player


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.image = pygame.image.load('/home/boussenard/PycharmProjects/Gunner/data/Gun.png').convert_alpha()
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(self.player.rect.centerx+30, self.player.rect.centery))

        # location of gun on circle around player
        self.offset_vector = pygame.math.Vector2(30, 0)
        self.offset_vector_copy = self.offset_vector

        self.flipped = False
        self.angle = 0
        self.recoil = 0

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
        if self.angle < 0:
            self.angle += 360
        # calculating location of gun on circle
        self.offset_vector = self.offset_vector_copy.rotate(-self.angle)
        # rotating gun
        self.image = pygame.transform.rotate(self.original_image, self.angle)
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
        # giving angle and recoil values to player.py for look calculating
        return self.angle, self.recoil

    def bullet_data(self):
        # giving data to bullet.py
        return self.rect.centerx, self.rect.centery, self.angle, self.offset_vector

    def update(self, player_x, player_y, flip, shot):
        self.rotate(player_x, player_y, shot, flip)
        self.flip(flip)


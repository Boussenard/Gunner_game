import pygame
import sys
from settings import *
from player import Player
from gun import Gun
from cursor import Cursor
from bullet import Bullet
from interface import Interface


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Gunner')
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()

        # game objects
        self.player = Player()
        self.gun = Gun()
        self.cursor = Cursor()
        self.interface = Interface()

        # game groups
        self.bullet_group = pygame.sprite.Group()

    def run(self):
        while 1 == 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and self.gun.shot is False:
                    # adding bullet object into the group
                    self.bullet_group.add(Bullet(self.gun.rect.centerx, self.gun.rect.centery, self.gun.angle, self.gun.offset_vector))
                    # time of shot, start of recoil
                    self.gun.start_time = pygame.time.get_ticks()
                    self.gun.shot = True
                    # decrementing ammo value
                    self.gun.ammo -= 1

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((29, 29, 29))

            # updating objects ---------------------------------------------------------------- #
            self.player.update(self.gun.angle - self.gun.recoil)
            # updating data for gun
            self.gun.update(self.player.rect.centerx, self.player.rect.centery, self.player.flipped)
            self.cursor.update()
            self.interface.update(self.gun.shot)

            # updating groups ----------------------------------------------------------------- #
            self.bullet_group.update()

            # drawing game objects ------------------------------------------------------------ #
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.gun.image, self.gun.rect)
            self.screen.blit(self.cursor.image, self.cursor.rect)
            self.bullet_group.draw(self.screen)
            self.interface.interface_draw(self.screen, self.gun.ammo)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

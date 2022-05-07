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

        # gun recoil
        self.shot = False
        self.start_time = 0
        self.current_time = 0

    def run(self):
        while 1 == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # shooting
                elif event.type == pygame.MOUSEBUTTONDOWN and self.shot is False:
                    # adding bullet object into the group
                    x, y, angle, vector = self.gun.bullet_data()
                    self.bullet_group.add(Bullet(x, y, angle, vector))
                    # time of shot, start of recoil
                    self.start_time = pygame.time.get_ticks()
                    self.shot = True

            self.screen.fill((29, 29, 29))

            # waiting time to end recoil
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.start_time > 200:
                self.shot = False

            # updating objects
            self.player.update(self.gun.player_look_angle()[0], self.gun.player_look_angle()[1])
            # updating data for gun
            player_x, player_y, flip = self.player.gun_cords()
            self.gun.update(player_x, player_y, flip, self.shot)
            self.cursor.update()

            # updating groups
            self.bullet_group.update()

            # drawing game objects
            self.screen.blit(self.player.image, self.player.rect)
            self.screen.blit(self.gun.image, self.gun.rect)
            self.screen.blit(self.cursor.image, self.cursor.rect)
            self.bullet_group.draw(self.screen)
            self.interface.interface_draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

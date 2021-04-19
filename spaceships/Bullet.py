import pygame
import math


class Bullet(pygame.sprite.Sprite):

    def __init__(self, image_file, x,y,*bullets):
        pygame.sprite.Sprite.__init__(self,*bullets)
        self.image = pygame.transform.scale((pygame.image.load(image_file)),(20,20))
        self.rect = self.image.get_rect()
        self.rect.x = x + 15
        self.rect.y = y - 10
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


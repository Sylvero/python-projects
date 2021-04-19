import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, image_file, *all_sprites,):
        pygame.sprite.Sprite.__init__(self, *all_sprites,)
        self.image = pygame.transform.scale((pygame.image.load(image_file)), (40, 40))
        self.rect = self.image.get_rect()
        # self.rect.left, self.rect.top = location
        self.rect.x = random.randint(50, 950)
        self.rect.y = 30
        self.Xspeed = 5
        self.Yspeed = 50
        self.state = "alive"
        self.direction = ""

    def update(self):
        if self.rect.x < 0:
            self.direction = "right"
            self.rect.y += self.Yspeed
        elif self.rect.x > 950:
            self.direction = "left"
            self.rect.y += self.Yspeed

        if self.direction == "left":
            self.rect.x -= self.Xspeed
        else:
            self.rect.x += self.Xspeed


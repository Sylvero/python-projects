import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image_file)),(10,10))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.rectx = 0
        self.recty = 420
        self.speed = 5

    def shoot(self,x,y):
        while True:
            self.recty -= self.speed
            if self.recty < 0:
                pass

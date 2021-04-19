import pygame


class Player(pygame.sprite.Sprite):



    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image_file)),(50,50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.rectx = 350
        self.recty = 420
        self.speed = 3

    def move_right(self):
        self.rectx += self.speed

    def move_left(self):
        self.rectx -= self.speed
        


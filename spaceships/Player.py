import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load("images\spaceship.png")),(50,50))
        self.life_image = pygame.transform.scale((pygame.image.load("images\spaceship.png")),(20,20))
        self.life_image_rect = self.life_image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (500,670)
        self.speed = 0
        self.lifes = 3

    def update(self):
        self.speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.speed = 3
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.speed = -3
        self.rect.x += self.speed


    def show_lifes(self,screen):
        p = 20
        for i in range(0,self.lifes):
            screen.blit(self.life_image,(400+p,10))
            p += 20



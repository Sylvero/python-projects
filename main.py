import pygame
import sys
from Player import *
from Bullet import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption('Spaceships')
    img = pygame.image.load("images\Background.jpg")
    BackGround = pygame.transform.scale(img,(700,500))
    backdropbox = BackGround.get_rect()
    Player1 = Player("images\spaceship.png",(350,420))
    bullet = Bullet("images\Bullet.png", (Player1.rectx, Player1.recty - 10))
    pygame.display.flip()
    screen.blit(BackGround, backdropbox)
    clock = pygame.time.Clock()



    while True:
        screen.blit(BackGround, backdropbox)
        screen.blit(Player1.image,(Player1.rectx,Player1.recty))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.K_SPACE:
                bullet = Bullet("images\Bullet.png", (Player1.rectx, Player1.recty - 10))
                bullet.shoot(Player1.rectx, Player1.recty - 10)
                screen.blit(bullet.image, (Player1.rectx, Player1.recty - 10))
                pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            Player1.move_right()
        elif keys[pygame.K_a]:
            Player1.move_left()



        screen.blit(Player1.image, (Player1.rectx, Player1.recty))
        pygame.display.flip()
        clock.tick(60)









if __name__ == '__main__': main()


import pygame
import sys
from Player import *
from Bullet import *
from Enemy import *
import datetime

def text(screen,score):
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Score:'+ str(score), False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))



def main():
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((1000,700))
    pygame.display.set_caption('Spaceships')
    img = pygame.image.load("images\Background.jpg")
    BackGround = pygame.transform.scale(img,(1000,700))
    backdropbox = BackGround.get_rect()
    Player1 = Player()
    score = 0


    # enemy = Enemy("images\enemy.png")
    pygame.display.flip()
    screen.blit(BackGround, backdropbox)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    mobs_group = pygame.sprite.Group()
    all_sprites.add(Player1)
    start = pygame.time.get_ticks()
    now = pygame.time.get_ticks()
    hits = pygame.sprite.groupcollide(mobs_group, bullets_group, True, True)



    while True:

        hits = pygame.sprite.groupcollide(mobs_group, bullets_group, True, True)
        for hit in hits.items():
            score += 1

        now = pygame.time.get_ticks()
        screen.blit(BackGround, backdropbox)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullets_group.__len__() < 1:
                        bullet = Bullet("images\Bullet.png", Player1.rect.x, Player1.rect.y,bullets_group)

        if now - start > 1000:
            start = now
            mob = Enemy("images\enemy.png", all_sprites)
            mobs_group.add(mob)




        all_sprites.update()
        bullets_group.update()
        bullets_group.draw(screen)
        all_sprites.draw(screen)
        text(screen, score)
        Player1.show_lifes(screen)


        # screen.blit(Player1.image, (Player1.rectx, Player1.recty))

        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__': main()


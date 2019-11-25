


import pygame
from os import path
import time


img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 900 
HEIGHT = 650 
FPS = 60 


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    

    def __init__(self):
        

        pygame.sprite.Sprite.__init__(self)
        

        player_img = pygame.image.load(path.join(img_dir, "sniper.png")).convert()
        self.image = player_img

        self.image = pygame.transform.scale(player_img, (60, 48))
        

        self.image.set_colorkey(BLACK)
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #if self.rect.up > HEIGHT:
        #    self.rect.up = HEIGHT
        #if self.rect.down < 0:
         #   self.rect.down = 0


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'tela.png')).convert()
background_rect = background.get_rect()


player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)


try:
    

    running = True
    while running:
        

        clock.tick(FPS)
        

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_UP:
                    player.speedy = -8
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    time.sleep(0.1)
                    player.speedy = 4

        all_sprites.update()

            

           
    

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        

        pygame.display.flip()
        
finally:
    pygame.quit()

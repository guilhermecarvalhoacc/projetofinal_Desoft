


import pygame
from os import path


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

        self.speedy = random.randrange(0,8)


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
    

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        

        pygame.display.flip()
        
finally:
    pygame.quit()

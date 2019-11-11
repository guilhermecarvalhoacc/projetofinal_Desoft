import pygame
from os import path
import time
import random


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

class Mob1(pygame.sprite.Sprite):
    
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "bloco.jpg")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (300, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 550
        # Sorteia um lugar inicial em y
        self.rect.y = 400
class Mob2(pygame.sprite.Sprite):
    
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "bloco.jpg")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (300, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = 100
        # Sorteia um lugar inicial em y
        self.rect.y = 550
            





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
        self.pulando = 0

    def pula(self):
        self.pulando = 40

    def update(self):

        if self.pulando == 0:
            self.speedy = 0
        elif self.pulando > 20:
            self.speedy = -9
            self.pulando -= 1
        else:
            self.speedy = 9
            self.pulando -= 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.bottom < 53:
            self.rect.bottom = 53
 

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'tela.png')).convert()
background_rect = background.get_rect()

player = Player()

# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Cria um grupo só dos meteoros
mobs = pygame.sprite.Group()

# Cria 8 meteoros e adiciona no grupo meteoros
m1 = Mob1()
all_sprites.add(m1)
mobs.add(m1)
m2 = Mob2()
all_sprites.add(m2)
mobs.add(m2)

try:
    

    running = True
    while running:
        

        clock.tick(FPS)
        
        #print(player.rect.bottom)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                if event.key == pygame.K_UP:
                    if player.pulando == 0:
                        player.pula()
                




            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    pass

        all_sprites.update()

      

           
    

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        

        pygame.display.flip()
        
finally:
    pygame.quit()

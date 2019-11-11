import pygame
from os import path
import time
import random

balas = 10


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



class Plataforma(pygame.sprite.Sprite):

    def __init__(self,x,y,w,h):

        pygame.sprite.Sprite.__init__(self)

        plataforma_img = pygame.image.load(path.join(img_dir, "bloquinho_master.jpg")).convert()
        self.image = plataforma_img

        self.image = pygame.transform.scale(plataforma_img,(w,h))

        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y





class Player(pygame.sprite.Sprite):
    

    def __init__(self):

        
        

        pygame.sprite.Sprite.__init__(self)
        

        player_img = pygame.image.load(path.join(img_dir, "sniper.png")).convert()
        self.image = player_img

        self.image = pygame.transform.scale(player_img, (70, 70))
        

        self.image.set_colorkey(WHITE)
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0
        self.pulando = 0

    def pula(self):
        self.pulando = 30

    def update(self):

        #if self.pulando == 0:
        #    self.speedy = 9
        if self.pulando > 15:
            self.speedy = -9
            self.pulando -= 1
        elif contato:
            if player.rect.bottom > plataforma.rect.y and player.rect.bottom < (plataforma.rect.y + 10) :
                player.rect.bottom = plataforma.rect.y
            #self.speedy = 0     
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

class Bullet(pygame.sprite.Sprite):

    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)

        bullet_image = pygame.image.load(path.join(img_dir,"ammunition-305176_960_720.png")).convert()
        self.image = bullet_image

        self.image = pygame.transform.scale(bullet_image,(30,10))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.center = center

        self.speedx = -9


    def update(self):
        self.rect.x += self.speedx

class Bullet_laser(pygame.sprite.Sprite):

    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)

        bullet_laser_image = pygame.image.load(path.join(img_dir,"34623233ddb35cc.png")).convert()
        self.image = bullet_laser_image

        self.image = pygame.transform.scale(bullet_laser_image,(30,10))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.center = center

        self.speedx = -9


    def update(self):
        self.rect.x += self.speedx

class Laser_gun(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.player = None

        laser_gun_img = pygame.image.load(path.join(img_dir, "Alien_Laser_Rifle1.png"))
        self.image = laser_gun_img

        self.image = pygame.transform.scale(laser_gun_img,(50,50))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(0,WIDTH)
        self.rect.centery = 0

        self.speedx = 0
        self.speedy = 5

        #self.radius = int(self.rect.width * .85 / 2)

        self.game_clock = 1
    
    def set_player(self,player):
        self.player = player

    def update(self):
        if self.player is not None:
            self.rect.center = player.rect.center
        if self.rect.bottom < 640:
            self.rect.y += self.speedy


    


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'tela.png')).convert()
background_rect = background.get_rect()


player = Player()
plataforma = Plataforma(100,550,300,50)

all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
bullets = pygame.sprite.Group()
guns = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(plataforma)
plataformas.add(plataforma)


try:
    

    running = True
    while running:
        x = random.randint(1,500)
        if x == 3:
            y = random.randint(1,5)
            if y == 3:
                gun_laser = Laser_gun()
                all_sprites.add(gun_laser)
                guns.add(gun_laser)
        

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
                    elif contato:
                        player.pula()
                if event.key == pygame.K_SPACE:
                    if pegou_arma:
                        bullet_laser = Bullet_laser(player.rect.center)
                        all_sprites.add(bullet_laser)
                        bullets.add(bullet_laser)
                        balas -= 1
                    else:
                        bullet = Bullet(player.rect.center)
                        all_sprites.add(bullet)
                        bullets.add(bullet)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    pass


        contato = pygame.sprite.spritecollide(player, plataformas, False)
        pegou_arma = pygame.sprite.spritecollide(player,guns,False)
        for arma in pegou_arma:
            arma.set_player(player)

        if balas == 0:
            sem_balas = pygame.sprite.spritecollide(player,guns,True)
            if sem_balas:
                balas = 10
        # if contato:
        #         player.rect.bottom = contato[0].rect.top
                #player.rect.bottom = plataforma.rect.y


        
            

           
    
        all_sprites.update()

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        

        pygame.display.flip()
        
finally:
    pygame.quit()
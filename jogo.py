import pygame
from os import path
import time
import random

balas_1 = 10
balas_2 = 10


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

        self.w = w
        self.h = h

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

        self.lado = "esquerdo"
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2 + 200
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0
        self.pulando = 0

    def pula(self):
        self.pulando = 45

    def update(self):

        if self.pulando > 22:
            self.speedy = -9
            self.pulando -= 1
        elif contato:
            if self.rect.bottom > plataforma.rect.y and self.rect.bottom < (plataforma.rect.y + 10) :
                self.rect.bottom = plataforma.rect.y
            elif self.rect.bottom > (plataforma.rect.y +10) and self.rect.centerx < plataforma.rect.x + plataforma.w and self.rect.centerx > plataforma.rect.x + (plataforma.w - 10):
                self.rect.centerx = plataforma.rect.x + plataforma.w
            elif self.rect.bottom > (plataforma.rect.y +10) and self.rect.centerx > (plataforma.rect.x - 40) and self.rect.centerx < plataforma.rect.x +10:
                self.rect.centerx = plataforma.rect.x - 40    
        else:
            self.speedy = 9
            if self.pulando > 0:
                self.pulando -= 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx < 0:
            player_img = pygame.image.load(path.join(img_dir, "sniper.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img, (70, 70))
            self.image.set_colorkey(WHITE)
            self.lado = "esquerdo"
        elif self.speedx > 0:
            player_img = pygame.image.load(path.join(img_dir, "sniper2.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img, (70, 70))
            self.image.set_colorkey(WHITE)
            self.lado = "direito"
        

        if self.rect.right > WIDTH + 40 and self.speedx ==  8:
            self.rect.x = 0
        if self.rect.left < -40 and self.speedx == -8:
            self.rect.x = WIDTH
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.bottom < 53:
            self.rect.bottom = 53

class Player_2(pygame.sprite.Sprite):
    

    def __init__(self):

        
        

        pygame.sprite.Sprite.__init__(self)
        

        player2_img = pygame.image.load(path.join(img_dir, "um-quadrado-azul-grande-300x263.png")).convert()
        self.image = player2_img

        self.image = pygame.transform.scale(player2_img, (70, 70))
        

        self.image.set_colorkey(WHITE)

        self.lado = "esquerdo"
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2 - 200
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0
        self.pulando = 0

    def pula(self):
        self.pulando = 45

    def update(self):

        #if self.pulando == 0:
        #    self.speedy = 9
        if self.pulando > 22:
            self.speedy = -9
            self.pulando -= 1
        elif contato2:
            if self.rect.bottom > plataforma.rect.y and self.rect.bottom < (plataforma.rect.y + 10) :
                self.rect.bottom = plataforma.rect.y
            elif self.rect.bottom > (plataforma.rect.y +10) and self.rect.centerx < plataforma.rect.x + plataforma.w and self.rect.centerx > plataforma.rect.x + (plataforma.w - 10):
                self.rect.centerx = plataforma.rect.x + plataforma.w
            elif self.rect.bottom > (plataforma.rect.y +10) and self.rect.centerx > (plataforma.rect.x - 40) and self.rect.centerx < plataforma.rect.x +10:
                self.rect.centerx = plataforma.rect.x - 40
            #self.speedy = 0     
        else:
            self.speedy = 9
            if self.pulando > 0:
                self.pulando -= 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx < 0:
            player2_img = pygame.image.load(path.join(img_dir, "um-quadrado-azul-grande-300x263.png")).convert()
            self.image = player2_img
            self.image = pygame.transform.scale(player2_img, (70, 70))
            self.lado = "esquerdo"
        elif self.speedx > 0:
            player2_img = pygame.image.load(path.join(img_dir, "um-quadrado-azul-grande-300x263.png")).convert()
            self.image = player2_img
            self.image = pygame.transform.scale(player2_img, (70, 70))
            self.lado = "direito"
        

        if self.rect.right > WIDTH + 40 and self.speedx ==  8:
            self.rect.x = 0
        if self.rect.left < -40 and self.speedx == -8:
            self.rect.x = WIDTH
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

        self.speedx = -13


    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()
        if player.lado == "esquerdo" or player2.lado == "esquerdo":
            self.speedx = -13
        elif player.lado == "direito" or player2.lado == "direito":
            self.speedx = +13
            
class Bullet_laser(pygame.sprite.Sprite):

    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)

        bullet_laser_image = pygame.image.load(path.join(img_dir,"34623233ddb35cc.png")).convert()
        self.image = bullet_laser_image

        self.image = pygame.transform.scale(bullet_laser_image,(30,10))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.center = center

        self.speedx = -13


    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()
        if player.lado == "esquerdo" or player2.lado == "esquerdo":
            self.speedx = -13
        elif player.lado == "direito" or player2.lado == "direito":
            self.speedx = +13


class Laser_gun(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.player = None
        self.player2 = None

        laser_gun_img = pygame.image.load(path.join(img_dir, "Alien_Laser_Rifle1.png"))
        self.image = laser_gun_img

        self.image = pygame.transform.scale(laser_gun_img,(50,50))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(0,WIDTH)
        self.rect.centery = 0

        self.speedx = 0
        self.speedy = 5

        self.game_clock = 1
    
    def set_player(self,player):
        self.player = player
    
    def set_player2(self,player2):
        self.player2 = player2

    def update(self):
        if self.player is not None:
            self.rect.center = player.rect.center
        if self.player2 is not None:
            self.rect.center = player2.rect.center
        elif contato_arma and self.rect.bottom < (plataforma.rect.y + 10):
            if self.rect.bottom > plataforma.rect.y:
                self.rect.bottom = plataforma.rect.y + 5
        elif self.rect.bottom < 640:
            self.rect.y += self.speedy

        if player.lado == "esquerdo" or player2.lado == "esquerdo":
            laser_gun_img = pygame.image.load(path.join(img_dir, "Alien_Laser_Rifle1.png"))
            self.image = laser_gun_img
            self.image = pygame.transform.scale(laser_gun_img,(50,50))
            self.image.set_colorkey(BLACK)
        elif player.lado == "direito" or player2.lado == "direito":
            laser_gun_img = pygame.image.load(path.join(img_dir, "Alien_Laser_Rifle.png"))
            self.image = laser_gun_img
            self.image = pygame.transform.scale(laser_gun_img,(50,50))
            self.image.set_colorkey(BLACK)


    


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'tela.png')).convert()
background_rect = background.get_rect()


player = Player()
player2 = Player_2()
plataforma = Plataforma(250,480,450,50)

all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()
bullets = pygame.sprite.Group()
guns = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(plataforma)
plataformas.add(plataforma)


try:
    

    running = True
    while running:
        x = random.randint(1,200)
        if x == 3:
            y = random.randint(1,5)
            if y == 3:
                gun_laser = Laser_gun()
                all_sprites.add(gun_laser)
                guns.add(gun_laser)
        

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
                    if player.pulando == 0:
                        player.pula()
                    elif contato and player.rect.bottom >= plataforma.rect.y and player.rect.centerx < plataforma.rect.x + plataforma.w and player.rect.centerx > (plataforma.rect.x - 40):
                        player.pula()
                if event.key == pygame.K_l:
                    if pegou_arma:
                        bullet_laser = Bullet_laser(player.rect.center)
                        all_sprites.add(bullet_laser)
                        bullets.add(bullet_laser)
                        balas_1 -= 1
                    else:
                        bullet = Bullet(player.rect.center)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                if event.key == pygame.K_a:
                    player2.speedx = -8
                if event.key == pygame.K_d:
                    player2.speedx = +8
                if event.key == pygame.K_w:
                    if player2.pulando == 0:
                        player2.pula()
                    elif contato2 and player2.rect.bottom >= plataforma.rect.y and player2.rect.centerx < plataforma.rect.x + plataforma.w and player2.rect.centerx > (plataforma.rect.x - 40):
                        player2.pula()
                if event.key == pygame.K_SPACE:
                    if pegou_arma2:
                        bullet_laser = Bullet_laser(player2.rect.center)
                        all_sprites.add(bullet_laser)
                        bullets.add(bullet_laser)
                        balas_2 -= 1
                    else:
                        bullet = Bullet(player2.rect.center)
                        all_sprites.add(bullet)
                        bullets.add(bullet)
                

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_a:
                    player2.speedx = 0
                if event.key == pygame.K_d:
                    player2.speedx = 0
                if event.key == pygame.K_w:
                    pass


        contato = pygame.sprite.spritecollide(player, plataformas, False)
        contato2 = pygame.sprite.spritecollide(player2, plataformas, False)
        pegou_arma = pygame.sprite.spritecollide(player,guns,False)
        pegou_arma2 = pygame.sprite.spritecollide(player2,guns,False)
        contato_arma = pygame.sprite.groupcollide(plataformas,guns,False,False)

        for arma in pegou_arma:
            arma.set_player(player)
            if balas_1 == 0:
                arma.kill()
                balas_1 = 10

        for arma in pegou_arma2:
            arma.set_player2(player2)
            if balas_2 == 0:
                arma.kill()
                balas_2 = 10

                
        all_sprites.update()

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        

        pygame.display.flip()
        
finally:
    pygame.quit()
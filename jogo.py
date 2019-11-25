import pygame
from os import path
import time
import random
from setup import *

dano_p1 = 4
dano_p2 = 4 

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), "snd")

#criando a plataforma
class Plataforma(pygame.sprite.Sprite):

    def __init__(self,x,y,w,h):

        pygame.sprite.Sprite.__init__(self)

        self.w = w
        self.h = h

        plataforma_img = pygame.image.load(path.join(img_dir, "Imagem4.png")).convert()
        self.image = plataforma_img

        self.image = pygame.transform.scale(plataforma_img,(w,h))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
#criando jogador 1 
class Player(pygame.sprite.Sprite):
    

    def __init__(self, screen):
        #criando a tela do jogo 
        self.screen = screen 
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471.png")).convert()
        self.image = player_img

        self.image = pygame.transform.scale(player_img, (80, 90))
        self.image.set_colorkey(BLACK)

        self.lado = "direito"
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2 - 200
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0
        self.pulando = 0
        self.health = 200

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
            player_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471_1.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img, (80, 90))
            self.image.set_colorkey(BLACK)
            self.lado = "esquerdo"
        elif self.speedx > 0:
            player_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471.png")).convert()
            self.image = player_img
            self.image = pygame.transform.scale(player_img, (80, 90))
            self.image.set_colorkey(BLACK)
            self.lado = "direito"
        

        if self.rect.right > WIDTH + 40 and self.speedx ==  8:
            self.rect.x = 0
        if self.rect.left < -40 and self.speedx == -8:
            self.rect.x = WIDTH
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.bottom < 53:
            self.rect.bottom = 53

    def lifeBar(self):
        pygame.draw.rect(self.screen, (0,0,0), (45, 45, 210, 30))
        pygame.draw.rect(self.screen, (255,0,0), (50, 50, 200, 20))
        if self.health >= 0:
            pygame.draw.rect(self.screen, (0,255,0), (50, 50,self.health,20))        

#criando jogador 2 
class Player_2(pygame.sprite.Sprite):
    

    def __init__(self, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        player2_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471_B_1.png")).convert()
        self.image = player2_img

        self.image = pygame.transform.scale(player2_img, (80, 90))
        self.image.set_colorkey(BLACK)

        self.lado = "esquerdo"
        

        self.rect = self.image.get_rect()
        

        self.rect.centerx = WIDTH / 2 + 200
        self.rect.bottom = HEIGHT - 10

        self.speedy = 0
        self.speedx = 0
        self.pulando = 0
        self.health = 200

    def pula(self):
        self.pulando = 45

    def update(self):

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
        else:
            self.speedy = 9
            if self.pulando > 0:
                self.pulando -= 1

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx < 0:
            player2_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471_B_1.png")).convert()
            self.image = player2_img
            self.image = pygame.transform.scale(player2_img, (80, 90))
            self.image.set_colorkey(BLACK)
            self.lado = "esquerdo"
        elif self.speedx > 0:
            player2_img = pygame.image.load(path.join(img_dir, "kissclipart-cartoon-guy-with-gun-png-clipart-soldier-army-men-2bf3a53fc8702471_B.png")).convert()
            self.image = player2_img
            self.image = pygame.transform.scale(player2_img, (80, 90))
            self.image.set_colorkey(BLACK)
            self.lado = "direito"
        
        if self.rect.right > WIDTH + 40 and self.speedx ==  8:
            self.rect.x = 0
        if self.rect.left < -40 and self.speedx == -8:
            self.rect.x = WIDTH
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.bottom < 53:
            self.rect.bottom = 53
    def lifeBar(self):
        pygame.draw.rect(self.screen, (0,0,0), (645, 45, 210, 30))
        pygame.draw.rect(self.screen, (255,0,0), (650, 50, 200, 20))
        if self.health >= 0:
            pygame.draw.rect(self.screen, (0,255,0), (650,50,self.health,20))              
#criando a classe bala
class Bullet(pygame.sprite.Sprite):

    def __init__(self,center, bottom, id):
        pygame.sprite.Sprite.__init__(self)

        bullet_image = pygame.image.load(path.join(img_dir,"pngocean.com.png")).convert()
        self.image = bullet_image
        self.id = id

        self.image = pygame.transform.scale(bullet_image,(15,15))

        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        #center x, bottom y
        self.rect.center = center
        self.rect.bottom = bottom - 30

        if id == 1:
            if player.lado == "esquerdo":
                self.speedx = -13
            elif player.lado == "direito":
                self.speedx = 13

        if id == 2:
            if player2.lado == "esquerdo":
                self.speedx = -13
            elif player2.lado == "direito":
                self.speedx = 13

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()
#criando a classe da caixa para aumentar o poder de dano do tiro 
class Power_up(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        power_up_img = pygame.image.load(path.join(img_dir, "box-zebrawood.png")).convert()
        self.image = power_up_img

        self.image = pygame.transform.scale(power_up_img,(50,50))

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(0,WIDTH)
        self.rect.centery = 0

        self.speedx = 0
        self.speedy = 5

        self.game_clock = 1

    def update(self):

        if contato_box and self.rect.bottom < (plataforma.rect.y + 10):
            if self.rect.bottom > plataforma.rect.y:
                self.rect.bottom = plataforma.rect.y + 5

        elif self.rect.bottom < 640:
            self.rect.y += self.speedy

 
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")

clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'tela.png')).convert()
background_rect = background.get_rect()

bg_inicial = pygame.image.load(path.join(img_dir, 'imagem5.png')).convert()
bg_inicial_rect = bg_inicial.get_rect()
bg_inicial = pygame.transform.scale(bg_inicial, (900, 650))

shot_sound = pygame.mixer.Sound(path.join(snd_dir,"Gun+Silencer.wav"))
player_hurt = pygame.mixer.Sound(path.join(snd_dir,"Jab-SoundBible.com-1806727891.wav"))
box_destroyer = pygame.mixer.Sound(path.join(snd_dir,"Dropped Wooden Floor-SoundBible.com-382418821.wav"))

font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render('Player 1', True, BLACK)
textRect = text.get_rect()
textRect.center = (105,30)

text2 = font.render('Player 2', True, BLACK)
textRect2 = text.get_rect()
textRect2.center = (705,30)

player = Player(screen)
player2 = Player_2(screen)
plataforma = Plataforma(210,450,450,50)
ground = Plataforma(-50,640,1000,50)

all_sprites = pygame.sprite.Group()
plataformas = pygame.sprite.Group()

#grupo das balas
bullets = pygame.sprite.Group()
bullets2 = pygame.sprite.Group()

boxes = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(plataforma)
all_sprites.add(ground)
plataformas.add(plataforma)


tela_inicial = True
#loop principal 
try: 
    running = True
    while running:
        while tela_inicial:
            screen.fill(BLACK)
            screen.blit(bg_inicial, bg_inicial_rect)
            all_sprites.draw(screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   tela_inicial = False
                   running = False
                if event.type == pygame.KEYUP:
                    tela_inicial = False

        if len(boxes) <= 2:

            x = random.randint(1,200)
            if x == 3:
                y = random.randint(1,5)
                if y == 3:
                    box = Power_up()
                    all_sprites.add(box)
                    boxes.add(box)

        clock.tick(FPS)
        
        for event in pygame.event.get():


            if event.type == pygame.QUIT or player.health <= 0 or player2.health <=0:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    player.speedx = -8
                if event.key == pygame.K_d:
                    player.speedx = 8
                if event.key == pygame.K_w:
                    if player.pulando == 0:
                        player.pula()
                    elif contato and player.rect.bottom >= plataforma.rect.y and player.rect.centerx < plataforma.rect.x + plataforma.w and player.rect.centerx > (plataforma.rect.x - 40):
                        player.pula()
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.center, player.rect.bottom, 1)
                    all_sprites.add(bullet)
                    bullets2.add(bullet)
                    shot_sound.play()


                if event.key == pygame.K_LEFT:
                    player2.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player2.speedx = +8
                if event.key == pygame.K_UP:
                    if player2.pulando == 0:
                        player2.pula()
                    elif contato2 and player2.rect.bottom >= plataforma.rect.y and player2.rect.centerx < plataforma.rect.x + plataforma.w and player2.rect.centerx > (plataforma.rect.x - 40):
                        player2.pula()
                if event.key == pygame.K_l:
                    bullet = Bullet(player2.rect.center, player2.rect.bottom, 2)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    shot_sound.play()

                

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_d:
                    player.speedx = 0
                if event.key == pygame.K_w:
                    pass
                if event.key == pygame.K_LEFT:
                    player2.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player2.speedx = 0
                if event.key == pygame.K_UP:
                    pass

        #player e plafatforma
        contato = pygame.sprite.spritecollide(player, plataformas, False)
        #player2 e plataforma
        contato2 = pygame.sprite.spritecollide(player2, plataformas, False)

        #player1 e box
        pegou_power_up_p1 = pygame.sprite.groupcollide(bullets2,boxes,True,True)
        for box in pegou_power_up_p1: 
            dano_p1 += 0.5
            box_destroyer.play()

        #player2 e box
        pegou_power_up_p2 = pygame.sprite.groupcollide(bullets,boxes,True,True)
        for box in pegou_power_up_p2: 
            dano_p2 += 0.5
            box_destroyer.play()

        #colisao bala1 e bala2
        colisao_balas = pygame.sprite.groupcollide(bullets, bullets2, True, True)

        #colisao p1 e bala2
        bala2_p1 = pygame.sprite.spritecollide(player, bullets, False, pygame.sprite.collide_circle)
        for hit in bala2_p1:
            hit.kill() 
            player.health -= dano_p2
            player_hurt.play()    
        #colisao p2 e bala1
        bala1_p2 = pygame.sprite.spritecollide(player2, bullets2, False, pygame.sprite.collide_circle)
        for hit in bala1_p2:
            hit.kill()
            player2.health -= dano_p1
            player_hurt.play()
        #caixa e plataforma 
        contato_box = pygame.sprite.groupcollide(plataformas,boxes,False,False)
                
        all_sprites.update()
        
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)

        player.lifeBar()
        player2.lifeBar()

        if player.health <= 0 and player2.health > 0:
            mapa = pygame.image.load(path.join(img_dir, 'Imagem2.png')).convert()
            mapa_rect = mapa.get_rect()
            mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
            screen.blit(mapa, mapa_rect)
            pygame.display.flip()
            time.sleep(4)
        elif player2.health <= 0 and player.health > 0:
            mapa = pygame.image.load(path.join(img_dir, 'Imagem1.png')).convert()
            mapa_rect = mapa.get_rect()
            mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
            screen.blit(mapa, mapa_rect)
            pygame.display.flip()
            time.sleep(4)
        elif player2.health <= 0 and player.health <= 0:
            mapa = pygame.image.load(path.join(img_dir, 'Imagem3.png')).convert()
            mapa_rect = mapa.get_rect()
            mapa = pygame.transform.scale(mapa, (WIDTH, HEIGHT))
            screen.blit(mapa, mapa_rect)
            pygame.display.flip()

    

        pygame.display.flip()
        
finally:
    pygame.quit()



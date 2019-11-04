import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 480
HEIGHT = 600 
FPS = 60 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Mata-Mata")


clock = pygame.time.Clock()


background = pygame.image.load(path.join(img_dir, 'sniper.jpg')).convert()
background_rect = background.get_rect()

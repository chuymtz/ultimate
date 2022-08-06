import pygame
from sys import exit
from py.utils import read_game_config

# Config variables
vars = read_game_config('config.yml')
FPS = vars['clock']['timeframe']
HEIGHT = vars['screen']['height']
WIDTH = vars['screen']['width']

# Screen configs  --------------------------------------------------------------------+   
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ultimate')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50 )


# surfaces --------------------------------------------------------------------+
sky_surf = pygame.image.load('graphics/sky.png')
ground_surf = pygame.image.load('graphics/ground.png')
text_surf = test_font.render('Hola Chuy', False, 'Black')

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    screen.blit(text_surf, (300, 50))    
    
    pygame.display.update()
    clock.tick(FPS)

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

# surfaces --------------------------------------------------------------------+

test_font = pygame.font.Font('font/Pixeltype.ttf', 50 )
text_surf = test_font.render('Hola Chuy', False, 'Black')

sky_surf = pygame.image.load('graphics/sky.png')
ground_surf = pygame.image.load('graphics/ground.png')

# CHARACTERS ----------------------------------------------------------------------------+

snail_surf = pygame.image.load('graphics/snail/snail1.png')
snail_width, snail_height = snail_surf.get_size()
snail_x = 200
snail_y = 275
snail_step = -4


# Game loop ----------------------------------------------------------------------------+
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    screen.blit(text_surf, (300, 50))    
    
    screen.blit(snail_surf, (snail_x, snail_y))    
    
    snail_x += snail_step
    
    if snail_x <= -snail_width:
        snail_x = WIDTH + snail_width
    
    
    pygame.display.update()
    clock.tick(FPS)

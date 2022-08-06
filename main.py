import pygame
from sys import exit
from py.utils import read_game_config

def main():
    # Config variables
    vars = read_game_config('config.yml')
    FPS = vars['clock']['timeframe']
    HEIGHT = vars['screen']['height']
    WIDTH = vars['screen']['width']
    
    # Screen    
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption('Ultimate')
    clock = pygame.time.Clock()
    
    # surfaces
    
    test_surface = pygame.Surface((vars['surfaces']['test']['height'],
                                   vars['surfaces']['test']['width']))
    test_surface.fill(color = vars['surfaces']['test']['color'])
    
    # Game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(test_surface, (vars['surfaces']['test']['x'],
                                   vars['surfaces']['test']['y']))
        pygame.display.update()
        clock.tick(FPS)

    
if __name__ == '__main__':
    main()
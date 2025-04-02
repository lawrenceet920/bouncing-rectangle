# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config
import random

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def draw_rect(screen, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
def draw_text(screen, text, color, location, font_name='FreeMono.ttf', font_size=30, bold=False, italic=False):
    font = pygame.font.Font(font_name, font_size)
    font.set_bold(bold)
    font.set_italic(italic)

    text = font.render(text, True, color)
    screen.blit(text, location)


def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    square_info = {
        'color' : (255, 0 , 255),
        'size' : 50,
        'speed' : [5, 5],
        'location' : [random.randint(50, 750), random.randint(50, 550)]
    }
    while running:
        running = handle_events()
        screen.fill(config.WHITE)

        # Square
        if not (0 < square_info['location'][0] < config.WINDOW_WIDTH - square_info['size']):
            square_info['speed'][0] *= -1
        if not (0 < square_info['location'][1] < config.WINDOW_HEIGHT - square_info['size']):
            square_info['speed'][1] *= -1

        square_info['location'][0] += square_info['speed'][0]
        square_info['location'][1] += square_info['speed'][1]

        draw_rect(screen, square_info['color'], square_info['location'][0], square_info['location'][1], square_info['size'], square_info['size'])

        # Text
        draw_text(screen, 'Ethan Lawrence', config.BLACK, [50, 50], bold=True)
        draw_text(screen, 'Carrer Tech', config.BLUE, [50, 100])
        draw_text(screen, 'Animated Shape', config.RED, [50, 150], font_size=25, italic=True)

        pygame.display.flip()
        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()
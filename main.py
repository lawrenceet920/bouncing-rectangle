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
    squares = {}
    square_ct = 1
    squares['square 1'] = {
        'color' : (255, 0 , 255),
        'size' : 50,
        'speed' : [5, 5],
        'location' : [random.randint(0, 750), random.randint(0, 550)]
    }
    count_to_keyframe = 0
    while running:
        running = handle_events()
        screen.fill((200, 200, 200))


        count_to_keyframe += 1
        if count_to_keyframe == config.FPS/6:
            count_to_keyframe = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                square_ct += 1
                squares[f'square {square_ct}'] = {
                    'color' : (random.randint(0,225), random.randint(0,225), random.randint(0,225)),
                    'size' : random.randint(25,75),
                    'speed' : [random.randint(-7,7), random.randint(-7,7)],
                    'location' : [random.randint(0, 700), random.randint(0, 500)]
                }

        # Square
        del_list = []
        for square in squares:
            # Mouse
            mouse_pos = pygame.mouse.get_pos()
            this_square = pygame.Rect(squares[square]['location'][0], squares[square]['location'][1], squares[square]['size'], squares[square]['size'])
            if this_square.collidepoint(mouse_pos):
                del_list.append(square)

            if not (0 < squares[square]['location'][0] < config.WINDOW_WIDTH-1 - squares[square]['size']):
                squares[square]['speed'][0] *= -1
            if not (0 < squares[square]['location'][1] < config.WINDOW_HEIGHT-1 - squares[square]['size']):
                squares[square]['speed'][1] *= -1

            squares[square]['location'][0] += squares[square]['speed'][0]
            squares[square]['location'][1] += squares[square]['speed'][1]

            draw_rect(screen, squares[square]['color'], squares[square]['location'][0], squares[square]['location'][1], squares[square]['size'], squares[square]['size'])
        for square in del_list:
            del(squares[square])
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
import pygame
from sys import exit
from buttonClass import Button
from tileClass import Tile, manual_place, RightTile

WIDTH, HEIGHT = 1900, 1050
CENTER = (WIDTH // 2, HEIGHT // 2)
display = pygame.display.set_mode((WIDTH, HEIGHT))
gameState = 'menu'


def quit_game():
    pygame.quit()
    exit()


startButton = Button(pygame.Surface((400, 250)), CENTER)


def draw_axis(steps):
    for x in range(0, WIDTH, steps):
        pygame.draw.line(display, (255, 255, 255), (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, steps):
        pygame.draw.line(display, (255, 255, 255), (0, y), (WIDTH, y))


step = 50
'''tiles = [Tile(pos=(x, y), surf=pygame.Surface((step, step)), color=(0, 125, 0)) for x in range(0, WIDTH, step) for y in
         range(0, HEIGHT, step)]'''

tiles = [[Tile(pos=(x, y), surf=pygame.Surface((step, step)), color=(0, 125, 0)) for y in range(0, HEIGHT, step)] for x in range(0, WIDTH, step)]
print(len(tiles), len(tiles[0]))
tiles[15][18].set_sub_tile(RightTile(tiles[15][18]))

clock = pygame.time.Clock()
FPS = 60
while 1:
    clock.tick(FPS)
    display.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_game()

    if gameState == 'menu':
        startButton.draw(display)
        if startButton.check_click_state_surf():
            gameState = 'lvl1'

    if gameState == 'lvl1':
        draw_axis(step)
        manual_place(tiles)

        for row in tiles:
            for tile in row:
                tile.draw(display)


    pygame.display.update()

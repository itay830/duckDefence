import pygame
from sys import exit
from buttonClass import Button
from tileClass import Tile, manual_place, RightTile
from pickleData import *

WIDTH, HEIGHT = 1900, 1050
CENTER = (WIDTH // 2, HEIGHT // 2)
display = pygame.display.set_mode((WIDTH, HEIGHT))
gameState = 'menu'


def quit_game():
    pygame.quit()
    exit()


startButton = Button(pygame.Surface((400, 250)), CENTER)
createMapButton = Button(pygame.Surface((200, 200)), (400, 400))

def draw_axis(steps):
    for x in range(0, WIDTH, steps):
        pygame.draw.line(display, (255, 255, 255), (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, steps):
        pygame.draw.line(display, (255, 255, 255), (0, y), (WIDTH, y))


step = 50

tiles = [[Tile(pos=(x, y), surf=pygame.Surface((step, step)), color=(0, 125, 0)) for y in range(0, HEIGHT, step)] for x in range(0, WIDTH, step)]

clock = pygame.time.Clock()
FPS = 60
while 1:
    clock.tick(FPS)
    display.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_game()

    if gameState == 'menu':
        if startButton.check_click_state_surf():
            gameState = 'lv1'
        if createMapButton.check_click_state_surf():
            gameState = 'mapCreator'
        startButton.draw(display)
        createMapButton.draw(display)

    if gameState == 'mapCreator':
        draw_axis(step)
        manual_place(tiles)

        for row in tiles:
            for tile in row:
                tile.draw(display)


    pygame.display.update()

import pygame
from abc import ABC, abstractmethod
from typing import Callable

pygame.font.init()

font = pygame.font.SysFont("verdana", 10, True, False)


class Tile:
    def __init__(self, pos: tuple[int, int], surf: pygame.Surface, color):
        self.size = surf.get_width()
        self.surf = surf
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)
        self.txt = font.render(f"({pos[0]//self.size}, {pos[1]//self.size})", False, (255, 255, 255))
        self.txtRect = self.txt.get_rect(center=self.rect.center)
        self.subTile = self

    def draw(self, display: pygame.Surface):
        display.blit(self.surf, self.rect)
        display.blit(self.txt, self.txtRect)

    def set_sub_tile(self, sub_tile: object):
        self.subTile = sub_tile

    def logic(self):
        self.subTile.logic()


class MockTile(ABC):
    def __init__(self, tile: Tile):
        self.tile = tile

    @abstractmethod
    def logic(self):
        pass

    def get_dressed(self, color):
        self.tile.surf.fill(color)


class RightTile(MockTile):
    def __init__(self, tile: Tile):
        MockTile.__init__(self, tile)
        self.get_dressed((255, 0, 125))

    def logic(self):
        ...


def manual_place(tiles: set[Tile]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    for row in tiles:
        for tile in row:
            if tile.rect.collidepoint(mouse_pos):
                tile.surf.set_alpha(125)
                if mouse_pressed:
                    tile.set_sub_tile(RightTile(tile))

            else:
                tile.surf.set_alpha(255)

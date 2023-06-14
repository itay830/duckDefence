import pygame
from abc import ABC, abstractmethod
from typing import Union

pygame.font.init()

font = pygame.font.SysFont("verdana", 10, True, False)


class Tile:
    def __init__(self, pos: Union[tuple[int, int], pygame.Vector2], surf: pygame.Surface, color):
        self.size = surf.get_width()
        self.surf = surf
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)
        self.txt = font.render(f"({int(pos[0]) // self.size}, {int(pos[1]) // self.size})", False, (255, 255, 255))
        self.txtRect = self.txt.get_rect(center=self.rect.center)
        self.subTile = BlankTile(self)

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


class BlankTile(MockTile):
    def __init__(self, tile):
        MockTile.__init__(self, tile)

    def logic(self) -> None:
        return


class MoveTile(MockTile):
    def __init__(self, tile: Tile):
        MockTile.__init__(self, tile)
        self.get_dressed((255, 0, 125))

    def logic(self):
        ...


class TileMap:
    def __init__(self, tile_map: list[list[Tile]]):
        self.tiles = tile_map

        self.constSurfMap = pygame.Surface((0, 0))

    def draw_tiled_map(self, display: pygame.Surface) -> pygame.Surface:
        for row in self.tiles:
            for tile in row:
                tile.draw(display)

        return display.copy()

    def draw_const_map(self, display: pygame.Surface) -> None:
        display.blit(self.constSurfMap, (0, 0))

    def create_map_image(self, width: int, height: int) -> None:
        self.constSurfMap = self.draw_tiled_map(pygame.Surface((width, height)))

    def get_tile(self, pos: Union[pygame.Vector2, tuple[int, int]]) -> Tile:
        return self.tiles[int(pos[1])][int(pos[0])]


def create_map_with_csv(csv_data: list[list[str]], step: int) -> TileMap:
    tiles = []
    offset = pygame.Vector2(0, 0)

    for row in csv_data:
        tile_row = []
        for index in row:
            index = int(index)
            if index == 0:
                tile = Tile(offset, pygame.Surface((step, step)), (0, 128, 0))
                tile_row.append(tile)

            if index == 1:
                tile = Tile(offset, pygame.Surface((step, step)), (0, 128, 0))
                tile.set_sub_tile(MoveTile(tile))
                tile_row.append(tile)
            offset.x += step
        tiles.append(tile_row)
        offset.y += step
        offset.x = 0

    return TileMap(tiles)


def manual_place(tiles: list[list[Tile]]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    for row in tiles:
        for tile in row:
            if tile.rect.collidepoint(mouse_pos):
                tile.surf.set_alpha(125)
                if isinstance(tile.subTile, BlankTile):
                    tile.set_sub_tile(MoveTile(tile))

                else:
                    tile.set_sub_tile(BlankTile(tile))
                    tile.surf.fill((0, 128, 0))

            else:
                tile.surf.set_alpha(255)

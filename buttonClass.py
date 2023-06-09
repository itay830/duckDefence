import pygame


class Button:
    def __init__(self, surf: pygame.Surface, pos: tuple[int, int]):
        self.clickState = False
        self.held = False
        self.surf = surf
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=pos)

    def check_click_state_surf(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.clickState = False
            self.surf.fill((0, 0, 255))

            if self.held and not pygame.mouse.get_pressed()[0]:
                self.clickState = True

            if pygame.mouse.get_pressed()[0]:
                self.held = True
                self.surf.fill((0, 255, 0))
            else:
                self.held = False
        else:
            self.clickState = False
            self.held = False
            self.surf.fill((255, 0, 0))

        return self.clickState

    def draw(self, display):
        display.blit(self.surf, self.rect)
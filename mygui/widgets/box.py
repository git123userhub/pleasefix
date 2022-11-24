import pygame
from mygui import graphics

class Box(pygame.Surface):
    def __init__(self, master, size, position, background, bordercolor, borderwidth, cornerradius):
        super().__init__([x+2 for x in size], pygame.SRCALPHA, 32)

        self.master = master
        self.rect = pygame.Rect([x+y for x, y in zip(master.get_abs_offset(), position)], size)
        self.relpos = position

        self.background = background
        self.bordercolor = bordercolor
        self.borderwidth = borderwidth
        self.cornerradius = cornerradius

    def _render(self):
        pos = [self.borderwidth]*2
        size = [x-self.borderwidth*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self.background, self.cornerradius-1)
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self.bordercolor, self.cornerradius)

        return main_body, border_rect

    def place(self):
        render_rect = self._render()

        render_rect[1].draw()
        render_rect[0].draw()

        self.master.blit(self, self.relpos)
import pygame
from pygame import gfxdraw
import mygui

win = pygame.display.set_mode((800, 450))

box = mygui.widgets.Box(win, (200, 30), (100, 100), 'white', 'grey', 2, 8)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.fill("white")

    box.place()

    pygame.display.update()

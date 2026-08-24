import pygame
import sys

pygame.init()

FULL_HD_RESOLUTION = (1920, 1080)
BACKGROUND_COLOR = (0,0,0)

screen = pygame.display.set_mode(FULL_HD_RESOLUTION)

running = True
while (running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.display.flip()

pygame.quit()
sys.exit()
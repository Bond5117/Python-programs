import pygame
import random
import math
clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((1250,1250))
pygame.display.set_caption("pygame_test")

t = 0

running = True
while running:
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t += 0.02
    #screen.fill((0, 0, 0))
    r = 128 + 127 * math.sin(t)
    g = 128 + 127 * math.sin(t + 2 + 0 * math.pi/2)
    b = 128 + 127 * math.sin(t + 4 + 0 * math.pi)
    pygame.draw.rect(screen, (int(r), int(g), int(b)), (312.5 + r, 312.5 + g, 50, 50))
    #pygame.draw.line(screen, (int(r), int(g), int(b)), (50 + r, 50 + g), (50 + g, 50 + b), 1)
    pygame.display.flip()

pygame.quit
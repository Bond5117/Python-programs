#Import libraries
import pygame
import math
clock = pygame.time.Clock()
pygame.init()

#Independent variables
width = 1200
length = 800
screen = pygame.display.set_mode((width, length))
screen.fill((0, 0, 0))
theta = math.pi / 16
og_theta = theta
radius = 125 * math.pi / 16
og_radius = radius
rotation_speed = math.pi / 16
shrink_speed = 0.95
t = 0
old_x = width / 2
old_y = length / 2 + radius
line_width = 2
center_x = width / 2
center_y = length / 2
paused = False

#Main loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT: #Tab close
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r: #R key resets spiral
                screen.fill((0, 0, 0))
                theta = og_theta
                radius = og_radius
                t = 0
                old_x = width / 2
                old_y = length / 2 + radius

            if event.key == pygame.K_SPACE: #Spacebar pauses spiral
                paused = not paused

    if not paused: #Spiral animation
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        r = 128 + 127 * math.sin(t)
        g = 128 + 127 * math.sin(t + 2)
        b = 128 + 127 * math.sin(t + 4)
        pygame.draw.line(screen, (int(r), int(g), int(b)), (old_x, old_y), (x, y), line_width)
        theta -= rotation_speed
        radius *= shrink_speed
        t += 0.01
        old_x = x
        old_y = y
        pygame.display.flip()
pygame.quit #Closes tab/quits program
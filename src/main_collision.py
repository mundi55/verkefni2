#main-forrit sem inniheldur collision, reyna að koma árekstrarhlutanum yfir í sérklasa - ATH! kóði virkar ekki í núverandi mynd
import sys
import numpy as np
import pygame
import math
from pygame.locals import *

# set up the colors (RGB - red-green-blue values)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# set up pygame
pygame.init()

# set up the window
xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

n = 50 # Number of points
speed = 0.01
radius = 5

# Initial coordinates are uniformly random in (0, 1)
x = np.random.rand(n)
y = np.random.rand(n)
status = np.zeros(n)

# Point velocity is uniformly random in (0, speed)
vx = speed * np.random.rand(n)
vy = speed * np.random.rand(n)

# run the main loop
while True:
    # Clear screen
    windowSurface.fill(WHITE)

    # Update positions
    for i in range(n):
        # Reverse directon if point hits the boundary
        if x[i] < 0 or x[i] > 1:
            vx[i] = -1 * vx[i]
        if y[i] < 0 or y[i] > 1:
            vy[i] = -1 * vy[i]
        x[i] += vx[i]
        y[i] += vy[i]

    for i in range(n):
        for j in range(i+1,n):
            dist = math.sqrt(math.pow(x[i] - x[j],2) + math.pow(y[i] - y[j], 2))
            if dist < 2 * radius/xmax:
                if status[i] == 1:
                    status[j] = 1
                    #pygame.draw.circle(windowSurface, RED, \
                    #           (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
                if status[j] == 1:
                    status[i] = 1
                    #pygame.draw.circle(windowSurface, RED, \
                    #           (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
            

    # Redraw
    for i in range(n):
        if status[i] == 0:
            pygame.draw.circle(windowSurface, BLUE, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
        elif status[i] == 1:
            pygame.draw.circle(windowSurface, RED, \
                               (int(xmax * x[i]), int(ymax * y[i])), radius, 0)


    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
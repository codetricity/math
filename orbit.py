import sys, pygame
import math
import random

pygame.init()

FPS = 30
clock = pygame.time.Clock()

RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
circle_color = WHITE


SCREEN = pygame.display.set_mode((800, 600))

CENTER = (400, 300)
length = 200

x = CENTER[0] + length
y = CENTER[1] 


angle = 0

max_delay = 6
current_delay = max_delay


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)




    if current_delay > 0:
        current_delay -= 1
    else:
        current_delay = max_delay



        rad = math.radians(angle)
        lengthx = math.cos(rad) * 200
        lengthy = math.sin(rad) * 200

        _x = int(400 + lengthx)
        _y = int(300 - lengthy)

        pygame.draw.circle(SCREEN, RED, CENTER, 10 )
        pygame.draw.circle(SCREEN, circle_color, (_x, _y), 10)
        pygame.draw.line(SCREEN, WHITE, CENTER, (_x, _y), 1)
        if angle < 360:
            angle += 10
        else:
            circle_color = [random.randrange(0, 200),
                            random.randrange(0, 200),
                            random.randrange(0, 200)]
            angle = 0

    clock.tick(FPS)
    pygame.display.update()

import sys, pygame
import math
import random

pygame.init()

FPS = 50
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
speed = 1

max_delay = 0
current_delay = max_delay

direction = "left"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex = pygame.mouse.get_pos()[0]
            if mousex > 400 and mousex < 800:
                direction = "right"
            elif mousex < 400 and mousex > 0:
                direction = "left"




    if current_delay > 0:
        current_delay -= 1
    else:
        current_delay = max_delay


        
        angle2 = angle + 120
#        if angle2 > 360:
#            angle2 = 360 - angle2

        angle3 = angle + 240
#        if angle3 > 360:
#            angle3 = 360 - angle3
        

        rad = math.radians(angle)
        lengthx = math.cos(rad) * 200
        lengthy = math.sin(rad) * 200

        rad2 = math.radians(angle2)
        lengthx2 = math.cos(rad2) * 200
        lengthy2 = math.sin(rad2) * 200


        rad3 = math.radians(angle3)
        lengthx3 = math.cos(rad3) * 200
        lengthy3 = math.sin(rad3) * 200



        _x = int(400 + lengthx)
        _y = int(300 - lengthy)

        _x2 = int(400 + lengthx2)
        _y2 = int(300 - lengthy2)

        _x3 = int(400 + lengthx3)
        _y3 = int(300 - lengthy3)


        SCREEN.fill(BLACK)
        pygame.draw.circle(SCREEN, RED, CENTER, 10 )
        pygame.draw.circle(SCREEN, circle_color, (_x, _y), 10)
        pygame.draw.circle(SCREEN, circle_color, (_x2, _y2), 10)
        pygame.draw.circle(SCREEN, circle_color, (_x3, _y3), 10)
        pygame.draw.polygon(SCREEN, RED, ((_x, _y), (_x2, _y2), (_x3, _y3)), 2)

        if angle > -360 and angle < 360:
            if direction == "left":
                angle += speed
            elif direction == "right":
                angle -= speed
        else:
            circle_color = [random.randrange(0, 200),
                            random.randrange(0, 200),
                            random.randrange(0, 200)]
            angle = 0

    clock.tick(FPS)
    pygame.display.update()

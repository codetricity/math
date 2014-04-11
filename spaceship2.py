import sys, pygame
import math
import random

class Bullet(pygame.sprite.Sprite):
    def __init__(self, dist, ship_center, radian):
        pygame.sprite.Sprite.__init__(self)
        color = (255, 0, 0)
        self.image = pygame.Surface((6, 6))
        self.distance = dist
        self.radian = radian
        self.ship_center = ship_center
        self.rect = pygame.draw.circle(self.image, color, (3, 3), 3)
        self.speed = 2
        
    def update(self):
        self.distance = self.distance + self.speed
        self._x = math.cos(self.radian) * self.distance
        self._y = math.sin(self.radian) * self.distance
        self.x = int(ship_center[0] + self._x)
        self.y = int(ship_center[1] - self._y)
        self.rect.center = (self.x, self.y)

        

pygame.init()

FPS = 50
clock = pygame.time.Clock()

RED = (200, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (241, 172, 37)
LIGHT_BLUE = (149, 239, 248)

circle_color = WHITE

SIZE = (800, 600)

SCREEN = pygame.display.set_mode(SIZE)

CENTER = [400, 300]
ship_center = CENTER
size = 40

x = CENTER[0] + size
y = CENTER[1] 


angle = 0
speed = 1

thrust_max_delay = 3
thrust_delay = thrust_max_delay

max_delay = 0
current_delay = max_delay

direction = "left"
move_forward = False

bullet_group = pygame.sprite.Group()
fire = False
bullet_distance = 0

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire = True
            elif event.key == pygame.K_UP:
                move_forward = True
        elif event.type == pygame.KEYUP:
            move_forward = False
            fire = False
                
    if current_delay > 0:
        current_delay -= 1
    else:
        current_delay = max_delay
        
        angle2 = angle + 120
        angle3 = angle + 240

        rad = math.radians(angle)
        lengthx = math.cos(rad) * size
        lengthy = math.sin(rad) * size

        bulletx = math.cos(rad) * size * 2
        bullety = math.sin(rad) * size * 2

        rad2 = math.radians(angle2)
        lengthx2 = math.cos(rad2) * size
        lengthy2 = math.sin(rad2) * size


        rad3 = math.radians(angle3)
        lengthx3 = math.cos(rad3) * size
        lengthy3 = math.sin(rad3) * size


        _x = int(ship_center[0] + lengthx)
        _y = int(ship_center[1] - lengthy)

        _bulletx = int(ship_center[0] + bulletx)
        _bullety = int(ship_center[1] - bullety )

        if fire:
            bullet = Bullet(size + bullet_distance, ship_center, rad)
            bullet_group.add(bullet)
            fire = False

        bullet_group.update()

        _x2 = int(ship_center[0] + lengthx2)
        _y2 = int(ship_center[1] - lengthy2)

        _x3 = int(ship_center[0] + lengthx3)
        _y3 = int(ship_center[1] - lengthy3)

        mid_x = int((ship_center[0] + _x) /2)
        mid_y = int((ship_center[1] + _y) / 2)
        quarter_x = int((ship_center[0] + mid_x) / 2)
        quarter_y = int((ship_center[1] + mid_y) / 2)
        move_x = int((ship_center[0] + quarter_x) / 2)
        move_y = int((ship_center[1] + quarter_y) / 2)

        thrust_x = (_x2 + _x3) / 2
        thrust_y = (_y2 + _y3) / 2

        SCREEN.fill(BLACK)

        if move_forward:
            ship_center = [move_x, move_y]
            pygame.draw.circle(SCREEN, ORANGE, (thrust_x, thrust_y), 10, 1)
            if thrust_delay > 0:
                thrust_delay -= 1
            else:
                thrust_delay = thrust_max_delay
                pygame.draw.circle(SCREEN, LIGHT_BLUE, (thrust_x, thrust_y), 5, 1)
                    
                pygame.draw.circle(SCREEN, BLACK, (thrust_x, thrust_y), 10, 1)

        pygame.draw.polygon(SCREEN, RED, ((_x, _y), (_x2, _y2), ship_center, (_x3, _y3)), 2)

        bullet_group.draw(SCREEN)

     
#        pygame.draw.circle(SCREEN, RED, (_bulletx, _bullety), 3)

        if ship_center[0] < 0:
            ship_center[0] = SIZE[0]
        elif ship_center[0] > SIZE[0]:
            ship_center[0] = 0
        if ship_center[1] < 0:
            ship_center[1] = SIZE[1]
        elif ship_center[1] > SIZE[1]:
            ship_center[1] = 0


        if angle > -360 and angle < 360:
            if direction == "left":
                angle += speed
            elif direction == "right":
                angle -= speed
        else:
            angle = 0

    clock.tick(FPS)
    pygame.display.update()

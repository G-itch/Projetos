"""
import pygame
import keyboard
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pyg/ufo.png")
pygame.display.set_icon(icon)

player_image= pygame.image.load("pyg/space-invaders.png") 

playerx =370
playery = 480
playerx_change = 0 
playery_change = 0
angle = 360
def player(pi,x,y):
    screen.blit(pi,(x,y))
    v 
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: 
        angle += 1
        rot = pygame.transform.rotate(player_image, angle)
        screen.blit(rot,(playerx,playery))
    if pressed[pygame.K_RIGHT]:
        angle -+ 1
        rot = pygame.transform.rotate(player_image,angle)
        screen.blit(rot,(playerx,playery))
    if pressed[pygame.K_w] or pressed[pygame.K_UP]: 
        playery -= 0.1
    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        playery += 0.1
    
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    if playery <= 0:
        playery = 0
    elif playery >= 536:
        playery = 536
    screen.fill((255,255,255))
    player(player_image,playerx,playery)
    pygame.display.update()"""

import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("pyg/ufo.png")
pygame.display.set_icon(icon)

player_image= pygame.image.load("pyg/space-invaders.png") 

playerx =370
playery = 480
playerx_change = 0 
playery_change = 0
angle = 0
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            SystemExit
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        angle += 0.1
    if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
        angle -= 0.1
    if pressed[pygame.K_UP] or pressed[pygame.K_w]:
        playery -=0.1
    w,h = player_image.get_size()
    box = [pygame.math.Vector2(p) for p in ([(0,0),(w,0),(w,-h),(0,-h)])]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0],min(box_rotate, key = lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0],max(box_rotate, key = lambda p: p[1])[1])
    pivot = pygame.math.Vector2(w/2, -h/2)
    pivot_rotate = pivot.rotate(angle)
    pivot_move = pivot_rotate - pivot
    origin = (playerx + min_box[0] - pivot_move[0], playery - max_box[1] + pivot_move[1])
    potato = pygame.transform.rotate(player_image, angle)
    screen.fill((255,255,255))
    screen.blit(potato,origin)
    pygame.display.flip()
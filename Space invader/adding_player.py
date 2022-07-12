import pygame
import matplotlib.pyplot as plt
from threading import Timer
import cmasher as cmr
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("player.png")
#icon2=pygame.image.load("background.jpg")

#player defining
playerX=370
playerY=480
playerX_change=0
playerY_change=0
def player():
    screen.blit(playerimg,(playerX,playerY))

#showing players position on screen
pos_value="Initial"
font=pygame.font.Font("freesansbold.ttf",20)

def show_pos():
    pos=font.render(" Position : "+ str(pos_value) , True, (255,180,255))
    if playerX >=800 or playerY >=600:
        screen.blit(pos ,(200,200))
    elif playerX <=0 or playerY <=0:
        screen.blit(pos ,(200,200))
    else:
        screen.blit(pos, (10,10))



running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        #keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change= -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change= 0.1
            if event.key == pygame.K_UP:
                playerY_change= -0.1
            if event.key == pygame.K_DOWN:
                playerY_change= 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change= 0
            if event.key == pygame.K_RIGHT:
                playerX_change= 0
            if event.key == pygame.K_UP:
                playerY_change= 0
            if event.key == pygame.K_DOWN:
                playerY_change= 0
            
    
    screen.fill((255,10,50))
    #changing bg color on player's exit from screeen
    if playerX >=800 or playerY >=600:
        screen.fill((20,10,60))
    if playerX <=0 or playerY <=0:
        screen.fill((10,10,50))
    playerX += playerX_change
    playerY += playerY_change
    player()
    show_pos()
    pos_value=playerX , playerY
    pygame.display.update()

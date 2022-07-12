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
icon2=pygame.image.load("background.jpg")
enemy1=pygame.image.load("ufo.png")
enemy2=pygame.image.load("ufo_1.png")
enemy3=pygame.image.load("ufo_2.png")
enemy4=pygame.image.load("ufo_3.png")
enemy5=pygame.image.load("ufo_2.png")
enemy6=pygame.image.load("ufo_3.png")

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
    pos=font.render(" Position : "+ str(pos_value) , True, (255,255,255))
    screen.blit(pos, (10,10))

#adding enemies
num = 6
enemyimg=[enemy1,enemy2,enemy3,enemy4,enemy5,enemy6]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]

for i in range(num):
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,140))
    enemyX_change.append(random.uniform(0,1))
    enemyY_change.append(random.uniform(0,2))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))




running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        #keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change= -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change= 0.3
            if event.key == pygame.K_UP:
                playerY_change= -0.3
            if event.key == pygame.K_DOWN:
                playerY_change= 0.3

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
    screen.blit(icon2,(-200,-200))

    playerX += playerX_change
    playerY += playerY_change

    #player's movement
    if playerX <=0 :
        playerX =0
    elif  playerX >= 736 :
        playerX=736

    if playerY <=400 :
        playerY =400
    elif  playerY >= 536 :
        playerY=536
    

    #enemy's movoment
    for i in range(num):
        enemyX[i] += enemyX_change[i]    
        if enemyX[i] <= 0:
            enemyX_change[i] =  random.uniform(0,1)
            enemyY[i] += random.uniform(4,6)
        elif enemyX[i] >=736:
            enemyX_change[i] = -(random.uniform(0,1))
            enemyY[i] += random.uniform(4,6)
        
        enemy(enemyX[i],enemyY[i],i)


    player()
    show_pos()
    pos_value=playerX , playerY
    pygame.display.update()

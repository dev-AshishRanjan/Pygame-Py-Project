import pygame
import matplotlib.pyplot as plt
from threading import Timer
import cmasher as cmr
import random
import math
from pygame import mixer

from pygame.font import Font

pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#musics/ sounds
mixer.music.load("bg_music.mp3")
mixer.music.play(-1)


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

#showing score on screen
pos_value="Initial"
font=pygame.font.Font("freesansbold.ttf",20)

def show_score():
    pos=font.render(" Score : "+ str(pos_value) , True, (255,255,255))
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
    enemyX_change.append(random.uniform(0.3,1))
    enemyY_change.append(random.uniform(0.3,2))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))


#adding bullets
bullet=pygame.image.load("bullet.png")
bulletX=0
bulletY=playerY
bulletY_change= 2
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bullet,(x+16 , y+10))


#collision detection
def iscollision(enemyX,enemyY,bulletX,bulletY,i):
    distance=math.sqrt((math.pow(enemyX[i]-bulletX , 2)) + (math.pow(enemyY[i]-bulletY , 2)))
    if distance < 27:
        return True
    else :
        return False

score=0



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

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX=playerX
                    fire_bullet(playerX , playerY)

                    b=mixer.Sound("bullet_shot.wav")
                    b.play()

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
            enemyX_change[i] =  random.uniform(0.3,0.6)
            enemyY[i] += random.uniform(30,40)
        elif enemyX[i] >=736:
            enemyX_change[i] = -(random.uniform(0.3,0.6))
            enemyY[i] += random.uniform(30,40)

        #collision
        collision= iscollision(enemyX,enemyY,bulletX,bulletY,i)
        if collision:
            bulletY=playerY
            bullet_state ="ready"
            score +=1
            # print(score)

            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(50,140)

            #collision sound
            d=mixer.Sound("des2.wav")
            d.play()
        
        #enemy is called
        enemy(enemyX[i],enemyY[i],i)



    player()
    show_score()
    pos_value=score

    #bullet movement
    if bulletY <=0 :
        bulletY=playerY
        bullet_state="ready"
    
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change




    pygame.display.update()


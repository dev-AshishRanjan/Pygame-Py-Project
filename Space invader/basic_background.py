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

icon1=pygame.image.load("player.png")
#icon2=pygame.image.load("background.jpg")

#creating colors
colors=cmr.take_cmap_colors("twilight",5000, return_fmt="rgb")



running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    for i in range(len(colors)):
        screen.fill(colors[i])
        #screen.blit(icon1,(random.randint(0,800),random.randint(0,600)))
        screen.blit(icon,(random.randint(0,800),random.randint(0,600)))
        screen.blit(icon,(400,300))
        screen.blit(icon,(random.randint(0,800),random.randint(0,600)))
        pygame.display.update()

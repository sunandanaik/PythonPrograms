# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:17:30 2020

@author: DELL
"""

import pygame
import random
import math
from pygame import mixer #------ used for handling musics and sounds

#Creating our first Game Window
#print("hi")

#initialize the pygame
pygame.init()

#Title and Icon
#For Icon visit-https://www.flaticon.com/search?search-type=icons&word=space+invaders
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('d:/Pictures/spaceicon.png')
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load('d:/Pictures/spaceicon.png')
playerX=370
playerY=480
playerX_change=0

#Enemy
enemyImg =[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('d:/Pictures/alien.png'))
    enemyX.append(random.randint(0,800)) #reborn of enemy at random x and y locations
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40) #to move down by 40px

#Bullet
#ready state means u cant see bullet on screen and fire state means bullet moving
bulletImg=pygame.image.load('d:/Pictures/bullet.png')
bulletX=10
bulletY=480
bulletX_change=0.3
bulletY_change=40 #to move down by 40px
bullet_state="ready" 

#declare score variable
score =0
font = pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf',64)
textX = 10
textY = 10

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))


def show_score(x,y):
    s =font.render("Score :" + str(score),True,(0,255,0))
    screen.blit(s,(x,y))


#player function definition
def player(x,y):
    screen.blit(playerImg,(x,y))  #blit-used to draw on screen
    
    
#enemy function definition
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))  #blit-used to draw on screen
    
#bullet function definition
def fire_bullet(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bulletImg,(x +16,y+10)) #to make sure bullet appears on left side of spaceship
    
#Collision detection
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2) ) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    

#creating screen of width 800px and height 600px into tuple
screen=pygame.display.set_mode((800,600))

#Adding Background image
#background = pygame.image.load('d:/Pictures/spacebg.jpg')

#Background music
#mixer.music.load('d:/Pictures/background.wav')
#mixer.music.play(-1) #---(-1) means not adding in loop

#Game Loop
running=True
while running:
    #set screen background color with rgb=0,0,0--check in google: color to rgb
    screen.fill((0,0,255)) 
    
    #background image
    #screen.blit(background,(0,0))
    
    #movement mechanics in game development
    #playerX -=0.2  #increasing value of x moves space in right direction and vice versa
    #print(playerX)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
        #if key stroke is pressed to check whether its right or left
        if event.type == pygame.KEYDOWN:
            #print("keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = - 0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state =="ready":
                    #bullet_Sound=mixer.Sound('laser.wav')
                    #bullet_Sound.play()
                    #get the current x-coordinate of spaceship
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
    
    #eg: 5=5+ -0.1 -> 5 =5-0.1 and 5=5+0.1
    playerX +=playerX_change
    
    #Adding boundaries for player on x axis
    if playerX <= 0:
        playerX = 0
    elif playerX >=770:  #800-32px=778
        playerX = 770
    
    #Enemy movement
    enemyX[i] +=enemyX_change[i]
    
    #Adding boundaries for enemy on x axis so that it doesnt go out of edge
    for i in range(num_of_enemies):
        
        
        #Game Over
        if enemyY[i] >200:
            for j in range(num_of_enemies):
                enemyY[j]=2000  #set y-axis to 2000
            game_over_text()
            break
        
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]= 0.3
            enemyY[i] +=enemyY_change[i]
        elif enemyX[i] >=770:  #800-32px=778
            enemyX_change[i] = -0.3
            enemyY[i] +=enemyY_change[i]
            
         #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state="ready"
            score +=1
            #print(score)
            enemyX[i]=random.randint(0,735) #reborn of enemy at new random x and y locations
            enemyY[i]=random.randint(50,150)
            
        enemy(enemyX[i],enemyY[i],i) #function enemy calling
    
    #Bullet Movement
    if bulletY <= 0:
        bulletY =480
        bullet_state ="ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    
    #Collision
    collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    if collision:
        #explosion_Sound=mixer.Sound('laser.wav')
        #explosion_Sound.play()
        bulletY = 480
        bullet_state="ready"
        score +=1
        print(score)
        enemyX=random.randint(0,735) #reborn of enemy at new random x and y locations
        enemyY=random.randint(50,150)
    
    
    player(playerX,playerY) #function player calling
    show_score(textX,textY) #function show_score calling
    pygame.display.update()
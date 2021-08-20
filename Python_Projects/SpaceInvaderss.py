# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:35:31 2020

@author: DELL
"""
import pygame
import random
import math
#from pygame import mixer #------ used for handling musics and sounds

#initialize pygame
pygame.init()

#Screen
screen =pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load('Images/si.png')

pygame.display.set_icon(icon)

#Adding Background image
background = pygame.image.load('Images/background.png')

#Adding background music
pygame.mixer.music.load('Sounds/background.wav')
pygame.mixer.music.play(-1)

#Make Player
#Player
playerImg=pygame.image.load('Images/si.png')
pX=360
pY=480
pXchange = 0
pYchange = 0 #used to know how much to change player's coordinates
speed = 4 #used to know how fast player moves

#Make One Enemy
#enemyImg=pygame.image.load('Images/alien.png')
#eX = random.randint(100,700)
#eY = random.randint(100,300)
#eXchange =2.5 #used to move enemy at every 2.5 steps
#eYchange =15

#--Now to make multiple enemies
enemyImg =[]
eX = []
eY = []
eXchange =[]
eYchange= []
num_of_enemy = 5  #to addd more enemy images

#Looping to create multiple enemies
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('Images/alien.png'))
    eX.append(random.randint(100,700))
    eY.append(random.randint(100,300))
    eXchange.append(3)
    eYchange.append(15)

#Bullet
#ready state means u cant see bullet on screen and fire state means bullet moving
bulletImg=pygame.image.load('Images/bullet.png')
bX=pX
bY=pY
bYchange = -10 #bullet moves up in y direction only
bstate =0 #bullet is in ready state


#Score
score = 0 #to set score of the game
font=pygame.font.Font('freesansbold.ttf',32)
scoreCoordinate=(10,10)

def score_print(scr):
    screen.blit(font.render("Score :" +str(scr),True,(255,255,255)),scoreCoordinate)

def isCollision(eX,eY,bX,bY):
    distance = math.sqrt((bX-eX)**2 + (bY-eY)**2)
    if distance <=30:
        return True
    else:
        return False

#Fire Bullet function definition
def fire_bullet(x,y):
    global bstate
    bstate = 1 # to set bullet in fire state
    screen.blit(bulletImg, (x , y)) #draw bullet on screen


#player function definition
def player(x,y):
    screen.blit(playerImg, (x , y))  #blit-used to draw player image on screen

#One enemy function definition
#def enemy(x,y):
    #For one enemy to draw on screen
    #screen.blit(enemyImg, (x , y))  #blit-used to draw enemy image on screen

#Multiple  enemy function definition
#--Now for multiple enemy images to draw on screen
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x , y))

#Game over text function definition
def game_over_text(scr):
    msg = pygame.font.Font('freesansbold.ttf',64)
    msgCoordinate=(180,200)
    screen.blit(msg.render("GAME OVER!!!",True,(255,255,255)),msgCoordinate)
    
    final_score=pygame.font.Font('freesansbold.ttf',32)
    final_scoreCoordinate=(280,300)
    screen.blit(final_score.render("FINAL SCORE :" +str(scr),True,(255,255,255)),final_scoreCoordinate)


#Game Loop
running=True
while running:
    screen.fill((40,40,40))
    #blit-to draw background on screen
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        #QUIT
        if event.type == pygame.QUIT:
            running=False
         #if key stroke is pressed to check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pXchange = -speed
            if event.key == pygame.K_RIGHT:
                pXchange = speed
            if event.key == pygame.K_UP:
                pYchange= -speed
            if event.key == pygame.K_DOWN:
                pYchange = speed
            if event.key == pygame.K_SPACE:
                bsound=pygame.mixer.Sound('Sounds/laser.wav')
                bsound.play()
                bX,bY=pX,pY  #multiple initialization of variables in python
                fire_bullet(bX,bY) #fire bullet function calling
            
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pXchange = 0
            if event.key ==pygame.K_UP or event.key == pygame.K_DOWN:
                    pYchange = 0
    
    #Player Movement
    pX += pXchange   
    pY += pYchange  
    if pX <= 0:
        pX = 763
    elif pX >=763: #800-64px=763
        pX =0
    
    player(pX,pY) #Player function calling
    
    
    #For One Enemy Movement
    #eX += eXchange
   
    #if eX >= 736:
        #eY +=eYchange
        #eXchange = -eXchange
    #if eX <= 0:
        #eY +=eYchange
        #eXchange =-eXchange
    
   # enemy(eX,eY)#Enemy function calling
   
   
    #--Now for Multiple Enemies looping done
    for i in range(num_of_enemy):
        #Game Over
        if eY[i] >= 400:
            for j in range(num_of_enemy):
                eY[j] =800
            game_over_text(score)
            break
        
        eX[i] += eXchange[i]
        if eX[i] >=736:
             eY[i] += eYchange[i]
             eXchange[i] =-eXchange[i]
        if eX[i] <= 0:
            eY[i] += eYchange[i]
            eXchange[i] =- eXchange[i]
             
    
        
        #Collision Detection With Multiple enemy images
        collision = isCollision(eX[i],eY[i],bX,bY)
        if collision:
            #if True
            eX[i] = random.randint(100,700)
            eY[i] = random.randint(100,300)
            bstate = 0
            score +=1
            #print(score) #to print on terminal
        
        enemy(eX[i], eY[i], i) #Enemy function calling in loop
            
    #Bullet movement
    if bstate == 1:
        fire_bullet(bX,bY)  #fire_bullet function calling
        bY +=bYchange  #bYchange =-10 evry time y value of bullet changing
        if bY <=0:
            bstate = 0 #then set bullet to ready state again
     
            
    #If palyer touches enemy then game over
    if pX ==eX and pY == eY:
        game_over_text(score)
    #Collision Detection With One enemy image
    #collision = isCollision(eX,eY,bX,bY)
    #if collision:  #if True
        #eX = random.randint(100,700)
       # eY = random.randint(100,300)
        #bstate = 0
        #score +=1
        #print(score) #to print on terminal

    score_print(score)  #function calling
     #To display all changes on screen       
    pygame.display.update() 




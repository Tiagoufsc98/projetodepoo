import pygame
import os
#modulo de som
pygame.mixer.init()
#variáveis
run = True
width = 800
height = 600
px = 0
background = pygame.transform.scale(pygame.image.load(os.path.join('fundo','fundo.png')),(width,height))
clock = pygame.time.Clock()
fps = 30
som_fundo = pygame.mixer.Sound(os.path.join('audio','som_fundo.mp3'))
trilha = False
nave = pygame.transform.scale(pygame.image.load(os.path.join('fundo','nave.png')),(80,100))


#Configurações iniciais do canvas
pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Asteroids Game")




#Loop Principal #############################################################################
while run:
    if trilha == False:
        trilha = True
        som_fundo.play(-1)

        
    clock.tick(fps)
    px -=1
    win.fill((0,0,0))
    win.blit(background,(px,0))
    win.blit(background,(width+px,0))
    if px == -width:
        px = 0

    #nave###########################################
    win.blit(nave,(0,height/2))

    
    #Fechando game caso evento == click no 'X'########################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

import pygame

pygame.init


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Butterfly")

#game variables
doExit = False #variable to quit out of game loop



#BEGIN GAME LOOP######################################################
while not doExit:
    #FPS (frames per second)

    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program
    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
    pygame.draw.circle(screen, (255,0,255), (200, 300), 100)
    pygame.draw.circle(screen, (255,0,255), (400, 300), 100)
    pygame.draw.circle(screen, (255,0,230), (375, 400), 75)
    pygame.draw.circle(screen, (255,0,230), (225, 400), 75)
    pygame.draw.ellipse(screen,(250,255,0), (250, 200, 100, 300))
    pygame.draw.arc(screen,(255,100,100), (250,150,100,200),3.14, 2*3.14,9)
    pygame.draw.arc(screen,(255,100,100), (250,250,100,200),3.14, 2*3.14,9)
    pygame.draw.arc(screen,(255,100,100), (250,200,100,200),3.14, 2*3.14,9)
    pygame.display.flip() #update graphics each game loop
#END GAME LOOP#######################################################
pygame.quit()

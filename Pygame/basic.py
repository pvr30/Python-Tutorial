import pygame
pygame.init()
win = pygame.display.set_mode((500,500)) # this will get our window.

# This will change the window/game name
win = pygame.display.set_caption("MY GAME") 


#  Defining  a few varibles to represent our character.
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

# main loop or game loop.
while run:
     # This will delay the game the given amount of milliseconds.
     #  In our casee 0.1 seconds will be the delay
    pygame.time.delay(100)

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False   # Ends the game loop

    #pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height)) 

    pygame.display.update()


pygame.quit() # If we exit the loop this will execute and close our game
import pygame
game_window = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Moving Character")

x = 0
y = 0
width = 100
height = 100
val = 1  # This Value is very important it decides that how many steps our object will move

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # This will give us a dictionary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= val

    if keys[pygame.K_RIGHT]:
        x += val

    if keys[pygame.K_UP]:
        y -= val

    if keys[pygame.K_DOWN]:
        y += val

    game_window.fill((0, 0, 0)) # Fills the screen with black
    pygame.draw.rect(game_window, (255, 0, 0), (x, y, width, height))
    # pygame.draw.circle(game_window, (255, 0, 0), (100, 200), 50, 3)
    pygame.display.update()
pygame.quit()
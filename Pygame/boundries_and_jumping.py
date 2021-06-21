import pygame
game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Boundaries And Jumping")
run = True

x = 50
y = 50
width = 40
height = 50
val = 10

isJump = False
jumpCount = 10

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > val:   # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= val
    if keys[pygame.K_RIGHT] and x < 500-val-width:  # Making sure the top right corner of our character is less than the screen width - its width
        x += val

    if not isJump:  # Checks is user is not jumping
        if keys[pygame.K_UP] and y > val:   # Same principles apply for the y coordinate
            y -= val
        if keys[pygame.K_DOWN] and y < 500-val-height:
            y += val
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5  # this is for height of jump
            jumpCount -= 1
        else:  # This will execute if our jump is finished
            jumpCount = 10
            isJump = False
            # Resetting our Variables

    game_window.fill((0, 0, 0))
    pygame.draw.rect(game_window, (0, 255, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()
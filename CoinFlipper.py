import pygame
import random

pygame.init()
pygame.font.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (30, 144, 255)

# Screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("coinFlipper")

carryOn = True

clock = pygame.time.Clock()
color = GREEN

x = -63
y = 365

drawMiniRect = 0

# Background image
bg = pygame.image.load("images/bg.jpg")
screen.blit(bg, (0, 0))

# Game Title
myFont = pygame.font.SysFont('Comic Sans MS', 50)
textSurface = myFont.render('Coin Flipper!', False, (235, 235, 235))
screen.blit(textSurface, (210, 0))

# Coin info
secondText = pygame.font.SysFont('Comic Sans MS', 40)
secondTextSurface = secondText.render('RED = head', False, (219, 0, 0))
screen.blit(secondTextSurface, (466, 185))

# Coin info 2
thirdText = pygame.font.SysFont('Comic Sans MS', 40)
thirdTextSurface = thirdText.render('BLUE = tail', False, (0, 62, 232))
screen.blit(thirdTextSurface, (466, 245))

# Stats info
fourthText = pygame.font.SysFont('Comic Sans MS', 40)
fourthTextSurface = fourthText.render('History:', False, (235, 235, 235))
screen.blit(fourthTextSurface, (5, 300))

# Info rect
rect = pygame.Surface((1000,750))
rect.set_alpha(128)
rect.fill((255, 255, 255))
screen.blit(rect, (2, 360))

# main loop
while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1): #or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            pos = event.pos

            #click for flip
            if 250 < pos[0] < 450 and 150 < pos[1] < 350:
                flip = random.randint(0, 1)
                if color in [RED, BLUE]:
                    color = GREEN

                # flip
                elif flip == 0:
                    # coin = pygame.draw.rect(screen, RED, [250, 150, 200, 200], 0)
                    color = RED
                    drawMiniRect = 1
                else:
                    # coin = pygame.draw.rect(screen, BLUE, [250, 150, 200, 200], 0)
                    color = BLUE
                    drawMiniRect = 1

    # rect color info
    if drawMiniRect == 1:
        x += 70
        pygame.draw.rect(screen, color, [x, y, 50, 50], 0)
        drawMiniRect = 0

        if x >= 700:
            x = -63
            y += 70

        if y >= 500:
            x = -63
            y = 365

            screen.blit(bg, (0, 0))

            # Game Title
            myFont = pygame.font.SysFont('Comic Sans MS', 50)
            textSurface = myFont.render('Coin Flipper!', False, (235, 235, 235))
            screen.blit(textSurface, (210, 0))

            # Coin info
            secondText = pygame.font.SysFont('Comic Sans MS', 40)
            secondTextSurface = secondText.render('RED = head', False, (219, 0, 0))
            screen.blit(secondTextSurface, (466, 185))

            # Coin info 2
            thirdText = pygame.font.SysFont('Comic Sans MS', 40)
            thirdTextSurface = thirdText.render('BLUE = tail', False, (0, 62, 232))
            screen.blit(thirdTextSurface, (466, 245))

            # Stats info
            fourthText = pygame.font.SysFont('Comic Sans MS', 40)
            fourthTextSurface = fourthText.render('History:', False, (235, 235, 235))
            screen.blit(fourthTextSurface, (5, 300))

            # Info field
            rect = pygame.Surface((1000, 750))
            rect.set_alpha(128)
            rect.fill((255, 255, 255))
            screen.blit(rect, (2, 360))

    # coin
    pygame.draw.rect(screen, color, [250, 150, 200, 200], 0)

    # Text inside of the first square
    firstTextSize = pygame.font.SysFont('Comic Sans MS', 40)
    firstText = screen.blit(firstTextSize.render('click here', True, (0, 0, 0)), (256, 215))



    pygame.display.update()

    '''
        # Coin flip
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            flip = random.randint(0, 1)

            if flip == 0:
                coin = pygame.draw.rect(screen, RED, [250, 150, 200, 200], 0)

            else:
                coin = pygame.draw.rect(screen, BLUE, [250, 150, 200, 200], 0)

    '''

    pygame.display.update()

    pygame.display.flip()

    clock.tick(30)

pygame.quit()

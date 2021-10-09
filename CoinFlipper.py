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

# Background image
bg = pygame.image.load("bg.jpg")

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # Game Title
    myFont = pygame.font.SysFont('Comic Sans MS', 50)
    textSurface = myFont.render('Coin Flipper!', False, (0, 0, 0))
    screen.blit(textSurface, (210, 0))

    # Info field
    rect = pygame.draw.rect(screen, (BLACK), (2, 360, 695, 138), 2)
    pygame.display.update()

    # Coin Square
    coin = pygame.draw.rect(screen, GREEN, [250, 150, 200, 200], 0)

    # Реализовать исчезновение текста при нажатии пробела и появлении нового текста говорящей о выпавшей стороне монеты.

    # Coin flip
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        flip = random.randint(0, 1)

        if flip == 0:
            coin = pygame.draw.rect(screen, RED, [250, 150, 200, 200], 0)

        else:
            coin = pygame.draw.rect(screen, BLUE, [250, 150, 200, 200], 0)

    # Реализовать появление квадрата определенного цвета в зависимости от выпавшей стороны в пустом блоке "rect" так,
    # чтобы при каждом следующем подкидывании рядом с первым квадратом появлялся второй квадрат и так далее.

    # Text inside of the first square
    firstTextSize = pygame.font.SysFont('Comic Sans MS', 30)
    firstText = screen.blit(firstTextSize.render('Press Space', True, (0, 0, 0)), (265, 215))

    pygame.display.update()

    pygame.display.flip()

    clock.tick(30)

pygame.quit()

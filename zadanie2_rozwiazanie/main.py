import pygame
from math import sqrt

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" :-) ")
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (800, 600))


class Object:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


def movement(win, player, ball, bg):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y -= 2
    if keys[pygame.K_DOWN]:
        player.y += 2
    if keys[pygame.K_RIGHT]:
        player.x += 2
    if keys[pygame.K_LEFT]:
        player.x -= 2

    win.blit(bg, (0, 0))
    pygame.draw.circle(win, (0, 255, 0), (player.x, player.y), player.radius)
    dist = abs(sqrt((player.x - ball.x) ** 2 + (player.y - ball.y) ** 2))
    if dist > (ball.radius + player.radius):
        pygame.draw.circle(win, (255, 255, 255), (ball.x, ball.y), ball.radius)
    else:
        pygame.draw.circle(win, (255, 0, 0), (ball.x, ball.y), ball.radius)
    pygame.display.update()

    return player


player = Object(200, 200, 40)
ball = Object(500, 300, 25)

run = True

while run:
    player = movement(window, player, ball, bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
import pygame
import math

def draw(a):
    pygame.draw.line(screen, (0,0,255), (a, -1 * math.cos((a - 200) / 20) * 90 + 150),
                     ((a + 1), -1 * math.cos(((a+ 1) - 200) / 20) * 90 + 150), 2)

    pygame.draw.line(screen, (255,0,0), (a, -1 * math.sin((a - 200) / 20) * 90 + 150),
                     ((a+1), -1 * math.sin(((a+1) -200) / 20) * 90 + 150), 2)

pygame.init()

size = width, height = (400, 300)

screen = pygame.display.set_mode(size)
screen.fill((255,255,255))
pygame.draw.rect(screen, (0, 0, 0), (50, 50, 300, 200), 2)
pygame.draw.line(screen, (0, 0, 0), (50, 150), (350, 150), 2)
pygame.draw.line(screen, (0, 0, 0), (200, 50), (200, 250), 2)

a=50
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    if a<350:
        draw(a)
        a+=1

    pygame.display.flip()
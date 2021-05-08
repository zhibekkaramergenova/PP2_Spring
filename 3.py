import pygame
import math
pygame.init()
screenwidth, screenheight = 600, 480
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('TSIS 7')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
font = pygame.font.SysFont('comicsansms', 13)

nums = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
radians = ['-3π', ' 5π', '-2π', '-3π', '-π', '-π', '  0', ' π', '  π', '3π', '2π', '5π', '3π']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.rect(screen, black,(40, 40, screenwidth - 80, screenheight - 120), 3)
    pygame.draw.line(screen, black, (300, 40), (300, screenheight - 80), 3)
    pygame.draw.line(screen, black, (40, 220), (screenwidth - 40, 220), 3)
    for step in range(60, 600, 80):
        pygame.draw.line(screen, black, (step, 40), (step, screenheight - 80))
    for step in range(60, 400, 40):
        pygame.draw.line(screen, black, (40, step), (screenwidth - 40, step))
    for step in range(60, 550, 10):
        pygame.draw.line(screen, black, (step, 40), (step, 45))
        pygame.draw.line(screen, black, (step, screenheight - 85), (step, screenheight - 80))
        if step % 20 == 0:
            pygame.draw.line(screen, black, (step, 40), (step, 50))
            pygame.draw.line(screen, black, (step, screenheight - 90), (step, screenheight - 80))
        if step % 40 == 0:
            pygame.draw.line(screen, black, (step, 40), (step, 55))
            pygame.draw.line(screen, black, (step, screenheight - 95), (step, screenheight - 80))
    for step in range(60, 380, 10):
        pygame.draw.line(screen, black, (40, step), (45, step))
        pygame.draw.line(screen, black, (screenwidth - 45, step), (screenwidth - 40, step))
        if step % 20 == 0:
            pygame.draw.line(screen, black, (40, step), (50, step))
            pygame.draw.line(screen, black, (screenwidth - 50, step), (screenwidth - 40, step))
    pygame.draw.line(screen, white, (380, 61), (380, 99))

    y = 50
    for i in nums:

        text = font.render(i, True, black)
        screen.blit(text, (8, y))
        y += 40
    x = 50
    for i in range(len(radians)):
        if i % 2 == 0:
            screen.blit(font.render(radians[i], 1, black), (x, screenheight - 78))
        else:
            screen.blit(font.render(radians[i], 1, black), (x, screenheight - 80))
            pygame.draw.line(screen, black, (x, screenheight - 64), (x + 18, screenheight - 64))
            screen.blit(font.render('2', 1, black), (x + 6, screenheight - 65))
        x += 40

    font = pygame.font.SysFont('comicsansms', 18)
    screen.blit(font.render('sin x', 1, black), (365, 60))
    screen.blit(font.render('cos x', 1, black), (365, 75))
    screen.blit(font.render('X', 1, black), (295, 430))
    pygame.draw.line(screen, red, (410, 75), (435, 75), 1)
    for i in range(410, 435, 9): 
        pygame.draw.line(screen, blue, (i, 90), (i + 6, 90), 1)
    font = pygame.font.SysFont('comicsansms', 13)
    p_sin, p_cos, n = [], [],6
    for x in range(0, 480):
        y = int(math.sin(float(x) / 480 * n * math.pi) * 160 + 220)
        p_sin.append((x  + 60, y))
    for x in range(0, 481):
        y = int(math.cos(float(x) / 480 * n * math.pi) * 160 + 220)
        p_cos.append((x  + 60, y))
    pygame.draw.aalines(screen, red, 0, p_sin)
    for i in range(0, len(p_cos) - 1, 2):
        pygame.draw.aaline(screen, blue, p_cos[i], p_cos[i + 1])
    
    pygame.display.flip()
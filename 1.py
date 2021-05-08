import pygame
import random

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()


Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (140, 146, 172)
Yellow = (255, 255, 0)

size = (400, 600)
ok = False
gg = False
score = 0
f = pygame.font.SysFont("Times new roman", 20)
f2 = pygame.font.SysFont("Times new roman", 60)
go = f2.render("Game Over", True, Black)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")
enemyImage = pygame.image.load("Enemy.png")
playerImage = pygame.image.load("Player.png")
coinImage = pygame.image.load("coin.png")
streetImage = pygame.image.load("AnimatedStreet.png")


player_x = 150
player_y = 500

coin_x = random.randint(50, 350)
coin_y = random.randint(20, 50)
coin_dx = 60
coin_dy = 5

enemy_x = random.randint(50, 350)
enemy_y = random.randint(20, 50)
enemy_dx = 60
enemy_dy = random.randint(5, 10)

def show_player(x, y):
    screen.blit(playerImage, (x, y))

def show_enemy(x, y):
    screen.blit(enemyImage, (x, y))

def show_coin(x, y):
    screen.blit(coinImage, (x, y))

def scorex(x, y):
    screen.blit(coinImage, (x + 30, y))
    sc = f.render(": " + str(score), True, Red)
    screen.blit(sc, (x + 60, y - 1))

def collision(enemy_x, enemy_y, player_x, player_y):
    if enemy_x in range(player_x - 30, player_x + 40) and (enemy_y in range(player_y, player_y + 100)):
        return True
    return False

def take_coin(coin_x, coin_y, player_x, player_y):
    if coin_x in range(player_x - 30, player_x + 40) and (coin_y in range(player_y, player_y + 100)):
        return True
    return False


while not ok:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = True
        

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player_x -= 5
    if pressed[pygame.K_RIGHT]:
        player_x += 5

    enemy_y += enemy_dy
    if enemy_y > 600:
        enemy_y = 0
        enemy_x = random.randint(50, 350)
        enemy_dy = random.randint(8, 15)
    
    coin_y += coin_dy
    if coin_y > 600:
        coin_y = 0
    
    isCol = collision(enemy_x, enemy_y, player_x, player_y)
    if player_x < 0 or player_x > 360:
        player_x = player_x % 360

    tc = take_coin(coin_x, coin_y, player_x, player_y)
    if tc:
        score += 1
        coin_x = random.randint(50, 350)
        coin_y = 0
    if isCol:
        screen.fill(Black)
        go = f2.render("Game Over", True, Red)
        sc = f.render("Your score: " + str(score), True, White)
        screen.blit(go, (50, 230))
        screen.blit(sc, (140, 330))
    else:
        screen.blit(streetImage, (0,0))
        show_player(player_x, player_y)
        show_enemy(enemy_x, enemy_y)
        show_coin(coin_x, coin_y)
        scorex(270, 20)
    
    
    
    FramePerSec.tick(FPS)
    pygame.display.update()
pygame.quit()
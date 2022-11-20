#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random
from class_bullet import *
from class_aptechka import *
from class_player import *
from class_mob import *
WIDTH = 480
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 185, 36)
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Стрелялка")
clock = pygame.time.Clock()

background = pygame.image.load('фон игры.png').convert_alpha()
background_rect = background.get_rect()
 
player_img = pygame.image.load("корабль.png").convert_alpha()
mob_img = pygame.image.load("метеорит.png").convert_alpha()
aptechka_img = pygame.image.load("аптечка.png").convert_alpha()
bullet_img = pygame.image.load("заряд.png").convert_alpha()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
    



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs=pygame.sprite.Group()
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
aptechkas=pygame.sprite.Group()
def newaptechka():
    q = Aptechka()
    all_sprites.add(q)
    aptechkas.add(q)
bullets = pygame.sprite.Group()
for i in range(8):
    newmob()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        newmob()
for i in range (1):
    newaptechka()
        


        
score = 0
all_sprites.add(player)

# Цикл игры
running = True
while running:
    clock.tick(FPS)
    # Ввод события
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # Обновление
    all_sprites.update()
    hitPlayer = pygame.sprite.spritecollide(player, mobs, True)
    for hit in hitPlayer:
        player.shield -= 20
        newmob()
        if player.shield <= 0:
            running = False
    healPlayer = pygame.sprite.spritecollide(player, aptechkas, True)
    for hit in healPlayer:
        player.shield += 5
        if player.shield > 100:
            player.shield = 100
        newaptechka()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        score += 50
        all_sprites.add(m)
        mobs.add(m)
        
   
   

    
    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()







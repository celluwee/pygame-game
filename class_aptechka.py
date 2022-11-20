#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pygame
class Aptechka(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(aptechka_img, (45, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - 590)
        self.speedy = 2
        self.speedx = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or   self.rect.right > WIDTH + 20:
            self.rect.y = random.randrange(-100, -40)   


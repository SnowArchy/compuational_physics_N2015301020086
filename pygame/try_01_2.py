# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:08:18 2017

@author: Jiang Qi
"""

 
import pygame

# 调用 pygame.locals 使容易使用关键参数
from pygame.locals import *

# 定义Player对象 调用super赋予它属性和方法    
# 我们画在屏幕上的surface 现在是player的一个属性
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

def update(self,pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0,-5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0,5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5,0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5,0)
# 初始化 pygame
pygame.init()

# 创建屏幕对象
# 设定尺寸为 800x600
screen = pygame.display.set_mode((800,600))

# 初始化Player， 现在他仅仅是一个矩形
player = Player()

# 控制主循环的进行的变量
running = True

# 主循环
while running:
     # 事件队列中的循环
    for event in pygame.event.get():
        # check for KEYDOWN event: KEYDOWN is a constant defined in pygame.locals,which we imported earlier
            if event.type == KEYDOWN:
                # if the Esc KEY has been pressed set running to false to exit the main loop
                if event.key == K_ESCAPE:
                    running = False
                # check for QUIT event: if QUIT, set running to false
            elif event.type == QUIT:
                running = False

 pressed_keys = pygame.event.get_presssed()

    player.update(pressed_keys)  

    # 这一行表示：将surf画到屏幕 x：400.y:300的坐标上
    screen.blit(player.surf,(400,300))
    # 更新
    pygame.display.flip()

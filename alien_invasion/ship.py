import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """控制飞船的类"""
    
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()#将屏幕也视为矩形
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
                
        self.rect.midbottom = self.screen_rect.midbottom#对于每艘新飞船，都将其放于屏幕底部的中央
        
        self.x = float(self.rect.x)#在飞船的属性x中存储小数值，用于精确追踪飞船位置
        
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """根据移动标志调整飞船位置"""
        ##"if-elif"（只适用于二选一）与"if-if"（条件可同时满足）的选择需要谨慎考虑
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x#根据self.x更新rect对象
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
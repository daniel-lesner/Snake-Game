import pygame

class Snake:
    def __init__(self, game):
        self.screen = game.screen
        self.screenRect = game.screen.get_rect()
        
        self.image=pygame.image.load("assets/snake.bmp")
        self.imageRect=self.image.get_rect()
        
        self.imageRect.center=self.screenRect.center
        
        
        self.moving_right=True
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        
        self.speed=50
        
        
        
        
    def blitme(self):
        self.screen.blit(self.image,self.imageRect)
        
        
    def update_snake_position(self):
        if self.moving_right and self.imageRect.right<self.screenRect.right-34:
            self.imageRect.x+=self.speed
        elif self.moving_left and self.imageRect.left>34:
            self.imageRect.x-=self.speed
        elif self.moving_up and self.imageRect.top>64:
            self.imageRect.y-=self.speed
        elif self.moving_down and self.imageRect.bottom<self.screenRect.bottom-14:
            self.imageRect.y+=self.speed
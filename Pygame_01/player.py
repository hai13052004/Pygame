import pygame
from define import*

class Player():
    
    x=0
    y=0
    color =""
    
    def __init__(self,color,x,y) -> None:
        self.x=x
        self.u=y
        self.color=color 
        
    def show(self,surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,PLAYER_WIDTH,PLAYER_HEIGHT),width=0)
        
    def move_up(self):
        self.y=self.y-PLAYER_VELOCITY
        if self.y<0:
            self.y=0
    def move_down(self):
        
        if self.y+PLAYER_HEIGHT<WINDOW_HEIGHT:
            self.y=self.y+PLAYER_VELOCITY
        
        
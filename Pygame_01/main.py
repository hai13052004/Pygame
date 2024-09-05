import pygame
from define import *
from player import Player
#set tên cửa sổ
pygame.display.set_caption("game lậu ") 
#SET CHIỀU RỘNG CHIỀU CAO CỬA SỔ GAME
WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 

#tao anh dai dien cho game
programIcon=pygame.image.load('PYGAME/hoa-cuc-hoa-mi-16(1).jpg')
pygame.display.set_icon(programIcon)

def key_events():
     global run, window_color
     for event in pygame.event.get(): 
        if event.type == pygame.QUIT:#ấn nút tắt cửa sổ game
            run = False
            
            #bat key tu ban phim
        if event.type==pygame.KEYDOWN:
                 if event.key==pygame.K_UP:
                    playerRight.move_up()
                 if event.key==pygame.K_DOWN:
                    playerRight.move_down()
                 if event.key==pygame.K_w:
                    playerLeft.move_up()
                 if event.key==pygame.K_s:
                    playerLeft   .move_down()

#init player
playerLeft = Player(COLOR_RED,5,WINDOW_HEIGHT/2-PLAYER_HEIGHT/2)
playerRight = Player(COLOR_BLUE,WINDOW_WIDTH-PLAYER_WIDTH-5,WINDOW_HEIGHT/2-PLAYER_HEIGHT/2)

run=True
window_color=COLOR_BLACK
while True: 
    pygame.time.delay(100)
    WINDOW_GAME.fill(window_color)
    #key events
    key_events()
    
    #ve line
    pygame.draw.line(WINDOW_GAME, COLOR_LIGHTBLUE, (WINDOW_WIDTH/2,0) ,(WINDOW_WIDTH/2,WINDOW_HEIGHT), width=LINE_WIDTH)
    
    #VE PLAYER left
    playerLeft.show(WINDOW_GAME)
    #VE PLAYER right
    playerRight.show(WINDOW_GAME)
    #update lai giao dien                
    pygame.display.update()    
pygame.quit()
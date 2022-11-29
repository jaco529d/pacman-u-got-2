# Pac-Man clone made for learning/teaching git and Python

import random
import time
import pygame as pg

from pacman import PacMan
from ghost import Ghost
from level import Level

## Setup ##
pg.init()

font_press_enter = pg.font.Font(None, 32)

## Game loop ##
state = "LOAD"
running = True
while running:
    
    if state == "LOAD":
        level = Level("level2.txt")
        pacman = PacMan(level.player_pos_row, level.player_pos_col)
        ghost = Ghost(level.ghost_pos_row,level.ghost_pos_col)
        print("level.ghost: ", level.ghost_pos_row, level.ghost_pos_col)
        direction = None
        screen = pg.display.set_mode((len(level.tiles[0])*32,len(level.tiles)*32))
        pg.display.set_caption("Pac-Man (clone)")
        state = "READY"


    elif state == "READY":
        text = font_press_enter.render("Press [Enter] to play", True, (220,220,10))
        text_rect = text.get_rect(center=(17*32/2, 21*32/2))
        screen.blit(text, text_rect)

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    state = "PLAY"      

        pg.display.flip()  
        time.sleep(0.1)
        

    elif state == "PLAY":

        ## Handle events (keypresses etc.)
        events = pg.event.get()
        for event in events:

            # Close window (e.g. pressing [x] or Ctrl+F4)
            if event.type == pg.QUIT:
                running = False
            # Keypresses
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    direction = "up"
                elif event.key == pg.K_DOWN:
                    direction = "down"
                elif event.key == pg.K_LEFT:
                    direction = "left"
                elif event.key == pg.K_RIGHT:
                    direction = "right"
                elif event.key == pg.K_ESCAPE:
                    running = False
                elif event.key == pg.K_v: 
                    state = "END"
        
        ## Move / logic ##
        pacman.move(level,direction)
        ghost.move(level, pacman)

        if ghost.killed == True:
            state = "END"

        ## Draw ##
        screen.fill((0,0,0)) 
        level.draw(screen)
        ghost.draw(screen)
        pacman.draw(screen, direction)

        # Update window with newly drawn pixels
        pg.display.flip()  

        # Limit framerate by waiting a 10-100 milliseconds
        time.sleep(0.15)
    
    elif state == "END":
        screen.fill((0,0,0))
        text = font_press_enter.render("GAMEOVER", True, (220,220,10))
        text_rect = text.get_rect(center=(17*32/2, 21*32/2))
        screen.blit(text, text_rect)

        # Update window with newly drawn pixels
        pg.display.flip() 

        ## Handle events (keypresses etc.)
        events = pg.event.get()
        for event in events:

            # Close window (e.g. pressing [x] or Ctrl+F4)
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

import pygame as pg
import numpy as np

class Level:

    def __init__(self, file):

        self.tiles = [] #the map
        self.map = [] #for the pathfinding
        self.player_pos_row = 0
        self.player_pos_col = 0
        self.ghost_pos_row = 0
        self.ghost_pos_col = 0
        with open(file, "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                map_row = []
                c = 0
                for character in line:
                    row.append(character)
                    if character == "#":
                        map_row.append(0)
                    else:
                        map_row.append(1)
                    
                    c += 1
                    if character == "p":
                        self.player_pos_row = len(self.tiles)
                        self.player_pos_col = c
                    elif character == "g":
                        self.ghost_pos_row = len(self.tiles)
                        self.ghost_pos_col = c
                        print(self.ghost_pos_row)
                        print(self.ghost_pos_col)
                self.tiles.append(row)
                self.map.append(map_row)

        grid = np.array(self.map)


    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1) 
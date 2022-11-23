import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = [] #the map
        self.map = [] #for the pathfinding
        with open(file, "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                map_row = []
                for character in line:
                    row.append(character)
                    if character == "#":
                        map_row.append(0)
                    else:
                        map_row.append(1)
                self.tiles.append(row)
                self.map.append(map_row)
                #print(map_row)
        


    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)
                           


        
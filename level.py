import pygame as pg

class Level:

    def __init__(self, file):

        self.tiles = []
        self.player_pos_row = 0
        self.player_pos_col = 0
        with open(file, "r") as level_file:
            for line in level_file:
                line = line.rstrip("\r\n") # Remove line endings
                row = []
                for character in line:
                    row.append(character)
                    if character == "p":
                        print("found the P")
                        self.player_pos_row = 5
                        self.player_pos_col = 4
                self.tiles.append(row)
    

    def draw(self, screen):
        for row_idx, row in enumerate(self.tiles):
            for col_idx, tile in enumerate(row):
                if tile == "#":
                    pg.draw.rect(screen, (10,10,250), pg.Rect(col_idx*32+1, row_idx*32+1, 30, 30), 1)
                           


        
import pygame as pg
import random
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import rotate_matrix

class Ghost:

    def __init__(self, row, col):

        # https://sfxr.me/#34T6PktF8TcRjBGBCtaWAp8xrJeEmwSfouC2KVwAWC42iM2UWcDqruxhd8Xq4MFBc7kMaDGuyeyqde9ddiWDHprGh2dvs6Ery9NZQmbQM9gyXmSZzdhxPnMnw
        # https://sfxr.me/#34T6PkpqAUU8XZ3ze41FCou6ZCuAPdnvQEjkm2P1TPRMxjSRZdiQm9e5DJF1dPTvN8C3gPXJ7DuFniwZVHsmDC5qDkCUYDnkkgQAsqe9MaC2pHxKexVqdd5Jw
        self.sound_move0 = pg.mixer.Sound("sounds/pacman_move_0.wav")
        self.sound_move1 = pg.mixer.Sound("sounds/pacman_move_1.wav")
        self.sound_move0.set_volume(0.5)
        self.sound_move1.set_volume(0.5)

        self.col = col
        self.row = row

        self.images = []
        for i in range(2):
            img = pg.image.load(f"images/ghost_{i}.png")
            img = pg.transform.scale(img, (32,32))
            self.images.append(img)

        self.tick = 0

        self.finder = AStarFinder()


    def move(self, level, target):
        moving = False
        dir = ["up","down","left","right"]
        #choose direction
        direction = random.choice(dir)

        grid_rotated = rotate_matrix.clockwise(level.map)

        grid = Grid(len(level.map[0]), len(level.map), grid_rotated)

        start = grid.node(self.row,self.col)
        end = grid.node(target.row,target.col)

        try:
            path = self.finder.find_path(start,end,grid)
            print("path", path[0]) #brug try and except for ikke at finde en en tom liste og derved en fejl
            self.row = path[0][1][0]
            self.col = path[0][1][1]
        except:
            path = []

        self.tick += 1 
    
    def draw(self,screen):
        r = self.tick%2
        screen.blit(self.images[r], (self.col*32, self.row*32)) 
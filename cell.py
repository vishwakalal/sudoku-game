import pygame

RED = (255,0,0)
BLACK=(0,0,0)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value=value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketchval=0
        self.outline_col= BLACK


    def set_cell_value(self, value):
        self.value=value

    def set_sketched_value(self, value):
        self.sketchval=value


import pygame
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku


BLACK = (0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GRAY=(128, 128, 128)



pygame.init()
font=pygame.font.Font(None, 36)
font2=pygame.font.Font(None, 80)


class Cell:
    cell_width=640//9
    cell_height=640//9
    def __init__(self, value, row, col, screen):
        self.value=value
        self.row=row
        self.col=col
        self.sketched=0
        self.screen=screen
        self.selected=False


    def set_cell_value(self, value):
        self.value=value

    def set_sketched_value(self, value):
        self.sketched=value



    def draw(self):

        x= self.col*Cell.cell_width
        y= self.row*Cell.cell_height

        cell_border=pygame.Rect(x+5, y+5, Cell.cell_width, Cell.cell_height)
        pygame.draw.rect(self.screen, BLACK, cell_border, 1)

        if self.value!=0:
            text=font2.render(str(self.value), True, BLACK)
            self.screen.blit(text, (x+20, y+20))
        elif self.sketched!=0:
            text=font.render(str(self.sketched), True, GRAY)
            self.screen.blit(text, (x+10, y+10))

        if self.selected==True:
            pygame.draw.rect(self.screen, RED, cell_border, 5)











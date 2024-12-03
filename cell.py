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


    def draw(self):
        width=self.screen.get_width()//9
        length=self.screen.get_height()//9
        pygame.draw.rect(self.screen, self.outline_col, (width*self.col, row*length), 2)

    
        game_font=pygame.font.Font(None, 30)

        if self.value!=0:
            tex = game_font.render(str(self.value), True, BLACK)
            self.screen.blit(tex, ((self.col*width)+10, (self.row*length)+10))
        elif self.sketchval!=0:
            tex=game_font(str(self.sketchval), True, RED)
            self.screen.blit(tex, ((self.col*width+5), (self.row*length)+5))

    
    def restart(self):
        self.value=0
        self.sketchval=0

        





    
import pygame
from sudoku_generator import*
from cell import*

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected = None
        self.og_board = None
        self.cells = []
        for r in range(9):
            self.cells.append([None] * 9)


    def draw(self):
        #drawing all the cells
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                self.cells[r][c].draw()


        for i in range(10):
            # setting the correct line thickness for each line
            if i % 3 == 0:
                width = 3
            else:
                width = 1
            # drawing the horizontal lines
            pygame.draw.line(self.screen, BLACK, (0, self.height // 9 * i), (self.width, self.height // 9 * i), width)
            # drawing the vertical lines
            pygame.draw.line(self.screen, BLACK,(self.width // 9 * i, 0), (self.width // 9 * i, self.height), width)

    def select(self, row, col):
        # unselects last selected cell if any
        if self.selected != None:
            self.selected.outline_col = BLACK
        #selects the new cell and highlights it red
        self.selected = self.cells[row][col]
        self.selected.outline_col = RED

    def click(self, row, col):
        if row < self.width and col < self.height:
            row // (self.height // 9)
            col // (self.width // 9)
            return row, col
        return None

    def clear(self):
        if self.selected != None:
            self.selected.set_cell_value(0)
            self.selected.set_sketched_value(0)

    def sketch(self, value):
        if self.selected != None:
            self.selected.set_cell_value(value)

    def place_number(self, value):
        if self.selected != None:
            self.selected.set_cell_value(value)
            self.selected.set_sketched_value(0)

    def reset_to_orginal(self):
        for r in range(9):
            for c in range(9):
                cell = self.cells[r][c]
                if cell and self.og_board[r][c] == 0:
                    cell.restart()

        def is_full(self):
            for r in range(9):
                for c in range(9):
                    if self.cells[r][c].value == 0:
                        return False
            return True

        def update_board(self):
            for r in range(9):
                for c in range(9):
                    self.og_board[r][c] = self.cells[r][c].value

        def find_empty(self):
            for r in range(9):
                for c in range(9):
                    if self.cells[r][c].value == 0:
                        return r, c
            return None

        def check_board(self):
            for r in range(9):
                nums = []
                for c in range(9):
                    nums.append(self.cells[r][c].value)
                nums.sort()
                if sorted(nums) != list(range(1, 10)):
                    return False

            for c in range(9):
                nums = []
                for r in range(9):
                    nums.append(self.cells[r][c].value)
                nums.sort()
                if sorted(nums) != list(range(1, 10)):
                    return False

            for box_r in range(3):
                for box_c in range(3):
                    nums = []
                    for r in range(box_r * 3, box_r * 3 + 3):
                        for c in range(box_c * 3, box_c * 3 + 3):
                            nums.append(self.cells[r][c].value)
                    nums.sort()
                    if sorted(nums) != list(range(1, 10)):
                        return False

            return True



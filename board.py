from cell import*
from sudoku_generator import*

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.removed=0
        self.cell_board=[]
        self.selected=None
        self.mode='real'
        self.answerkey=[]


        if difficulty.lower()=="easy":
            self.removed=30
        elif difficulty.lower()=="medium":
            self.removed=40
        else:
            self.removed=50
        sudoku = SudokuGenerator(9, self.removed)

        sudoku.fill_values()
        print("answerkey:")
        self.answerkey = sudoku.get_board()
        print(self.answerkey)
        print()
        print()
        sudoku.print_board()
        sudoku.remove_cells()
        # print('game')
        # sudoku.print_board()
        self.board=sudoku.get_board()

        self.original_board = []
        for row in self.board:
            new_row = list(row)
            self.original_board.append(new_row)

        for row in range(9):
            cell_row = []
            for col in range(9):
                value = self.board[row][col]
                cell_row.append(Cell(value, row, col, screen))
            self.cell_board.append(cell_row)

    def draw_cells(self):
        for row in self.cell_board:
            for cell in row:
                cell.draw()



    def draw(self):
        self.draw_cells()
        for i in range(10):
            thickness=5
            if i%3==0:
                thickness=7
            pygame.draw.line(self.screen, BLACK, (5, i*Cell.cell_height+5), (self.width+5, i*Cell.cell_height+5), thickness)
            pygame.draw.line(self.screen, BLACK, (i*Cell.cell_width+5, 5), (i*Cell.cell_width+5, self.height+5), thickness)

    def select(self, row, col):
        if self.selected:
            self.selected.selected = False

        cell = self.cell_board[row][col]
        cell.selected = True
        self.selected = cell

    def click(self, row , col):
        if self.selected!=None:
            return (row, col)
        return None

    def clear(self):
        self.selected=None

    def sketch(self, value):
        self.selected.set_sketched_value(value)

    def place_num(self, value):
        if self.selected:
            self.selected.set_cell_value(value)
            self.board[self.selected.row][self.selected.col] = value

    def reset_to_original(self):
        self.board = []
        for row in self.original_board:
            copied_row = row[:]
            self.board.append(copied_row)
        for row in self.board:
            print(row)

        for row in range(9):
            for col in range(9):
                value = self.original_board[row][col]
                self.cell_board[row][col].set_cell_value(value)
                self.cell_board[row][col].set_sketched_value(0)


    def is_valid_board(self):

        for row in range(9):
            for col in range(9):
                current_value = self.board[row][col]
                answer_value = self.answerkey[row][col]
                if current_value != answer_value:
                    return False
        return True






























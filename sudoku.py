import pygame

from board import Board
from sudoku_generator import *
from cell import Cell

LVL1=(244,227,246)
LVL2 = (219,188,223)
LVL3=(188, 139, 194)
RED = (255,0,0)
GREEN = (0,255,0)

WIDTH=650
HEIGHT=740
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))



def scale(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

BKG= scale(pygame.image.load('jerry-pointing-1.jpg'), 1.7)
EASY= scale(pygame.image.load('easy.png'), 0.2)
MEDIUM= scale(pygame.image.load('medium.png'), 0.2)
HARD= scale(pygame.image.load('hard.png'), 0.2)
EXIT= scale(pygame.image.load('exit.png'), 0.13)
RESET= scale(pygame.image.load('reset.png'), 0.1)
RESTART = scale(pygame.image.load('restart.png'), 0.07)


def win():
    run = True
    while run:
        screen.fill(GREEN)
        screen.blit(EXIT, (360, 645))
        font = pygame.font.Font(None, 50)
        text_surface = font.render("You win!", True, WHITE)
        screen.blit(text_surface, (100, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 362 <= x <= 434 and 654 <= y <= 725:
                    pygame.quit()

def lose(board):
    run = True
    while run:
        screen.fill(RED)
        screen.blit(RESET, (220, 655))
        screen.blit(EXIT, (360, 645))
        font = pygame.font.Font(None, 50)
        text_surface = font.render("LOSER!!!! :(", True, WHITE)
        screen.blit(text_surface, (325, 370))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 226 <= x <= 284 and 659 <= y <= 723:
                    board.reset_to_original()
                    board.draw()
                    pygame.display.flip()
                    run = False
                elif 362 <= x <= 434 and 654 <= y <= 725:
                    pygame.quit()

def easy():
    running = True
    board = Board(640, 640, screen, 'easy')
    while running:
        screen.fill(LVL1)
        screen.blit(EXIT, (360, 645))
        screen.blit(RESET, (220, 655))
        screen.blit(RESTART, (60, 670))

        board.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 226 <= x <= 284 and 659 <= y <= 723:
                    board.reset_to_original()
                    board.draw()
                    pygame.display.flip()
                if 61 <= x <= 184 and 671 <= y <= 706:
                    running = False
                elif 362 <= x <= 434 and 654 <= y <= 725:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 0 <= x < 640 and 0 <= y < 640:
                    row, col = y // Cell.cell_height, x // Cell.cell_width
                    board.select(row, col)

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    board.mode = "sketch"
                elif event.key == pygame.K_r:
                    board.mode = "real"
                if board.selected:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                     pygame.K_8, pygame.K_9]:
                        if board.mode == "sketch":
                            board.sketch(int(event.unicode))
                        elif board.mode == "real":
                            board.place_num(int(event.unicode))
                        board.draw()
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if board.is_valid_board():
                        win()
                        running = False
                    else:
                        lose(board)

def medium():
    running = True
    board = Board(640, 640, screen, 'medium')
    while running:
        screen.fill(LVL2)
        screen.blit(EXIT, (360, 645))
        screen.blit(RESET, (220, 655))
        screen.blit(RESTART, (60, 670))
        board.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 220 <= x <= 295 and 654 <= y <= 725:
                    board.reset_to_original()
                    board.draw()
                    pygame.display.flip()
                if 61 <= x <= 184 and 671 <= y <= 706:
                    running = False
                elif 362 <= x <= 434 and 654 <= y <= 725:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 0 <= x < 640 and 0 <= y < 640:
                    row, col = y // Cell.cell_height, x // Cell.cell_width
                    board.select(row, col)

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    board.mode = "sketch"
                elif event.key == pygame.K_r:
                    board.mode = "real"

                if board.selected:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                     pygame.K_8, pygame.K_9]:
                        if board.mode == "sketch":
                            board.sketch(int(event.unicode))
                        elif board.mode == "real":
                            board.place_num(int(event.unicode))
                        board.draw()
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if board.is_valid_board():
                        win()
                        running = False
                    else:
                        lose(board)

def hard():
    running = True
    board = Board(640, 640, screen, 'hard')

    while running:
        screen.fill(LVL3)
        screen.blit(EXIT, (360, 645))
        screen.blit(RESET, (220, 655))
        screen.blit(RESTART, (60, 670))
        board.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 220 <= x <= 295 and 654 <= y <= 725:
                    board.reset_to_original()
                    board.draw()
                    pygame.display.flip()
                if 61 <= x <= 184 and 671 <= y <= 706:
                    running = False
                elif 362 <= x <= 434 and 654 <= y <= 725:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 0 <= x < 640 and 0 <= y < 640:
                    row, col = y // Cell.cell_height, x // Cell.cell_width
                    board.select(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    board.mode = "sketch"
                elif event.key == pygame.K_r:
                    board.mode = "real"

                if board.selected:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                                     pygame.K_8, pygame.K_9]:
                        if board.mode == "sketch":
                            board.sketch(int(event.unicode))
                        elif board.mode == "real":
                            board.place_num(int(event.unicode))
                        board.draw()
                        pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if board.is_valid_board():
                        win()
                        running = False
                    else:
                        lose(board)

def main_menu():
    running = True
    while running:
        screen.blit(BKG, (0, 0))
        screen.blit(EASY, (40, 240))
        screen.blit(MEDIUM, (40, 290))
        screen.blit(HARD, (40, 340))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 41 <= x <= 202 and 244 <= y <= 274:
                    easy()
                elif 41 <= x <= 203 and 290 <= y <= 325:
                    medium()
                elif 41 <= x <= 203 and 340 <= y <= 371:
                    hard()




main_menu()




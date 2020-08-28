import threading
import time
import os
import pygame
import sudoku.solver.solver as solver
from sudoku.gui.board import Board


def render_window(win, board, countdown):
    win.fill((31, 33, 34))
    fnt = pygame.font.SysFont('Helvetica Neue', 20)

    text = fnt.render("Time: " + format_time(countdown), 1, (160, 160, 160))
    # Render time
    win.blit(text, (8, 560))
    # Render board
    board.draw(win)


def format_time(secs):
    sec = secs % 60
    minute = secs//60
    return str(minute) + "m " + str(sec) + "s"


def play():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Game")
    board = Board(9, 9, 540, 540)
    key = None
    run = True
    solved = False
    start = time.time()
    while run:

        if not solved:
            play_time = round(time.time() - start)
            play_time = 20

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and not solved:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None

                        if board.is_solved():
                            print("Solved.")
                            solved = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        render_window(win, board, play_time)
        pygame.display.update()


def solve():
    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku Solver")
    board = Board(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    solver_thread = threading.Thread(target=solver.solve_board, args=(board,), daemon=True)
    solver_thread.start()
    while run:
        solved = board.is_solved()

        if not solved:
            play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        render_window(win, board, play_time)
        pygame.display.update()


def main():
    x = 200
    y = 200
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    play_option = "1"
    solver_option = "2"

    def enquire_choice():
        return input("""Choose an option [1-2]:
        1. Solve Sudoku
        2. Let the Computer solve it\n""").strip()

    choice = enquire_choice()

    if choice is play_option:
        pygame.init()
        play()
        pygame.quit()
    elif choice is solver_option:
        pygame.init()
        solve()
        pygame.quit()
    else:
        print("illegal choice "+choice)

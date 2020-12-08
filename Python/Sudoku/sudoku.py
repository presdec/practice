# @author : Philip Prescott-Decie
# @version : 1.0.0
# @date : 21-03-2020
# @email : presdec@gmail.com
# Tested and working on Ubuntu 18.04 with Python 3.7
# small test 2


import datetime
import numpy as np

intro = """\nSudoku solver, it uses backtracking to solve a NumPy generated board.
By Philip Prescott-Decie \xa92019.\n
 _____ _____ _____ _____    _____ _____ ____  _____ _____ _____
|  _  |  |  |_   _|     |  |   __|  |  |    \|     |  |  |  |  |
|     |  |  | | | |  |  |  |__   |  |  |  |  |  |  |    -|  |  |
|__|__|_____| |_| |_____|  |_____|_____|____/|_____|__|__|_____|
in == 100 lines ;)\n"""
print(intro)


def generate_sudoku(mask_rate=0.5):  # generates a new sudoku
    while True:
        n = 9
        m = np.zeros((n, n), np.int)
        rg = np.arange(1, n + 1)
        m[0, :] = np.random.choice(rg, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(rg, m[:r, c])
                    row_rest = np.setdiff1d(rg, m[r, :c])
                    avb1 = np.intersect1d(col_rest, row_rest)
                    sub_r, sub_c = r // 3, c // 3
                    avb2 = np.setdiff1d(np.arange(0, n + 1), m[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                    avb = np.intersect1d(avb1, avb2)
                    m[r, c] = np.random.choice(avb, size=1)
            break
        except ValueError:
            pass
    mm = m.copy()
    mm[np.random.choice([True, False], size=m.shape, p=[mask_rate, 1 - mask_rate])] = 0
    return mm


def solve(bo):  # keeps trying numbers, if nothing works it backtracks
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def valid(bo, num, pos):  # loop through numbers, check valid
    for i in range(len(bo[0])):  # Check row
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):  # Check column
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3; box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):  # Check box
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):  # print the board
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("  - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else: print(str(bo[i][j]) + " ", end="")


def find_empty(bo):  # loop through board, find first empty element
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col
    return None


def main():
    a = datetime.datetime.now()
    board = generate_sudoku(mask_rate=0.7)  # change mask rate to raise lower difficulty
    print_board(board)
    print("\nGenerated in -- " + str(int((datetime.datetime.now() - a).total_seconds() * 1000)) + " Milliseconds ---\n")
    g = datetime.datetime.now()
    solve(board)
    print_board(board)
    print("\nSolved in -- " + str(int((datetime.datetime.now()-g).total_seconds() * 1000)) + " Milliseconds ---")


main()

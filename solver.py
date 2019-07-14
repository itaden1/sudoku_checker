"""
Sudoku Solver

Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)
Sudoku Solution Validator

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Each row contains 1 to 9
Each column contains 1 to 9
Each 3x3 segment contains 1 to 9

Examples
validSolution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
    [5, 3, 4, 6, 7, 8, 9, 1, 2], 
    [6, 7, 2, 1, 9, 0, 3, 4, 8],
    [1, 0, 0, 3, 4, 2, 5, 6, 0],
    [8, 5, 9, 7, 6, 1, 0, 2, 0],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 0, 1, 5, 3, 7, 2, 1, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""

from abc import ABC, abstractmethod


class SudokuBoard(ABC):

    @abstractmethod
    def get_row(self, index):
        pass

    @abstractmethod
    def get_col(self, index):
        pass

    @abstractmethod
    def get_matrix_segment(self, x, y):
        pass


class StandardSudokuBoard(SudokuBoard):

    def __init__(self, matrix):
        self.matrix = matrix

    def get_row(self, index):
        return self.matrix[index]

    def get_col(self, index):
        return [r[index] for r in self.matrix]

    def get_matrix_segment(self, x, y):
        nx = x - x % 3
        ny = y - y % 3
        sub_matrix = []
        for i in range(nx,nx+3):
            line = []
            for j in range(ny,ny+3):
                line.append(self.matrix[i][j])
            sub_matrix.append(line)
        return sum(sub_matrix, [])


class ValidArray(ABC):

    @abstractmethod
    def check_array(self, array):
        pass


class IntArrayChecker(ValidArray):
    """Checks an array contains all required integers. Retuns a Boolean"""
    def __init__(self, valid_array=[]):
        self.valid_array = valid_array

    def check_array(self, array):
        if not sorted(array[:]) == self.valid_array:
            return False
        return True


def validate_board(matrix):
    board = StandardSudokuBoard(matrix)
    checker = IntArrayChecker([i for i in range(1,10)])
    for i in range(len(matrix)):
        print("row {}".format(i), checker.check_array(board.get_row(i)))
        print("col {}".format(i), checker.check_array(board.get_col(i)))
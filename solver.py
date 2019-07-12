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

class Solver:
    def __init__(self, board):
        self.board = board
        self.valid_array = [i for i in range(1,10)]
        self.checked = {}

    def valid(self):
        status = True
        if any(0 in i for i in self.board):
            return False

        while status:
            for i in range(0,3,9):
                status = self.check_segment(i,0)
                status = self.check_array(self.get_col(i))
                status = self.check_array(self.get_row(i))
            break
        return status

    def get_segment(self, x, y):
        """Find the nearest matrix of nine based on a coordinate"""
        nx = x - x % 3
        ny = y - y % 3
        matrix = []
        for i in range(nx,nx+3):
            line = []
            for j in range(ny,ny+3):
                line.append(self.board[i][j])
            matrix.append(line)
        return matrix

    def get_col(self, i):
        col = [c[i] for c in self.board]
        return col

    def get_row(self, x):
        return self.board[x]

    def check_array(self, array):
        return sorted(list(array)) == self.valid_array

    def check_segment(self, x, y):
        """Check a segment to ensure it contains nine uniqe numbers"""
        flat_list = sum(self.get_segment(x,y), [])
        return self.valid_array == sorted(flat_list[:]) and len(set(flat_list)) == 9


def validSolution(board):
    s = Solver(board)
    return s.valid()

from solver import IntArrayChecker, StandardSudokuBoard, validate_board
import unittest

class TestSudokuSolution(unittest.TestCase):

    def setUp(self):

        self.solver = IntArrayChecker([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.board = StandardSudokuBoard


        self.valid_array = [i for i in range(1, 10)]
        self.bad_length_array = [i for i in range(4, 7)]
        self.doubles_array = [1, 1, 2, 3, 4, 5, 6, 6, 9]
        self.incomplete_array = [0, 2, 3, 4, 0, 6, 7, 8, 9]
        self.bad_integer_array = [1, 2, 34, 4, 56, 6, 7, 8, 9]

        self.valid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                            [6, 7, 2, 1, 9, 5, 3, 4, 8],
                            [1, 9, 8, 3, 4, 2, 5, 6, 7],
                            [8, 5, 9, 7, 6, 1, 4, 2, 3],
                            [4, 2, 6, 8, 5, 3, 7, 9, 1],
                            [7, 1, 3, 9, 2, 4, 8, 5, 6],
                            [9, 6, 1, 5, 3, 7, 2, 8, 4],
                            [2, 8, 7, 4, 1, 9, 6, 3, 5],
                            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.invalid_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                              [6, 7, 2, 1, 9, 5, 3, 4, 8],
                              [1, 9, 8, 3, 4, 2, 5, 6, 7],
                              [5, 8, 9, 7, 6, 1, 4, 2, 3],
                              [4, 2, 6, 8, 5, 3, 7, 9, 1],
                              [7, 1, 3, 9, 2, 4, 8, 5, 6],
                              [9, 6, 1, 5, 3, 7, 2, 8, 4],
                              [2, 8, 7, 4, 1, 9, 6, 3, 5],
                              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

        self.unfinished_board = [[5, 3, 0, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]



    def test_check_array_valid(self):
        self.assertTrue(self.solver.check_array(self.valid_array))

    def check_array_bad_length(self):
        self.assertFalse(self.solver.check_array(self.bad_length_array))

    def check_array_doubles(self):
        self.assertFalse(self.solver.check_array(self.bad_length_array))

    def check_array_incomplete(self):
        self.assertFalse(self.solver.check_array(self.incomplete_array))

    def check_array_bad_integer(self):
        self.assertFalse(self.solver.check_array(self.bad_integer_array))

    def test_get_row(self):
        b = self.board(self.valid_board)
        self.assertEqual(b.get_row(0), [5, 3, 4, 6, 7, 8, 9, 1, 2])
        self.assertEqual(b.get_row(3), [8, 5, 9, 7, 6, 1, 4, 2, 3])

    def test_get_column(self):
        b = self.board(self.valid_board)
        self.assertEqual(b.get_col(0), [5, 6, 1, 8, 4, 7, 9, 2, 3])
        self.assertEqual(b.get_col(3), [6, 1, 3, 7, 8, 9, 5, 4, 2])

    def test_get_matrix_segment(self):
        b = self.board(self.valid_board)
        self.assertEqual(b.get_matrix_segment(0, 0), [5, 3, 4, 6, 7, 2, 1, 9, 8])
        self.assertEqual(b.get_matrix_segment(7, 5), [5, 3, 7, 4, 1, 9, 2, 8, 6])

    def test_validate_board(self):
        validate_board(self.valid_board)
        self.assertTrue(validate_board(self.valid_board))

    def test_invalid_board(self):
        validate_board(self.invalid_board)
        self.assertFalse(validate_board(self.invalid_board))

    def test_unfinished_board(self):
        validate_board(self.unfinished_board)
        self.assertFalse(validate_board(self.unfinished_board))


if __name__ == "__main__":
    unittest.main()
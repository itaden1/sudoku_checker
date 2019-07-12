import solver
import unittest

class TestSudokuSolution(unittest.TestCase):

    def setUp(self):
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

    def test_get_matrix(self):
        s = solver.Solver(self.valid_board)
        matrix = s.get_segment(2,2)
        self.assertEqual(matrix, [[5,3,4],[6,7,2],[1,9,8]])
    
    def test_check_array(self):
        s = solver.Solver(self.valid_board)
        self.assertTrue(s.check_array([8,4,5,6,2,3,1,7,9]))

    def test_diff_seg(self):
        s = solver.Solver(self.valid_board)
        self.assertTrue(s.check_segment(2,5))
        fs = solver.Solver(self.unfinished_board)
        self.assertFalse(fs.check_segment(2,2))

    def test_correct_solution(self):
        self.assertEqual(solver.validSolution(self.valid_board), True)

    def test_unfinished_solution(self):
        self.assertEqual(solver.validSolution(self.unfinished_board), False)

    def test_invalid_solution(self):
        s = solver.Solver(self.invalid_board)
        print(s.board)
        self.assertEqual(solver.validSolution(self.invalid_board), False)


if __name__ == "__main__":
    unittest.main()
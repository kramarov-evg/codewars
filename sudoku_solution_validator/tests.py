import unittest
import random
import copy
import sudoku_solution_validator as ssv


class Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    def invalidate_row(self, row_num, zero_based_invalidation=False):
        invalidated = copy.deepcopy(self.valid)
        if zero_based_invalidation:
            invalidated[row_num][random.randint(0, 8)] = 0
        else:
            i1, i2 = 0, 0
            while i1 == i2:
                i1, i2 = random.randint(0, 8), random.randint(0, 8)
            invalidated[row_num][i1] = invalidated[row_num][i2]
        return invalidated

    def invalidate_col(self, col_num, zero_based_invalidation=False):
        invalidated = copy.deepcopy(self.valid)
        if zero_based_invalidation:
            invalidated[random.randint(0, 8)][col_num] = 0
        else:
            i1, i2 = 0, 0
            while i1 == i2:
                i1, i2 = random.randint(0, 8), random.randint(0, 8)
            invalidated[i1][col_num] = invalidated[i2][col_num]
        return invalidated

    def invalidate_sub_grids(self, zero_based_invalidation=False):
        invalidated = [copy.deepcopy(self.valid) for i in range(9)]
        for i in range(3):
            for j in range(3):
                if zero_based_invalidation:
                    v_shift = i*3 + random.randint(0, 2)
                    h_shift = j*3 + random.randint(0, 2)
                    invalidated[i*3+j][v_shift][h_shift] = 0
                else:
                    v_shift1, v_shift2, h_shift1, h_shift2 = 0, 0, 0, 0
                    while v_shift1 == v_shift2:
                        v_shift1, v_shift2 = random.randint(0, 2), random.randint(0, 2)
                    while h_shift1 == h_shift2:
                        h_shift1, h_shift2 = random.randint(0, 2), random.randint(0, 2)
                    invalidated[i*3+j][v_shift1][h_shift1] = invalidated[i*3+j][v_shift2][h_shift2]
        return invalidated

    def test_row_err(self):

        # Invalidated 1st row
        invalid_1st_row_zero = self.invalidate_row(0, zero_based_invalidation=True)
        invalid_1st_row = self.invalidate_row(0, zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_1st_row_zero), False,
                         msg='Undetected error with zero in first row')
        self.assertEqual(ssv.valid_solution(invalid_1st_row), False,
                         msg='Undetected error with repeating numbers in first row')

        # Invalidate middle row
        invalid_mid_row_zero = self.invalidate_row(random.randint(1, 7), zero_based_invalidation=True)
        invalid_mid_row = self.invalidate_row(random.randint(1, 7), zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_mid_row_zero), False,
                         msg='Undetected error with zero in middle row')
        self.assertEqual(ssv.valid_solution(invalid_mid_row), False,
                         msg='Undetected error with repeating numbers in middle row')

        # Invalidate last row with zero
        invalid_1st_row_zero = self.invalidate_row(-1, zero_based_invalidation=True)
        invalid_1st_row = self.invalidate_row(-1, zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_mid_row_zero), False,
                         msg='Undetected error with zero in last row')
        self.assertEqual(ssv.valid_solution(invalid_mid_row), False,
                         msg='Undetected error with repeating numbers in last row')

    def test_col_err(self):

        # Invalidated 1st col
        invalid_1st_col_zero = self.invalidate_col(0, zero_based_invalidation=True)
        invalid_1st_col = self.invalidate_col(0, zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_1st_col_zero), False,
                         msg='Undetected error with zero in first col')
        self.assertEqual(ssv.valid_solution(invalid_1st_col), False,
                         msg='Undetected error with repeating numbers in first col')

        # Invalidate middle col
        invalid_mid_col_zero = self.invalidate_col(random.randint(1, 7), zero_based_invalidation=True)
        invalid_mid_col = self.invalidate_col(random.randint(1, 7), zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_mid_col_zero), False,
                         msg='Undetected error with zero in middle col')
        self.assertEqual(ssv.valid_solution(invalid_mid_col), False,
                         msg='Undetected error with repeating numbers in middle col')

        # Invalidate last col with zero
        invalid_1st_col_zero = self.invalidate_col(-1, zero_based_invalidation=True)
        invalid_1st_col = self.invalidate_col(-1, zero_based_invalidation=False)

        self.assertEqual(ssv.valid_solution(invalid_mid_col_zero), False,
                         msg='Undetected error with zero in last col')
        self.assertEqual(ssv.valid_solution(invalid_mid_col), False,
                         msg='Undetected error with repeating numbers in last col')

    def test_sub_grid_err(self):
        invalid_sub_grids_zero = self.invalidate_sub_grids(zero_based_invalidation=True)
        invalid_sub_grids = self.invalidate_sub_grids(zero_based_invalidation=False)
        for i in range(9):
            self.assertEqual(ssv.valid_solution(invalid_sub_grids_zero[i]), False,
                             msg='Undetected error with zero in sub-grid ({},{})'.format(i // 3, i % 3))
            self.assertEqual(ssv.valid_solution(invalid_sub_grids[i]), False,
                             msg='Undetected error with repeating numbers in sub-grid ({},{})'.format(i // 3, i % 3))

    def test_valid(self):
        self.assertEqual(ssv.valid_solution(self.valid), True, msg='False negative result')


if __name__ == "__main__":
    unittest.main(verbosity=2)

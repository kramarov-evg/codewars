def valid_solution(board):

    # check for error in row/col
    for i in range(9):
        v_set = set()
        h_set = set()
        for j in range(9):
            if (board[i][j] == 0) or (board[i][j] in h_set) or (board[j][i] == 0) or (board[j][i] in v_set):
                return False
            else:
                h_set.add(board[i][j])
                v_set.add(board[j][i])

    # check for error in sub-grids
    # iterating over sub-grids' top-left corners
    for i in range(3):
        for j in range(3):
            sub_grid_set = set()

            # iterating inside sub-grids
            for i_shift in range(3):
                for j_shift in range(3):
                    if (board[i*3 + i_shift][j*3 + j_shift] == 0) or (
                            board[i*3 + i_shift][j*3 + j_shift] in sub_grid_set):
                        return False
                    else:
                        sub_grid_set.add(board[i*3 + i_shift][j*3 + j_shift])
    return True

# Source: https://leetcode.com/problems/sudoku-solver/description/


# TODO: INCOMPLETE!!!

import numpy as np

class Sudoku:
    def __init__(self, init_board: list):
        self.board = init_board

    def fill_rows(self):
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == '.':
                    for i in range(1, 10):
                        if i not in self.board[y] and i not in [col[x] for col in self.board]:
                            self.board[y][x] = i
                            break                   
                        
        return self.board

    def getBlocks(self):
        answer = np.array(self.board).reshape((3,3,3,3)).transpose((0,2,1,3)).reshape((9,9))
        return answer


    def display_board(self):
        for y in range(9):
            print('')
            for x in range(9):
                print(self.board[y][x], end='')
        print('')




if __name__ == "__main__":
    init_board_setup = [
        [5,3,'.','.',7,'.','.','.','.'],
        [6,'.','.',1,9,5,'.','.','.'],
        ['.',9,8,'.','.','.','.',6,'.'],
        [8,'.','.','.',6,'.','.','.',3],
        [4,'.','.',8,'.',3,'.','.',1],
        [7,'.','.','.',2,'.','.','.',6],
        ['.',6,'.','.','.','.',2,8,'.'],
        ['.','.','.',4,1,9,'.','.',5],
        ['.','.','.','.',8,'.','.',7,9],
    ]
    s = Sudoku(init_board_setup)
    s.display_board()
    print(s.getBlocks())
    # s.fill_rows()
    # s.display_board()
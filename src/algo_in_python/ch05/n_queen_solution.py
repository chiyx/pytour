#! /usr/bin/env python3
# coding = utf-8

# n_queen_solution.py - n皇后问题解法


class NQueeenSolution():

    def __init__(self, n):
        self.n = n
        self.cols = {}
        # self.board = [[0] * n for i in range(n)]

    def canPut(self, row, col):
        for (r, c) in self.cols.items():
            if c == col:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True

    def search(self, row):
        if row == self.n:
            return
        for col in range(self.n):
            if self.canPut(row, col):
                self.cols[row] = col
                break
        self.search(row + 1)

if __name__ == '__main__':
    solution = NQueeenSolution(8)
    solution.search(0)
    print(solution.cols)

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def validOneDirection(self, i, j, d1, d2, board) :
        mark = [0 for k in range(9+1)]
        while i < len(board) and j < len(board[0]) :
            if board[i][j] != '.' :
                mark[int(board[i][j])] += 1
            i, j = i+d1, j+d2
        return not filter(lambda x : x >= 2, mark) 
    def checksubbox(self, i, j, board) :
        mark = [0 for k in range(9+1)]
        for d1 in range(0, 3) :
            for d2 in range(0, 3) :
                if board[i+d1][j+d2] != '.' :
                    mark[int(board[i+d1][j+d2])] += 1
        return not filter(lambda x : x >= 2, mark) 

    def isValidSudoku(self, board):
        valid = True
        for i in range(9) :
            if valid and  not self.validOneDirection(i, 0, 0, 1, board) or \
               not self.validOneDirection(0, i, 1, 0, board) :
                valid = False
        for i in range(0, 9, 3) :
            for j in range(0, 9, 3) :
                if valid and  not self.checksubbox(i, j, board):
                    valid = False
        return valid 
        
















test = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]

sol = Solution()
print sol.isValidSudoku(test)

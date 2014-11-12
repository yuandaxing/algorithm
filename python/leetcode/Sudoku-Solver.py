class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def tryValidNum(self, i, j, board) :
        v = [0 for k in range(9)]
        for k in range(9) :
            if board[k][j] != '.' :
                v[board[k][j]-1] += 1
            if board[i][k] != '.' :
                v[board[i][k]-1] += 1
        i, j = (i / 3) * 3, (j / 3) * 3
        for m in range(3) :
            for n in range(3) :
                if board[i+m][j+n] != '.' :
                    v[board[i+m][j+n]-1] += 1
        return v
    def solve(self, board, k, pos) :
        if k >= len(pos) : return True
        v = self.tryValidNum(pos[k][0], pos[k][1], board)
        for i in range(9) :
            if not v[i] :
                board[pos[k][0]][pos[k][1]] = i+1
                if self.solve(board, k+1, pos) : return True
        board[pos[k][0]][pos[k][1]] = '.'
        return False
    def solveSudoku(self, board):
        pos, newboard = [], []
        for m in range(9) :
            newboard.append([])
            for n in range(9) :
                if board[m][n] == '.' :
                    pos.append([m, n])
                    newboard[m].append('.')
                else :
                    newboard[m].append(int(board[m][n]))
        self.solve(newboard, 0, pos)
        for i in range(9) :
            board[i] = ''.join(map(str, newboard[i]))


board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

sol = Solution()

sol.solveSudoku(board)
print board

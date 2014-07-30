class Solution:
        # @param board, a 9x9 2D array
        # Capture all regions by modifying the input board in-place.
        # Do not return any value.
	#O(N^2) algorithm
        # new a matrix, initialize X 1, O 0
        # for i mark it 2, search its sorround
        # if cur is boundary, return false, else 
        # return it's surround state.
        # if i return true, mark all the surround 1. else
        # mark all surround false.
        # S[i][j] = S[i+1][j] and S[i][j+1] and S[i-1][j] and S[i][j-1]
        # S[i][j] =  0 < i, j < 9 and true if S[i][j] > 0 else recursive()
	# mark region 1 or -1 
        # mark cur and it's surroun.
        def solve(self, board):
                def checkStatus(i, j, status) :
                        queue,res = [(i, j)], True
                        while len(queue) :
                                i, j = queue.pop(0) 
                                if i < 0 or i >= len(status) or j < 0 or \
                                   j >= len(status[0]) :
                                        res = False; continue
                                elif status[i][j] == 2 or board[i][j] == 'X' :
                                        continue
                                status[i][j] = 2
                                queue.append((i+1, j))
                                queue.append((i, j+1))
                                queue.append((i-1, j))
                                queue.append((i, j-1))
                        return res
                def markX(i, j) :
                        queue = [(i, j)]
                        while len(queue) :
                                i, j = queue.pop(0) 
                                if i < 0 or i >= len(board) or j < 0 or \
                                   j >= len(board[0]) :
                                        continue
                                elif  board[i][j] == 'X' :
                                        continue
                                board[i][j] = 'X'
                                queue.append((i+1, j))
                                queue.append((i, j+1))
                                queue.append((i-1, j))
                                queue.append((i, j-1))
                saveBoard = board
                board = [list(i) for i in saveBoard]
                status = [[0 for j in range(len(board[i]))] \
                                  for i in range(len(board))] 
                for i in range(len(board)) :
                        for j in range(len(board[i])) :
                                if board[i][j] == 'O' and \
                                   status[i][j] == 0 :
                                        if checkStatus(i, j, status) :
#                                                print i, j
                                                markX(i, j)
                for i in range(len(saveBoard)) :
                        saveBoard[i] = ''.join(board[i])
sol = Solution()
b1 = ["OOOOXX","OOOOOO","OXOXOO","OXOOXO","OXOXOO","OXOOOO"]
sol.solve(b1)
print b1

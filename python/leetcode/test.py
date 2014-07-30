class Solution:
        def solve(self, board):
                def checkStatus(i, j, status) :
                        queue = [(i, j)]
                        while len(queue) :
                                i, j = queue.pop(0) 
                                if i < 0 or i >= len(status) or j < 0 or \
                                   j >= len(status[0]) :
                                        return False
                                elif status[i][j] == 2 or board[i][j] == 'X' :
                                        continue
                                status[i][j] = 2
                                queue.append((i+1, j))
                                queue.append((i, j+1))
                                queue.append((i-1, j))
                                queue.append((i, j-1))
                        return True
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
                board = [list(i) for i in board]
                status = [[0 for j in range(len(board[i]))] \
                                  for i in range(len(board))] 
                for i in range(len(board)) :
                        for j in range(len(board[i])) :
                                if board[i][j] == 'O' and \
                                   status[i][j] == 0 :
                                        if checkStatus(i, j, status) :
                                                markX(i, j)
                return [''.join(i) for i in board]

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def __init__(self) :
        pass
    def init(self, board, word) :
        self.board = board 
        self.word = word
        self.track = [[None for j in board[i]] for i in range(len(board))]
        self.direction = [[-1, 0], [0, -1], [1,0], [0,1]]
        self.M = len(board)
        self.N = len(board[0])
    def search(self, i, j, k) :
        if k >= len(self.word):
            return True
        if i<0 or i >= self.M or j < 0 or j >= self.N :
            return False
        if self.board[i][j] != self.word[k] or self.track[i][j] :
            return False
        self.track[i][j] = True
        for d in self.direction :
            if self.search(i+d[0], j+d[1], k+1) :
                return True
        self.track[i][j] = False
        return False 
    def exist(self, board, word):
        board = map(lambda e : e[0], board)
        self.init(board, word)
        for i in range(self.M) :
            for j in range(self.N) :
                if self.search(i, j, 0) :
                    return True
        return False

board = [
  "ABCE",
  "SFCS",
  "ADEE"
]
sol = Solution()
print sol.exist(board, 'ABCB')

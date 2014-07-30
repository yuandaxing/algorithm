class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    # search all the element, set the first element of the row and column to be zero
    # then search again, set all the content to be zero
    #
    def setZeroes(self, matrix):
        if len(matrix) == 0 : return 
        if len(matrix[0]) == 0 : return
        firstR, firstC = all( matrix[0]), \
                         all([z[0] for z in matrix])
        for i in range(1, len(matrix)) :
            for j in range(1, len(matrix[i])) :
                if matrix[i][j] == 0 :
                    matrix[0][j], matrix[i][0] = 0, 0
        for i in range(1, len(matrix)) :
            for j in range(1, len(matrix[i])) :
                if matrix[i][0] == 0 or matrix[0][j] == 0 :
                    matrix[i][j] = 0
        if not firstR :
            for i in range(len(matrix[0])) :
                matrix[0][i] = 0
        if not firstC :
            for row in matrix :
                row[0] = 0

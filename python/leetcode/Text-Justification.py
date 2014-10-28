#F[i,j] = min(F[i,k]+F[i+k, j-k]} or 
#F[i, 1 or 2 or 3 or 4]
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    MAX_VAL = 5000
    def fullJustify(self, words, L):
        F = [[self.MAX_VAL for i in range(len(words)+1)]
             for j in range(len(words))]
        ' initialize the function'
        accu = [0 for i in range(len(words))]
        for i in range(len(words)) :
            accu[i] = len(words[i]) + (0 if i-1 < 0 else accu[i-1])
            
        for i in range(len(words)) :
            for j in range(1, len(words)-i+1) :
                count = accu[i+j-1]-(0 if i-1 < 0 else accu[i-1])
                left = L - count - j + 1
                if left < 0 :
                    break
                F[i][j] = L - count 
        
        trace = [None for i in range(len(words)+1)]
        for j in range(2, len(words)+1) :
            for k in range(1, j) :
                if  F[0][j-k] + F[j-k][k] < F[0][j] :
                    F[0][j] = F[0][j-k] + F[j-k][k]
                    trace[j] = j-k
        
        slice, i = [], len(words)
        while trace[i] :
            slice.append(trace[i])
            i = trace[i]

        slice = slice[-1::-1] + [len(words)]
        text, wordn = [], 0
        for s in range(len(slice)) :
            j = slice[s] - wordn
            last = True if s == len(slice)-1 else False 
            space = F[wordn][j]
            num = j
            rem, each = space, 0
            if num > 1 :
                rem, each = (space - num + 1, 1) if last else \
                            (space % (num-1), space / (num-1))
            cur = words[wordn]
            for z in range(1, j) :
                cur += ' '*each
                if not last and rem :
                    cur += ' '
                    rem -= 1
                cur += words[wordn+z]
            if rem :
                cur += ' '*rem 
            text.append(cur)
            wordn = slice[s]
        return text 

test1 = ["a"]
words = ["This", "is", "an", "example", "of", "text", "justification."]
words2 = ["a","b","c","d","e"]
words3 = ["What","must","be","shall","be."]
sol = Solution()
print sol.fullJustify(words3, 12)
                
                

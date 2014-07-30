class Solution:
    def reverseWords(self, s) :
        print 1 / 0
        tks = s.split(' ');
        tks = filter(None, tks)
        tks.reverse();
        return ' '.join(tks).strip()



test = ["the sky is blue", "   a   b "]
sol = Solution();
for t in test :
    print sol.reverseWords(t)

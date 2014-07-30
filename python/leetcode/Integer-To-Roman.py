class Solution:
    # @return a string
    def __init__(self) :
        self.N_0_9 = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        self.N_10_90 = ['', 'X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        self.N_100_900 = ['', 'C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        self.N_1000_3000=['', 'M', 'MM', 'MMM']


    def findV(self, roman, array, n) :
        lenA = len(array)
        for i in range(len(array)) :
            if roman.startswith(array[lenA-1-i]) :
                return n * (lenA-1-i), len(array[lenA-1-i])
    def romanToInt(self, s):
        sum = 0
        cur, used = self.findV(s, self.N_1000_3000, 1000)
        sum, s = sum + cur, s[used:]
        cur, used = self.findV(s, self.N_100_900, 100)
        sum, s = sum + cur, s[used:]
        cur, used = self.findV(s, self.N_10_90, 10)
        sum, s = sum + cur, s[used:]
        cur, used = self.findV(s, self.N_0_9, 1)
        sum = sum + cur
        return sum
        
    def intToRoman(self, num):
        return SELF.N_1000_3000[num / 1000] +  SELF.N_100_900[num % 1000 / 100]+\
            SELF.N_10_90[num % 100 / 10] + SELF.N_0_9[num % 10]

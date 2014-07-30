def IsPalin(integer) :
    temp = integer
    reV = 0;
    while(temp != 0) :
        rem = temp % 10
        temp = temp / 10
        reV = reV * 10 + rem

    return reV == integer

def IsPalin1(integer) :
    intStr = '';
    temp = integer
    while(temp != 0) :
       intStr += str(temp % 10)
       temp =  temp / 10

    return intStr == intStr[::-1]

def IsPalin2(integer) :
    temp = integer
    K = 1;
    while(temp / 10 > K): K*=10

    while(temp != 0) :
        high = temp / K
        low = temp % 10
        if(low != high) :
            return False
        temp = (temp % K) / 10
        K /= 100
    return True

def TestPalin(integer, isPalin):
    if isPalin(integer) :
        print integer, 'is palindrome'
    else :
        print integer, 'is not palindrome'

testCase = [0, 4, 1000, 12321]
testfun = [IsPalin, IsPalin1, IsPalin2]

for fn in testfun :
    for test in testCase :
        TestPalin(test, fn)

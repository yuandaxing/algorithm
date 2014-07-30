# [ F(n)  ] =  [ 1 1 ] [ F(n-1] ] 
# [ F(n-1)] =  [ 1 0 ] [ F(n-2] ]
#    [ 1 1 ] ^ n - 1      
#    [ 1 0 ]   is what we should compute


def FabMatrix( n ) :
    F = [ [1, 0] [0, 1] ]
    A = [ [1, 1] [1, 0] ]
    while n != 0 :
        if ( n % 2 == 1 ) :
            F = F * A
        A = A * A
        n >>= 1

    return F

n = int(raw_input("input Fabnacci : "))

tempMatrix = FabMatrix( n -1 ) * [1, 1];

print tempMatrix[0]

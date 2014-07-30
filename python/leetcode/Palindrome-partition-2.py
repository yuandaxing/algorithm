
#Given a string s, partition s such that every substring of
# the partition is a palindrome.
#Return the minimum cuts needed for a palindrome partitioning of s.
#For example, given s = "aab",
#Return 1 since the palindrome partitioning ["aa","b"] could
# be produced using 1 cut.

#Solution.1
# A[0, k] the minimal cut of string A[0:k]
# A[0, j] = min{ A[0, k] + 1 if s[k+1, j] is palindrome }
# o(N^3)

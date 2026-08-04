a = input("Enter String1:")
b = input("Enter String2:")
d = len(a)
c = len(b)
dp = [[0 for i in range(c + 1)] for j in range(d + 1)]
for i in range(1,d+1):
    for j in range(1,c+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
# print("Length of Longest Common Subsequence:", dp[d][c])

def lcs(a,b):
    i = d
    j = c
    lcs = ""
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            lcs = a[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs,dp[d][c]
longest_common_subsequence, length = lcs(a,b)
print("Longest Common Subsequence:", longest_common_subsequence)
print("Length of Longest Common Subsequence:", length)
"""
Output:-
Enter String1:adfaaada
Enter String2:sdadadaed
Longest Common Subsequence: daada
Length of Longest Common Subsequence: 5
"""

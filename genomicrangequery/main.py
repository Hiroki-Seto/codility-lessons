# coding: utf-8 #
# メモリエラー


A = [4, 2, 2, -50, 1]

def solution(A):

    n_a = len(A)

    dp = [[None for i in range(n_a+10)] for i in range(n_a+10)]

    minimal = 10*10
    point = -1
    for i in range(n_a):
        for j in range(i+1, n_a):
            if dp[i][j-1]:
                dp[i][j] = dp[i][j-1] + A[j]
            elif dp[i-1][j]:
                dp[i][j] = dp[i-1][j] - A[i]

            dp[i][j] = sum(A[i:j+1])

            if minimal > dp[i][j]/(j-i+1):
                minimal = dp[i][j]/(j-i+1)
                point = i

    return point



print(solution((A)))
# coding:utf-8 #

def solution(A):

    N_ = len(A)

    A = sorted(A)

    result = []

    for i in range(0, N_):
        if A[i] in result:
            result.remove(A[i])
        else:
            result.append(A[i])

    return result[0]


N = int(input())

A = []

for _ in range(N):
    A.append(int(input()))

result = solution(A)

print(result)



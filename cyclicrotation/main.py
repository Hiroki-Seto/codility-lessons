# coding:utf-8 #

def solution(A, K):

    N_ = len(A)

    result = [0 for _ in range(N_)]

    for i in range(N_):
        result[(i+K)%N_] = A[i]

    return result


N = int(input())
K = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

print(A)

result = solution(A, K)

print(result)
# coding:utf-8 #
# small elementsのケースを考えられていない。考える


A = [21, 1]

def solution(A):

    N = len(A)
    sum1 = sum(A[:1])
    sum2 = sum(A[1:])
    result = abs(sum1 - sum2)

    if N == 2:
        return result

    for i in range(1, N):
        sum1 = sum1 + A[i]
        sum2 = sum2 - A[i]
        tmp = abs(sum1 - sum2)
        print(tmp)
        result = min([result, tmp])

    return result

print(solution(A))
# coding:utf-8 #

def solution(A):

    if not A:
        return 1

    A = sorted(A)

    for i, v in enumerate(A):
        if i+1 != v:
            return i+1
    return i+2

A = []

print(solution(A))
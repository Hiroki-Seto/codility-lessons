
A = [1, 2, 3, 4, 5, 7]

def solution(A):

    N = len(A)
    A = sorted(A)

    for i, v in enumerate(A):
        if i+1 != v:
            return 0
    return 1

print(solution(A))
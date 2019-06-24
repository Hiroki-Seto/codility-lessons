# coding: utf-8 #


def solution(A):
    # correctness 100, performance 100
    n_a = len(A)

    count = 0
    add_val = 1

    ind = -1

    for i in range(n_a):
        if A[i] == 0:
            ind = i
            break

    if ind == -1:
        return 0

    for v in A[ind+1:]:
        if v == 0:
            add_val += 1
        else:
            count += add_val


    if count > 1000000000:
        return -1

    return count


A = [0, 1, 0, 1, 1]
print(solution(A))
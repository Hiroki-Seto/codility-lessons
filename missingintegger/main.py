# coding: utf-8 #

def solution(A):
    # correctness 100, performance 100

    A = set(A)

    A = sorted(A)

    n_a = len(A)

    counter = 0

    for v in A:

        if v < 1:
            n_a -= 1
            continue
        else:
            counter += 1

        if counter != v:
            return counter

    if counter == 0:
        return 1

    if counter == n_a:
        return A[-1] + 1

    return counter


A = [i for i in range(200) if i != 101]
print(solution(A))
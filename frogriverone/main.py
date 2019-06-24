
A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

def solurion(X, A):

    N = len(A)

    data = set([i for i in range(1, X+1)])
    for i, v in enumerate(A):
        data.discard(v)
        if not data:
            return i

    return -1

print(solurion(X, A))
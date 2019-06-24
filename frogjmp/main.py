
def solution(X, Y, D):
    new_Y = Y - X

    if new_Y % D == 0:
        return int(new_Y / D)
    else:
        return int(new_Y / D) + 1

X = 10
Y = 100000
D = 20

print(solution(X, Y, D))

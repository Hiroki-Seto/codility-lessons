
def solution(N):

    N = format(N, 'b')
    L = len(N)
    count = 0
    tmp = 0
    for i in range(L):
        if i == 0:
            continue

        if N[i] == '0':
           tmp += 1
        elif N[i] == '1':
            if count < tmp:
                count = tmp
            tmp = 0
    return count


N = int(input())
binary = format(N, 'b')

print(N)
print(binary)
print(solution(N))
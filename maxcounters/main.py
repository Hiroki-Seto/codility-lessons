# correctness 100, performance 100 complete
def solution(N, A):

    counter = [0 for i in range(N)]

    max_opt = N + 1

    max_val = 0
    const_val = 0

    for v in A:

        if v == max_opt:
            const_val = max_val
            continue

        check_val = counter[v-1]

        if const_val > check_val:
            counter[v-1] = const_val + 1
        else:
            counter[v-1] = check_val + 1

        max_val = max(counter[v-1], max_val)

    for i in range(N):
        if counter[i] < const_val:
            counter[i] = const_val



    return counter


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
print(solution(N, A))


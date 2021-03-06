def solution_bf(Z):

    def is_prime(x):
        if x in [0,1]:
            return False

        res = True
        for i in range(2, x):
            if x % i == 0:
                res = False
                break
        return res

    first = 2
    second = 3
    while first * second <= Z:
        last_first = first
        last_second = second
        first = second
        for i in range(first + 1, Z):
            if is_prime(i):
                second = i
                break


    return last_first * last_second


def solution_bf2(Z):
    N = int(Z**0.5) + 10
    A = [False, False] + [True for i in range(2, N + 1)]
    
    for i in range(2, int(N**0.5) + 1):
        if A[i]:
            k = 0
            j = i**2
            while j <= N:
                A[j] = False
                k += 1
                j = i**2 + k * i
    
    P = [i for i, a in enumerate(A) if a]
    
    for i in range(1, len(P)):
        if P[i] * P[i - 1] > Z:
            return P[i - 1] * P[i - 2]

    return P[i] * P[i - 1]


solution = solution_bf2


tc = int(input())
for i in range(1, tc + 1):
    Z = input()
    # if i != 3:
    #     continue
    out = solution(int(Z))
    print("Case #{}: {}".format(i, out))
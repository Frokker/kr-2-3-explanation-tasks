def solve():
    n = int(input())
    k = int(input())

    end_zero = 0
    end_nonzero = k - 1

    for _ in range(2, n + 1):
        end_zero, end_nonzero = end_nonzero, (end_zero + end_nonzero) * (k - 1)

    print(end_zero + end_nonzero)

if __name__ == '__main__':
    solve()
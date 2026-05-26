def solve():
    n = int(input())

    if n == 0:
        print('True')
        return

    a = list(map(int, input().split()))
    total = sum(a)

    if total % 2 != 0:
        print('False')
        return

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for x in a:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]

    print('True' if dp[target] else 'False')

if __name__ == '__main__':
    solve()
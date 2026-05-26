def solve():
    n = int(input())
    a = list(map(int, input().split()))

    cur = best = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)

    print(best)

if __name__ == '__main__':
    solve()
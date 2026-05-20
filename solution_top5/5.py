def solve():
    n, x, y = map(int, input().split())

    if n == 1:
        print(min(x, y))
        return

    first = min(x, y)
    need = n - 1
    left, right = 0, need * min(x, y)

    while left < right:
        mid = (left + right) // 2
        if mid // x + mid // y >= need:
            right = mid
        else:
            left = mid + 1

    print(first + left)

if __name__ == '__main__':
    solve()
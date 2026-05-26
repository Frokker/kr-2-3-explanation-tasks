def can(length, wires, k):
    total = 0
    for w in wires:
        total += w // length
        if total >= k:
            return True
    return False

def solve():
    n, k = map(int, input().split())
    wires = [int(input()) for _ in range(n)]

    left, right, ans = 1, max(wires), 0
    while left <= right:
        mid = (left + right) // 2
        if can(mid, wires, k):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
   
    print(ans)

if __name__ == '__main__':
    solve()
def solve():
    n, r = input().split()
    n = int(n)
    r = float(r)

    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    r2 = r * r + 1e-9
    result = []

    for i, (x, y) in enumerate(points):
        count = 0
        for a, b in points:
            dx = x - a
            dy = y - b
            if dx * dx + dy * dy <= r2:
                count += 1
        result.append((-count, i, count))

    result.sort()

    for _, i, count in result[:10]:
        print(i, count)

if __name__ == '__main__':
    solve()
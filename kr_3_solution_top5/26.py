from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    answer = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '+':
                answer += 1
                grid[i][j] = '.'
                queue = deque([(i, j)])

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '+':
                            grid[nx][ny] = '.'
                            queue.append((nx, ny))

    print(answer)

if __name__ == '__main__':
    solve()
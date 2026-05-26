from collections import deque

def solve():
    s = input().strip()
    d = deque()

    for ch in s:
        if not d or ch >= d[0]:
            d.appendleft(ch)
        else:
            d.append(ch)

    print(''.join(d))

if __name__ == '__main__':
    solve()
def solve():
    n, m = map(int, input().split())

    digits = []
    pos = {}
    rem = n % m

    while rem != 0 and rem not in pos:
        pos[rem] = len(digits)
        rem *= 10
        digits.append(str(rem // m))
        rem %= m

    if rem == 0:
        print('0.' + ''.join(digits))
    else:
        i = pos[rem]
        print('0.' + ''.join(digits[:i]) + '(' + ''.join(digits[i:]) + ')')

if __name__ == '__main__':
    solve()
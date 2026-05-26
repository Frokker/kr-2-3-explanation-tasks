def unpack(s):
    stack = ['']
    nums = []
    i = 0

    while i < len(s):
        if s[i].isdigit():
            nums.append(int(s[i]))
            i += 1
        elif s[i] == '[':
            stack.append('')
            i += 1
        elif s[i] == ']':
            part = stack.pop() * nums.pop()
            stack[-1] += part
            i += 1
        else:
            stack[-1] += s[i]
            i += 1

    return stack[0]

def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return a[:i]

def solve():
    n = int(input())
    strings = [input().strip() for _ in range(n)]

    prefix = unpack(strings[0])
    for s in strings[1:]:
        prefix = lcp(prefix, unpack(s))
        if prefix == '':
            break

    print(prefix)

if __name__ == '__main__':
    solve()
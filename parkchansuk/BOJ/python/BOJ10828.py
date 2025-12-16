# BOJ 10828. 스택 / D2
import sys

stk = []


N = int(sys.stdin.readline())
for _ in range(N):
    op = list(map(str, sys.stdin.readline().split()))
    if op[0] == 'push':
        stk.append(int(op[1]))

    elif op[0] == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif op[0] == 'size':
        print(len(stk))

    elif op[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)

    elif op[0] == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)
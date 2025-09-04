import sys
T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    string = list(map(str, sys.stdin.readline().strip()))

    stack = []
    top = -1
    ans = 'YES'

    for x in string:
        if x == '(':
            stack.append(x)
            top += 1
        else: # x == ')'
            if stack:
                stack.pop()
                top -= 1
            else:
                ans = 'NO'
                break
    if stack:
        ans = 'NO'
    print(ans)
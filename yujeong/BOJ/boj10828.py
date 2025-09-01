# 10828. 스택 / D2

# 입력을 여러 번 받는데 input으로만 받으니 시간초과 이슈...!!
import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':        # 명령이 push이면
        stack.append(cmd[1])
    elif cmd[0] == 'top':       # 명령이 top이면
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':      # 명령이 size이면
        print(len(stack))
    elif cmd[0] == 'empty':     # 명령이 empty이면
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'pop':       # 명령이 pop이면
        if stack:
            print(stack.pop())
        else:
            print(-1)
N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]  # push인 경우에만 길이2인 리스트 나머지는 1인 리스트
stack = []
for i in arr:
    if i[0] == 'push':
        stack.append(int(i[1]))
    elif i[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif i[0] == 'size':
        print(len(stack))
    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
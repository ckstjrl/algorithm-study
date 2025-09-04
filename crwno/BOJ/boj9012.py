T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input().split()))
    stack = ['(']
    i = 0
    res = 'NO'
    while stack:
        if arr[0][i] == '(':
            stack.append(arr[0][i])
        elif arr[0][i] == ')':
            stack.pop()
        i += 1
        if i == len(arr[0]):
            if stack == ['(']:
                res = 'YES'
            else:
                res = 'NO'
            break
    print(res)
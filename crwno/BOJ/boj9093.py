T = int(input())
for tc in range(1, T + 1):
    arr = input()
    i = 0
    stack = []
    ans = []
    while i < len(arr):
        if arr[i] == ' ':
            ans.append(' ')
            for j in range(len(stack)):
                ans.append(stack[-j - 1])
            stack = []
        else:
            stack.append(arr[i])
        i += 1
    if stack:
        ans.append(' ')
        for k in range(len(stack)):
            ans.append(stack[-k - 1])
    for i in range(1, len(ans) - 1):
        print(ans[i], end='')
    print(ans[len(ans) - 1])
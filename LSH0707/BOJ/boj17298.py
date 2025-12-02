N = int(input())
arr = list(map(int, input().split()))
ans = [-1] * N
max_v = arr[-1]
stack = []
for i in range(N-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
    # 스택에 현재 수보다 큰 수만 남기고 pop
        stack.pop()
    if stack:
    # 스택이 있다면 stack[-1]->현재 수보다 큰 가장 왼쪽 수
        ans[i] = stack[-1]
    stack.append(arr[i])  # 현재 수 스택에 append

print(*ans)

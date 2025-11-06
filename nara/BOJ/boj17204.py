import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
count = 0
def func():
    global count
    visit = [False] * N
    stack = [arr[0]]

    while stack:
        a = stack.pop()
        count += 1
        if a == K:
            return count
        if not visit[a]:
            visit[a] = True
            stack.append(arr[a])
        else:
            return -1

print(func())
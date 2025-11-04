# BOJ1863. 스카이라인 쉬운거

N = int(input()) # 빌딩 고도가 바뀌는 지점

skyline = []

for _ in range(N):
    idx, height = map(int, input().split())
    skyline.append(height)

skyline.append(0)

stack = []
cnt = 0

for s in skyline:
    while stack and stack[-1] > s:
        if stack[-1] == s:
            break
        stack.pop()
        cnt += 1
    if not stack or stack[-1] != s:
        stack.append(s)

print(cnt)

from collections import deque

N, M = map(int, input().split())

josephus = []

q = deque()
for i in range(1, N+1):
    q.append(i)

while q:
    for _ in range(M-1):
        q.append(q.popleft())
    josephus.append(str(q.popleft()))

ans = ', '.join(josephus)

print(f'<{ans}>')


    









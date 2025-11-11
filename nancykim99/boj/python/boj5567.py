'''
BOJ5567 : 결혼식 (S2)

해결 방법 : 일단 인접리스트 구해서, 그래프 형태로 만들고, bfs를 상근이를 기준으로 실행.
상근이가 1이기에, 3까지는 초대할 친구이기에 친구들 중에 3까지의 친구들의 수를 구하기.
'''

from collections import deque

n = int(input())
m = int(input())

lst = [[] for _ in range((n+1))]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

visited = [0] * (n+1)

def bfs(r):
    queue = deque()
    queue.append(r)
    visited[r] = 1
    while queue:
        t = queue.popleft()
        # visited[t] = 1
        for friend in lst[t]:
            if not visited[friend]:
                visited[friend] = visited[t] + 1
                queue.append(friend)             

bfs(1)

cnt = 0
for i in range(2, n+1):
    if 1 < visited[i] <= 3:
        cnt += 1

print(cnt)
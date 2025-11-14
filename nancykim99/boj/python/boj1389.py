'''
BOJ1389 : 케빈 베이컨의 6단계 법칙 (S1)

해결 방법 :
1. 친구들을 쌍방으로 인접리스트에 넣기
2. bfs로 각 친구들까지의 거리를 구하기
3. 각 bfs의 최소합을 구해 최소거리합을 구해, 친구 사이가 젤 적은 친구 찾기
'''

from collections import deque

def bfs(num):
    q = deque()
    q.append(num)
    while q:
        t = q.popleft()
        for friend in friends[t]:
            if not visited[friend]:
                q.append(friend)
                visited[friend] = visited[t] + 1
    return sum(visited)

n, m = map(int, input().split())

friends = [[] for _ in range((n+1))]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

temp = []
x = 21e8
for i in range(1, (n+1)):
    visited = [0] * (n+1)
    y = bfs(i)
    if y < x:
        x = y
        temp.clear()
        temp.append(i)
    elif y == x:
        temp.append(i)

if not temp:
    print(x)
else:
    print(min(temp))
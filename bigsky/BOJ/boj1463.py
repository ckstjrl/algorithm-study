# BOJ1463: 1로 만들기
from collections import deque

N = int(input())
q = deque([(N, 0)])
visited = set([N])

while q:
    num, cnt = q.popleft()
    
    if num == 1:
        print(cnt)
        break

    if num % 3 == 0 and num // 3 not in visited:
        q.append((num // 3, cnt + 1))
        visited.add(num // 3)
    
    if num % 2 == 0 and num // 2 not in visited:
        q.append((num // 2, cnt + 1))
        visited.add(num //2)
    
    if num - 1 not in visited:
        q.append((num - 1, cnt + 1))
        visited.add(num - 1)
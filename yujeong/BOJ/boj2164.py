# 2164. 카드2

from collections import deque

N = int(input())

q = deque(range(1, N+1))

while len(q)>1:             # 카드가 마지막으로 한장만 남기 전까지 
    q.popleft()             # 제일 위 카드는 버리고
    q.append(q.popleft())   # 그다음으로 위에 있는 카드는 제일 아래로 옮기고 

print(*q)
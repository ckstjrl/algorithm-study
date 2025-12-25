from collections import deque
N = int(input())
q = deque(x for x in range(1,N+1))  # 1부터 N 이 담긴 deque 선언
ans = []
while len(q) >= 2:  # 카드가 2장 이상일 때만
    cur = q.popleft()
    ans.append(cur)     # 맨 앞장은 버리고
    nx = q.popleft()    # 다음장은 밑에 넣기
    q.append(nx)
if ans:
    print(*ans, end= ' ')   # ans 출력
    print(q.popleft())  # 큐에 남은 값 출력
else:
    print(N)
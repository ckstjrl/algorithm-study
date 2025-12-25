"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

"""

import sys
from collections import deque

def bfs(x):
    visited = [0] * (10**6+1)   # 최대 정수 값 + 1 을 배열 크기로 할당
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        cur = q.popleft()
        if cur == 1:    # 1까지 나누면 stop!
            return visited
        for i in range(3):  # % 2, % 3, - 1 총 3가지 연산을 위해 flag로 사용
            if i == 0:
                if cur % 3 == 0:    # 3으로 나누어 떨어지면
                    nx = cur// 3    # 3으로 나누고
                    if visited[nx] == 0:    # 방문한 적 없으면 최신화
                        q.append(nx)
                        visited[nx] = visited[cur] + 1
            elif i == 1:
                if cur % 2 == 0:    # 2로 나누어 떨어지면
                    nx = cur // 2   # 2로 나누고
                    if visited[nx] == 0:    # 방문한 적 없으면 최신화
                        q.append(nx)
                        visited[nx] = visited[cur] + 1

            else:
                nx = cur - 1    # 1을 빼주기
                if visited[nx] == 0:    # 방문한 적 없으면 최신화
                    q.append(nx)
                    visited[nx] = visited[cur] + 1
                    
input = sys.stdin.readline

x = int(input())
visited = bfs(x)
print(visited[1]-1) # 1을 이미 주고 시작해서 빼고 출력
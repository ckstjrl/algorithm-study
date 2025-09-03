"""
BOJ1463. 1로 만들기

[문제]
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

* X가 3으로 나누어 떨어지면, 3으로 나눈다.
* X가 2로 나누어 떨어지면, 2로 나눈다.
* 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

[입력]
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.

[출력]
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""

from collections import deque

def make_one_by_bfs(N):

    # 방문 여부 및 연산 횟수를 기록할 리스트
    # visited[x] = N에서 x까지 도달하는 데 걸린 연산 횟수, -1(default) : 도달하지 못함
    visited = [-1] * (N + 1)

    # BFS를 위한 큐 생성
    q = deque()

    # 시작 노드(N)에서 출발 → 시작점의 연산 횟수를 0으로 설정
    visited[N] = 0
    q.append(N)

    # BFS 시작
    while q:
        x = q.popleft()  # 현재 숫자 꺼내기

        # 목표 숫자(1)에 도착하면, 연산 횟수를 반환
        if x == 1:
            return visited[x]

        # 가능한 연산을 조건에 따라 큐에 추가
        else:
            # x가 6으로 나누어 떨어질 때 → 3으로 나누기, 2로 나누기, 1 빼기 모두 가능
            if x % 6 == 0:
                for nx in (x // 3, x // 2, x - 1):
                    if visited[nx] == -1:  # 아직 방문하지 않은 경우만 처리
                        visited[nx] = visited[x] + 1  # 연산 횟수 +1
                        q.append(nx)

            # x가 3으로만 나누어 떨어지는 경우 → 3으로 나누기, 1 빼기
            elif x % 3 == 0:
                for nx in (x // 3, x - 1):
                    if visited[nx] == -1:
                        visited[nx] = visited[x] + 1
                        q.append(nx)

            # x가 2로만 나누어 떨어지는 경우 → 2로 나누기, 1 빼기
            elif x % 2 == 0:
                for nx in (x // 2, x - 1):
                    if visited[nx] == -1:
                        visited[nx] = visited[x] + 1
                        q.append(nx)

            # 그 외의 경우 → 1 빼기만 가능
            else:
                nx = x - 1
                if visited[nx] == -1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)

# main
N = int(input())
print(make_one_by_bfs(N))
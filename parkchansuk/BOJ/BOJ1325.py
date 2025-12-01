# BOJ 1325. 효율적인 해킹 / D2
'''
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다.
김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다.
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다.
컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

hack = [0]*(N+1)
for i in range(1, N+1):
    q = deque()
    q.append(i)
    visited = [0]*(N+1)
    visited[i] = 1
    cnt = 0
    while q:
        f = q.popleft()
        cnt += 1
        for nxt in trust[f]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = 1
    hack[i] = cnt

best = []
best_v = max(hack)
for b in range(1, N+1):
    if hack[b] == best_v:
        best.append(b)

print(*best)

'''
A가 B를 신뢰한다 -> B를 해킹하면 A도 해킹할 수 있다.
이 의미로 받아들이고
그래프를 만들 때 B index에 B를 신뢰하는 컴퓨터 번호를 집어 넣음

BFS 활용
모든 컴퓨터에서 시작하는 경우를 다 확인해야 함.
i번째 해킹시 trust[i]에 있는 컴퓨터중 해킹 시도한 적 없는 컴퓨터를 q에 넣고 while문 반복
각 index에서 시작하여 해킹한 컴퓨터의 수를 hack리스트에 저장

이후 hack의 최댓값을 찾아서
그 값과 동일한 값을 가진 index를 다시 best에 넣어 출력
'''
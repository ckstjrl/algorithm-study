# BOJ 13565. 침투 / D2
'''
문제
인제대학교 생화학연구실에 재직중인 석교수는 전류가 침투(percolate) 할 수 있는 섬유 물질을 개발하고 있다.
이 섬유 물질은 2차원 M × N 격자로 표현될 수 있다.
편의상 2차원 격자의 위쪽을 바깥쪽(outer side), 아래쪽을 안쪽(inner side)라고 생각하기로 한다.
또한 각 격자는 검은색 아니면 흰색인데, 검은색은 전류를 차단하는 물질임을 뜻하고 흰색은 전류가 통할 수 있는 물질임을 뜻한다.
전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급되고, 이후에는 상하좌우로 인접한 흰색 격자들로 전달될 수 있다.
김 교수가 개발한 섬유 물질을 나타내는 정보가 2차원 격자 형태로 주어질 때,
바깥쪽에서 흘려 준 전류가 안쪽까지 침투될 수 있는지 아닌지를 판단하는 프로그램을 작성하시오.

입력
첫째 줄에는 격자의 크기를 나타내는  M (2 ≤ M ≤ 1,000) 과 N (2 ≤ N ≤ 1,000) 이 주어진다.
M줄에 걸쳐서, N개의 0 또는 1 이 공백 없이 주어진다.
0은 전류가 잘 통하는 흰색, 1은 전류가 통하지 않는 검은색 격자임을 뜻한다.

출력
바깥에서 흘려준 전류가 안쪽까지 잘 전달되면 YES를 출력한다.
그렇지 않으면 NO를 출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
ans = 'NO'

for j in range(M):
    if arr[0][j] == 0 and visited[0][j] == 0:
        q = deque([(0, j)])
        visited[0][j] = 1

        while q:
            ti, tj = q.popleft()

            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ni, nj = ti + di, tj +dj
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1

for k in range(M):
    if visited[N-1][k] == 1:
        ans = 'YES'
        break

print(ans)

'''
BFS로 진행
시작점은 0번째 행에서 '0'인 좌표에서 시작
visited에 방문할 수 있는 모든 경우 저장
이후 visited 마지막 행에 1이 있으면 YES 없으면 NO로 판단하여 출력
'''
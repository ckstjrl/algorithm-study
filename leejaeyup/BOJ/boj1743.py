'''
문제
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 

이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 

통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 

선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

입력
첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.

좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.

출력
첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.
'''


from collections import deque

N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

visited = [[False] * M for _ in range(N)]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]


def bfs(sr, sc):    # (sr, sc)에서 시작해서 연결된 음식물(1)의 크기를 리턴
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    size = 1

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:     # 범위 안 + 아직 방문 X + 음식물(1)인 칸만 확장하자.
                if not visited[nr][nc] and board[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    size += 1
    return size


max_size = 0

for i in range(N):      # 모든 칸을 보면서 새 덩어리 발견하면 BFS.
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            cur = bfs(i, j)
            if cur > max_size:
                max_size = cur

print(max_size)
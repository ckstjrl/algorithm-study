from collections import deque

def bfs(N, M):
    # visited에 방문 여부 및 현재 칸까지의 최소 이동 칸 수를 저장
    visited = [[0] * M for _ in range(N)]

    # BFS를 위한 큐 생성
    q = deque()
    q.append([0, 0])  # 시작점 (0,0) 좌표 삽입
    visited[0][0] = 1  # 시작 칸도 포함하므로 1로 설정

    while q:
        ti, tj = q.popleft()  # 현재 위치 좌표 꺼내기

        # 도착점 (N-1, M-1)에 도착한 경우 최소 칸 수 반환
        if (ti, tj) == (N - 1, M - 1):
            return visited[ti][tj]

        # 상하좌우로 이동하기 위한 방향 벡터
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj  # 다음 위치 좌표

            # 다음 좌표가 유효한 범위 내에 있고, 이동 가능한 칸(1)이며, 아직 방문하지 않은 경우
            if 0<=wi<N and 0<=wj<M and maze[wi][wj] != 0 and visited[wi][wj] == 0:
                q.append([wi, wj])  # 큐에 다음 위치 추가
                # 현재 위치까지의 이동 칸 수 + 1을 저장
                visited[wi][wj] = visited[ti][tj] + 1

    # 도착할 수 없는 경우(문제 조건상 발생하지 않음)
    return 0

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# BFS 실행 및 결과 출력
print(bfs(N, M))
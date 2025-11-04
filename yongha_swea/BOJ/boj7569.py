#boj7569 토마토

from collections import deque


def bfs(H, M, N):
    # 큐 생성
    q = deque()

    # 최소일수 확인을 위한 count, 다 익는거 불가능한 경우 -1 출력
    count = -1

    # 잘 익은 토마토 모두 찾아서 모두 queue에 추가 (enqueue)
    for k in range(H):
        for i in range(N):
            for j in range(M):
                # if 익은 토마토라면
                if arr[k][i][j] == 1:
                    q.append((k, i, j))  # 토마토의 좌표를 queue에 삽입한다, 위아래도 추가됐기 때문에 3단 for문

    tomato_count = len(q)

    # queue 가 비울 때까지 돈다 - 익은 토마토가 더 이상 없을 때까지를 뜻한다.

    while q:
        z, i, j = q.popleft()  # 익은 토마토의 경로를 가져온다.
        tomato_count -= 1

        for dz, di, dj in [[1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0]]:  # 우하좌상 체크 (추가로 z축 상하도 체크)
            nz, ni, nj = z + dz, i + di, j + dj  # 중심 기준 우하좌상 좌표 값

            if 0 <= nz < H and 0 <= ni < N and 0 <= nj < M:
                if arr[nz][ni][nj] == 0:
                # 덜 익은 토마토가 있다면, 큐에 삽입
                # 해당 토마토는 큐에 넣으면서 익은 토마토로 표시해둔다. 그래야 또 체크를 안한다 (visited).
                    q.append((nz, ni, nj))
                    arr[nz][ni][nj] = 1

        # 하루치 토마토를 다 했으면 다음날
        if tomato_count == 0:
            count += 1

            # 새로 체크할 토마토의 갯수를 가져온다
            tomato_count = len(q)

    for h in range(H):
        for n in range(N):
            for m in range(M):
                #0이 하나라도 남아있으면 -1 리턴
                if arr[h][n][m] == 0:
                    return -1

    else:
        return count


# 입력
M, N, H = map(int, input().split())

# 배열 생성
arr = [[list(map(int, input().split())) for _ in range(N)]for _ in range(H)]

ans = bfs(H, M, N)

# 결과 출력
print(ans)
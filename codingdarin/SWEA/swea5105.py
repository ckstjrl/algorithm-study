# 5105. [기본] 6일차 - 미로의 거리 (제출용) (D3)
# 미로: 0은 통로, 1은 벽, 2는 출발, 3은 도착
# 답: 미로 경로 길이 -2 , 없으면 0

from collections import deque

def bfs(arr, n):
    distance = [[0] * n for _ in range(n)]
    q = deque()

    #우하좌상 델타
    di, dj = [0,1,0,-1], [1,0,-1,0]

    # 출발지 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                q.append((i,j))
                distance[i][j] = 1
                break

    while q:
        x, y = q.popleft()

        if arr[x][y] == '3':
            return distance[x][y] -2

        for a,b in zip(di, dj):
            nx, ny = x+a, y+b
            if 0 <= nx < n and 0 <= ny < n:  #인덱스 범위 체크
                if arr[nx][ny] != '1' and distance[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return 0    #도달 불가능

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_arr = [list(input()) for i in range(N)]

    ans = bfs(my_arr, N) # 스타트-엔드 사이 길이 출력
    print(f"#{tc} {ans}")
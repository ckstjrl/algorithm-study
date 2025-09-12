#boj1012: 유기농 배추

from collections import deque

T = int(input())

for tc in range(1, T+1):
    #가로, 세로, 배추 개수
    M, N, K = map(int, input().split())

    #배추 표기하기:
    plant = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        plant[y][x] = 1

    #visited 배열:
    visited = [[0] * M for _ in range(N)]

    count = 0

    #우하좌상 이동 배열:
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    #이동
    for y in range(N):  #8
        for x in range(M): #10

            #방문한 적이 없고 배추가 있다면 queue에 넣고 카운트 1 증가
            if plant[y][x] == 1 and visited[y][x] == 0:
                q = deque()
                q.append((y, x))
                visited[y][x] = 1
                count += 1

                #queue가 비지 않는 동안 넣어둔 배추의 위치 뽑아내기
                while q:
                    cur_y, cur_x = q.popleft()

                    #뽑아낸 배추 위치를 기반으로 우하좌상을 돌면서 또다른 배추가 보이면 queue로 납치
                    for i in range(4):
                        ny, nx = cur_y + dy[i], cur_x + dx[i]

                        #out of index가 되지 않는 한에서라는 제약 걸기
                        if 0 <= ny < N and 0 <= nx < M:
                            if plant[ny][nx] == 1 and visited[ny][nx] == 0:
                                #방문 표시
                                visited[ny][nx] = 1
                                q.append((ny, nx))


    print(f'{count}')
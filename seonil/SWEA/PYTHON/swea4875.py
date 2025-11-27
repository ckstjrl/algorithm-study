T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    maze = [list(input()) for _ in range(N)]

    # 미로의 시작점, 도착 지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (i,j)
            elif maze[i][j] == '3':
                goal = (i,j)

    # 스택에는 '내가 앞으로 갈 곳의 좌표'를 넣을 것이다.(거기로 순간이동함)
    # visited에는 '내가 이미 간 곳의 좌표'를 넣을 것이다.
    # 스택에서 하나하나 좌표들을 꺼내면서, 안 갔으면 visited에 적는다. 다음으로 그 좌표 상하좌우 중 빈 공간의 좌표들을 모두 스택에 넣는다. 
    # 위처럼 하면 시작점과 붙어있는 모든 길을 순회 가능하다. 따라서 이 중에서 도착지점 찾으면 탐색 종료하고 결과를 반환한다.


    # 처음 스택에 시작점 좌표를 push
    stack = [start]

    # visited는 빈 set로 설정하여 중복을 피함
    visited = set()

    # pathExists : start - goal 지점을 잇는 경로가 존재하면 True, 아니면 False를 반환
    pathExists = False

    # 스택이 비어 있을 때까지 반복
    while stack:

        # 스택에서 좌표를 pop하고 그곳으로 x, y좌표를 이동
        x, y = stack.pop()

        # 만약 좌표가 도착점이라면, pathExists = True이고 탐색 종료
        if (x,y) == goal:
            pathExists = True
            break

        # 만약 좌표가 이미 간 곳(visited)이었다면, 이번 pop에는 아무것도 하지 않음
        if (x, y) in visited:
            continue

        # 뽑은 좌표를 visited에 기록
        visited.add((x,y))

        # 뽑은 좌표로부터 우하좌상 4방향을 탐색하고, 벽이 아닌 모든 칸의 좌표를 스택에 push
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0<=nx<N and 0<=ny<N and maze[nx][ny] != '1':
                stack.append((nx, ny))

    # 결과 반환
    print(f'#{test_case} {1 if pathExists else 0}')
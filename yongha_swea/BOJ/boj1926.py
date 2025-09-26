from collections import deque

# n: 행, m: 열
n, m = map(int, input().split())

# 배열
arr = [list(map(int, input().split())) for _ in range(n)]

#방문 여부 확인용
visited = [[0] * m for _ in range(n)]

max_area = 0

area = 0

count = 0

# delta
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for y in range(n):
    for x in range(m):
        if arr[y][x] == 1 and visited[y][x] == 0:
            q = deque()
            q.append((y, x))
            visited[y][x] = 1
            count += 1

            #이 부분을 먼저 생각하지 못했는데 queue에 들어오는 순간 우선 넓이 1을 가지고 시작해야 맞다
            area = 1

            #하나의 그림에서 이어져있는 동안만 돌아가는 while loop (넓이 반영)
            while q:
                cur_y, cur_x = q.popleft()

                for i in range(4):
                    ny, nx = cur_y + dy[i], cur_x + dx[i]

                    #out of index 막기 위한 제약
                    if 0 <= ny < n and 0 <= nx < m:
                        if arr[ny][nx] == 1 and visited[ny][nx] == 0:                            
                            visited[ny][nx] = 1
                            q.append((ny, nx))
                            area += 1
            
            if area >= max_area:
                max_area = area

print(f'{count}')
print(f'{max_area}')
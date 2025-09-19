# BOJ 1987 . 알파벳 (D3 /G4)

#------------------------3회차: 백준 정답코드 참고
import sys

input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
graph = [input() for _ in range(r)]

#델타 배열
dx = [0,1,0,-1]
dy = [1,0,-1,0] 

for _ in range(r):
    graph.append(list(sys.stdin.readline().strip()))

def dfs(sx,sy):
    q = set()
    q.add((sx,sy,graph[sx][sy]))
    squares = 0

    while q:
        x, y, now_visited = q.pop()

        squares = max(squares, len(now_visited))
        if squares == 26:
            return 26
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < r) and (0 <= ny < c) and graph[nx][ny] not in now_visited:
                q.add((nx, ny, now_visited + graph[nx][ny]))
    return squares
print(dfs(0,0))



# #------------------------2회차 풀이: pypy만 통과

# input = lambda: sys.stdin.readline().rstrip()

# R, C = map(int, input().split())
# arr = [input() for _ in range(R)]

# #델타 배열
# di = [0,1,0,-1]
# dj = [1,0,-1,0] 

# max_length = 0
# visited = [False] * 26  # A~Z용

# def dfs(i, j, visited_bits, length):
#     global max_length
    
#     bit = 1 << (ord(arr[i][j]) - ord('A'))  # 비트 위치
#     if visited_bits & bit:  # 이미 방문했나?
#         return
    
#     visited_bits |= bit  # 방문 표시
#     max_length = max(max_length, length)
    
#     for k in range(4):
#         ni, nj = i + di[k], j + dj[k]
#         if 0 <= ni < R and 0 <= nj < C:
#             dfs(ni, nj, visited_bits, length + 1)
    
#     # 백트래킹 (visited_bits는 값 복사라 자동으로 복구됨)

# dfs(0, 0, 0, 1)

# print(max_length)



# #------------------------1회차 풀이: pypy만 통과
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# R, C = map(int, input().split())
# arr = [input() for _ in range(R)]

# #델타 배열
# di = [0,1,0,-1]
# dj = [1,0,-1,0] 

# max_length = 0

# def dfs(i, j, path):
#     global max_length
#     # 일단 현재 위치 처리
#     cur_c = arr[i][j]
#     if cur_c in path:
#         return
    
#     temp = path
#     path += cur_c
#     max_length = max(max_length, len(path))
    
#     # 재귀 시동
#     for xi, xj in zip(di,dj):
#         ni, nj = i+xi, j+xj
#         if 0 <= ni < R and 0<= nj < C:
#             dfs(ni, nj, path)
    
#     #백트래킹
#     path = temp
        
    
# dfs(0, 0, '') #현재위치, txt
# print(max_length)
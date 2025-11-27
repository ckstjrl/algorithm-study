# BOJ1987(D3): 알파벳
# set를 이용한 bfs: 딱히 더 빠르진 않았다..!
# 메모리: 113832KB, 시간: 6748ms
import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
alphas = [input() for _ in range(R)]

def bfs(x, y):
    max_len = 0
    my_set = set([(x, y, alphas[x][y])])

    while my_set:
        x, y, path = my_set.pop()
        max_len = max(max_len, len(path))
        if max_len == 26:
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            n_alpha = alphas[nx][ny]
            if n_alpha not in path:
                my_set.add((nx, ny, path + n_alpha))
    
    return max_len

print(bfs(0, 0))


# DFS + 유니코드정수를 이용
# 메모리: 164712KB, 시간: 5220ms
# import sys
# input = lambda: sys.stdin.readline().rstrip()

# def dfs(x, y):
#     global ans
#     s_ascii = ord(alphas[x][y]) - 65
#     ans = max(ans, visited[s_ascii])

#     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             continue
#         n_ascii = ord(alphas[nx][ny]) - 65
#         if visited[n_ascii]:
#             continue
#         visited[n_ascii] = visited[s_ascii] + 1
#         dfs(nx, ny)
#         visited[n_ascii] = 0


# R, C = map(int, input().split())
# alphas = [input() for _ in range(R)]
# visited = [0] * 26
# s_ascii = ord(alphas[0][0]) - 65
# visited[s_ascii] = 1
# ans = 0

# dfs(0, 0)

# print(ans)


# BFS로 풀었지만 시간초과&메모리초과로 터짐...
# import sys
# from collections import deque

# input = lambda: sys.stdin.readline().rstrip()

# R, C = map(int, input().split())
# alphas = [input() for _ in range(R)]

# q = deque([(0, 0, set(alphas[0][0]))])
# ans = 1  # set의 최대 길이

# while q:
#     x, y, my_set = q.popleft()
#     ans = max(ans, len(my_set))
#     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#         nx, ny = x + dx, y + dy
#         if nx < 0 or nx >= R or ny < 0 or ny >= C:
#             continue
#         alpha = alphas[nx][ny]
#         if alpha in my_set:
#             continue
#         n_set = my_set.union({alpha})
#         q.append((nx, ny, n_set))

# print(ans)

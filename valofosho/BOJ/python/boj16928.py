from collections import deque

def check(i):
    if 0<= i <101:
        return True
    else:
        return False

def bfs():
    q = deque()
    q.append(1)    
    # visited 최대 배열 생성
    visited = [10000] * 101
    visited[1] = 0
    while q:
        cur = q.popleft()
        for i in range(1,7):
            nx = cur + i
            # 100 초과면 continue
            if nx > 100:
                continue
            if check(nx):
                step = visited[cur] + 1
                # 연쇄 사다리/뱀 처리
                
                if ladder[nx]:
                    nx = ladder[nx]
                elif snake[nx]:
                    nx = snake[nx]
                if step < visited[nx]:
                    visited[nx] = step
                    q.append(nx)
                        
    return visited[100]

N, M = map(int, input().split())
ladder = [0] * 101
snake = [0] * 101
for _ in range(N):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(M):
    a, b = map(int, input().split())
    snake[a] = b
a = bfs()
print(a)
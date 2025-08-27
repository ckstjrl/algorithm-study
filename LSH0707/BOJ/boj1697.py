from collections import deque

N, K = map(int, input().split())

def find(N, K):
    q = deque()
    q.append((N, 0))  # 큐에 초기위치, 시간 추가
    visited = set()   # 지나간 위치 세트
    visited.add(N)

    while q:
        p, sec = q.popleft()  # 큐에서 현재위치, 현재시간 가져오고 pop
        if p == K:
            return sec  # 동생위치랑 현재위치랑 같으면 현재시간 반환
        for di, dj in [[1, -1], [1, 1], [2, 0]]: 
            a = di * p + dj  # 현재위치에서 -1 +1 *2한 위치
            if 0 <= a <= 100000 and a not in visited:
                visited.add(a)  
                q.append((a, sec + 1))  # 큐랑 visited에 각각 추가

print(find(N, K))

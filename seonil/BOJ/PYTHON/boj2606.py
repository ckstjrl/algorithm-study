def count_infected_by_dfs(adj_lst):
    # 방문 여부를 기록할 리스트 (0: 미방문, 1: 방문)
    visited = [0] * (N + 1)

    # 시작 컴퓨터 (1번)
    start = 1

    stack = [start]   # DFS를 위한 스택
    cnt = 0           # 감염된 컴퓨터 수 카운트

    # DFS 탐색 시작
    while stack:
        v = stack.pop()  # 스택에서 하나 꺼내기

        # 이미 방문한 컴퓨터라면 건너뛰기
        if visited[v] == 1:
            continue

        # 현재 컴퓨터 방문 처리
        visited[v] = 1
        cnt += 1  # 감염된 컴퓨터 수 증가

        # 현재 컴퓨터와 연결된 컴퓨터들을 확인
        for w in adj_lst[v]:
            # 아직 방문하지 않은 컴퓨터라면 스택에 추가
            if visited[w] == 0:
                stack.append(w)

    # 시작점(1번 컴퓨터) 자신은 빼고 감염된 컴퓨터 수 반환
    return cnt - 1


# 컴퓨터의 수 입력 (정점 개수)
N = int(input())

# 네트워크 연결 쌍의 수 입력 (간선 개수)
E = int(input())

# 인접 리스트 초기화
adj_lst = [[] for _ in range(N + 1)]

# 네트워크 연결 정보 입력
for i in range(E):
    a, b = map(int, input().split())
    # 무방향 간선 그래프이므로, 인접 리스트에 양방향으로 추가
    adj_lst[a].append(b)  
    adj_lst[b].append(a)

# DFS를 통해 감염된 컴퓨터 수 계산
ans = count_infected_by_dfs(adj_lst)

# 결과 출력
print(ans)
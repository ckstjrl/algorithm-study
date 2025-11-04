'''
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''


from collections import deque

T = int(input().strip())

moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

for _ in range(T):
    l = int(input())  # 보드 한 변의 길이.
    sr, sc = map(int, input())  # 시작 위치.
    tr, tc = map(int, input())  # 목표 위치.

    if sr == tr and sc == tc:       # 시작 == 목표면 0.
        print(0)
        continue

    visited = [[-1] * l for _ in range(l)]      # 방문 배열: -1이면 아직 방문 안 함, 0 이상이면 해당 칸까지의 이동 횟수.
    visited[sr][sc] = 0

    q = deque()
    q.append((sr, sc))

    ans = -1  # 정답. 초기값을 -1으로 설정해둠.

    while q:
        r, c = q.popleft()

        for dr, dc in moves:
            nr, nc = r + dr, c + dc     # 보드 범위 안이고, 아직 방문 안 했다면,
            if 0 <= nr < l and 0 <= nc < l and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1     # 목표에 도착하면 바로 정답 출력.
                if nr == tr and nc == tc:
                    ans = visited[nr][nc]
                    q.clear()  # 큐 비우고 바깥 while 종료.
                    break
                q.append((nr, nc))

    if ans == -1:   # 만약 ans가 -1이면 visited에서 꺼내자.
        ans = visited[tr][tc]


    print(ans)
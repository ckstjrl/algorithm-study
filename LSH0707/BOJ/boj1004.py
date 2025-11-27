import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    arr = [[] for _ in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        arr[i] = [a, b, c]
    cnt = 0
    for i in range(n):
        c_1 = (arr[i][0] - x1) ** 2 + (arr[i][1] - y1) ** 2  # 출발점과 행성간의 거리 제곱
        c_2 = (arr[i][0] - x2) ** 2 + (arr[i][1] - y2) ** 2  # 도착점과 행성간의 거리 제곱
        if c_1 <= arr[i][2] ** 2 and c_2 <= arr[i][2] ** 2:  # 출발 도착 모두 행성계 안에 위치하면 진입/이탈 안함
            continue
        elif c_1 <= arr[i][2] ** 2:  # 출발점만 행성계 안이면 진입/탈출 필요 cnt+1
            cnt = cnt + 1
        elif c_2 <= arr[i][2] ** 2:  # 도착점만 행성계 안이면 진입/탈출 필요 cnt+1
            cnt = cnt + 1
    print(cnt)
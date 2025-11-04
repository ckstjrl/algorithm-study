import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort()  # 1차 점수 기준 오름차순 정렬
    ans = 1  # 1차 1등 합격
    score = arr[0][1]  # 합격자 2차점수 기록
    for i in range(1, N):  # 1차 2등부터 순회
        if arr[i][1] < score:  # 2차 등수가 기록된 등수보다 작으면 합격자+1, 2차 등수 기록
            ans = ans + 1
            score = arr[i][1]
    print(ans)
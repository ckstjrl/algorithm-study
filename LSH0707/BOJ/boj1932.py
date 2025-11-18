import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int, input().split()))
max_v = [[] for _ in range(N)]

for i in range(N):  # 같은 모양 빈 배열
    max_v[i] = [0] * (i+1)
    if i == 0:  # 맨 위층 값 기록
        max_v[i][0] = arr[0][0]
    else:
        for j in range(i+1):  # dp (해당 칸에서의 최댓값 기록)
            if j == 0:
                max_v[i][j] = max_v[i-1][j] + arr[i][j]
            elif j == i:
                max_v[i][j] = max_v[i-1][j-1] + arr[i][j]
            else:
                max_v[i][j] = max(max_v[i-1][j-1], max_v[i-1][j]) + arr[i][j]
                
print(max(max_v[N-1]))  # 맨 아랫줄 최댓값 출력력
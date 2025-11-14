# 1080. 행렬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 행렬 크기 N*M
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]

# A의 3*3 부분 행렬 모든 원소를 뒤집기
def reverse(x, y):
    for cx in range(x, x+3):
        for cy in range(y, y+3):
            A[cx][cy] ^= 1

# 예외 1: 처음부터 같으면 뒤집기 횟수 0 출력
if A == B:
    print(0)
# 예외 2: 3*3 부분 행렬 만들 수 없는 경우 -1 출력
elif N < 3:
    print(-1)
# 그 외: 좌상->우하 뒤집기 필요한 경우 뒤집으며 B 만들어지는 경우 cnt, 아니면 -1 출력
else:
    cnt = 0     # 뒤집는 횟수
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:  # A와 B 원소가 다름; 뒤집기 필요
                reverse(i, j)
                cnt += 1
    print(cnt if A==B else -1)
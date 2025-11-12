import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

def reverse(si, sj):  # (si, sj)를 좌상단으로 두고 3X3만큼 뒤집기
    for i in range(3):
        for j in range(3):
            if A[si+i][sj+j] == 0:
                A[si + i][sj + j] = 1
            else:
                A[si + i][sj + j] = 0

cnt = 0
for i in range(N-2):  # 뒤집을 수 있는 모든 시작좌표 순회
    for j in range(M-2):
        if A[i][j] != B[i][j]:  # 행렬 A와 행렬 B의 좌상단 좌표가 다른 경우 뒤집기 -> cnt+1
            reverse(i, j)
            cnt = cnt + 1
if A == B:  # 가능한 모든 좌표에 대해 뒤집고 두 행렬이 같은 경우 횟수 출력
    print(cnt)
else:
    print(-1)
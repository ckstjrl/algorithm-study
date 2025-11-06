import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def paper(i, j, N):  # 좌상단좌표가 (i,j) N*N만큼 검사해서 종이면 1리턴 아니면 0리턴
    start = arr[i][j]
    for p in range(i, i+N):
        for q in range(j, j+N):
            if arr[p][q] != start:
                return 0
    return 1

p_cnt = {-1:0, 0:0, 1:0}

def cnt(i, j, N):  # 좌상단좌표가 (i,j) N*N 크기 검사해서 종이에 적힌 수 기록후 리턴
    if paper(i, j, N) == 1:
        p_cnt[arr[i][j]] = p_cnt[arr[i][j]] + 1
        return
    for p in range(3):
        for q in range(3):  # 재귀 -> N*N 크기 종이 9개로 나눠서 검사, 카운트
            cnt(i+p*(N//3), j+q*(N//3), (N//3))

cnt(0, 0, N)
for i in [-1, 0, 1]:
    print(p_cnt[i])
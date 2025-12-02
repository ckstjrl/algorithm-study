import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mission = [list(map(int, input().split())) for _ in range(2)]

cnt = 0
def func(day, contribute, prev):
    global cnt
    if day == N:
        if contribute >= M:
            cnt += 1
        return
    for i in range(2):
        for j in range(3):
            if j == prev:
                tmp = contribute + mission[i][j] // 2
            else:
                tmp = contribute + mission[i][j]
            func(day+1, tmp, j)

func(0, 0, -1)
print(cnt)
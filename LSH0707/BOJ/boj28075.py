N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]
ans = 0
def spy(point, cnt, place):  # (진척도, 임무 수행 횟수, 전날 수행한 장소)
    global ans
    if cnt == N:  # 임무 횟수 N -> 진척도 M 이상인 경우 ans+1 리턴
        if point >= M:
            ans = ans + 1
        return
    for i in range(2):
        for j in range(3):
            if j == place:  # 전날 수행한 장소와 같은 경우 진척도//2
                spy(point+(arr[i][j]//2), cnt+1, j)
            else:
                spy(point+arr[i][j], cnt+1, j)
spy(0, 0, None)
print(ans)
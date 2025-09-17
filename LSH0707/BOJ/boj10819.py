N = int(input())
arr = list(map(int, input().split()))
max_v = 0
visited = [0] * N
def s(lst, cnt):
    global max_v
    if cnt == N:  # 길이 N 되면
        max_vv = 0
        for i in range(N-1):  # 값
            max_vv = max_vv + abs(lst[i] - lst[i+1])
        if max_vv > max_v:  # 최댓값 기록
            max_v = max_vv
        return
    for i in range(N):  # N개숫자 중복없이 조합
        if visited[i] == 0:  # 방문기록 없는 숫자
            visited[i] = 1  
            s(lst + [arr[i]], cnt+1)
            visited[i] = 0
s([], 0)
print(max_v)
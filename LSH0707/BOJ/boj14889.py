N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
def stat():  # 두 팀의 점수를 구하고 차이의 절대값을 리턴
    start = 0
    link = 0
    for i in range(N):
        for j in range(i+1, N):
            if visited[i] == 1 and visited[j] == 1:
                start = start + arr[i][j] + arr[j][i]
            if visited[i] == 0 and visited[j] == 0:
                link = link + arr[i][j] + arr[j][i]
    return abs(start - link)
min_diff = float('inf')
def team(cnt, idx):
    global min_diff
    if cnt + N - 1 - idx + 1 < N / 2:  # 현재팀원수 + 남은 후보 < 전체인원/2 이면 종료
        return
    if cnt == N / 2:  # 팀원수가 전체인원의 절반으로 나눠진경우
        diff = stat()  # 점수 차이 구하고 최소차이값 기록
        if diff < min_diff:
            min_diff = diff
        return
    for i in range(idx,N):  # vistied=1인 경우 start팀
        if visited[i] == 0:
            visited[i] = 1
            team(cnt+1, i+1) 
            visited[i] = 0
team(0, 0)
print(min_diff)
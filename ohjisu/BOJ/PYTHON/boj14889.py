import sys
input = lambda :sys.stdin.readline().rstrip()


def cal_power(team):  # team_power 구하기
    total_power = 0
    team_size = len(team)
    for i in range(team_size):
        for j in range(i + 1, team_size):  # (i, j) 조합
            p1 = team[i]
            p2 = team[j]
            total_power += S[p1][p2] + S[p2][p1]
    return total_power


def find_min(cnt, start_idx, start_team):
    global min_result
    if cnt == N//2:
        link_team = []
        for i in range(1, N + 1):
            if used[i] == 0:  # used가 0이면 링크 팀
                link_team.append(i)
        now_result = abs(cal_power(start_team) - cal_power(link_team))
        # 최솟값 업데이트
        min_result = min(min_result, now_result)
        return

    for i in range(start_idx, N + 1):
        if used[i]:
            continue
        used[i] = 1
        start_team.append(i)

        find_min(cnt + 1,  i + 1, start_team)

        used[i] = 0
        start_team.pop()

N = int(input())
S = [[0] * N]
for _ in range(N):
    S.append([0] + list(map(int, input().split())))
min_result = float('inf')
used = [0] * (N + 1)
find_min(0, 1, [])
print(min_result)
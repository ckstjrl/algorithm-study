# 14889. 스타트와 링크

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 스타트 팀, 링크 팀으로 나누는 모든 경우 만들기 
def split_teams(N):
    nums = list(range(1, N+1))
    result = []
    for comb in combinations(nums, N//2):
        other = tuple(sorted(set(nums) - set(comb)))
        # 중복 방지를 위해 첫 원소가 1을 포함할 때만 카운트
        if 1 in comb:
            result.append((comb, other))
    return result

teams = split_teams(N)
min_diff = 9999
for team in teams:
    # 링크 팀 능력치 합 구하기 
    team_link = team[0]
    link_score = 0
    link_pairs = combinations(team_link, 2)     # 링크 팀의 두 멤버 모든 조합에 대해
    for t1, t2 in link_pairs:
        link_score += arr[t1-1][t2-1] + arr[t2-1][t1-1]     # 능력치 구해서 score에 더함

    # 스타트 팀 능력치 합 구하기 
    team_start = team[1]
    start_score = 0
    start_pairs = combinations(team_start, 2)   # 스타트 팀의 두 멤버 모든 조합에 대해
    for t1, t2 in start_pairs:
        start_score += arr[t1-1][t2-1] + arr[t2-1][t1-1]    # 능력치 구해서 score에 더함
    
    # 차이의 최솟값 구하기 
    min_diff = min(min_diff, abs(link_score - start_score))

print(min_diff)


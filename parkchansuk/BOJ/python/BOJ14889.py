# BOJ 14889. 스타트와 링크 / D2
'''
문제
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다.
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.
BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

def divide_teams(n):
    # 사람이 1부터 n까지 번호를 가진다고 가정
    people = list(range(n))

    # 모든 경우의 팀 분할을 저장할 리스트
    team_divisions = []

    def ncr(start, team1):
        # 팀1이 n//2명을 채우면, 팀2는 나머지 사람들이 됨
        if len(team1) == n // 2:
            team2 = [person for person in people if person not in team1]
            team_divisions.append((team1, team2))
            return

        # 다음 사람을 팀1에 추가하거나, 더 이상의 조합을 만들지 않기 위해 재귀 호출
        for i in range(start, n):
            ncr(i + 1, team1 + [people[i]])

    # 초기 호출
    ncr([], 0, [])

    return team_divisions

team_list = divide_teams(N)
synergy_cal = []
for team12 in team_list:
    team1 = team12[0]
    team2 = team12[1]
    synergy1 = 0
    synergy2 = 0

    for i in team1:
        for j in team1:
            if i != j:
                synergy1 += arr[i][j]

    for y in team2:
        for x in team2:
            if y != x:
                synergy2 += arr[y][x]

    synergy = abs(synergy1-synergy2)

    synergy_cal.append(synergy)

print(min(synergy_cal))

'''
같은 인원 수를 갖은 두개의 팀을 만듦
팀 1을 N//2 크기 까지 조합으로 뽑고 팀 2는 people 중 팀 1에 없는 사람을 넣어서 완성
팀 조합들을 리스트에 넣어서 계산과정 거침
계산한 값의 차를 synergy_cal 리스트에 넣고 min값을 답으로 출력
'''
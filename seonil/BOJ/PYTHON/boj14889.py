"""
BOJ14889. 스타트와 링크

[문제]
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5	 

예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

[입력]
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

[출력]
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# DFS 기반으로 스타트 팀 구성 후보를 생성하고, 각각의 완성된 팀 후보들로부터 능력치 차이를 계산
def dfs(idx, count):
    global min_diff

    # 가지치기 1: 이미 스타트 팀 인원이 N // 2를 초과한 경우 종료
    if count > N // 2:
        return
    
    # 가지치기 2: 이미 가능한 최솟값이 0이면 더 이상 탐색할 필요 없으므로 종료
    if min_diff == 0:
        return

    # 모든 플레이어에 대해 팀 배정이 끝난 경우
    if idx == N:
        # 스타트 팀의 인원이 정확이 N // 2일 때만 능력치 차이 계산
        if count == N // 2:
            start_sum, link_sum = 0, 0  # 두 팀의 능력치 합을 저장할 변수들을 0으로 초기화
            # 모든 (i, j) 쌍을 순회하면서
            for i in range(N):
                for j in range(N):
                    if selected[i] and selected[j]: # 둘 다 start 팀에 뽑힌 경우,
                        start_sum += S[i][j]        # 스타트 팀의 능력치를 더함
                    elif not selected[i] and not selected[j]:   # 둘 다 start에 안 뽑혀서 link 팀인 경우,
                        link_sum += S[i][j]                     # 링크 팀의 능력치를 더함
            diff = abs(start_sum - link_sum)    # 완성된 팀의 능력치 차이를 계산
            min_diff = min(min_diff, diff)      # 전역 최솟값 갱신
        return

    # 현재 idx 플레이어를 스타트 팀에 넣음
    selected[idx] = True
    dfs(idx + 1, count + 1)

    # 현재 idx 플레이어를 링크 팀에 넣음
    selected[idx] = False
    dfs(idx + 1, count)

# main
N = int(input())    # N : 축구를 하기 위해 모인 플레이어 수
S = [list(map(int, input().split())) for _ in range(N)]     # S : 능력치 시너지 배열

selected = [False] * N
min_diff = int(1e9)

# 대칭 제거: 0번 플레이어는 무조건 스타트 팀에 포함
#(팀을 서로 바꾼 경우는 동일하므로, 0번을 고정하면 탐색 공간이 절반으로 줄음)
selected[0] = True
dfs(1, 1)
print(min_diff)

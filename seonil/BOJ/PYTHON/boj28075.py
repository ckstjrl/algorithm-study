"""
BOJ28075. 스파이

[문제]
스파이 민겸이는 이웃 나라와의 평화를 위해 N일간 임무를 수행한다.
민겸이는 정보 수집과 감시 2가지 임무를 수행한다. 각 임무는 수족관, 시청, 학교에서 수행할 수 있다.
두 임무는 성격이 크게 다르기 때문에 하루에 한 가지 임무만 수행할 수 있으며, 수족관, 시청, 학교는 멀리 떨어져 있기 때문에 하루에 한 가지 장소에서만 임무를 수행할 수 있다.
또한, 민겸이는 반드시 하루에 최소 하나의 임무를 수행해야 한다.

다시 말해, 민겸이는 하루에 위 표의 6가지 행동 중 하나를 선택하여 할 수 있다.
민겸이는 각 장소에서 각 임무를 수행할 때, 임무 완수를 위한 진척도를 얻을 수 있다. 그러나 민겸이는 스파이이기 때문에, 같은 장소에서 오래 근무하면 사람들의 눈에 띄어 얻을 수 있는 진척도가 낮아진다.
민겸이가 전날에 임무를 수행한 곳과 같은 장소를 선택하면 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다.
이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨에 유의하자.
민겸이의 기여도는 얻은 진척도의 합이다. 각 장소에서 각 임무를 수행했을 때 얻을 수 있는 진척도가 주어질 때 민겸이가 M 이상의 기여도를 얻을 수 있는 임무 수행 방법이 몇 가지인지 구하라.

[입력]
첫째 줄에는 민겸이가 임무를 수행하는 총 일수 N과 민겸이가 얻고 싶은 최소 기여도 M이 공백으로 구분되어 주어진다.
둘째 줄에 민겸이가 정보 수집 임무를 수족관, 시청, 학교에서 수행했을 때 얻을 수 있는 진척도가 순서대로 공백으로 구분되어 주어진다.
셋째 줄에 민겸이가 감시 임무를 수족관, 시청, 학교에서 수행했을 때 얻을 수 있는 진척도가 순서대로 공백으로 구분되어 주어진다.

[출력]
민겸이가 기여도를 M 이상 얻을 수 있는 임무 수행 방법이 몇 가지인지 출력한다.

[제한]
* 1 ≤ N ≤ 8
* 1 ≤ M ≤ 25
주어지는 모든 진척도는 0 이상 10 이하의 짝수이다.
주어지는 모든 수는 정수이다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# dfs로 기여도 합이 M을 넘는 경우가 몇 가지인지 계산하는 함수
def dfs(day, last, total):

    # 메모이제이션: 같은 상태(day, last, total)가 오면 다시 계산하지 않도록 하기
    key = (day, last, total)
    if key in memo:
        return memo[key]
    
    # 모든 N일을 다 채운 경우 → total이 M 이상이면 성공 1가지, 아니면 0가지
    if day == N:
        return 1 if total >= M else 0
    
    cnt = 0 # 가능한 모든 경우의 수 합산

    # 모든 임무들을 순회하면서
    for i in range(2):
        for j in range(3):
            gain = tasks[i][j]  # 오늘의 기여도 계산

            # 만약 전날과 장소가 같다면 오늘의 기여도는 절반
            if j == last:
                gain //= 2
            
            # 오늘의 기여도를 누적하고 다음 날로 진행
            cnt += dfs(day + 1, j, total + gain)
    
    # 계산 결과 저장 후 반환
    memo[key] = cnt
    return cnt

# main
N, M = map(int, input().split())    # 임무를 수행하는 총 일수 N, 최소 목표 기여도 M
tasks = [list(map(int, input().split())) for _ in range(2)]     # 기여도 정보 입력 받기
memo = {}   # 메모이제이션 딕셔너리
result = dfs(0, -1, 0)    # 첫날(day=0), 전날 장소 없음(last=-1), 총 기여도 0으로 dfs 수행
print(result)   # 결과 반환

"""
# 새로 배운 것: lru_cache를 이용하면 메모이제이션을 데코레이터를 사용하여 간단하게 구현할 수 있다!!
# 위 코드랑 똑같이 동작함

import sys
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

@lru_cache(None)
def dfs(day, last, total):

    if day == N:
        return 1 if total >= M else 0
    
    cnt = 0
    for i in range(2):
        for j in range(3):
            gain = tasks[i][j]

            if j == last:
                gain //= 2
            
            cnt += dfs(day + 1, j, total + gain)
    
    return cnt

# main
N, M = map(int, input().split())
tasks = [list(map(int, input().split())) for _ in range(2)]
print(dfs(0, -1, 0))
"""
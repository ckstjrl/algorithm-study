# BOJ 26069. 붙임성 좋은 총총이 / D2
'''
총총이는 친구 곰곰이의 소개로 제2회 곰곰컵에 출연할 기회를 얻었다!
총총이는 자신의 묘기인 무지개 댄스를 선보여, 여러분의 환심을 사려 한다.
이 댄스는 중독성이 강하기 때문에, 한번 보게 된 사람은 모두 따라 하게 돼버린다.
사람들이 만난 기록이 시간 순서대로 N개 주어진다. (총총이는 토끼이지만 이 문제에서는 편의상 사람이라고 가정한다.)
무지개 댄스를 추지 않고 있던 사람이 무지개 댄스를 추고 있던 사람을 만나게 된다면, 만난 시점 이후로 무지개 댄스를 추게 된다.
기록이 시작되기 이전 무지개 댄스를 추고 있는 사람은 총총이 뿐이라고 할 때, 마지막 기록 이후 무지개 댄스를 추는 사람이 몇 명인지 구해보자!

입력
첫번째 줄에는 사람들이 만난 기록의 수 N이 주어진다.
두번째 줄부터 N개의 줄에 걸쳐 사람들이 만난 기록이 주어진다.
i + 1번째 줄에는 i번째로 만난 사람들의 이름 A_i와 B_i가 공백을 사이에 두고 주어진다.
A_i와 B_i는 숫자와 영문 대소문자로 이루어진 최대 길이 20의 문자열이며, 서로 같지 않다.
총총이의 이름은 ChongChong으로 주어지며, 기록에서 1회 이상 주어진다.
동명이인은 없으며, 사람의 이름은 대소문자를 구분한다. (ChongChong과 chongchong은 다른 이름이다.)

출력
마지막 기록 이후 무지개 댄스를 추는 사람의 수를 출력하라.
'''
import sys
input = sys.stdin.readline

def find_Chong(meet):
    for i in range(N):
        for j in range(2):
            if meet[i][j] == 'ChongChong':
                return i

N = int(input().strip())
meet = [list(input().split()) for _ in range(N)]
raindow = set()
c_i = find_Chong(meet)
raindow.update(meet[c_i])
for i in range(c_i+1, N):
    for j in range(2):
        if meet[i][j] in raindow:
            raindow.update(meet[i])

answer = len(raindow)
print(answer)

'''
총총이가 있는 좌표를 먼저 찾음
총총이가 있는 행에 있는 사람은 set에 들어감
총총이를 만난 순간 부터 N번째까지 set안에 있는 사람과 만난 사람은 set에 들어감
set에 있는 사람의 수 = 무지개댄스를 추는 사람 수
'''
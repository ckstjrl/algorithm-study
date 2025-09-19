# 1159. 농구 경기
'''
상근이는 내일 경기에 나설 선발 명단을 작성해야 한다.
누가 선발인지 기억하기 쉽게 하기 위해 성의 첫 글자가 같은 선수 5명을 선발하려고 한다.
만약, 성의 첫 글자가 같은 선수가 5명보다 적다면, 상근이는 내일 있을 친선 경기를 기권하려고 한다.
상근이는 내일 경기를 위해 뽑을 수 있는 성의 첫 글자를 모두 구해보려고 한다.

[입력]
첫째 줄에 선수의 수 N
다음 N개 줄에는 각 선수의 성이 주어진다.

[출력]
상근이가 선수 다섯 명을 선발할 수 없는 경우에는 "PREDAJA" (따옴표 없이)를 출력한다.
선발할 수 있는 경우에는 가능한 성의 첫 글자를 사전순으로 공백없이 모두 출력한다.

빈 리스트 2개 만들어서 우선 첫 글자 다 넣기.
리스트1 돌면서 있는 거 숫자 세기.
- 5개 이상이면서 리스트1에 없으면 리스트2에 추가 -> 중복 제거
- 사전 순으로 정렬하자.
'''
n = int(input())
player = []
lst = []
for i in range(n):
    name = input()
    player.append(name[0])

for ch in player:
    cnt = 0
    for j in player:
        if ch == j:
            cnt += 1
    if cnt >= 5 and ch not in lst:
        lst.append(ch)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
if len(lst) == 0:
    print("PREDAJA")
else:
    for c in lst:
        print(c, end="")
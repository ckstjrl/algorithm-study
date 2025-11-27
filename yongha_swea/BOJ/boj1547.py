# M: 컵 위치를 바꾼 횟수
# M 줄에 걸쳐서 컵을 변경한 위치
# 공은 [0]번 자리에 주어지며 그 위치가 변하지 않는다

#초기 컵 세팅
setting = [1, 2, 3]

changed = [0, 0, 0]

M = int(input())

# 공은 항상 첫번째 자리를 고수하고 있기 때문에 마지막에 index, 0에 위치한 컵을 찾으면 된다
for _ in range(M):
    cup1, cup2 = map(int, input().split())

    change1 = setting.index(cup1)

    change2 = setting.index(cup2)

    #위치 변경
    setting[change1], setting[change2] = setting[change2], setting[change1]

#0번 위치에 있는 컵 출력
print(setting[0])
'''
BOJ15686 : 치킨 배달 (S5)

해결 방법 : 
1. 치킨 가게, 집 좌표 구하기
2. 치킨 가게의 조합 구하기
3. 집을 돌면서 치킨 가게까지의 최소 거리 구하기
    3-1. 치킨 가게까지의 거리를 구하는데, 이미 최소 거리를 넘어선 경우, pass
'''

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
bbq = [] # 치킨가게 좌표
bbq_num = 0 # 치킨가게 수
houses = []
chosen_bbq_list = [] # 선택한 치킨가게
min_dist = 21e8

# 치킨 가게 좌표 꺼내기
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            bbq.append((i, j))
            bbq_num += 1
        if city[i][j] == 1:
            houses.append((i, j))

# 치킨 가게에서 m만큼 고르기
def choose_bbq(cnt, chosen):
    if cnt == bbq_num:
        if len(chosen) == m:
            temp = [i for i in chosen]
            chosen_bbq_list.append(temp)
        return
    chosen.append(bbq[cnt])
    choose_bbq(cnt + 1, chosen)
    chosen.pop()
    choose_bbq(cnt + 1, chosen)

choose_bbq(0, [])

# 집을 돌면서 치킨 가게까지의 최소 거리를 구하기
for bbqs in chosen_bbq_list:
    bbq_dist = 0
    for house in houses:
        min_d = 21e8
        for bbq in bbqs:
            d = abs(house[0] - bbq[0]) + abs(house[1] - bbq[1])
            min_d = min(d, min_d)
        bbq_dist += min_d
        if bbq_dist > min_dist:
                break
    if bbq_dist < min_dist:
        min_dist = bbq_dist

print(min_dist)
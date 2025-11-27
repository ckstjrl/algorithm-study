# boj2490 윷놀이

T = 3

for tc in range(T):
    # 윷놀이 윷 받기
    yoot_comb = list(map(int, input().split()))

    ans = ''

    #앞 뒤 지정해서 받기
    front = yoot_comb.count(0)
    back = yoot_comb.count(1)

    if front == 4:
        ans = 'D'
    if front == 3:
        ans = 'C'
    if front == 2:
        ans = 'B'
    if front == 1:
        ans = 'A'
    if front == 0:
        ans = 'E'

    print(ans)
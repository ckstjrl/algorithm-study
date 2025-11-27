# 1970. 쉬운 거스름돈
T = int(input())
for tc in range(1, T+1):
    m = int(input())
    change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    change_cnt = [0]*8

    for i in range(8):
        change_cnt[i] = m // change_list[i]
        m -= change_cnt[i] * change_list[i]

    print(f'#{tc}\n{" ".join(map(str, change_cnt))}')
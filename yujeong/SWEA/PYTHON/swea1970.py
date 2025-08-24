# 1970. 쉬운 거스름돈 / D2

T = int(input())

for tc in range(T):
    N = int(input())    # 손님에게 거슬러줘야 할 돈 N원
    # 돈의 종류: 50000원, 10000원, 5000원, 1000원, 500원, 100원, 50원, 10원
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * 8

    for i in range(8):
        cnt[i] += N // money[i]
        N -= cnt[i] * money[i]
    
    print(f'#{tc+1}')
    print(*cnt)

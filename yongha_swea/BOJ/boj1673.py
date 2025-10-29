# BOJ1673 치킨 쿠폰

# n: 치킨 한 마리 주문 가능 쿠폰, k: 보너스 쿠폰을 위한 도장 수 (도장 == 치킨 1마리 당 한 개)

# 치킨 개수를 단계별로 생각해보기
# 치킨의 쿠폰 수: 우선 치킨의 개수, 이 때 치킨의 수가 보너스 스탬프 수보다 많다면 그 몫만큼 치킨수를 더하고 그 나머지는 남은 스탬프의 수
# 이때 스탬프의 수 + 보너스 치킨 수가 다시 보너스 스탬프 수보다 크다면 위의 몫 만큼 치킨수를 더하고 나머지를 남은 스탬프로 저장하기 반복

#더 이상 input이 없을때까지 반복
while True:
    try:
        n, k = map(int, input().split())

        chicken = n

        bonus = chicken // k
        stamp = chicken % k

        #보너스 치킨이 0이라면 거기에서 종료
        while bonus != 0:
            chicken += bonus
            #보너스로 받은 치킨의 수만큼 스탬프도 늘어난다
            stamp = stamp + bonus

            #만약 스탬프 수가 다시 보너스 수가 되면 해당 수만큼 보너스 치킨을 추가로 받는다.
            #그게 아니라면 보너스 치킨은 0이 되고 loop를 탈출하게 된다.
            if stamp >= k:
                bonus = stamp // k
                stamp = stamp - (bonus * k)
            else:
                bonus = 0

        print(chicken)
    except:
        break



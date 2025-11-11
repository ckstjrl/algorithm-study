'''
BOJ13305 / D2): 주유소

해결 방법 : 그리디. 주유소를 돌면서, 다음 주유소 가격이 현재 가격보다 작으면, 가격 바꾸기. 아니면 안 바꾸기.
'''

city_cnt = int(input())
dists = list(map(int, input().split()))
price = list(map(int, input().split()))

total_price = 0
min_price = int(21e8)
for i in range(city_cnt-1):
    if price[i] < min_price:
        min_price = price[i]
    total_price += min_price * dists[i]

print(total_price)
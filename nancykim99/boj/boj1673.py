'''
BOJ1673 / D1): 치킨 쿠폰

해결 방법 : 
4마리 시킴 -> 1마리 시킴
10마리 시킴 -> 3마리 더 시킴 -> 1마리 시킴
n을 k로 나눈 몫이 새로운 쿠폰 -> 답에 저장하기
n을 나머지 + 새로운 쿠폰으로 갱신하기 (새롭게 구매한 치킨의 수) -> n이 k보다 작으면, 더이상 치킨을 살 수 없게됨
'''
import sys

for line in sys.stdin:
    n, k = map(int, line.split())

    ans = n

    while n >= k:
        temp = n // k
        ans += temp
        n = n % k + temp

    print(ans)



"""
2869. 달팽이는 올라가고 싶다

문제 푸는 idea:
달팽이가 올라가는 높이 A, 미끄러지는 높이 B, 막대의 총 높이를 V라고 하고,
n일차 낮에 이 달팽이가 막대 끝을 넘었다고 하자.
n일차에 이 달팽이가 올라가는 최고 peak 높이를 생각해보면 다음과 같다.
peak = nA - (n-1)B >= V
이제 부등식의 양변을 n에 대해 정리하면:
nA - nB + B >= V
n(A-B) >= V-B
n >= (V-B)/(A-B)
부등식을 만족하는 최소의 자연수 n을 구하면 이 문제의 답을 얻을 수 있다.
"""

import math

# 입력 받기
A, B, V = map(int, input().split())

# 최소 n값을 계산
n = (V-B) / (A-B)

# 최소 n값보다 큰 최소의 자연수 day값을 올림으로 출력
day = math.ceil(n)
print(day)



"""
문제 보자마자 FM으로 이렇게 짰는데 시간초과되길래 당황했다.
다시 보니 brute-force하고 연산량이 불필요하게 많은 것 같다.

## 오답 코드(시간초과)
A, B, V = map(int, input().split())

height = 0
day = 0

while True:
    day += 1
    height += A
    if height >= V:
        break
    else:
        height -= B

print(day)
"""
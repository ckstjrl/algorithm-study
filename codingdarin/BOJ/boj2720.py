# BOJ 2720. 세탁소 사장 동혁 (D1 / B3)
# https://www.acmicpc.net/problem/2720

T = int(input())
for _ in range(T):
    C = int(input())
    
    # 각 동전의 개수 계산
    quarters = C // 25
    C %= 25
    dimes = C // 10
    C %= 10
    nickels = C // 5
    C %= 5
    pennies = C
    print(quarters, dimes, nickels, pennies)

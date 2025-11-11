'''
BOJ2777 : 숫자놀이 (S2)

해결 방법 : 9부터 2까지 그리디기법으로 나누면서, 나눠지면, 자릿수 추가하고, 안 된다면 -1을 출력하기
'''

tc = int(input())

for _ in range(tc):
    n = int(input())
    ans = 0
    if n == 1:
        ans = 1
    else:
        while True:
            if n < 10:
                ans += 1
                break
            flag = 0
            for i in range(9, 1, -1):
                if n % i == 0:
                    n //= i
                    ans += 1
                    flag = 1
                    break
            if flag == 0 and n >= 10:
                ans = -1
                break
    print(ans)

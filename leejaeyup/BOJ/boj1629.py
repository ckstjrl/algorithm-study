'''
문제
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
'''



A, B, C = map(int, input().split())

def power(a, b):            # b가 0이면 a^0 = 1이다.
    if b == 0:
        return 1
    
    half = power(a, b // 2) # b를 반으로 쪼갬
    
    if b % 2 == 0:          # 짝수일 때: (a^(b//2))^2
        return (half * half) % C
    else:                   # 홀수일 때: a * (a^(b-1))
        return (half * half * a) % C

print(power(A, B) % C)
# boj1373. 2진수 8진수 (D1 / B1)
# https://www.acmicpc.net/problem/1373

import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    binary = input()
    # 3자리씩 끊어서 8진수로 변환
    n = len(binary)
    # 앞에 0을 채워서 길이를 3의 배수로 맞춤
    if n % 3 == 1:
        binary = '00' + binary
    elif n % 3 == 2:
        binary = '0' + binary

    octal_digits = ''
    for i in range(0, len(binary), 3):
        three_bits = binary[i:i+3]
        octal_digits += str(int(three_bits, 2))
        
    # 결과 출력 (앞의 불필요한 0 제거)
    result = octal_digits.lstrip('0')
    print(result if result else '0')
    
solve()
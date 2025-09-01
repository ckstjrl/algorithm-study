T = int(input())

for tc in range(1, T+1):
    N, str1 = map(str, input().split())
    N = int(N)

    str_10 = int(str1, 16) # 16진수에서 10진수로 변환
    binary_string = bin(str_10)[2:] # 슬라이싱을 이용하여 0b 접두사를 제거함
    result = binary_string.zfill(4*N)

    print(f'#{tc} {result}')

# 새로 배운 것 :
# 1. bin("string") : 10진수 숫자를 2진수 문자열로 변환 -> 0b0010101 (이런식으로 변환됨)
# 2. int('string', 16) : 16진수 숫자를 10진수 문자열로 변환
# 3. .zfill(int) : 문자열의 길이가 int가 될때까지 문자열 앞에 0을 채움
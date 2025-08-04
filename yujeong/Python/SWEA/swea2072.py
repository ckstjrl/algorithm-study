# 2072. 홀수만 더하기 / D1 

T = int(input())

for tc in range(T):
    nums = list(map(int, input().split()))
    
    odd_sum = 0          # 홀수 합을 담을 변수 

    for n in nums:       # 숫자 리스트 순회하며 
        if n % 2 != 0:   # 2로 나눈 나머지가 0이 아닌 경우 (=홀수인 경우)
            odd_sum += n # odd_sum에 합하기
    
    print(f'{tc+1} {odd_sum}')
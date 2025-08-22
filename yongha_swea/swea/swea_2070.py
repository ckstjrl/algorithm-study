T = int(input())
for test_case in range(1, T + 1):

    #a, b를 한 줄에 받아서 변수 두개에 하나씩 넣어주기
    a, b = map(int, input().split())
    
    #b가 a보다 작은 경우
    if a > b:
        ans = '>'
    
    #a가 b보다 작은 경우
    elif a < b:
        ans = '<'
    
    #b와 a가 동일한 경우
    else:
        ans = '='
        
    print(f'#{test_case} {ans}')
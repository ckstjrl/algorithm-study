# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
# 많은 수가 아닌 2개의 수를 비교할 때는 arr 없이 N,M 같이 간단하게 입력 후 비교 가능 

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    if N > M :
        result = '>'
    elif N == M :
        result = "="
    else:
        result = "<"
    
    print(f'#{tc} {result}')
    
# 출력값이 입력값 바로 밑에 나오는게 신경쓰이지만 답이 맞으니깐 패스 

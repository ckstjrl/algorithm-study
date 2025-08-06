# 2805. 농작물 수확하기 / D3

T = int(input())

for tc in range(T):
    N = int(input())
    answer = 0

    # 1X1 크기 농장인 경우 
    if N == 1:
        arr = int(input())
        answer = arr
    
    # 그 외
    else:
        for i in range(N//2):  # 마름모 윗부분
            arr = list(map(int, input()))
            for x in range(N//2 - i, N//2 + i + 1):
                answer += arr[x]
        
        arr = list(map(int, input()))  # 마름모 중간
        for a in arr:
            answer += a

        for j in range(N//2): # 마름모 아랫부분
            arr = list(map(int, input()))
            for x in range(j + 1, N - j - 1):
                answer += arr[x]
    
    print(f'#{tc+1} {answer}')
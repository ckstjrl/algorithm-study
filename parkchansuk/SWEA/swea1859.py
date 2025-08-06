T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price_arr = list(map(int, input().split()))
    max_p = 0  # 비쌀 때 팔아야 함
    profit = 0  # 팔아서 본 이득
    for i in range(N-1, -1, -1): # 예시 중 1 1 3 1 2 같은 문제를 해결하려면 뒤에서 부터 해야함
        if max_p < price_arr[i]:  
            max_p = price_arr[i]
            # 예시 1 1 3 1 2 로하면
            # 1. max_p = 2
            # 3. max_p = 3
        else : 
            profit += max_p - price_arr[i]
            # 2. max_p = 2 보다 price_arr[3]이 더 작으니 팔아서 이득을 봐야함
            # 4. max_p = 3 > price_arr[1]
            # 5. max_p = 3 > price_arr[0]
    
    print(f'#{tc} {profit}') # '#'안써서 fail 한번 나옴. 다음번엔 주의할 것

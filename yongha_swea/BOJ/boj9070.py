#BOJ9070 장보기

# 테스트 케이스 받기

T = int(input())

for tc in range(T):
    fish_num = int(input())
    
    # #아래 부분에서 리스트로 받는 것보다 int로 값을 받는 것에 더 유리한 부분이 있어서 해당 부분 변경
    # weight_per_price = []
    # 
    # price = 0
    
    best_ratio = 0
    best_price = 0

    # 어묵의 수에 맞춰서 input 받기
    for num in range(fish_num):
        weight, price = map(int, input().split())

        ratio = weight / price
        
        #list에서 변경한 만큼 각 수를 따로 저장해주기
        if ratio > best_ratio or (ratio == best_ratio and price < best_price):
            best_ratio = ratio
            best_price = price

        #삭제한 원안 (list에 넣는 방식)
        # weight_per_price.append(calc)
    print(best_price)
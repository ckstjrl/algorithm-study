T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().strip()))
    check = [0] * 10
    total = 0
    for i in arr:
        check[i] += 1
     
    for i in range(10):
        # 3번 이상 카운트에 대해 triplet 후 -3
        while check[i] >= 3:
            check[i] -= 3
            total += 1
    for i in range(8):
        # 연속된 리스트 슬라이스가 모두 0 이상이라면 run 
        while check[i] > 0 and check[i+1] > 0 and check[i+2] > 0:
            check[i] -= 1
            check[i+1] -= 1
            check[i+2] -= 1
            total += 1
    # run이나 triplet의 개수가 총 2개면 Baby-Gin
    if total == 2:
        print(f"#{test_case} true")
    else:
        print(f"#{test_case} false")
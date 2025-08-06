T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    check = [0] * 10
    for i in arr:
        check[i] += 1
    cur = check[0]
    idx = 0
    #check 의 값 = 등장 횟수, idx= 숫자
    for i in range(10):
        if check[i] >= cur:
            cur = check[i]
            idx = i
    print(f"#{test_case} {idx} {cur}")
T = int(input()) # test case 받기
for i in range(1, T):
    arr = list(map(int, input().split())) # arr list type으로 받기
    sum_odd = 0 # 홀수 합 초기값 설정
    
    for j in arr : # j 에서 arr 값 하나씩 뽑아서 순회
        if j % 2 == 1: # j가 홀수이면 sum_odd에 누적 합 
            sum_odd += j
    print('#'+str(i), sum_odd) # 값 출력 
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_all = 0    #총합을 담을 변수
    for i in arr:
        sum_all += i  #리스트의 요소를 순회하며 총합에 add
    min_all = int(round(sum_all / 10, 0)) #평균 내기

    print(f"#{t} {min_all}")
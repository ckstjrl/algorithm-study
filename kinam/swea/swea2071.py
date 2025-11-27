'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
'''
T = int(input())
for t in range(1, T+1):
    N = 10
    arr = list(map(int, input().split()))

    sum = 0 
    for i in arr:
        sum += i

    result = int(round(sum / N, 0)) # round로 첫째 자리에서 반올림하고 정수형 취하기
    print(f"#{t} {result}")
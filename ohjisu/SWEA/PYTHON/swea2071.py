"""
2071. 평균값 구하기
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)


[제약 사항]

각 수는 0 이상 10000 이하의 정수이다.


"""

T = int(input())
for test_case in range(1, T+1):
    input_num = list(map(int, input().split()))
    sum = 0
    count = 0
    for num in input_num :
        sum += num
        count += 1

    result = 0
    print(f'#{test_case} {round(sum/count)}')
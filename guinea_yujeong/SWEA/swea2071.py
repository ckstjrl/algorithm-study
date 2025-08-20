# 10개의 수를 입력받아, 평균값을 출력하는 프로그램 작성 
# 소수점 첫째 자리에서 반올림

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split())) 
    sum_n = sum(numbers) # 모든 숫자 합산
    len_n = len(numbers) # 리스트 요소 개수 반환 
    def calculate_average(numbers):
        return sum_n / len_n #평균값 구하기  

    calculate_average(numbers)

    print(f'#{tc} {average}')


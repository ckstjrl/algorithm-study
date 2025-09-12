'''
문제
45656이란 수를 보자.

이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

입력
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''



N = int(input())

# stairs[len][digit] = 길이가 len이고 끝자리가 digit인 계단 수의 개수.
stairs = []
for _ in range(N + 1):
    stairs.append([0] * 10)  # 각 자리마다 10개의 칸을 둠.


for d in range(1, 10):
    stairs[1][d] = 1  # 한 자리 수는 각자 한 개씩 있음.

# 길이 2부터 N까지 채워나가자.
for length in range(2, N + 1):
    for digit in range(10):  # 끝자리가 digit일 경우를 계산하자.
        if digit - 1 >= 0:  # digit-1에서 올 수 있다.
            stairs[length][digit] += stairs[length - 1][digit - 1]
        if digit + 1 <= 9:  # digit+1에서 올 수 있다.
            stairs[length][digit] += stairs[length - 1][digit + 1]
        stairs[length][digit] %= 1000000000

# 길이 N의 모든 경우를 합치자.
answer = 0
for d in range(10):  # 0부터 9까지 끝나는 모든 경우를 더해보자.
    answer += stairs[N][d]
    answer %= 1000000000    #

print(answer)
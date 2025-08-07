# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

# [제약 사항]
# 각 수는 0 이상 10000 이하의 정수이다.

# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

# [출력]
# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# T = int(input())

# for tc in range(1, T + 1):
#     numbers = (list(map(int, input().split)))
#     max_num = numbers[0] # 최대값

#     for i in range(numbers):
#         if i > max_num: #입력값을 다 순회하고 제일 큰 값 출력하기 
#             max_num = i

#     print(f'#{tc} {max}')

T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))  # 10개의 수 입력
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    print(f"#{tc} {max_num}")

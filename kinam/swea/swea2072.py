'''2072. 홀수만 더하기
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.
'''

T = int(input())

for t in range(1, T+1):
    n = list(map(int, input().split()))

    result = 0

    for i in n:
        if i % 2 != 0: # 2로 나눠서 0이 아니면(짝수가 아니면) i더하기
            result += i

    print(f"#{t} {result}")
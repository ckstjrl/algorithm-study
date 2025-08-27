'''
[Bronze I] FizzBuzz - 28702

[문제 링크](https://www.acmicpc.net/problem/28702) 

성능 요약
메모리: 32412 KB, 시간: 40 ms

분류
수학, 문자열

제출 일자
2025년 8월 22일 17:16:21

문제 설명
FizzBuzz 문제는 i=1,2,⋯
i=1,2,⋯ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.
i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.
i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

입력
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 8 이하입니다. 
입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

출력
연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.
'''


arr = [input() for _ in range(3)]

default = []
for i, a in enumerate(arr) :
    if a.isdigit() :
        default.append([i, int(a)])

if default[-1][0] == 2 :
    result = default[-1][1] + 1
elif default[-1][0] == 1 :
    result = default[-1][1] + 2
else :
    result = default[-1][1] + 3

print('FizzBuzz' if result%15==0 else 'Fizz' if result%3 == 0 else 'Buzz' if result%5 == 0 else result)
# [문제]
# FizzBuzz 문제는 
# $i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

# i가 3의 배수이면서 5의 배수이면 “FizzBuzz”를 출력합니다.
# i가 3의 배수이지만 5의 배수가 아니면 “Fizz”를 출력합니다.
# i가 3의 배수가 아니지만 5의 배수이면 “Buzz”를 출력합니다.
# i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력합니다.
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 
# 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

# [입력]
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 8 이하입니다. 
# 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

# [출력]
# 연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# 입력 받기
words = [input().strip() for _ in range(3)]

for i, w in enumerate(words):
    if w.isdigit():
        n = int(w) - i
        if [fizzbuzz(n), fizzbuzz(n+1), fizzbuzz(n+2)] == words:
            print(fizzbuzz(n+3))
            break
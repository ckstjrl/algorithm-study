# 28702. FiZZBuzz

s1 = input()
s2 = input()
s3 = input()

# 숫자가 있으면 그걸 토대로 다음에 올 수를 찾을 수 있음
if s1.isnumeric():
    target = int(s1) +3
elif s2.isnumeric():
    target = int(s2) + 2
elif s3.isnumeric():
    target = int(s3) + 1

# 아닌 경우 출력은 무조건 Fizz
else:
    ans = 'Fizz'

# 숫자가 3 또는 5의 배수인지에 따라, 규칙에 맞게 출력 결정
if target%3==0 and target%5==0:
    ans = 'FizzBuzz'
elif target%3==0:
    ans = 'Fizz'
elif target%5==0:
    ans = 'Buzz'
else:
    ans = target

print(target)
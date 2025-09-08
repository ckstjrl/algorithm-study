#정수의 형태 그대로 사용할 숫자1은 정수 형태로 받기
num1 = int(input())
#들어오는 값을 반대로 뒤집어야 하는 숫자2는 reverse를 위해서 list로 받기
origin_num2 = input()
num2 = list(map(int, origin_num2))

num2.reverse()

#거꾸로 뒤집은 수를 하나씩 숫자1에 곱해주기
for i in num2:
    print(num1 * i)

#마지막으로 전체 곱셈 값을 print해주기
print(num1 * int(origin_num2))
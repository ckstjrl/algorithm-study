num1 = int(input())
num2 = int(input())
result = num1 * num2
result3 = num1 * (num2 % 10)
num2 //= 10
result4 = num1 * (num2 % 10)
num2 //= 10
result5 = num1 * (num2 % 10)

print(result3)
print(result4)
print(result5)
print(result)
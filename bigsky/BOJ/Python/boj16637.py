# BOJ16637: 괄호 추가하기
N = int(input())
expression = input()
max_value = -float('inf')

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def dfs(index, c_value):
    global max_value

    if index == len(expression):
        max_value = max(max_value, c_value)
        return

    n_value = calculate(c_value, int(expression[index + 1]), expression[index])
    dfs(index + 2, n_value)

    if index + 4 <= len(expression):
        b_value = calculate(int(expression[index + 1]), int(expression[index + 3]), expression[index + 2])
        n_value = calculate(c_value, b_value, expression[index])
        dfs(index + 4, n_value)

dfs(1, int(expression[0]))

print(max_value)

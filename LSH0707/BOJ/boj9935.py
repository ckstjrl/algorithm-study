arr = input()
change = list(input())
stack = []
for x in arr:
    stack.append(x)
    if len(stack) >= len(change):  # 스택 길이가 지울문자 길이 이상인 경우
        if stack[len(stack)-len(change):] == change:  # 스택 맨뒤문자열이 지울문자와 같은경우
            for _ in range(len(change)):  # pop
                stack.pop()
if stack:  # 남은 문자열 출력(없으면 FRULA)
    print(''.join(stack))
else:
    print("FRULA")
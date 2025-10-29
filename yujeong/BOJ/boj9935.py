# 9935. 문자열 폭발

s = input()         # 원본 문자열
bomb = input()      # 폭발 문자열
s_len = len(s)      # 원본 문자열 길이
b_len = len(bomb)   # 폭발 문자열 길이 

stack = []          # 문자열을 담을 스택; 스택으로 옮기는 과정에서 폭발 문자열이 발견되면 날리기
for i in range(s_len):
    stack.append(s[i])
    # 스택의 끝 b_len 자리만큼이 폭발 문자열과 일치하면 폭발
    if s[i] == bomb[-1] and len(stack) >= b_len:
        if ''.join(stack[-b_len:]) == bomb:
            for _ in range(b_len):
                stack.pop()

print(''.join(stack) if stack else "FRULA")     # 남은 문자열을 형식에 맞게 출력
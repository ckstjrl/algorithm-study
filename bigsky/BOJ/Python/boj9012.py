# BOJ9012(D2): 괄호
N = int(input())

for _ in range(N):
  pars = list(input())
  stack = []

  for i in range(len(pars)):
    if pars[i] == '(':  # 여는 괄호는 스택에 추가
      stack.append(pars[i])
    elif pars[i] == ')' and stack:  # 닫는 괄호는 스택에 여는 괄호 있을 때만 pop
      stack.pop()
    else:  # 그 외의 입력은 NO
      print('NO')
      break
  else:  # 모든 입력이 끝난 후 스택에 여는 괄호가 남아있다면 NO
    if stack:
      print('NO')
    else:  # 모든 조건을 통과하면 YES!
      print('YES')
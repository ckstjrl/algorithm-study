'''
BOJ2504 : 괄호의 값 (G5)

1. 문자열을 스택에 하나씩 넣으면서 확인하기
2. 여는 괄호 -> 스택에 넣기
3. 닫는 괄호 -> 여는 괄호면, 괄호 값을 스택에 넣기
    3-2. 숫자들이면, 다 더해서 계산해서 스택에 넣기
4. 스택에 숫자만 있으면, 합하기 -> 정답
'''

import sys
s = sys.stdin.readline().strip()

st = []
flag = True
ans = 0

for b in s:
    if not flag:
        break
    if b in ('(', '['):
        st.append(b)
        continue
    if b in (')', ']'):
        n = []           
        inner = True     
        while inner:
            if not st:
                ans = 0
                flag = False
                break
            p = st.pop()
            if isinstance(p, int):
                n.append(p)
            elif p not in ('(', '['):
                ans = 0
                flag = False
                inner = False
            else:
                if b == ')' and p == '(':
                    if n:
                        a = sum(n) * 2
                    else:
                        a = 2
                    st.append(a)
                    inner = False   
                elif b == ']' and p == '[':
                    if n:
                        a = sum(n) * 3
                    else:
                        a = 3
                    st.append(a)
                    inner = False   
                else:
                    ans = 0
                    flag = False
                    inner = False

if not flag:
    print(0)
else:
    for x in st:
        if not isinstance(x, int):
            print(0)
            break
        ans += x
    else:
        print(ans)

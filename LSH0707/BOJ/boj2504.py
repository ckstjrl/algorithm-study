s = input().strip()
arr = []
for x in s:  # (), [] -> 숫자로 치환
    if x in '([':
        arr.append(x)
    if x == ')':
        if arr and arr[-1] == '(':
            arr.pop()
            arr.append(2)
        else:
            arr.append(x)
    if x == ']':
        if arr and arr[-1] == '[':
            arr.pop()
            arr.append(3)
        else:
            arr.append(x)
stack = []
for y in arr:  # 올바르지 못한 괄호열인지 검사 -> stack남으면 0출력
    if y in [2, 3]:
        continue
    elif y in '([':
        stack.append(y)
    else:
        if y == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(y)
        if y == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(y)
if stack:
    print(0)
else:
    st = []
    for i in arr:  # 괄호값 계산
        if i in [2, 3, '(', '[']:
            st.append(i)
        else:
            if i == ')':
                v = 0
                while st[-1] != '(':
                    v = v + st.pop()
                st.pop()
                v = v * 2
                st.append(v)
            else:
                v = 0
                while st[-1] != '[':
                    v = v + st.pop()
                st.pop()
                v = v * 3
                st.append(v)
    print(sum(st))

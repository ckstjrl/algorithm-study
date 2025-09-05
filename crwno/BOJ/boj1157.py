s = str(input())
s = s.upper()

max_cnt = 0
stack = []
max_stack = [0]
prev = 0
max_alpha = []
for i in range(len(s)):
    cnt = 0
    p = s[i]
    for j in s:
        if j == p:
            if j in stack:
                break
            cnt += 1
    if p not in stack:
        stack.append(p)
    if max_cnt <= cnt:
        max_cnt = cnt
        prev = max_stack.pop()
        max_stack.append(max_cnt)
        max_alpha.append(p)

if prev == max_cnt:
    print('?')
else:
    print(max_alpha.pop())
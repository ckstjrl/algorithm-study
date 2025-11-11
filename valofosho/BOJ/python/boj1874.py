"""
1~n 까지 수를 스택에 넣었다가 뽑으면 수열
스택에 push하는 순서는 반드시 오름차순
스택을 이용해 수열을 만들 수 있는지 
있다면 어떤 순서로 push or pop

N의 최고점이 찍히고 다시 작은 수가 찍히는건 가능
최고점 찍고 작은 수찍고 다시 커지면 불가능

"""
N = int(input())
arr = []
stack = []
cnt = 1
ans = []
for i in range(N):
    arr.append(int(input()))

for num in arr:
    if cnt <= num:
        for asc in range(cnt, num+1):
            stack.append(asc)
            ans.append('+')
        cnt = num + 1
        while stack and stack[-1] >= num:
            stack.pop()
            ans.append('-')
    elif cnt > num:
        if stack and stack[-1] >= num:
            while stack and stack[-1] >= num:
                stack.pop()
                ans.append('-')
        else:
            ans = []
            break

if ans:
    print('\n'.join(ans))
else:
    print("NO")


# 예전에 풀었던 풀이
N = int(input())
s, t, f = [], [], []
for i in range(N):
    a=int(input())
    s.append(a)
comp=1
error_code=0
for idx in range(N):
    while comp <= s[idx]:
        t.append(comp)
        f.append("+")
        comp+=1
    if t[-1] == s[idx]:
        t.pop()
        f.append("-")
    else:
        print("NO")
        error_code=1
        break
if not error_code == 1:
    print('\n'.join(f))

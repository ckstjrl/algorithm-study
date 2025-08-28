N, K = map(int, input().split())
arr = list(range(1, 1+N))
ans = []
p = 0
while len(arr) > 0:
    p = (p + K - 1) % len(arr) # 다음번호 만들기
    ans.append(arr.pop(p)) # pop
print(str(ans).replace('[', '<').replace(']', '>'))

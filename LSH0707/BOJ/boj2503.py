import sys
input = sys.stdin.readline

def b(ans, guess):
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == ans[i]:
            strike = strike + 1
        elif guess[i] in ans:
            ball = ball + 1
    return strike, ball
N = int(input())
q = []
for _ in range(N):
    number, x, y = input().strip().split()
    q.append((number, int(x), int(y)))
result = 0
for num in range(123, 988):
    n_str = str(num)
    if '0' in n_str or len(set(n_str)) < 3:
        continue
    ans = 0
    for q_n, q_s, q_b in q:
        strike, ball = b(n_str, q_n)
        if strike != q_s or ball != q_b:
            ans = 1
            break
    if ans == 0:
        result = result + 1
print(result)
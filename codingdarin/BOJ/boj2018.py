# BOJ 2018. 수들의 합 5 (D1 / S5)

N = int(input())

# 투포인터
start = 1
end = 1
total = 1
cnt = 0

while end <= N:
    if total == N:
        cnt += 1
        total -= start
        start += 1
    elif total < N:
        end += 1
        total += end
    else:  # total > N
        total -= start
        start += 1

print(cnt)
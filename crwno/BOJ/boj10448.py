T = int(input())

num_1 = 0
p = 1
nums = []
while num_1 + p <= 1000:
    k = num_1 + p
    num_1 = k
    p += 1
    nums.append(num_1)

ans = []

for _ in range(T):
    K = int(input())
    res = 0

    for a in nums:
        if a > K:
            break
        for b in nums:
            if a + b > K:
                break
            c = K - a - b
            if c in nums:
                res = 1
                break
        if res == 1:
            break

    ans.append(res)

for i in ans:
    print(i, end='\n')
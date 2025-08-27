# BOJ1541. 잃어버린 괄호 D3

arr = input().split('-') # -를 기준으로 split

sum2 = []

for i in arr:
    sum = 0
    tmp = i.split('+') # 괄호 안 + 연산 계산
    for j in tmp:
        sum += int(j)
    sum2.append(sum)

n = sum2[0]

for i in range(1, len(sum2)): # 괄호 밖 - 연산 계산
    n -= sum2[i]

print(n)








# BOJ 3273. 두 수의 합 (D2)

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

compare= set()
cnt = 0
for each in arr:
    other = x - each
    if other in compare:
        cnt+=1
    compare.add(each)

print(cnt)
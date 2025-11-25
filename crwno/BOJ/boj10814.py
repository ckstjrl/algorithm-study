N = int(input())

ages = [[] for _ in range(201)]
for _ in range(N):
    age, name = map(str, input().split())
    ages[int(age)].append(name)

for i in range(201):
    if ages[i]:
        for name in ages[i]:
            print(i, name)
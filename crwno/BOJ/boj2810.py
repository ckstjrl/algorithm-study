N = int(input())
seats = input()
num_S = 0
num_L = 0
for i in range(len(seats)):
    if seats[i] == 'S':
        num_S += 1
    elif seats[i] == 'L':
        num_L += 1

ans = num_S + num_L // 2
if num_L == 0:
    print(ans)
else:
    print(ans + 1)
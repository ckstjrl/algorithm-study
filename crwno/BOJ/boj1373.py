num_2 = input()

num_8 = []
k = len(num_2) // 3
if len(num_2) % 3 == 0:
    for i in range(k):
        num_8.append(num_2[3 * i:3 * i + 3])
elif len(num_2) % 3 == 1:
    num_8.append(num_2[0])
    for i in range(k):
        num_8.append(num_2[3 * i + 1:3 * i + 4])
else:
    num_8.append(num_2[0:2])
    for i in range(k):
        num_8.append(num_2[3 * i + 2:3 * i + 5])

ans = [0] * len(num_8)

for i in range(len(num_8)):
    for j in range(len(num_8[i])):
        ans[i] += int(num_8[i][j]) * (2 ** (len(num_8[i]) - j - 1))

for i in range(len(ans)):
    print(ans[i], end='')
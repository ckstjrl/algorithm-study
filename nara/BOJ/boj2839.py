sugar = int(input())
count_list = []
min_count = sugar

for i in range(sugar // 5 + 1):
    tmp = sugar
    count = 0
    count += i
    tmp -= (5 * i)

    count += tmp // 3
    tmp %= 3
    if tmp != 0:
        count = -1
    count_list.append(count)

for i in count_list:
    if i != -1:
        if min_count > i:
            min_count = i
if min_count == sugar:
    min_count = -1

print(min_count)
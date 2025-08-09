N = int(input())
arr = list(map(str, range(1, N + 1))) # [1 2 3 4 5 6 7...]
new_arr = []

for i in arr:
    count_i = 0
    for j in range(len(i)):
        if i[j] in ['3', '6', '9']:
            count_i = count_i + 1
        else:
            pass
    if count_i == 0:
        pass
    else:
        i = '-' * count_i
    new_arr.append(i)
print(*new_arr)


# N = int(input())
# arr = list(map(str, range(1, N + 1))) # [1 2 3 4 5 6 7...]
# new_arr = []
# 
# for i in arr:
#     count_i = 0
#     for j in range(len(i)):
#         if i[j] in ['3', '6', '9']:
#             count_i = count_i + 1
#     if count_i != 0:   <--- 승준수정
#         i = '-' * count_i
#     new_arr.append(i)
# print(*new_arr)
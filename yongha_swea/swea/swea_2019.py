key = int(input())

ans_list = []

ans = ''

cur_num = 1

for i in range(key+1):
    ans_list.append(str(cur_num))
    cur_num = cur_num * 2

ans = ' '.join(ans_list)

print(ans)
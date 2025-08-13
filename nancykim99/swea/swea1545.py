N = int(input())

num_list = []
for i in range(N+1): # 숫자를 하나씩 꺼내서 저장
    num_list.append(i)

num_list.sort(reverse=True) # 숫자를 거꾸로 sort

result_list = []
for i in range(N+1): # sort한 int들을 str으로 다시 저장
    result_list.append(str(num_list[i]))

result = ' '.join(result_list) # list를 str으로 저장

print(result)
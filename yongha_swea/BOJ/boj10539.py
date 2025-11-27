#boj10539 수빈이와 수열

arr_length = int(input())

arr = list(map(int, input().split()))

ans = ''

for mul in range(arr_length):
    # index error를 피하기 위한 방법으로 첫번째 수는
    # 그 값 자체가 첫째값이 되기 때문에 예외 처리
    if mul == 0:
        ans = ans + str(arr[mul]) + ' '
    #첫번째 자리를 처리해줬기 때문에 1부터 arr_len-1 까지 loop 한다고 생각을 하면 된다
    else:
        ans_num = (arr[mul] * (mul + 1)) - (arr[mul-1] * (mul))
        ans = ans + str(ans_num) + ' '

print(ans)

# 아래는 잘못 구현한 케이스 A를 구하는 식을 만들어버렸다
# for div in range(1, arr_length+1):
#     cur_num = arr[div-1]
#     sum_num += cur_num
#     ans_num = sum_num / div
#     ans = ans + str(ans_num) + ' '

# print(ans)
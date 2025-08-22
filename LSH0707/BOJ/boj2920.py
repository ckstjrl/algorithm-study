arr = list(map(int, input().split()))

if arr == [i for i in range(1, 9)]:
    print('ascending')
elif arr == [i for i in range(8, 0, -1)]:
    print('descending')
else:
    print('mixed')  # 2가지 경우 제외 mixed 출력
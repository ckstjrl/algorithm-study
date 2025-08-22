# 2920. 음계

scale = list(map(int, input().split()))

# 내장함수 사용
# if scale == sorted(scale):
#     print('ascending')
# elif scale == sorted(scale, reverse=True):
#     print('descending')
# else:
#     print('mixed')

# 내장함수 없이
if scale == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif scale == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')
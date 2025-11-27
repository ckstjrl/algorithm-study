# BOJ 2920.음계 / D1
arr=[1, 2, 3, 4, 5, 6, 7, 8]
in_arr = list(map(int, input().split()))

if in_arr == arr:
    print('ascending')

elif in_arr == arr[::-1]:
    print('descending')
else:
    print('mixed')
N = int(input())

num_arr = [int(input()) for _ in range(N)]

num_arr.sort()

for i in num_arr:
    print(i)
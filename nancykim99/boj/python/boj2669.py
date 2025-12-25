# 1 <= x, y <= 100

# 사각형의 왼쪽 아래 x, y
# 오른쪽 위 x, y



arr = [[0] * 101 for _ in range(101)]

for _ in range(4):
    s_x, s_y, l_x, l_y = map(int, input().split())

    for i in range(s_x, l_x):
        for j in range(s_y, l_y):
            arr[i][j] += 1
    
area = 0
for k in range(101):
    for l in range(101):
        if arr[k][l] > 0:
            area += 1

print(area)







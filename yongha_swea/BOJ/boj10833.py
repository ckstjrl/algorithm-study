# N = 학교 수
# students, apple = a, b

N = int(input())

stu_list = []

apple_list = []

total = 0

for _ in range(N):
    stu, apple = map(int, input().split())

    stu_list.append(stu)

    apple_list.append(apple)


for i in range(N):
    rest = apple_list[i] % stu_list[i]

    total = total + rest

print(total)
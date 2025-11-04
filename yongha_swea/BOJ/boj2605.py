#boj2605 줄 세우기

students = int(input())

draw_arr = list(map(int, input().split()))

line = []

ans = ''

for i in range(students):
    student = i + 1

    if draw_arr[i] == 0:
        #0의 경우 가장 앞자리에 학생 넣기
        line.insert(0, student)
    else:
        #0이 아닌 숫자가 나왔을 때 해당 값의 위치로 해당 학생 넣어주기
        line.insert(draw_arr[i], student)

#0이 가장 앞이 아닌 마지막으로 가는 방식이기 때문에 마지막에 뒤집기
line.reverse()

#출력 방식에 맞춰서 str으로 바꾸기
for i in line:
    ans = ans + str(i) + ' '

print(ans)


'''
BOJ1244. 스위치 켜고 끄기
해결 방법 : 그냥 구현 후 진행... 더 줄일 수 있지 않을까...
'''
import sys
switch = int(sys.stdin.readline())
switch_arr = ['*'] + list(map(int, sys.stdin.readline().split()))
student = int(sys.stdin.readline())

student_arr = []
for _ in range(student):
    gender, num = map(int, sys.stdin.readline().split())
    student_arr.append((gender, num))
# [(1, 3), (2, 3)]

for i in range(student):
    if student_arr[i][0] == 1: # 남자인 경우
        for j in range(1, switch+1):
            if j % student_arr[i][1] == 0: # 배수인 경우, 스위치 변경
                if switch_arr[j] == 1:
                    switch_arr[j] = 0
                else:
                    switch_arr[j] = 1
    else: # 여자인 경우
        flag = True
        while flag:
            c = student_arr[i][1]
            if switch_arr[c] == 1:
                switch_arr[c] = 0
            else:
                switch_arr[c] = 1
            for x in range(1, switch+1):
                if 0<(c-x)<=switch and 0<(c+x)<=switch:
                    a = c - x
                    b = c + x
                    if switch_arr[a] == switch_arr[b]:
                        if switch_arr[a] == 1 and switch_arr[b] == 1:
                            switch_arr[a] = 0
                            switch_arr[b] = 0
                        elif switch_arr[a] == 0 and switch_arr[b] == 0:
                            switch_arr[a] = 1
                            switch_arr[b] = 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break

switch_arr.pop(0)
for i in range(len(switch_arr)):
    switch_arr[i] = str(switch_arr[i])
ans = ' '.join(switch_arr)

for i in range(1, len(switch_arr) // 20 + 2):
    num_pre = (i-1) * 40
    num = i * 40
    print(ans[num_pre:num])
# 10162. 전자레인지

T = int(input())

buttons = [300, 60, 10]     # 단위가 큰 버튼부터 누르기
cnt =[0, 0, 0]              # 각 버튼을 누른 횟수 count

for i in range(3):
    cnt[i] += T // buttons[i]   # 각 버튼의 시간 단위로 나눈 몫 = 버튼을 누른 횟수
    T %= buttons[i]

if T>0:         # 나누어떨어지지 않으면 불가능
    ans = [-1]
else:
    ans = cnt


print(*ans)
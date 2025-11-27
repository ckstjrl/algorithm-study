# 2869. 달팽이는 올라가고 싶다
'''
하루에 올라가는 거리 : A-B
전날까지 도달해야 하는 거리 : V-B == 다음날 그냥 A로 올라가기만 하면 됨
이때 딱 맞아 떨어지면 일수 그대로 계산,
소숫점으로 떨어지면 하루 더해야 함
'''

A, B, V = map(int, input().split())
day = (V-B)/(A-B)   # 하루종일 가고 내려가는 것 : A-B / 목표치 : V-B
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1) # 소숫점이면 올림해줘야함
    
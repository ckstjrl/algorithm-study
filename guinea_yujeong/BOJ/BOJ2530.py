'''
백준 2530번 : 인공지능 시계 

문제 
훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 초 단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
'''

a, b, c = map(int, input().split())
f_time = int(input())

c += f_time 
carry_min, c = divmod(c, 60) # 60초 넘을경우 분으로 더하기

b += carry_min
carry_hour, b = divmod(b, 60) #60분 넘을 경우 시간에 더하기

a += carry_hour
a %= 24

print(a, b, c)


'''
memo 
divmod(x, 60) 몫=캐리, 나머지 = 정상화 값 을 한번에 얻을 수 있음 

'''

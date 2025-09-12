'''
백준 2438번 : 별 찍기 - 1

첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

n = int(input())
star = ''
for i in range(1, n+1):
    star = '*' * i
    print(star)

# 5585. 거스름돈
'''
거스름돈 = 500, 100, 50, 10, 5, 1
1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

거스름돈 : 1000 - input()
동전 종류를 리스트화해서 for문으로 돌면서 몫으로 갯수 구함.
'''
money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
cnt = 0
for c in coin:
    p_cnt = money // c
    cnt += p_cnt
    money -= c * p_cnt
print(cnt)
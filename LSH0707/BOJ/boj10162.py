T = int(input())
if T % 10 != 0:
    print(-1)
else:
    print(T//300, (T%300)//60, ((T%300)%60)//10)  # 큰 단위부터 나눈 몫 구하고 출력
#boj10870: 피보나치 수 5

n = int(input())

#재귀문 이용
def fibo(n):
    #2이상의 경우 본인 이전 두 수의 합을 return
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    #1, 0의 경우에는 본인을 return
    else:
        return n
#return값 출력
print(fibo(n))
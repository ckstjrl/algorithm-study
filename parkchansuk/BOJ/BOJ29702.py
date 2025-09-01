# BOJ 28702. FizzBuZZ /D2
'''
3의 배수 & 5의 배수 = FizzBuzz
3의 배수 & ~5의 배수 = Fizz
~3의 배수 & 5의 배수 = Buzz
~3의 배수 & ~5의 배수 = i 그대로 출력
입력 이후에 올 숫자를 예상하고 출력
'''
"""
1~15 문자열이 계속 반복됨
i, i, F, i, B, F, i, i, F, B, i, F, i, i, FB의 반복
3개씩 끊으면 총 10가지의 경우 발생
[i, i, F] [i, F, i] 등 여러 문자열이 올 수 있는 경우 아무거나 출력
"""
import sys
arr = [sys.stdin.readline().strip() for _ in range(3)]+[0] # 입력을 엔터 기준으로 받음
def find_three(a): # arr[2]를 기준으로 다음에 나올 숫자를 구해주는 함수
    if a[2] == 'Fizz':
        if a[1] == 'Buzz':
            return int(a[0]) + 3 # i B F
        else:
            return int(a[1]) + 2 # i i F/ B i F
    elif a[2] == 'Buzz':
        if a[1] == 'Fizz':
            return int(a[0]) + 3 # i B F
        else:
            return int(a[1]) + 2 # F i B
    elif a[2] == 'FizzBuzz':
        return int(a[1]) + 2 # i i FB
    else:
        return int(a[2]) + 1 # i F i / B F i / F i i / F B i

arr[3] = find_three(arr) # 다음에 나올 숫자가 15의 배수인지, 5의 배수인지, 3의 배수인지 판단
if arr[3] % 15 == 0:
    print('FizzBuzz')
elif arr[3] % 5 == 0:
    print('Buzz')
elif arr[3] % 3 == 0:
    print('Fizz')
else:
    print(str(arr[3]))
    

''' 10개의 경우의 수를 전부 계산하려고 하다 실패
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()
arr = ['Fizz', 'Buzz', 'FizzBuzz']

if a not in arr: # iiF, iFi, iFB, iiFB case
    if b in arr and c in arr:
        print(int(a)+3) # iFB
    else:
        if c not in arr:
            print('Buzz') # iFi
        else:
            if c == 'Fizz':
                print('Buzz') # iiF
            else:
                print(int(b)+2) # iiFB

else: # FiB, Fii, FBi, BFi, BiF case
    if b not in arr and c not in arr:
        print('FizzBuzz') # Fii
    else:
        if a == 'Fizz':
            print('Fizz') # FBi FiB
        else:
            if b == 'Fizz':
                print(int(c)+1) # BFi
            else:
                print(int(b)+2) # BiF
'''

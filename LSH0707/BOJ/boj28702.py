a = input()
b = input()
c = input()
if a.isdigit() == True: # 입력값 3개중 최소 1개는 숫자이므로 다음에올 숫자 찾기
    d = int(a) + 3
elif a.isdigit() == False and b.isdigit() == True:
    d = int(b) + 2
elif a.isdigit() == False and b.isdigit() == False and c.isdigit() == True:
    d = int(c) + 1

if d % 15 == 0:
    print('FizzBuzz')
elif d % 5 == 0:
    print('Buzz')
elif d % 3 == 0:
    print('Fizz')
else:
    print(d)
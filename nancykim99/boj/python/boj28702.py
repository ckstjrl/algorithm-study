arr = []

for _ in range(3):
    t = input()
    if t != 'Fizz' and t != 'Buzz' and t != 'FizzBuzz':
        t = int(t)
    arr.append(t)

for i in range(3):
    if i == 0 and type(arr[i]) == int:
        ans = arr[i] + 3
    elif i == 1 and type(arr[i]) == int:
        ans = arr[i] + 2
    elif i == 2 and type(arr[i]) == int:
        ans = arr[i] + 1

if ans % 3 == 0 and ans % 5 != 0:
    ans = 'Fizz'
elif ans % 3 != 0 and ans % 5 == 0:
    ans = 'Buzz'
elif ans % 3 == 0 and ans % 5 == 0:
    ans = 'FizzBuzz'

print(ans)
#boj5585 거스름돈

#동전 옵션은 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

pay = int(input())

money = 1000 - pay

count = 0

while money >= 500:
    count += 1
    money -= 500

while money >= 100:
    count += 1
    money -= 100    

while money >= 50:
    count += 1
    money -= 50

while money >= 10:
    count += 1
    money -= 10

while money >= 5:
    count += 1
    money -= 5

while money >= 1:
    count += 1
    money -= 1

print(count)  
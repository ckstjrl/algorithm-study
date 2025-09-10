# BOJ30802: 웰컴 키트
N = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundle = 0
pencil_bundle = N // P
pencil1 = N % P

for num in shirt:
    if num % T != 0:
        shirt_bundle += num // T + 1
    else:
        shirt_bundle += num // T

print(shirt_bundle)
print(pencil_bundle, pencil1)

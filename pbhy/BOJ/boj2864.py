# 2864. 5와 6의 차이
'''
상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다.
이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.

if 5:
- 최소 : 5로 구한 것
- 최대 : 6으로 구한 것
if 6:
- 최소 : 5로 구한 것
- 최대 : 6으로 구한 것
계산시 숫자 한 글자씩 읽으면서 *10으로 자릿수 밀어주자.
숫자 자릿수 찾아가면서 5가 나오면 6으로, 6이 나오면 5로 하는 계산 하면 됨.
'''
a, b = input().split()
min_a = 0
for ch in a:
    if ch == '6':
        min_a = min_a * 10 + 5
    else:
        min_a = min_a * 10 + int(ch)

min_b = 0
for ch in b:
    if ch == '6':
        min_b = min_b * 10 + 5
    else:
        min_b = min_b * 10 + int(ch)
min_v = min_a + min_b

max_a = 0
for ch in a:
    if ch == '5':
        max_a = max_a * 10 + 6
    else:
        max_a = max_a * 10 + int(ch)

max_b = 0
for ch in b:
    if ch == '5':
        max_b = max_b * 10 + 6
    else:
        max_b = max_b * 10 + int(ch)
max_v = max_a + max_b
print(min_v, max_v)
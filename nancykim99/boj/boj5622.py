# BOJ5622. 다이얼

word = list(input())

ans = 0

for char in word:
    if char in ('A', 'B', 'C'):
        ans += 3
    if char in ('D', 'E', 'F'):
        ans += 4
    if char in ('G', 'H', 'I'):
        ans += 5
    if char in ('J', 'K', 'L'):
        ans += 6
    if char in ('M', 'N', 'O'):
        ans += 7
    if char in ('P', 'Q', 'R', 'S'):
        ans += 8
    if char in ('T', 'U', 'V'):
        ans += 9
    if char in ('W', 'X', 'Y', 'Z'):
        ans += 10

print(ans)
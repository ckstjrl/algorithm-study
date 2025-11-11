'''
BOJ2872 : 우리집엔 도서관이 있어 (S1)

해결방법 : 일단 순서대로 되어 있는 순서를 먼저 구하기.
    1. 가장 마지막 책 위에 -1한 책이 있으면 skip
    2. 그 다음에 -1한 책이 위에 있으면 skip을 일단 반복하기
    3. 반복하지 못하는 경우, 책의 수에서 반복하지 못한 수를 빼기
    4. 뺀 수가 정답
'''

n = int(input())
books = []

for i in range(n):
    b = int(input())
    books.append(b)

books.reverse()

r_cnt = 0
x = n
for i in range(n):
    if books[i] == x:
        r_cnt += 1
        x -= 1

ans = n - r_cnt 
print(ans)
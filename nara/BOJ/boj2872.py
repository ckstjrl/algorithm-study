import sys
input = sys.stdin.readline

N = int(input())
books = [int(input()) for _ in range(N)]

max_value = max(books)
max_index = books.index(max_value)

ans = N - 1 - max_index

for i in range(max_index - 1, -1, -1):
    if books[i] + 1 != max_value:
        ans += 1
    else:
        max_value = books[i]
print(ans)
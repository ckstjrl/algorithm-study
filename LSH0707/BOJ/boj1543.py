A = input().strip()
B = input().strip()
cnt = 0
while True:
    C = A.replace(B, '1', 1)
    if A != C:  # 중복 단어 한번씩 replace하고 바뀌면 cnt+1 아니면 break
        cnt = cnt + 1
        A = C
    else:
        break
print(cnt)
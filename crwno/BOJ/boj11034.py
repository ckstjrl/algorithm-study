while True:
    try:
        A, B, C = map(int, input().split())
        cnt = 0
        while (B - A > 1) or (C - B > 1):
            left = B - A
            right = C - B

            if left > right:
                new_B = A + 1
                new_A = A
                new_C = B
            else:
                new_B = B + 1
                new_A = B
                new_C = C

            A, B, C = new_A, new_B, new_C
            cnt += 1

        print(cnt)
    except EOFError:
        break

# try, except 말고 뭐있지
R, B = map(int, input().split())

total = R + B
W = 3

while W < (total // 3) + 1:

    if total % W == 0:
        L = total // W
        if (L - 2) * (W - 2) == B:
            print(L, W)
            break
        else:
            W += 1
    else:
        W += 1
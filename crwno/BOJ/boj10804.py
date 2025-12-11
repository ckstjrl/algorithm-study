cards = [0] * 20
cnt = 1
for i in range(20):
    cards[i] += cnt
    cnt += 1

for _ in range(10):
    s, e = map(int, input().split())
    st = []
    for idx in range(e - 1, s - 2, -1):
        st.append(cards[idx])
    for idx in range(s - 1, e):
        cards[idx] = st[idx - s + 1]
for i in range(20):
    print(cards[i], end=' ')
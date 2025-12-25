sentence = input()
sentence_rev = []

for i in sentence:
    if ord(i) - 3 < 65:
        sentence_rev.append(chr(ord(i) + 23))
    else:
        sentence_rev.append(chr(ord(i) - 3))

print(''.join(sentence_rev))

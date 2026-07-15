x = 121
x = str(x)

i = 0
j = len(x) - 1

while i < j:
    if x[i] != x[j]:
        print(False)
        break

    i += 1
    j -= 1
else:
    print(True)
for i in range(1, 11):
    if i % 2 == 0 and (i> 4 or i < 8):
        print(i)

print("---------")

for i in range(1, 11):
    if i % 2 != 0 and (i< 3 or i > 7):
        print(i)
number = int(input())

i = 0
while i in range(number):
    if 2**i == number:
        print("YES")
        break
    elif 2**i > number:
        print("NO")
        break
    i += 1
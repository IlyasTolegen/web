number = int(input())
i = 2
while i <= number:
    if number%i == 0:
        print(i)
        break
    i+=1
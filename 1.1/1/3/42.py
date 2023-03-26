number = input()
decimal = 0
power = 0
for i in reversed(range(len(number))):
    if int(number[i]):

        decimal += 2**power
    power+=1
print(decimal)
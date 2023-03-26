number = int(input())
reversedNumber = 0
for i in range(10000):
    reversedNumber += number%10
    number//=10
    if(number == 0):
        break
    reversedNumber*=10
print(reversedNumber)
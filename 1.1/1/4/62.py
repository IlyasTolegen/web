number = int(input())
str = input()
list = str.split()

for i in range(len(list)):
    if not int(list[i])%2:
        print(list[i], end = ' ')
number = int(input())
str = input()
list = str.split()

cnt = 0
reversedList = []
temp = ''
for i in range(len(list)//2):
    temp = list[i]
    list[i] = list[len(list)-i-1]
    list[len(list) - i - 1] = temp
print(*list)
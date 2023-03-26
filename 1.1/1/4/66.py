number = int(input())
str = input()
list = str.split()

cnt = 0
for i in range(1,len(list)-1):
    if (int(list[i]) > int(list[i-1]) and int(list[i]) > int(list[i+1])):
        cnt+=1
print(cnt)
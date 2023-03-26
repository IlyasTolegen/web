number = int(input())
str = input()
list = str.split()
cnt = 0
for i in range(len(list)):
    if int(list[i]) > 0:
        cnt+=1
print(cnt)
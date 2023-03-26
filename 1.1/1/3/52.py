number = int(input())
cnt = 0
for i in range(number):
    num = input()
    for j in range(len(num)):
        if(num[i]== '0'):
            cnt+=1
print(cnt)
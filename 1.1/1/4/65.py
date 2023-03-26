number = int(input())
str = input()
list = str.split()

cnt = 0
for i in range(1,len(list)):
    if (int(list[i]) >= 0 and int(list[i-1]) >= 0) or (int(list[i])<= 0 and int(list[i-1]) <= 0):
        print("YES")
        exit()
    
print("NO")
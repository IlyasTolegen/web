number = int(input())
cnt = 1
for i in range(1, number//2+1):
    if number%i == 0:
        cnt+=1
        i*=2
print(cnt)
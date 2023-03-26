x = input()
d = input()
cnt = 0
for i in range(len(x)):
    if d in x:
        cnt+=1
        x = x.replace(d, '', 1)
    else:
        break
print(cnt)
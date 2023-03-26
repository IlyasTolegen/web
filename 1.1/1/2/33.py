userAnswer = int(input())

compAnswer = int(input())

if(userAnswer == compAnswer):
    print("YES")
elif(userAnswer != compAnswer and userAnswer != 1 and compAnswer!=1):
    print("YES")
else:
    print("NO")
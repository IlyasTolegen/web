if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    max = -101
    temp = -101
    for i in range(len(arr)):
        if(int(arr[i]) > max):
            temp = max
            max = int(arr[i])
        elif (int(arr[i]) == max):
            continue
        elif(temp > int(arr[i])):
            continue
        elif (temp < int(arr[i])):
            temp = int(arr[i])
    print(temp)

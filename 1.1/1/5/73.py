def xor(x, y):
    return (not x)*y + x*(not y)

list = input().split()

print(xor(int(list[0]), int(list[1])))
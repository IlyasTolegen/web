
def last2(str):
    if len(str) < 2:
        return 0
    last_two = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i + 2] == last_two:
            count += 1
    return count


print(last2('ooolllooo'))
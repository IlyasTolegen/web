def love6(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
        return True
    else:
        return False


print(love6(6, 6))
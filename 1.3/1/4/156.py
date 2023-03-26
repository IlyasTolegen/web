def string_bits(str):
    result = ""
    for i in range(0, len(str), 2):
        result += str[i]
    return result


print(string_bits('qwert'))
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

print(string_splosion('Hello'))
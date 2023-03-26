def is_leap(year):
    leap = False
    
    # Write your logic here
    if not year % 4 and year % 100:
        leap = True
    elif not year % 400:
        leap = True
    else:
        leap = False
    return leap 

year = int(input())
print(is_leap(year))
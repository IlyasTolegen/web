def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 6]:
            return 'off'
        else:
            return '10:00'
    else:
        if day in [0, 6]:
            return '10:00'
        else:
            return '7:00'


print(alarm_clock(1, False))
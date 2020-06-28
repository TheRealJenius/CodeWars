def dig_pow(n, p):
    
    # turning the number into a string and making a list of integers:
    numbers = [int(number) for number in str(n)]

    total = 0

    for number in numbers:
        total +=  number ** p
        p += 1 # incrementing the count of power
    
    if total % n == 0: # if there is no remainder
        return int(total / n) # it doesn't have to be an int, I just wanted it tidy
        
    return -1


# print(dig_pow(46288,3))

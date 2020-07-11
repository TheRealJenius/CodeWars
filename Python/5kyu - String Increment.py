def increment_string(strng):
    
    # number = "".join(s for s in strng if s.isalpha() is False) # turns it into a string (saves us 8 lines of code below)
    '''
    Old code...
    
    digits = 0
    for s in strng:
        if s.isalpha(): # if there are letters
            all_letters = True
        else:
            all_letters = False
            digits += 1
    number = strng[(len(strng) - digits):]
    '''

    # couldn't use either of the above solutions due to test cases like this "()\\^@'83452$?}#\\2117399000504041" -.-(I know...)

    #working  backwards through the string
    i = -1
    number = ""
    number_list = [str(i) for i in range(0,10)]
    while (len(strng) > 0) and (strng[i] in number_list):
        number += strng[i]
        i -= 1
        if (len(strng) + i < 0): # if the code passes the first character in the string
            break
    number = number[::-1] # reversing back the number
    new_number = 1 if number == "" else int(number) + 1 
    zeroes = len(number) - len(str(new_number)) # to account for the leading zeroes
    strng = strng + '1' if number == "" else strng.replace(number, (("0" * zeroes) + str(new_number))) # replcaing the previous number by position allows us to overrite it

    return strng


print(increment_string("00000"))
print(increment_string("1"))
print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar00"))
print(increment_string("foobar099"))
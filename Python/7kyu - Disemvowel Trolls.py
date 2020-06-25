import pytest as test 

def disemvowel(string):
    '''
    Removing the vowels from troll messages
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']

    for vowel in vowels:
        string = string.replace(vowel,'') # for the lowercase characters
        string = string.replace(vowel.upper(),'') # for the uppercase characters

    return string

# assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
# print(disemvowel("This website is for losers LOL!"))
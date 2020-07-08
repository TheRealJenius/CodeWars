def duplicate_count(text):
    # Your code goes here
    duplicates = {} # dictionary for duplicates
    duplicates_count = 0
    for i in range(len(text)):
        character = text[i].lower() # ensures we caputre the capitlaized characters
        if character in duplicates:
            duplicates[character] += 1 # adds one to the count to recognise the duplicates
        else:
            duplicates[character] = 1 # sets a default value of 1 if it isn't already in the dictionary
    
    for character in duplicates:
        if duplicates[character] > 1:
            duplicates_count += 1
    
    return duplicates_count

'''
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdea"), 1)
test.assert_equals(duplicate_count("indivisibility"), 1)
'''
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])[a-zA-Z\d]{6,}$"
'''
Tutorials - https://www.programiz.com/python-programming/regex
          - https://www.tutorialspoint.com/python/python_reg_expressions.htm
Testing   - https://regex101.com/

Failed Attempts:

[a-zA-Z0-9]{6,}
[[a-z][A-Z][\d]|[a-z][\d][A-Z]|[\d][a-z][A-Z]]{6,}
[a-z]{1,}[A-Z]{1,}[\d]{1,}
^[a-zA-Z\d]{6,}$
(?=.+[a-z])(?=.+[A-Z])(?=.+[\d]){6,}
(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])[a-zA-Z\d]{6,}


^ $   = ensures the expression between is matched between the beginning and end of the line
?=.   = ensures the pointer moves forward by one to search for a match
*     = checks for 0 or more matches
[a-z] = checks for lowercase a-z
[A-Z] = checks for uppercase A-Z
\d    = check for numbers 0-9 (the same as [0-9])
{6,}  = ensures there is a minimum of 6 characters (up to unlimted) that match the expression on the left
()    = groups an expression
[]    = specifies a set of characters
'''
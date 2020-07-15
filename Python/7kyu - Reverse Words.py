def reverse_words(text):
    # Using enumerate I can confirm when I've reached the end of the list, to avoid words like the last test case catching me out
    return "".join((s[::-1] + " ") if i != len(text.split(" "))-1 else s[::-1] for i, s in enumerate(text.split(" ")))

'''
test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
test.assert_equals(reverse_words('apple'), 'elppa')
test.assert_equals(reverse_words('a b c d'), 'a b c d')
test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')
test.assert_equals(reverse_words('hello hello'), 'olleh olleh')
'''
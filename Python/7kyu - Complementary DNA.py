def DNA_strand(dna):
    '''
    Solution 1:
    
    complement = ""
    for symbol in dna:
        if symbol == "A":
            complement += "T"
        elif symbol == "T":
            complement += "A"
        elif symbol == "C":
            complement += "G"
        elif symbol == "G":
            complement += "C"
    return complement
    '''

    return dna.translate(dna.maketrans("ATCG","TAGC"))
    # maketrans swaps each character with the relative character on the other side (can have more than one value)
    # translate maps the value with the character it represents

print(DNA_strand("AAAA")) # TTTT
print(DNA_strand("ATTGC")) # TAACG
print(DNA_strand("GTAT")) # CATA
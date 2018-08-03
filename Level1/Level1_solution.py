def answer(plaintext):
    # generate code table from the source code, so that I don't have to do it on my own
    source_code = {
        "code":"100100101010100110100010",
        "Braille":"000001110000111010100000010100111000111000100010",
        "The quick brown fox jumps over the lazy dog":"000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
    }
    code_table = dict()
    for text, code in source_code.items():
        while (len(text)):
            # if uppercase, record the code for uppercase, then move the code over 6 positions.
            if text[0].isupper():
                code_table['upper_case'] = code[:6]
                code = code[6:]
                letter = text[0].lower()
            else:
                letter = text[0]
            # record the code for the first letter
            code_table[letter] = code[:6]
            # move the text and code over 1/6 positions
            text = text[1:]
            code = code[6:]
    # process the plain text
    code = ''
    while (len(plaintext)):
        if plaintext[0].isupper():
            code += code_table['upper_case']
            code += code_table[plaintext[0].lower()]
        else:
            code += code_table[plaintext[0]]
        plaintext = plaintext[1:]
    return code

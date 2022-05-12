from corpus_loader import word_list, name_list


# function takes in a plain text phrase and a numeric shift.
def encrypt(plain, shift):
    encrypted_text = ""
    for char in plain:
        if char.isalpha():
            # get ASCII code for character
            char_num = ord(char)
            # create variable to remember ASCII shift to index 0
            baseline_index = 0
            if (
                char_num >= 65 and char_num <= 90
            ):  # this range is for uppercase letters in ASCII
                # this subtracts the ASCII offset for uppercase range
                char_num -= 65
                # stores how far the uppercase letters were shifted from their original ASCII values
                baseline_index = 65
            elif (
                char_num >= 97 and char_num <= 122
            ):  # this range is for lowercase letters in ASCII
                # this subtracts the ASCII offset for lowercase range
                char_num -= 97
                # stores how far the lowercase letters were shifted from their original ASCII values
                baseline_index = 97
            # implements the shift passed in to the function
            char_num += shift
            # wrap back around if past 26
            char_num = char_num % 26
            # shift back to original ASCII range with offset
            char_num += baseline_index
            # convert back to character
            shifted_char = chr(char_num)
            # add it to the output
            encrypted_text += shifted_char
        else:
            # add non-alpha characters to output
            encrypted_text += char
    return encrypted_text


# function takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
def decrypt(encoded, shift):
    # multiplying the original shift by -1 reverses the encryption
    return encrypt(encoded, shift * -1)


# function will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
def crack(encoded):
    phrase = "It was the best of times, it was the worst of times."
    # brute force method. This tries every possible offset before it loops around
    for i in range(26):
        if encrypt(encoded, i * -1) == phrase:
            return encrypt(encoded, i * -1)
    # if we get through all 26 then we know there's not a solution, so it will return an empty string
    return ""

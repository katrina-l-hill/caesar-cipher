import random
import re
from corpus_loader import word_list, name_list


# function takes in a plain text phrase and a numeric shift.
def encrypt(plain, shift):
    encrypted_text = ""
    for char in plain:
        letters = int(char)
        shifted_letters = (letters + shift) % 10
        encrypted_text += str(shifted_letters)
    return encrypted_text


# function takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
def decrypt(encoded, shift):
    return encrypt(encoded, shift)


# function will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
def crack(encoded):
    pass


# use ord() method to convert char to int

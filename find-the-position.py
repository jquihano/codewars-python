# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Ouput :: "Position of alphabet: 1"

def position(alphabet):
    alphabet_char = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet_char)):
        if alphabet_char[i] == alphabet:
            return 'Position of alphabet: %s' %(str(i+1))
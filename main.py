from string import ascii_letters
import string

alphabet = list(string.ascii_lowercase)


# Zakodowanie
def encode():
    bces = input("Enter text to encode: ")
    shift = input("Type the shift number")
    aces = ''
    shift = int(shift)

    for c in bces:
        if c in alphabet:
            if alphabet.index(c) + shift < len(alphabet):
                aces = aces + alphabet[alphabet.index(c) + shift]
            else:
                aces = aces + alphabet[(alphabet.index(c) + shift - 25)]
        else:
            aces += c
    print(aces)


# Dekodowanie
def decode():
    bces = input("Enter text to decode: ")
    shift = input("Type the shift number")
    aces = ''
    shift = int(shift)
    for c in bces:
        if c in alphabet:
            if alphabet.index(c) - shift > 0:
                aces = aces + alphabet[alphabet.index(c) - shift]
            else:
                aces = aces + alphabet[(alphabet.index(c) - shift - 1)]
        else:
            aces += c
    print(aces)


def question():
    x = input("encode or decode? ")
    if x == "encode":
        encode()
    elif x == "decode":
        decode()


active = True
while active:
    question()
    dec = input("Continue? yes/no")
    if dec == "no":
        active = False

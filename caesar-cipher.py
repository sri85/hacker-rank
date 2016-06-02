# https://www.hackerrank.com/challenges/caesar-cipher-1
key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
# ToDo: Handle upper case issue
    result = ''
    for l in plaintext.lower():
        try:

            i = (key.index(l) + n) % 26
            if l.islower():
                result += key[i]
            else:
                result += key[i].upper()
        except ValueError:
            result += l
    return result

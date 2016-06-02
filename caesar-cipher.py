key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):

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

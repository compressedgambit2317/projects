import random


def keyGen():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    key = random.sample(alphabet, len(alphabet))
    return key


def clean_string(s):
    s = ''.join(c for c in s if c.isalnum())
    s = s.lower()
    s = ''.join(s)
    return s

def cipher(message, alpha, key):
    cipher_dict = dict(zip(alpha, key))
    cipher_message = ''.join(cipher_dict.get(c, c) for c in message)
    return cipher_message

def decipher(message, alpha, key):
    decipher_dict = dict(zip(key, alpha))
    decipher_message = ''.join(decipher_dict.get(c, c) for c in message)
    return decipher_message

def main():
    key = keyGen()
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    message = input('Enter a message: ')
    message = clean_string(message)
    cipher_message = cipher(message, alpha, key)
    print('Encrypted message:', cipher_message)
    decipher_message = decipher(cipher_message, alpha, key)
    print('Decrypted message:', decipher_message)

if __name__ == '__main__':
    main()

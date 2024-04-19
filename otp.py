import random

def open_file(file):
    message = ""
    f = open(file, 'r')
    content = f.read()
    for c in content:
        message = message + c
    return message

def generate_key(message):
  
    for c in message:
        key = key + chr(random.randint(0, 255))
    return key

def encrypt(message, key):
    encrypted_message = ""
    counter = 0
    for c in message:
        encrypted_message = encrypted_message + chr(ord(c) ^ ord(key[counter])) 
        counter = counter + 1
    return encrypted_message



print("Welcome to the One Time Pad encryption algorithm")
print("Please enter the name of the file you would like to encrypt: ")
file = input()
message = open_file(file)
print("The content of the file is: ")
print(message)
print("The message, encrypted with the One Time Pad algorithm is: ")
key = generate_key(message)
encrypted_message = encrypt(message, key)
print(encrypted_message)
decrypted_messag = encrypt(encrypted_message,key)
print("The message, decrypted with the One Time Pad algorithm is: ")
print(decrypted_messag)


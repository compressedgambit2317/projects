with open("encrypted_message.txt", "r") as file:
    encrypted_message = [int(line) for line in file]

with open("private_key.txt", "r") as file:
    d = int(file.readline())
    n = int(file.readline())

decrypted_message = [pow(char, d, n) for char in encrypted_message]

decrypted_message = "".join([chr(char) for char in decrypted_message])

with open("decrypted_message.txt", "w") as file:
    file.write(decrypted_message)

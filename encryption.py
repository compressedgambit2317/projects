with open("message.txt", "r") as file:
     message = file.read()

message = [ord(char) for char in message]

with open("public_key.txt", "r") as file:
    n = int(file.readline())
    e = int(file.readline())

encrypted_message = [pow(char, e, n) for char in message]

with open("encrypted_message.txt", "w") as file:
    for char in encrypted_message:
        file.write(str(char) + "\n")

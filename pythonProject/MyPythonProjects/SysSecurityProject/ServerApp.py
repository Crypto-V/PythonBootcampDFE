"""
Server-Client Encrypted Communication.
Assignment 1
Student Name: Verejan Vasile
Teacher: Amjad Alam
"""
import base64
import hashlib
import socket
import os
import codecs
import sys

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

server = socket.socket()


def send_file(filename):
    """
    The main purpose of this method is to send the file to the client side:
    @:param filename- file that will be sent
    @:param file_size- getting the file size using buildIn library 'os'
    """
    file_size = os.path.getsize(filename)
    client1.send(f"{filename} {separator} {file_size}".encode())
    with open(filename, "rb") as f:
        content = f.read(buff_size)
        client1.sendall(content)
    print("--Sending file...")
    print("File sent!")
    print("___________________________")


def receive_file():
    """
    Purpouse of this method is to recive the file
    decode it and write the further information into the file.
    @:param filename and filesize provided when sending the file.
    """
    file_info = client1.recv(buff_size).decode()
    filename, filesize = file_info.split(separator)
    file = os.path.basename(filename)
    with open(file, "wb") as file:
        content = client1.recv(buff_size)
        file.write(content)

    print("      ____________")
    print("File |*****t1.txt|  Received! 😊")
    print("      ------------ ")
    print("___________________________")


def initialise_server():
    """
    By importing the Socket library we will have access to the information
    that will be necessary to establish the connection to the client module
    @:param local_name- we will obtain it when using the buildIn methods
    of socket class which will represent the name of your computer.
    @:param ip_address- computer Ip address.
    @:param port_number- port number is the actual port through which will make the
    connection.
    @:param separator- used for separating the filename from file_size.
    @:param buff_size - refers to the size allocated for the temporary storage.
    @:param common_prime and common base will be calculated by us and
    implemented in both classes (Server and Client)
    @param secret_key - will be deducted based on common_prime and
    common_base and will be unique to each class that will be used
    to generate the common_secret key.
    """
    global ip_address
    global port_number
    global buff_size
    global separator
    global common_prime
    global common_base
    global secret_key
    global local_name

    # getting the computer name
    local_name = socket.gethostname()
    # get ip address by host name
    ip_address = socket.gethostbyname(local_name)
    # assigning the port number
    port_number = 55000
    # assigning the buffer size
    buff_size = 4096

    separator = "::"
    common_prime = 29
    common_base = 9
    secret_key = 5


def server_start():
    """
    As soon as we call this method our server will be initialised,
    and it will be waiting for the client to join
    @:param server- will be set to server = socket.socket()
    and will be declared on the top of the program for further use.

    """
    server.bind((ip_address, port_number))
    server.listen(3)  # Number 3 represents the number of clients it can listen.
    print(f"Server: [{local_name}: {ip_address}: {port_number}]\n--Ready for pairing... ")
    print("Conected!")
    print("___________________________")


def generate_and_send_PK():
    """
    This method will generate the public key encode it and sending it to the client.
    @:param pk- represent the obtained public key after applying the formula
    for generating one which is  (common_base ** secret_key) % common_prime .

    """

    pk = (common_base ** secret_key) % common_prime
    client1.send(str(pk).encode())
    print("--Generating public key...")
    print("Done!👍")
    print("--Sending PK to the client!")
    print("Sent!👍")
    print("___________________________")


def recieve_PK():
    """
    This method will have the purpouse of receiving the PK ,
    decoding it and returning it fo further use.
    :return: client_pk
    """
    client_pk = client1.recv(buff_size).decode()
    client_pk = int(client_pk)
    print("--Waiting for Client Public Key...")
    print(f"Public Key Received!: |{client_pk}|")
    print("___________________________________")
    return client_pk


def common_secret_key(client_pk):
    """
    :param- sec_key represents the key the will be shared between
    server and client.
    :return: sec_key
    """
    sec_key = (client_pk ** secret_key) % common_prime
    print(f"Common key was generated and the key is:  |{sec_key}|")
    print("______________________________________________________________")
    return sec_key


def convert_to128(common_secret_key):
    """
    This method will convert our already generated common key into 128 bit.
    That will be used for first level of encryption.
    As you can see hash library will be used in this method for hashing
    messages easily.
    :return converted_key
    """

    converted_key = hashlib.sha256(str(common_secret_key).encode()).hexdigest()
    converted_key = codecs.encode(codecs.decode(converted_key, 'hex'), 'base64').decode()
    converted_key = converted_key.rstrip("\n")
    converted_key = converted_key.encode('utf-8')

    print(f"Encrypted key: |{converted_key}|")
    print("_______________________________________________________________")
    return converted_key


def generate_AES_key():
    """
    By using this method will be able to encrypt our
    file using the Advanced Encryption Standart which will bring
    our file to the second level of encryption.
    """
    password = b"password"
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    AES_key = base64.urlsafe_b64encode(kdf.derive(password))

    with open("secret_msg.txt", "wb") as f:
        f.write(AES_key)
    print(f"AES was generated!:>|{AES_key}|")
    print("______________________________________________________________")
    return AES_key


# to be updated
# Encoding file
def encoder():
    """
    This method will encode our file where:
    @:param plain_file- represent the file written into .txt format
    @:param encrypted_file- file after encryption from .txt to .enc

    """
    plain_file = "secret_msg.txt"
    encrypted_file = "secret_msg.enc"

    with open(plain_file, 'rb') as f:  # reading the bytes from the plain_text file
        data = f.read()
    # Fernet is an implementation of symmetric authenticated cryptography.
    # Which makes the message to be impossible to read without the key.
    uid = Fernet(converted_key)
    encrypted_text = uid.encrypt(data)

    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_text)


# function for decoding file
def decoder():
    """Decoder will decode our file using converted_key"""
    encrypted_file = 'secret_msg.enc'
    # Converting the r_file received from client and convert into txt.
    decrypted_file = "secret_msg.txt"
    with open(encrypted_file, 'rb') as f:
        data = f.read()

    uid = Fernet(converted_key)
    encrypted_text = uid.decrypt(data)

    with open(decrypted_file, 'wb') as f:
        f.write(encrypted_text)


# ===========================
# Main program start here
# ===========================

"""
The next lines of codes will represent the method call to create 
the interaction between both classes.
"""

# Initialising the server and waiting for response.
initialise_server()
server_start()

# Accepting the incoming connection.
client1, address = server.accept()

# Receiving the file.
receive_file()

# Creating the public key and sending it to client.
generate_and_send_PK()

# Receiving pk from client
received_client_pk = recieve_PK()

# calling the method to generate the common secret key
sec_key = common_secret_key(received_client_pk)

# Converting our key into 128bit.
converted_key = convert_to128(sec_key)

# Generating the AES key for second level of encryption
AES_key = generate_AES_key()

# Encryptinc with AES key and sending..
encoder()
send_file("secret_msg.enc")

#Receiving and decoding the AES
receive_file()
decoder()
with open("secret_msg.txt", "rb") as f:
    AES_key_toServer = f.read().decode()
print(f"AES key from the client : [{AES_key_toServer}]")


# Chating start from here:
print("_____________________________")
print("|Encrypted chat starts here!|")
print("|___________________________|\n")

# After first answer you will have the option to stop or continue the chat.
while True:
    message = input("Server:> ").encode()
    with open("secret_msg.txt", "wb") as f:
        # second level of encryption
        uid = Fernet(AES_key)
        message = uid.encrypt(message)
        f.write(message)

    encoder()
    send_file("secret_msg.enc")

    receive_file()  # will recive secret_msg1.enc
    decoder()  # will convert it to .txt

    with open("secret_msg.txt", "rb") as f:
        message = f.read()
        uid = Fernet(AES_key)
        message = uid.decrypt(message)
        message = message.decode()

    print("Client :> ", message)
    prompt = int(input("Would you like to reply: 1:Yes/2:No-> "))
    if prompt == 1:
        continue
    else:
        sys.exit()

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

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def send_file(filename):
    """
    The main purpouse of this method is to send the file to the client side:
    @:param filename- file that will be sent
    @:param file_size- getting the file size using buildin library 'os'
    """
    file_size = os.path.getsize(filename)
    client.send(f"{filename} {seperator} {file_size}".encode())
    with open(filename, "rb") as f:
        content = f.read(buff_size)
        client.sendall(content)
    print("--Sending file...")
    print("File sent!")
    print("___________________________")


def receive_file():
    """
    Purpouse of this method is to recive the file
    decode it and write the further information into the file.
    @:param filename and filesize provided when sending the file.
    """

    file_info = client.recv(buff_size).decode()
    filename, filesize = file_info.split(seperator)
    file = os.path.basename(filename)
    with open(file, "wb") as f:
        content = client.recv(buff_size)
        f.write(content)


    print("                 ____________")
    print("--Receiving file |*****t1.txt| from the server! 😊")
    print("                 ------------ ")
    print("File received!👍")
    print("__________________________________________________")


def client_initilisation():
    """
    By importing the Socket library we will have access to the information
    that will be necessary to establish the conection to the client module
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
    global seperator
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

    seperator = "::"
    common_prime = 29
    common_base = 9
    secret_key = 3


def client_start():
    """
    As soon as we call this method our client will be initialised.
    @:client server- will be set to client = socket.socket() which will
    give us the ability to use the necessary methods such as connect in our case.
    """
    global client
    client = socket.socket()
    client.connect((ip_address, port_number))
    print(f"--Connecting to [ {local_name} ]...")
    print("Client Conected!!")
    print("___________________________")


def generate_and_send_PK():
    """
    This method will generate the public key encode it and sending it to the client.
    @:param pk- represent the obtained public key after applying the formula
    for generating one which is  (common_base ** secret_key) % common_prime .

    """

    pk = (common_base ** secret_key) % common_prime
    client.send(str(pk).encode())
    print("--Generating Public Key...")
    print("Generated!👍")
    print("--Sending PK to the server...")
    print("Sent!👍")
    print("___________________________")


def recieve_PK():
    """
    This method will have the purpouse of receiving the PK ,
    decoding it and returning it fo further use.
    :return: client_pk
    """
    client_pk = client.recv(buff_size).decode()
    client_pk = int(client_pk)
    print(f"Public Key Received!: |{client_pk}|")
    print("___________________________")
    return client_pk


def common_secret_key(client_pk):
    """
    :param- sec_key represents the key the will be shared between
    server and client.
    :return: sec_key
    """
    sec_key = (client_pk ** secret_key) % common_prime
    print(f"Common key was generated and the key is:  |{sec_key}|")
    print("______________________________________________________")
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
    print("___________________________________________")
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
    print("____________________________________________")
    return AES_key


# to be updated
# Encoding file
def encoder():
    """
    Fernet is an implementation of symmetric authenticated cryptography.
    Which makes the message to be impossible to read without the key.
    This method will encode our file where:
    @:param plain_file- represent the file written into .txt format
    @:param encrypted_file- file after encryption from .txt to .enc

    """
    plain_file = "secret_msg.txt"
    encrypted_file = "secret_msg.enc"

    with open(plain_file, 'rb') as f:
        data = f.read()

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
# Initialising the client.
client_initilisation()
client_start()

# Sending the file secret1.txt to the server.
send_file("secret1.txt")

# Receiving the public key from server
received_server_pk = recieve_PK()

# Creating the public key and sending it to server.
generate_and_send_PK()
sec_key = common_secret_key(received_server_pk)

# Converting the key into 128bits.
converted_key = convert_to128(sec_key)

receive_file()  # Client is receiving the secret_msf.txt
decoder()  # Decoding the file
# Decoding the file that hold the generated AES key.
with open("secret_msg.txt", "rb") as f:
    AES_key = f.read().decode()
print(f"Received AES key: [{AES_key}]\n")


#Generating AES and sending to the server
AES_key_toServer =generate_AES_key();
encoder()
send_file("secret_msg.enc")

# Chating start here
print("_____________________________")
print("|Encrypted chat starts here!|")
print("|___________________________|\n")

while True:
    receive_file()  # will recive secret_msg1.enc
    decoder()  # will convert it to .txt

    with open("secret_msg.txt", "rb") as f:
        message = f.read()
        uid = Fernet(AES_key)
        message = uid.decrypt(message)
        message = message.decode()

    print("Server :> ", message)

    message = input("Client:> ").encode()

    with open("secret_msg.txt", "wb") as f:
        uid = Fernet(AES_key)
        message = uid.encrypt(message)
        f.write(message)

    encoder()
    send_file("secret_msg.enc")

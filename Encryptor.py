import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as PBK
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding


class Encrypt:
    def __init__(self):
        self.password = None
        self.__pem_private_key = None

    def get_password(self):
        # queries the user for a password
        # ensures that the user's password is correct and passes it to the caller
        while True:
            p1 = input("Please enter a password:\n")
            p2 = input("Please repeat your password:\n")

            if p1 == p2:
                # password is encoded as bytes
                self.password = p1.encode()
                break
            print("Passwords do not match")

        return self.password

    def load_pem(self, password, name=None):
        # loads a pem file from the current directory
        if name is None:
            name = input("Enter the name of the pem file to load:\n")

        try:
            with open(name, 'rb') as pem:
                p = pem.read()
            pem.close()
        except FileNotFoundError as f_error:
            print(f_error)
            exit()

        # decrypts it with the provided password if possible
        # returns private key to the user
        try:
            self.__pem_private_key = load_pem_private_key(p, password, default_backend())
        except ValueError as v:
            print(v)
            exit()

        return self.__pem_private_key

    def aes(self, message):
        # encodes the message as binary and generates a salt value
        b_message = message.encode()
        salt = os.urandom(16)

        password = self.get_password()

        # generates the key derivative
        pbk = PBK(algorithm=SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = base64.urlsafe_b64encode(pbk.derive(password))
        # prints out the key to the user
        print("Derived Key:", key.decode(), "\nKeep this safe!\n")
        fern = Fernet(key)

        # encrypts and writes to a file
        e_message = fern.encrypt(b_message)
        name = input("Enter a name for the message to be output as:\n")
        with open(name, 'w') as w:
            w.write(e_message.decode())
        w.close()

    def rsa(self, message):
        # encodes the message as binary
        b_message = message.encode()
        password = self.get_password()

        # generates the private and public keys
        priv_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

        # writes the private key to an encoded pem file, and writes it to the disk
        pem = priv_key.private_bytes(encoding=serialization.Encoding.PEM,
                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                     encryption_algorithm=serialization.BestAvailableEncryption(password))

        name = input("Enter a name for the pem file without an extension:\n") + ".pem"
        with open(name, 'wb') as w:
            w.write(pem)
        w.close()

        # loads and decrypts the pem file to retrieve the private and public keys
        pub_key = self.load_pem(password, name=name).public_key()

        # pads the message, and encrypts it
        e_message = pub_key.encrypt(b_message,
                                    padding=padding.OAEP(mgf=padding.MGF1(algorithm=SHA256()),
                                                         algorithm=SHA256(), label=None))

        # encodes the public key to bytes for reference
        print_pub_key = pub_key.public_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()

        # saves the public key file
        pname = input("Enter a name for the public key file:\n")
        try:
            with open(pname, 'w') as p:
                p.write(print_pub_key)
            p.close()
        except FileNotFoundError:
            print("File name cannot be blank")
            exit()

        # saves the encrypted message as a file
        try:
            fname = input("Enter a name for the message file:\n")
            with open(fname, 'wb') as f:
                f.write(e_message)
            p.close()
        except FileNotFoundError:
            print("File name cannot be blank")

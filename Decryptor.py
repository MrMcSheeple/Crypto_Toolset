from Encryptor import Encrypt
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.fernet import Fernet


class Decrypt(Encrypt):
    def __init__(self):
        super(Decrypt, self).__init__()

    @staticmethod
    def dec_aes():
        key = input("Enter your AES decryption key:\n").encode()
        fname = input("Enter the name of the file to decrypt:\n")

        try:
            with open(fname, 'r') as f:
                e_message = f.read().encode()
            f.close()

        except FileNotFoundError as f_error:
            print(f_error)
            exit()

        f = Fernet(key)
        message = f.decrypt(e_message).decode()

        print()
        print(message)

    def dec_rsa(self):
        password = super(Decrypt, self).get_password()
        priv_key = super(Decrypt, self).load_pem(password)

        try:
            fname = input("Provide the name of the file to be decrypted:\n")
            with open(fname, 'rb') as f:
                e_message = f.read()
            f.close()
        except FileNotFoundError as f_error:
            print(f_error)
            exit()

        # decrypts the pem file and uses it to decrypt the message and write it to disk
        try:
            message = priv_key.decrypt(e_message, padding=padding.OAEP(mgf=padding.MGF1(algorithm=SHA256()),
                                                                       algorithm=SHA256(), label=None))
            print()
            print(message.decode())
        except ValueError:
            print("Decryption Failed. Are you using the right key file?")
            exit()

# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from cryptography.fernet import Fernet

KEY_PATH = 'E:/key'
DJANGO_KEY_PATH = 'E:/key1'


def decrypt(token):
    with open(KEY_PATH, 'r') as file:
        KEY = file.read().strip()
    f = Fernet(KEY)
    return f.decrypt(token).decode()


def get_secret_key():
    with open(DJANGO_KEY_PATH, 'r') as file:
        KEY = file.read().strip()
    return KEY


if __name__ == '__main__':
    key = Fernet.generate_key()  # Store somewhere safe
    print(key)
    f = Fernet(key)
    token = f.encrypt(b"A really secret message. Not for prying eyes.")
    print(token)
    print(f.decrypt(token))

    print(get_secret_key())
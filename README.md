# SOC Analyst Toolkit - Confidentiality - Dominic Cheruiyot
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as kf:
        kf.write(key)
    print("[+] Key saved as secret.key - PROTECT THIS!")
    return key

def encrypt_file(filename, key):
    f = Fernet(key)
    data = open(filename, "rb").read()
    enc = f.encrypt(data)
    open(filename + ".enc", "wb").write(enc)
    print(f"[+] {filename} -> {filename}.enc")

# LAB USAGE
if __name__ == "__main__":
    open("customer_data.txt","w").write("Customer: John Doe, Ac: 123456, Bal: Ksh 50,000")
    key = generate_key() if not os.path.exists("secret.key") else open("secret.key","rb").read()
    encrypt_file("customer_data.txt", key)
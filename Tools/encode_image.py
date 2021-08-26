from cryptography.fernet import Fernet
from datetime import date
import base64
time = date.today()

key = Fernet.generate_key()
fileencrypt = input("[+] Please Specify the Path to the Image to Encrypt: ")
    
with open("FernetKeys.revise7", 'wb') as keyinfile:
    keyinfile.write(key)
    f = Fernet(key)
        
    with open(fileencrypt, "rb") as file:
        org = file.read()
        encrypted = f.encrypt(org)
            
        with open(fileencrypt, "wb") as encrypted_file:
            encrypted_file.write(encrypted)
            print(time.strftime("%d/%m/%Y"),"[+] Your Encrypted Image is: ", fileencrypt)
            print(time.strftime("%d/%m/%Y"),"[+] Your Fernet Decryption Key is: ", key)
            print(time.strftime("%d/%m/%Y"),"Waiting for System Intercation..")
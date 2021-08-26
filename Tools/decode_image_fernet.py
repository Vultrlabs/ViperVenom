from cryptography.fernet import Fernet # Using cryptography package.
from datetime import date
import base64

time = date.today()
fileencrypted = input("[+] Please Specify the Path to the Encrypted Image: ")
    
with open(fileencrypted, 'rb') as enc:
    encryptedd = enc.read()
    
with open("FernetKeys.revise7", 'rb') as keysfile: # INSERT YOUR FERNET KEY BEFORE EXECUING THE DECRYPTION PART
    key = keysfile.readline()
    f = Fernet(key)
    decrypting = f.decrypt(encryptedd)
        
    with open(fileencrypted, 'wb') as dec:
        dec.write(decrypting)
    print(time.strftime("%d/%m/%Y"),"[+] File Decrypted.")
from cryptography.fernet import Fernet
import csv

Key = Fernet.generate_key()
Cipher = Fernet(Key)

with open("Key.key",'wb') as KeyFile:
    KeyFile.write(Key)

with open('C.csv','rb') as file:
    FileData = file.read()
    Encryptedata = Cipher.encrypt(FileData)

with open('C.csv','wb') as Write:
    C = Write.write(Encryptedata)

# Decrypt the CSV file
with open('C.csv', 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()
    decrypted_data = Cipher.decrypt(encrypted_data)

    with open('C.csv', 'r') as read:
        reads = csv.reader(read)
        for line in reads:
            print(line)
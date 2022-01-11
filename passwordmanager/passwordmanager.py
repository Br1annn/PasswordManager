from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')      
    key = file.read()
    file.close()
    return key

mPwd = input("master password: ")
key = load_key() + mPwd.bytes
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            websiteN,user,passw = data.split('|')
            print('Website: ',websiteN,'User: ',user,'Password: ',passw)
            fer.decrypt((passw.encode()).decode())

def add():
    websiteName = input('Website: ')
    name = input('Name: ')
    password = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(websiteName + '|' + name + '|' + fer.encrypt(password.encode()).decode() + '\n')

while True:

    mode = input("add,view,q\n")
    if mode == 'q':
        break

    elif mode == 'view':
        view()

    elif mode == 'add':
        add()

    else:
        print("Invalid")
        continue


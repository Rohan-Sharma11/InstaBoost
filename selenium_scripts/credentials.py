# credentials.py
import getpass

username = input('Enter your Instagram username: ')
password = getpass.getpass('Enter your Instagram password: ')

with open('config.py', 'w') as f:
    f.write(f'username = {username!r}\n')
    f.write(f'password = {password!r}\n')
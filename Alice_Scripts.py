import simplecrypt
import urllib.request as urllib

passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

with open("encrypted.bin", 'rb') as f:
    encrypted = f.read()
# print(repr(encrypted))
print(encrypted)
#
# with open("Passwords.txt", 'r') as z:
#      passwords = z.read()
# print(passwords)

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is right')

b'RVrF2qdMpoq6Lib'
print(simplecrypt.decrypt(b'RVrF2qdMpoq6Lib', encrypted).decode('utf8'))
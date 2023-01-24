import base64
from random import randint

flag = "kctf{************}"

def encrypt(s, option):
    if option == 0:
        ret = base64.b64encode(s)
    elif option == 1:
        ret = base64.b32encode(s)
    elif option == 2:
        ret = base64.b16encode(s)
    else:
        ret = base64.b85encode(s)

    return ret


encrypted_flag = flag.encode('utf-8')

for _ in range(12):
    option = randint(0, 3)
    encrypted_flag = encrypt(encrypted_flag, option)

with open("encode_mania.txt", 'w') as f:
    f.write(encrypted_flag.decode())
